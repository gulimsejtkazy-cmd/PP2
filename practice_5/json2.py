import re
import json

# 1. Read the contents of the receipt file
with open("raw.txt", "r", encoding="utf-8") as f:
    text = f.read()

# 2. Remove newlines to handle prices that may be broken across lines
clean_text = text.replace("\n", " ")

# 3. Find all prices in the format "123,45" or "1 234,56"
prices = re.findall(r"\d[\d\s]*,\d{2}", clean_text)
# Convert price strings to float, removing spaces and replacing comma with dot
price_values = [float(p.replace(" ", "").replace(",", ".")) for p in prices]

# 4. Find product names
# Works for formats like "1. Milk", "2. Bread", even if there are line breaks
products = re.findall(r"\d+\.\s*([^\d]+?)(?=\d+\.|$)", text)
products = [p.strip() for p in products]  # Remove extra spaces

# 5. Calculate the total of all prices
total = sum(price_values)

# 6. Find date and time in the format dd.mm.yyyy hh:mm:ss
datetime_match = re.search(r"\d{2}\.\d{2}\.\d{4}\s\d{2}:\d{2}:\d{2}", text)

# 7. Find payment method: "Bank card" or "Cash"
payment_match = re.search(r"(Банковская карта|Наличные)", text)

# 8. Create a dictionary of products with their corresponding prices
data = {
    "products": [
        {"name": name, "price": price_values[i] if i < len(price_values) else None} 
        for i, name in enumerate(products)
    ],
    "total_calculated": total,
    "date_time": datetime_match.group() if datetime_match else None,
    "payment_method": payment_match.group() if payment_match else None
}

# 9. Print the dictionary as formatted JSON
print(json.dumps(data, indent=4, ensure_ascii=False))
