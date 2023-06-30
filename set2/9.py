sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New York"
}

keys = ["name", "salary"]
dict = {}

for key in keys:
    if key in sample_dict:
        dict[key] = sample_dict[key]

print(dict)
