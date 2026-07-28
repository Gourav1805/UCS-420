print("hello world")
a = 12
b = 23
print(a+b)
print("Gourav")
print("Garv")
print("Madaan")

print("Garv" + " "+ "madaan")
print("Garv" + " " , b)

# using for loop
for i in range(1,11):
    print(i)

print("table of 5")

for i in range(1,11):
    print(5*i)

i=1

while i <= 4:
    print(4*i)
    i+=1

num =0 
for i in range(1,11):
    num+=i
print(num)
    
print(list(range(1,11)))
print(list(range(1,10,2)))
print(list(range(3,19,3)))
print(list(range(-10,-20,3)))
print(list(range(-10,-20,-3)))

# input a number
num= int(input("give a number"))
for i in range(1,num):
    print(7*i)
