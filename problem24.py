text = "C# Sharp Program to display the bangladeshgove following pattern using the alphabet."
new_text = list(text.split(" "))

# way one
def Sorted(new_text):
    lis2 = sorted(new_text, key=len)
    return lis2


ss = str(Sorted(new_text)[-1:])
print(ss)
print(type(ss))

# way two
word = ""
count = 0
for i in new_text:
    if len(i) > count:
        word = i
        count = len(i)
print(word)

