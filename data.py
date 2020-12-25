
# time complexity for this problem
# 1.problem
n=10
count=0
for i in range(1,n):
    i+=1
    for j in range(1,n):
        j+=1
        count+=1
        print("hello")
    print(count)
# when i=1 ,it will run 1 times
# when i=2,it will run 2 times
# total number of times count++ will run is 0+1+2+3...(N-1)
# time complexity of nested loop is equal to the number of times the innermost statement is executed
# the time complexity for this loop is O(n2)

# 2.problem
n=10
count=0
for i in range(1,n):
    i*=3
    for j in range(1,n):
        j+=1
        count+=1
        print("hi")
print(count)
# when i =n ,it will run n times.
# when i=n*3 it will run n*3 times. ans so on
# the total number of times count++ will run is n + n*3 + n*6 +...=3*n.so the time complexity  will be O(N)