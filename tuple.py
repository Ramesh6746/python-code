t1=(1,2,3,0,45,22,34,32)
t=()
for i in t1:
    if i<i+1 :
        t=(i)
        if i>i+1:

        
         t=(i+1)
print(t)
print(min(t1))
print(min(t1))



# import code
# from typing import Dict


# def add(a,b):
#     return a+b
# print(add(23,22))
# total = add(33,22)
# print(total)

# def char(a):
#     return a[-1:]
# print(char("ramesh"))
    
# def cha(aa):
#     return aa[::-1]
    
# all=cha('rameshfghjk')
# print(all)

# def ch(aa):
#     return aa[::2]
# print('goood')
# print(ch("ramesh"))
# # even
# def even(a):
#     if a%2==0:
#         return 'even'
#     else:
#         return 'odd'
# a=45678907654
# print(even(a))
        
# # gratest number
# def gratest(a,b):
#     if a<b:
#         return 'gratest number :b=',b
    
#     else :
#         return 'gratest number :b=',a
# a=23
# b=34
# print(gratest(a,b))

# def find_gratest(a,b,c,d,f):
#     if a>b and a>=c and a>=d and a>=f:
#         return 'a',a
#     elif b>=c and b >=d and b>=f and b>=a :
#         return b
#     elif c>=d  and c>=f and c>=b and c>=a :
#         return c
#     elif d>=f and d>=a and d>=b and d>=c :
#         return c
#     else:
#         return  f

# t=find_gratest(1,2,12,3,0)
# print(f"gratest number is : {t} ")
        

# # palindrom

# def palindrom(pali):
#     s=''
#     for i in pali:
#         s=i+s
#     if s==pali:
#         return 'string is palindrom :',s
#     else:
#         return 'string is not palindrom :',pali

# print(palindrom('pal'))
# '''
# # reverse 
# i =2345
# rev=0
# while(i>0):
#     rev=(rev*10)+i%10
#     i=i//10
# print(rev)'''


# def reverse(i):
#     rev=0
#     while i>0:
#         rev=(rev*10) + i%10
#         i=i//10
        
#     return(rev)
# r=reverse(6789)
# print(r)


# def palin(i):
#     orig=i
#     rev=0
#     while i>0:
#         rev=(rev*10)+i%10
#         i=i//10
#     if rev==orig:
#         return "palindrom no :", rev
#     else:
#         return "not palindrom no :",orig
# print(palin(121))

# # prime number 
# '''def prime(n):
#     for num in range(1,n):
#         if num>1:
#             for i in range(2,num):
#                 if num%i==0:
#                     break
#             else:
#                 print(num , end=" ")

# prime(50)

# def checkprime(n):
#     i=1
#     count=0
#     while i<=n:
#         if i%n==0:
#             count = count+1
#         i=i+1
#     if (count==2):
#         print('prime no :',count)
#     else:
#         print('not prime no :',count)
# print(checkprime(7))'''
# n=5


# i=1
# count=0
# while i<=n:
#     if i%n==0:
#         count = count+1
#     i=i+1
# if(count==2):
#     print('prime no :',n)
# else:
#     print('not prime no :',n)


# n=112
# i=2
# x=0
# while i<n:
#     if n%i==0:
#         x=1
#         print(n,'not prime no :')
#         break
#     i=i+1
# if x==0:
#     print(n,'is prime no :')

# n=27
# i=1
# count=0
# while(i<=n):
#     if i%n==0:
#         count=count+1
#     i=i+1
# if count==2:
#     print('prime no is',n)
# else:
#     print('not prime no ',n)


# d={'k1':'v1','k2':'v2','k3':'v3','k4':'v4','k5':'v5','k6':'v6'}
# l=['k','k1','k2','k3']
# stu_dict={i:f'd'for i in l}

# print(stu_dict)
def hello():
    print("hello")
hello()
def add_10(x):
    return x+10
print(add_10(10))

def even_add(x):
    if x%2==0:
        print("even number")
    else:
        print("not even")
even_add(12)
g=lambda x:x*x*x
print(g(10))

r5 