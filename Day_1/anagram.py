str1="silent"
str2="listen"
if len(str1)!=len(str2):
    print("not anagram")
else:
    if sorted(str1)==sorted(str2):
        print("this is anagram")
    else:
     print("not a anangram")

def check(str1,str2):
    if len(str1)!=len(str2):
        print("not anagram")
    else:
        if sorted(str1)==sorted(str2):
            print("this is anagram")
        else:
            print("not a anangram")

print(check("silent","listen"))

