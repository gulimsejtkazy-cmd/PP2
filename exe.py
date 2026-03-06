import re

pattern = r"\b[A-Z][a-z]+\b"
text = "London paris Astana"
print(re.findall(pattern, text))