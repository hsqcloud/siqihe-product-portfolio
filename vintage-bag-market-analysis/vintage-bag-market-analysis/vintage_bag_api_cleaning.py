import pandas as pd

# Mock product data
data = [
    {"title": "Vintage Dior Bag", "price": 650, "brand": "Dior", "color": "Black"},
    {"title": "Gucci Classic", "price": 720, "brand": "Gucci", "color": "Brown"},
    {"title": "LV Speedy", "price": 820, "brand": "Louis Vuitton", "color": "Beige"},
    {"title": "Vintage Fendi", "price": 430, "brand": "Fendi", "color": "Black"}
]

df = pd.DataFrame(data)

# Add price category for analysis
df["price_category"] = pd.cut(df["price"], bins=[0, 500, 750, 1000], labels=["Low", "Mid", "High"])

# Grouped summary
summary = df.groupby(["brand", "price_category"]).size().reset_index(name="count")

print(summary)
