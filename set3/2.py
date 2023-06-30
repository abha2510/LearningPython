
name_age_dict = {}


def add_name_age(name, age):
    name_age_dict[name] = age

def update_age(name, new_age):
    if name in name_age_dict:
        name_age_dict[name] = new_age


def delete_name(name):
    if name in name_age_dict:
        del name_age_dict[name]


add_name_age("John", 25)
print(name_age_dict)

update_age("John", 26)
print(name_age_dict)

delete_name("John")
print(name_age_dict)
