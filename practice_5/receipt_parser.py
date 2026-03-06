#1 
import re

pattern = r"^ab*$"
print(bool(re.match(pattern, "abbb")))  
# re.match checks if the entire string matches the pattern.
#2
import re

pattern = r"^ab{2,3}$"
print(bool(re.match(pattern, "abb")))   # True
print(bool(re.match(pattern, "abbbb"))) # False
#3
import re

pattern = r"\b[a-z]+(_[a-z]+)+\b"
text = "hello_world test_string ABC"
print(re.findall(pattern, text))#returns all matches
#4
import re

text = "Hello World, This Is Python"

matches = re.findall(r"[A-Z][a-z]+", text)

print(matches)
#5
import re

pattern = r"^a.*b$"
print(bool(re.match(pattern, "axxxb")))  # True
#6
import re

text = "Hello, world. How are you?"

new_text = re.sub(r"[ ,\.]", ":", text)

print(new_text)
#7
import re

def snake_to_camel(text):
    return re.sub(r"_([a-z])", lambda m: m.group(1).upper(), text)

print(snake_to_camel("hello_world_test"))
#8
import re

text = "HelloWorldTest"
result = re.split(r"(?=[A-Z])", text)
print(result)
#9
import re

text = "HelloWorldTest"
result = re.sub(r"(?<!^)([A-Z])", r" \1", text)
print(result)
#10
import re

def camel_to_snake(text):
    return re.sub(r"([A-Z])", r"_\1", text).lower()

print(camel_to_snake("helloWorldTest"))