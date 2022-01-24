import sys
def function():
    for x in range(10):
        yield x**2

g1=function()
print(g1)
def integers_starting_from(n):
    while True:
        yield n
        n +=1

x=[1,2,3,4,5,6,7,8,9,10]
print(sys.getsizeof(x))
print(sys.getsizeof(range(1,11)))
for element in x:
    print(element)
print("-"*67)

for i in range(1,11):
    print(i)


