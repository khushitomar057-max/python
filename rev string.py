str1=input("enter any string:")
print("forward string")
i=0
while i<len(str1):
    print(str1[i],end="")
    i+=1
print("\n reversed string")
i=len(str1)-1
while i>=0:
    print(str1[i], end="")
    i-=1
