import re

pattern = r"^ab*$"  
print(bool(re.match(pattern, "abbb")))  



pattern = r"^ab{2,3}$"  
print(bool(re.match(pattern, "abb")))   
print(bool(re.match(pattern, "abbbb"))) 



pattern = r"\b[a-z]+(_[a-z]+)+\b"  

text = "hello_world test_string ABC"
print(re.findall(pattern, text)) 



text = "Hello World, This Is Python"
matches = re.findall(r"[A-Z][a-z]+", text)  

print(matches)  


pattern = r"^a.*b$"  

print(bool(re.match(pattern, "axxxb")))  



text = "Hello, world. How are you?"
new_text = re.sub(r"[ ,\.]", ":", text)  

print(new_text)  



def snake_to_camel(text):
    return re.sub(r"_([a-z])", lambda m: m.group(1).upper(), text)
    
print(snake_to_camel("hello_world_test"))  # "helloWorldTest"



text = "HelloWorldTest"
result = re.split(r"(?=[A-Z])", text)  

print(result) 



text = "HelloWorldTest"
result = re.sub(r"(?<!^)([A-Z])", r" \1", text)  

print(result) 


# 
def camel_to_snake(text):
    return re.sub(r"([A-Z])", r"_\1", text).lower()
   
print(camel_to_snake("helloWorldTest"))  # "hello_world_test"