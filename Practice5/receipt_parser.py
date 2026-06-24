import re
import json
import os


# 1. Read raw.txt
current_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_dir, "raw.txt")

with open(file_path, "r", encoding="utf-8") as file:
    text = file.read()


# Helper function: convert price string to float
# Example: "18 009,00" -> 18009.00
def price_to_float(price):
    return float(price.replace(" ", "").replace(",", "."))


# 2. Extract all product prices from the receipt
# This pattern finds prices after the word "Стоимость"
pattern_prices = r"Стоимость\s+(\d[\d\s]*,\d{2})"
all_prices = re.findall(pattern_prices, text)


# 3. Find all product names
lines = text.splitlines()
product_names = []

for index, line in enumerate(lines):
    line = line.strip()

    # Product number looks like: 1. or 2. or 10.
    if re.fullmatch(r"\d+\.", line):
        if index + 1 < len(lines):
            product_name = lines[index + 1].strip()
            product_names.append(product_name)


# 4. Extract total amount from receipt
total_match = re.search(r"ИТОГО:\s*([\d\s]+,\d{2})", text)
total_amount = total_match.group(1) if total_match else None


# 5. Calculate total amount from extracted product prices
calculated_total = sum(price_to_float(price) for price in all_prices)


# 6. Extract date and time information
pattern_datetime = r"Время:\s+(\d{2}\.\d{2}\.\d{4})\s+(\d{2}:\d{2}:\d{2})"
datetime_match = re.search(pattern_datetime, text)

date = datetime_match.group(1) if datetime_match else None
time = datetime_match.group(2) if datetime_match else None


# 7. Find payment method
payment_match = re.search(r"Банковская карта|Наличные", text)
payment_method = payment_match.group() if payment_match else None


# 8. Combine product names and prices
products = []

for name, price in zip(product_names, all_prices):
    products.append({
        "name": name,
        "price": price
    })


# 9. Create structured output
output_data = {
    "products": products,
    "product_count": len(products),
    "prices": all_prices,
    "total_amount_from_receipt": total_amount,
    "calculated_total": round(calculated_total, 2),
    "date": date,
    "time": time,
    "payment_method": payment_method
}


# 10. Print structured output as JSON
print(json.dumps(output_data, indent=4, ensure_ascii=False))


# 11. Save structured output to JSON file
output_path = os.path.join(current_dir, "receipt_output.json")

with open(output_path, "w", encoding="utf-8") as file:
    json.dump(output_data, file, indent=4, ensure_ascii=False)

print("\nStructured output was saved to receipt_output.json")