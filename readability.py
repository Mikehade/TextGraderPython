from cs50 import get_string
import math

s = get_string("Text: ")
l = 0
d = 0
w = 1
sen = 0
spe = 0
for i in range(len(s)):
    if (s[i].isalpha()):
        l += 1
    elif (s[i].isnumeric()):
        d += 1
    elif (s[i] == ' ' and s[i + 1] != ' '):
        w += 1
    elif (s[i] == '?' or s[i] == '!' or s[i] == '.'):
        sen += 1
    else:
        spe += 1
# total no of words
#print(f"The number of words in string are : {w} ")
#print(f"The number of letters in string are : {l} ")
#print(f"The number of sentences in string are : {sen} ")

g = (l * 100) / w  # get average value of letter per 100 words
h = (sen * 100) / w  # gets value of sentence per 100 words
x = round((g * 0.0588) - (h * 0.296) - 15.8)  # use index formula to solve for grade
# print(x)
#x = math.floor(x)
if (x < 1):
    print("Before Grade 1")  # if grade is less than 1 output before grade 1
elif (x > 16):
    print("Grade 16+")  # if grade is greater than 16, output grade 16+
else:
    print(f"Grade {x}")  # if grade falls within range then output value of x
#print(f"avg of l is {g}, avg of s is {h}")