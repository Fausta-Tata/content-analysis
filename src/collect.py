import pandas as pd
from dotenv import load_dotenv
from googleapiclient.discovery import build
import os

from src.config import ENV_PATH, RAW, CUTOFF, CHANNELS

load_dotenv(ENV_PATH)


def get_youtube_api():
    """Create a YouTube API client."""
    api_key = os.getenv("YOUTUBE_API_KEY")
    if not api_key:
        raise ValueError("YOUTUBE_API_KEY not found in environment variables.")
    return build("youtube", "v3", developerKey=api_key)


def get_channel_videos(yt, channel_id, cutoff=CUTOFF):
    """
    Retrieve video data from a YouTube channel published on/after `cutoff`.

    Args:
        yt: YouTube API client.
        channel_id (str): Channel ID (starts with "UC").
        cutoff (str): Earliest publish date, format YYYY-MM-DD.

    Returns:
        pd.DataFrame: One row per video.
    """
    uploads = "UU" + channel_id[2:] # Convert Id Channel to Upload Playlist: "UC" to "UU"
    ids, token, stop = [], None, False

    # Retrieve video IDs from the uploads playlist
    while not stop:
        res = yt.playlistItems().list(
            part="contentDetails", playlistId=uploads,
            maxResults=50, pageToken=token).execute()

        for item in res["items"]:
            tanggal = item["contentDetails"]["videoPublishedAt"][:10]
            if tanggal < cutoff:
                stop = True
                break
            ids.append(item["contentDetails"]["videoId"])

        token = res.get("nextPageToken")
        if not token:
            break

    # Fetch video details and statistics using the video IDs
    rows = []
    for i in range(0, len(ids), 50):
        res = yt.videos().list(
            part="snippet,statistics,contentDetails",
            id=",".join(ids[i:i + 50])).execute()
        for v in res["items"]:
            s, st = v["snippet"], v["statistics"]
            rows.append({
                "video_id": v["id"],
                "title": s["title"],
                "description": s.get("description", "")[:500],
                "tags": "|".join(s.get("tags", [])),
                "published_at": s["publishedAt"],
                "duration": v["contentDetails"]["duration"],
                "views": int(st["viewCount"]) if "viewCount" in st else None,
                "likes": int(st["likeCount"]) if "likeCount" in st else None,
                "comments": int(st["commentCount"]) if "commentCount" in st else None,
            })

    # Store the collected data in a Pandas DataFrame
    df = pd.DataFrame(rows)
    df["collected_at"] = pd.Timestamp.now()
    return df


def main():
    yt = get_youtube_api()
    out_dir = RAW / "youtube"
    out_dir.mkdir(parents=True, exist_ok=True)

    for group, channel_id in CHANNELS.items():
        try:
            print(f"[INFO] Starting: {group}")
            df = get_channel_videos(yt, channel_id)
            df["group"] = group            
            filename = group.replace(" ", "_") + "_youtube.csv"
            df.to_csv(out_dir / filename, index=False)
            print(f"[SUCCESS] {group}: {len(df)} videos saved.")
        except Exception as e:
            print(f"[ERROR] {group}: {e}")


if __name__ == "__main__":
    main()