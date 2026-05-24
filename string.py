string ='I am learing python and i NEED to complete in days'
print(string.capitalize())
print(string.casefold())
B='akhil'
print(B.center(50))
print(string.count('a'))
c='Akhilsai.com {}'
print(c.endswith('.com'))
print(string.find('y'))
print(c.format('company'))
print(string.index('a'))
d='akhil'
#print(d.isalnum())
#print(d.isalpha())
#print(string.islower())
#print(string.isupper())
#print(string.isprintable())
# print(string.isspace())
print(d[0::5])
print(string.split())
text = "xyx     xxpythonxy"

print(text.strip("yx"))
print("xyPythonyx".strip("xy"))
print("mississippi".strip("mis"))
print("###Hello###".strip("#"))
print("abcPythonabc".removeprefix("abc"))