import re
import json

# 1. Чтение файла
with open("raw.txt", "r", encoding="utf-8") as f:
    text = f.read()

# 2. Убираем лишние переносы строк для цен
clean_text = text.replace("\n", " ")

# 3. Ищем цены
prices = re.findall(r"\d[\d\s]*,\d{2}", clean_text)
price_values = [float(p.replace(" ", "").replace(",", ".")) for p in prices]

# 4. Ищем продукты
# Подходит для формата: "1. Молоко", "2. Хлеб", даже если есть переносы строк
products = re.findall(r"\d+\.\s*([^\d]+?)(?=\d+\.|$)", text)
products = [p.strip() for p in products]  # убираем лишние пробелы

# 5. Считаем сумму
total = sum(price_values)

# 6. Дата и время (формат dd.mm.yyyy hh:mm:ss)
datetime_match = re.search(r"\d{2}\.\d{2}\.\d{4}\s\d{2}:\d{2}:\d{2}", text)

# 7. Метод оплаты
payment_match = re.search(r"(Банковская карта|Наличные)", text)

# 8. Формируем словарь с продуктами и ценами
data = {
    "products": [{"name": name, "price": price_values[i] if i < len(price_values) else None} 
                 for i, name in enumerate(products)],
    "total_calculated": total,
    "date_time": datetime_match.group() if datetime_match else None,
    "payment_method": payment_match.group() if payment_match else None
}

# 9. Вывод JSON
print(json.dumps(data, indent=4, ensure_ascii=False))