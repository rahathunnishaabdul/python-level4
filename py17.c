print("sum of N number")
print("--------------")
SN=int(input("Enter the starting number:"))
EN=int(input(" Enter the ending number:"))
D=int(input("Enter the difference"))
print("Result")
print("---------------")
print("series")
count=0
sum=0
for i in range(SN,EN+1,D):
     print("+" ,+i)
     sum=sum+i;
     count+=1
print("sum value:",sum)
print("count value:",count)
                    
