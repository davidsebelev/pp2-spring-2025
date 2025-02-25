import re

pattern = r"ab*"  
txt = input()

if re.fullmatch(pattern, txt):
    print("Совпадает")
else:
    print("Не совпадает")


#Write a Python program that matches a string that has an 'a' followed by two to three 'b'.

word = input()
pattern = r"ab{2,3}$"

if re.fullmatch(pattern, word):
    print("yes")
else:
    print("no")


#Напишите программу на Python для поиска последовательности строчных букв, соединенных подчеркиванием.


word = input()
pattern = r"[a-z]_+[a-z]+"

if re.fullmatch(pattern, word):
    print("finded")
else:
    print("not finded")


#Write a Python program to find the sequences of one upper case letter followed by lower case letters.

word = input()
pattern = r"[A-Z]+[a-z]"
if re.fullmatch(pattern, word):
    print("yes")
else:
    print("no")

#Write a Python program that matches a string that has an 'a' followed by anything, ending in 'b'.
h = input()
pattern = r"^a.*b$"

if re.fullmatch(pattern, h):
    print("yes")
else:
    print("no")

#program changing ., with :

text = "lorem ,ipsum. lorem"
result = re.sub(r"[ ,\.]", ":", text)
print(result)

#snakecase to camel

def snake_to_camel(snake_str):

    return re.sub(r'_([a-z])', lambda m: m.group(1).upper(), snake_str)


snake_string = "this_is_snake_case"
camel_string = snake_to_camel(snake_string)

print(camel_string)  

#
import re

text = "LoremIpsumDown"

parts = re.split(r'(?=[A-Z])', text)
parts = [part for part in parts if part]

print(parts)

#
import re

s = "HelloWorldPython"


result = re.sub(r'(?<!^)(?=[A-Z])', ' ', s)

print(result)  

#
import re


s = "helloWorldPython"


snake_case = re.sub(r'(?<!^)(?=[A-Z])', '_', s).lower()

print(snake_case)  



