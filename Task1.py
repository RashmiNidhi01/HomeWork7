from random import randint
from random import seed
list=[]
seed(2020)

for i in range(0,20):
	value = randint(100, 120)
	list.append(value)

print(list)

#median
n = len(list) 
list.sort() 
  
if n % 2 == 0: 
    med1 = list[n//2] 
    med2 = list[n//2 - 1] 
    avg = (med1 + med2)/2
else: 
    avg = list[n//2] 
print("The Median is: " + str(avg))

# mode
list.sort()
list2=[]
i = 0
while i < len(list) : 
    list2.append(list.count(list[i])) 
    i += 1

dic1 = dict(zip(list, list2))
dic2={j for (j,k) in dic1.items() if k == max(list2) } 
  
print("The Mode is :" + str(dic2))