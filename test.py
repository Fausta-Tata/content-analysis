import pandas as pd

path = r"C:\Users\faust\Downloads\dataset_tiktok-scraper_2026-11-18_16-46-52-314.csv"

df = pd.read_csv(path)
df["createTimeISO"] = pd.to_datetime(
    df["createTimeISO"],
    errors="coerce",
    utc=True
)
print(df["createTimeISO"].max())
print(df["createTimeISO"].min())
print(len(df))
