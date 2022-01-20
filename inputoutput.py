name=input("What is your name?")
print(name)
print("Welcome Grace.")
n=int(input("Enter a number:"))
print(n+100)
fname="gaciuki"
lname="davie"
print("name:",fname,lname)
fname="lexi"
lname="roxy."
print(fname,lname)
days={1:"monday",2:"tuesday",3:"wednesday",4:"thursday",5:"friday"}
for k,v in days.items():
    print(k,v, sep="-->")
if True:
    print("thursday",end='/')
    print(4,end='/')
    print("friday")
for n in range(10):
    print(n)
print(11%3)
print("-"*67)
print(ord("a"))
print(ord("#"))
print(ord("t"))
print(chr(23))
print(chr(90))
print(chr(35))
print("%d %s cost $%.2f'" %(6,"banana",1.74))
print("Hello, my name is %s."%"graham")
#integer conversion types
w="%d,%i,%u"%(42,35,76)
print(w)
#hexadecimal integer value
r="%x, %X" % (456,456)
print(r)
#octal integer value
t="%o"%16
print(t)
#floating point conversion types
q="%f,%F"%(3.14159,3.14)
print(q)
#exponential conversion
e="%e,%E"%(1000.0,1000.0)
print(e)
x=float("NaN")
print("%f,%e,%F,%E"%(x,x,x,x,))
y=float("inf")
print("%f,%e,%F,%E"%(y,y,y,y))
#floating point or exponential
p="%g"%0.00000000005
print(p)
m="%G"%0.00000000005
print(m)
#character conversion types
print("%c"%98)
print("[%c]"%"y")
print("%c"%8721)






