tuple_list = [("John", 25), ("Jane", 30)]
res=''
for name, age in tuple_list:
   res += f"{name} is {age} years old. "

res = res.strip() 

print(res)