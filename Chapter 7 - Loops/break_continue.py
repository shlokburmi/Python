for i in range(100):
    if(i==34):
        break    # it will break the loop when i is 34 and will not execute the print statement for 34
    print(i)

print("Using continue")

for i in range(100):
    if(i==34):
        continue   # it will skip the current iteration and move to the next one
    print(i)
    
print("Using pass")

for i in range(100):
        pass
i=0
while(i<100):
    print(i)
    i+=1
    