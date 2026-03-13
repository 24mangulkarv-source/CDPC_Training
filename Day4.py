def add():
   a=int(input("Enter value:"))
   b=int(input("Enter value:"))
    res=a+b
    print(res)
if_name_ == '_main_';
    add()
    
def add(x,y):
    res=x+y
    print(res)
 if_name_ == '_main_';
    a=int(input("Enter value:"))
    b=int(input("Enter value:"))
    add(a,b)
  
def add(x,y):
   res=x+y
   return res

 if __name__ == '__main__':
    a=int(input("Enter value:"))
    b=int(input("Enter value:"))
    res=add(a,b)
    print(res)
    
  
def arithmatic(x,y):
   res1=x+y
   res2=x-y
   res3=x*y
   res4=x/y 
   return res1,res2,res3,res4

if __name__ == '__main__':
    a=int(input("Enter value:"))
    b=int(input("Enter value:"))
    r1,r2,r3,r4=arithmatic(a,b)
    print(r1,r2,r3,r4)    
  
ls=[]
print(type(ls))

ls=list()
print(type(ls))

ls=[11,22,33,44,55,66]
print(ls)
for i in range(len(ls))
    print(ls[i])
    
for x in ls:
    print(x)

ls=[11,22,33,44,55,66,77,88]
ls.append(77)
ls.append(88)
print(ls)
print(ls[0])
print(ls[-8])
print(ls[2:5])
print(ls[3:6])
print(ls[:6])
print(ls[2:])
print(ls[:])
print(ls[::1])
print(ls[::2])
print(ls[::-2])
print(ls[::-1])
print(ls[::-3])

s="Vidhi"
print(s[2:4])
rev=s[::-1]
print(rev)

no=2345
s=str(no)
s=s[::-1]
int(s)
int(s)
print(type(s))

#reversr string without shortcut without inbuild function
 s = vidhi
rev = ""
for i in s:
    rev = i + rev
print("Reverse string is:", rev)
 
 
 
