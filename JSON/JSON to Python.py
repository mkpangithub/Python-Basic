import json

x = {
    "name": "John",
    "age" :  30,
    "city": "India"
}

y = json.dumps(x)

print(y)