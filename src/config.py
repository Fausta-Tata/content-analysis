from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
RAW = ROOT / "data" / "raw"
PROCESSED = ROOT / "data" / "processed"
ENV_PATH = ROOT / ".env"

CUTOFF = "2025-01-01"


CHANNELS = {
    "aespa"         : "UC9GtSLeksfK4yuJ_g1lgQbg",
    "riize"         : "UCdVD0MsYecQaIE5Ru-pOIQQ",
    "hearts2hearts" : "UC7Q3HUnJA3nvjZR2JeMn2Cw",
    "nct_dream"     : "UCXURHJRGr4-EB3l87kcbElw",
    "nct_127"       : "UCk2E0dbAyEJWnrN2bbQOcbg",
    "nct_wish"      : "UCiZqWVAeChfqlom5ZPR3ZJA",
    "way_v"         : "UC-ZHt5Zgadfx-B1CM63Lqew"
}


PRE_DAYS = 30
DURING_DAYS = 14
POST_DAYS = 42

MAIN_TYPES = ["single album", "mini album", "studio album"]