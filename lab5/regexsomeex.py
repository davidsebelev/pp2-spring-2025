import re


txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)
#ищет начинается ли с the или заканчивается spain


text = "rustam ggnc"
x = re.findall("[a-z]", text)
print(x) #вывести все буквы в интервале от a-z

texti = "that will be cost 300 bucks"
z = re.findall("\d", texti)
print(z) #вывести все числа

textik = " world hello"
y = re.findall("he..o", textik)
print(y) #вывести слово начинается с 2х букв до последей буквы ну и ищет подохдящие

texto = "hello planet"
#check if the string starts with hello
#check if the string ends with planet
x = re.findall("^hello", texto)
z = re.findall("planet$", texto) 
if x:
    print("YEs")
elif z:
    print("NO")


textis = "hellniggerso"
h = re.findall("he.*o", textis)# тут разница с he..o то что можно любое слово всунть в этот промежуток
print(h)

textis = "hello"
h = re.findall("he.+o", textis) # один или более символов
print(h)

txt = "hello"
z = re.findall("he.?0", txt)
print(z) #zero or one occurence like 1 or 0

txt = "hello"
z = re.findall("he.{2}o", txt) # найджи слово от he до o и еще любые 2 символа по середине
print(z)

import re

txt = "The rain in Spain falls mainly in the plain!"

#Check if the string contains either "falls" or "stays":

x = re.findall("falls|stays", txt)

print(x)

if x:
  print("Yes, there is at least one match!")
else:
  print("No match")