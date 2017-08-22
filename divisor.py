x = int(input("Enter x value"))
y = range(1, 100)
divisor=[]
for i in y:
    if (i%x)==0:
        divisor.append(i)

print(divisor)
