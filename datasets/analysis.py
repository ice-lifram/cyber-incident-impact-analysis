import pandas as pd

master = pd.read_csv("incidents_master.csv")
market = pd.read_csv("market_impact.csv")

# Standardize tickers
for df in [master, market]:
    df["stock_ticker"] = (
        df["stock_ticker"]
        .astype(str)
        .str.strip()
        .str.upper()
    )

print("=" * 50)
print("INCIDENT MASTER")
print("=" * 50)

print("Rows:", len(master))
print("Unique Tickers:", master["stock_ticker"].nunique())

print("\nTop 20 Tickers:")
print(master["stock_ticker"].value_counts().head(20))

print("\n")

print("=" * 50)
print("MARKET IMPACT")
print("=" * 50)

print("Rows:", len(market))
print("Unique Tickers:", market["stock_ticker"].nunique())

print("\nTop 20 Tickers:")
print(market["stock_ticker"].value_counts().head(20))
