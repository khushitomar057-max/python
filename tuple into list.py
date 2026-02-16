names=[("aarush","pratik"),"anita",("aman",),("aarsh",)]
boys=0
girls=0
for i in names:
    if isinstance(i,tuple):
        for j in i:
            boys+=1
    else:
        girls+=1 
print("number of boys:",boys)
print("number of girls:",girls)
