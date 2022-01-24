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

w=[1,2,3,4,5,6,7,8,9,10]
print(sys.getsizeof(w))
print(sys.getsizeof(range(1,11)))
for element in w:
    print(element)
print("-"*67)

for i in range(1,11):
    print(i)

from itertools import islice
multiples_of_four=(x*4 for x in integers_starting_from(1))
first_ten_multiples_of_four=list(islice(multiples_of_four,10))
print(first_ten_multiples_of_four)
print("*"*56)
multiples_of_three=(w*3 for w in integers_starting_from(1))
first_10_multiples_of_three=list(islice(multiples_of_three,10))
print(first_10_multiples_of_three)
for idx, number in enumerate(multiples_of_three):
    print(number)
    if idx==9:
        break
#fibonacci
import itertools
def n():
    a, b=1, 1
    while True:
        yield a
        a, b=b, a+b
first_ten_fibs=list(itertools.islice(n(), 10))
print(first_ten_fibs)
