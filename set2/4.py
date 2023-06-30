result1 = ''
result2 = ''
str1 = 'PyNaTive'

for ch in str1:
    if ch.islower():
        result1 += ch
    elif ch.isupper():
        result2 += ch

res = result1 + result2
print(res)

   
