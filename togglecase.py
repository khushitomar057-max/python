str1=input("enter any string:")
result=""
for ch in str1:
    if "a"<= ch <="z":
        result+= chr(ord(ch)-32)
    elif"A"<= ch<= "Z":
        result+= chr(ord(ch)+32)
    else:
        result+= ch
            
print(" given string in toggle case:",result)
