"""This File Make Manual Data for Music Releases from 2025 Until 2026"""
import os
import pandas as pd
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent   
sys.path.append(str(ROOT))
from config import MAIN_TYPES

releases = pd.DataFrame([
    {"group": "aespa", "release_name": "Dirty Work", "release_date": "2025-06-27", "type": "single album"},
    {"group": "aespa", "release_name": "Dirty Work (Remixes)", "release_date": "2025-06-30", "type": "remix single"},
    {"group": "aespa", "release_name": "Dark Arts", "release_date": "2025-07-15", "type": "promotional single"},
    {"group": "aespa", "release_name": "Rich Man", "release_date": "2025-09-05", "type": "mini album"},
    {"group": "aespa", "release_name": "Rich Man (English Ver.)", "release_date": "2025-09-12", "type": "single"},
    {"group": "aespa", "release_name": "Rich Man (Remixes)", "release_date": "2025-09-19", "type": "remix single"},
    {"group": "aespa", "release_name": "Gabby's Dollhouse: The Movie Soundtrack", "release_date": "2025-09-26", "type": "soundtrack single"},
    {"group": "aespa", "release_name": "SYNK : aeXIS LINE - 2025 Special Digital Single", "release_date": "2025-11-17", "type": "special single"},
    {"group": "riize", "release_name": "Hug", "release_date": "2025-01-08", "type": "digital single special"},
    {"group": "riize", "release_name": "ODYSSEY", "release_date": "2025-05-19", "type": "studio album"},
    {"group": "riize", "release_name": "Fame", "release_date": "2025-11-24", "type": "single album"},
    {"group": "hearts2hearts", "release_name": "The Chase", "release_date": "2025-02-24", "type": "single album"},
    {"group": "hearts2hearts", "release_name": "STYLE", "release_date": "2025-06-18", "type": "digital single"},
    {"group": "hearts2hearts", "release_name": "Pretty Please", "release_date": "2025-09-24", "type": "digital single"},
    {"group": "hearts2hearts", "release_name": "FOCUS", "release_date": "2025-10-20", "type": "mini album"},
    {"group": "hearts2hearts", "release_name": "FOCUS (Remixes)", "release_date": "2025-11-21", "type": "remix album"},
    {"group": "hearts2hearts", "release_name": "ScreaM Rookies : The Chase (Remixes)", "release_date": "2025-12-17", "type": "remix album"},
    {"group": "nct 127", "release_name": "You In Vague Memory (2025 SMTOWN : THE CULTURE, THE FUTURE)", "release_date": "2025-02-14", "type": "participation single"},
    {"group": "nct 127", "release_name": "K-POP ScreaM 2", "release_date": "2025-04-11", "type": "remix album"},
    {"group": "nct dream", "release_name": "Go Back To The Future", "release_date": "2025-07-14", "type": "studio album"},
    {"group": "nct dream", "release_name": "Beat It Up", "release_date": "2025-11-17", "type": "mini album"},
    {"group": "nct wish", "release_name": "Miracle", "release_date": "2025-01-22", "type": "digital single special"},
    {"group": "nct wish", "release_name": "Make You Shine (English Version)", "release_date": "2025-03-28", "type": "soundtrack single"},
    {"group": "nct wish", "release_name": "poppop", "release_date": "2025-04-14", "type": "mini album"},
    {"group": "nct wish", "release_name": "Surf", "release_date": "2025-08-12", "type": "digital single"},
    {"group": "nct wish", "release_name": "COLOR", "release_date": "2025-09-01", "type": "mini album"},
    {"group": "nct wish", "release_name": "Would You Marry Me? OST Pt. 3", "release_date": "2025-10-17", "type": "soundtrack single"},
    {"group": "nct wish", "release_name": "Dreamcatcher", "release_date": "2025-11-06", "type": "digital single"},
    {"group": "nct wish", "release_name": "Princess Catch! Teenieping : Princepingsong", "release_date": "2025-12-11", "type": "soundtrack single"},
    {"group": "wayv", "release_name": "BIG BANDS", "release_date": "2025-07-18", "type": "mini album"},
    {"group": "wayv", "release_name": "Eternal White", "release_date": "2025-12-08", "type": "special album"},
    {"group": "aespa", "release_name": "Keychain", "release_date": "2026-02-27", "type": "soundtrack single"},
    {"group": "aespa", "release_name": "ATTITUDE", "release_date": "2026-03-06", "type": "soundtrack single"},
    {"group": "aespa", "release_name": "WDA (Whole Different Animal) (feat. G-DRAGON)", "release_date": "2026-05-11", "type": "digital single"},
    {"group": "aespa", "release_name": "LEMONADE", "release_date": "2026-05-29", "type": "studio album"},
    {"group": "aespa", "release_name": "KISS N TELL", "release_date": "2026-07-24", "type": "mini album"},
    {"group": "aespa", "release_name": "SYNK : aeXIS LINE - 2026 Special Digital Single", "release_date": "2026-08-09", "type": "special single"},
    {"group": "aespa", "release_name": "SYNK : COMPLaeXITY - 2026 Special Digital Single", "release_date": "2026-09-14", "type": "special single"},
    {"group": "aespa", "release_name": "Santa Baby", "release_date": "2026-11-13", "type": "collaboration single"},
    {"group": "riize", "release_name": "All of You", "release_date": "2026-02-09", "type": "japanese single"},
    {"group": "riize", "release_name": "Perfect Crown OST Part. 4", "release_date": "2026-04-18", "type": "soundtrack single"},
    {"group": "riize", "release_name": "KILL SHOT", "release_date": "2026-04-19", "type": "japanese digital single"},
    {"group": "riize", "release_name": "II", "release_date": "2026-06-15", "type": "mini album"},
    {"group": "riize", "release_name": "Sunburst", "release_date": "2026-08-26", "type": "japanese single"},
    {"group": "riize", "release_name": "Insomnia", "release_date": "2026-10-26", "type": "digital single"},
    {"group": "riize", "release_name": "Lowkey (with PLAVE)","release_date": "2026-11-30", "type": "collaboration single"},
    {"group": "hearts2hearts", "release_name": "RUDE!", "release_date": "2026-02-20", "type": "digital single"},
    {"group": "hearts2hearts", "release_name": "RUDE! (Japanese Ver.)", "release_date": "2026-03-18", "type": "japanese digital single"},
    {"group": "hearts2hearts", "release_name": "iScreaM Vol.39 : RUDE! (Remixes)", "release_date": "2026-03-27", "type": "remix single"},
    {"group": "hearts2hearts", "release_name": "Lemon Tang", "release_date": "2026-06-22", "type": "mini album"},
    {"group": "hearts2hearts", "release_name": "ICONIC HEART", "release_date": "2026-08-10", "type": "japanese single"},
    {"group": "hearts2hearts", "release_name": "Moonride", "release_date": "2026-09-09", "type": "promotional single"},
    {"group": "hearts2hearts", "release_name": "ICONIC HEART (Korean Ver.)", "release_date":"2026-10-05", "type": "digital single"},
    {"group": "hearts2hearts", "release_name": "Candy Box Lover", "release_date": "2026-10-11", "type": "soundtrack single"},
    {"group": "hearts2hearts", "release_name": "Next Chapter", "release_date": "2026-10-16", "type": "promotional single"},
    {"group": "nct 127", "release_name": "BLINGY", "release_date": "2026-08-24", "type": "studio album"},
    {"group": "nct 127", "release_name": "iScreaM Vol.41 : Blingy Remixes", "release_date": "2026-09-30", "type": "remix single"},
    {"group": "nct dream", "release_name": "DREAM AFTER DREAM", "release_date": "2026-11-09", "type": "studio album"},
    {"group": "nct wish", "release_name": "Wishcat Magic Card - Wishing Star", "release_date": "2026-01-07", "type": "soundtrack single"},
    {"group": "nct wish", "release_name": "WISHLIST", "release_date": "2026-01-14", "type": "japanese mini album"},
    {"group": "nct wish", "release_name": "Same Sky", "release_date": "2026-02-27", "type": "soundtrack single"},
    {"group": "nct wish", "release_name": "Ode to Love", "release_date": "2026-04-20", "type": "studio album"},
    {"group": "nct wish", "release_name": "K-POP ScreaM 3", "release_date": "2026-05-11", "type": "remix album"},
    {"group": "nct wish", "release_name": "RE:WORKS 2", "release_date": "2026-10-08", "type": "remix album"},
    {"group": "nct wish", "release_name": "I SPY", "release_date": "2026-10-12", "type": "mini album"},
    {"group": "wayv", "release_name": "Vision Wings", "release_date": "2026-08-10", "type": "mini album"}
])

"""Choose Main Types of The Realeses"""
#print(realeses['type'].unique())
releases['is_main_releases'] = releases['type'].isin(MAIN_TYPES)

# Sort Data with group and realese_date
releases = releases.sort_values(['group', 'release_date']).reset_index(drop=True)

# Add realese_id from Number 1
releases.insert(0, "release_id", range(1, len(releases) + 1))

# Save to CSV Format
if not releases.empty:
  try:
    file_path = "data/raw/releases.csv"
    releases.to_csv(file_path, index=False)
    print(f"Sukses! {len(releases)} baris data tersimpan di {file_path}")

  except Exception as err:
    print(f"Gagal menyimpan file: {err}")
else:
  print("Data kosong, tidak ada yang disimpan.")


print(releases.head())



