# # # # # # class phone:
# # # # # #     def make_call(self):
# # # # # #         print("make the call ")
# # # # # #     def playing_game(self):
# # # # # #         print("play the game :")
# # # # # # p1 = phone()
# # # # # # p1.make_call()
# # # # # # p1.playing_game()

# # # # # # parameters passs
# # # # # from ast import Return
# # # # # from typing_extensions import Self

# # # # # from pygame import Color


# # # # # class car :
# # # # #     def brand(self,BMW,TATA):
# # # # #         self.BMW = BMW
# # # # #         print(BMW)
# # # # #         self.TATA = TATA
# # # # #         print(TATA)
# # # # #         return BMW,TATA
# # # # #     def cost(self,prise, color):
# # # # #         self.prise = prise
# # # # #         print(prise)
# # # # #         self.color = color
# # # # #         print(color)
        

   
    
# # # # # p2 = car()
# # # # # p2.brand('BMW NO 1 CAR','TATA NO 2 CAR  ')
# # # # # p2.cost(12333432,'blue')

# # # # #  creating a class with constructor


# # # # # class Employee:
# # # # #     def __init__( self,name,age,salary,gender):
# # # # #         self.name = name
# # # # #         self.age = age
# # # # #         self.salary = salary
# # # # #         self.gender = gender

# # # # #     def employee_details(self):
# # # # #         print("Name of employee is ",self.name)
# # # # #         print("age of employee is ",self.age)
# # # # #         print("salary of employee is ",self.salary)
# # # # #         print("gender of employee is ",self.gender)

# # # # # e1 = Employee('stark', 22, 35000, 'male')
# # # # # e1.employee_details()


# # # # # inheritance

# # # # class vehicle:
# # # #     def __init__(self,cost ,milease):

# # # #         self.cost = cost
        
# # # #         self.milease = milease
# # # #     def show_car_details(self):
       
# # # #         print("cost of car is ",self.cost)
       
# # # #         print("milease of car is ",self.milease)
# # # # v1 = vehicle(2550000, 56)
# # # # v1.show_car_details()




# # # # class Car(vehicle):
# # # #     def show_car(self):
# # # #         print("I am a car")

# # # # c1 = Car(12000,34)
# # # # c1.show_car_details()
# # # # c1.show_car(
# # # def rev(s, l, r) :
# # #     while l<r :
# # #         temp = s[l]
# # #         s[l] = s[r]
# # #         s[r] = temp
# # #         l += 1
# # #         r -= 1
# # # def reverse(s):
     
# # #     temp = ['']*len(s)
# # #     x = 0
     
# # #     for i in range(len(s)) :
# # #         if s[i] >= 'a' and s[i] <= 'z' or s[i] >= 'A' and s[i] <= 'Z' :
            
# # #             temp[x] = s[i]
# # #             x += 1
# # #     rev(temp, 0, x)
     
# # #     lst = list(s)
# # #     x = 0
     
# # #     for i in range(len(s)) :
# # #         if s[i] >= 'a' and s[i] <= 'z' or s[i] >= 'A' and s[i] <= 'Z' :
            
# # #             lst[i] = temp[x]
# # #             x += 1
     
# # #     revStr = ""
# # #     for i in range(len(s)) :
# # #         revStr += lst[i]
         
# # #     print("reverse string is :",revStr);
     

# # # if __name__ == "__main__" :
     
# # #     s="Ab,c,de!$"
     
# # #     reverse(s)



# # # dict1 = {"a1":10,"b2":20,"c3":30} 
# # # for k,v in dict1.items():

# # #     dict1[k]= v+1
# # # print(dict1)


# # # def Convert(string):
# # #     list1=[]
# # #     list1[:0]=string
# # #     return list1
# # # # Driver code
# # # str1="[1,2,'3',4,'ab']"
# # # print(Convert(str1))


# # # import re

# # # def Convert(string):
# # #     return re.findall('[a-zA-Z]', string)
      
# # # # Driver code
# # # str1="[1,2,'3',4,'ab']"
# # # print("List of character is : ",Convert(str1))



# # # 2
# # # 3
# # # 4
# # # str1="9 8 7 6 5 4 3 2 ]"
# # # list1=list(str1.split())
# # # list2=list(map(int,list1))
# # # print(list2)
# # # overloading 
# # class vehicle:
# #     def __init__(self,mileage,cost):
# #         self.mileage = mileage
# #         self.cost = cost

# #     def show_details(self):
# #         print("i am a vehicle")
# #         print('mileage of vehicle is ',self.mileage)
# #         print('cost of vehicle is',self.cost)



# # class car(vehicle):
# #     def __init__(self, mileage, cost,tyres,hp):
# #         super().__init__(mileage, cost)
# #         self.tyres = tyres
# #         self.hp = hp
# #     def show_car_details(self):
    
# #         print("i am a vehicle")
# #         print('tyres of vehicle is ',self.tyres)
# #         print('hp of vehicle is',self.hp)
# # c1 = car(12,234567, 4, 4)
# # c1.show_details()
# # c1.show_car_details()


# # class parent1():
# #     def assign_string_one(self,str1):
# #         self.str1 =str1
# #     def show_string_one(self):
# #         return self.str1


# # class parent2():
# #     def assign_string_two(self,str2):
# #         self.str2 = str2
# #     def show_string_two(self):
# #         return self.str2

# # class derived(parent1,parent2):
# #     def assign_string_two(self,str3):
# #         self.str3 = str3
# #     def show_string_three(self):
# #         return self.str3


# # d1 = derived()
# # d1.assign_string_one('hello')
# # d1.assign_string_two('str3')


# # d1.show_string_one()
# # d1.show_string_two()
# # d1.show_string_three()
# # multilevel inheritance
# class parent:
#     str1 = "python"
# class child(parent):
#     str2 = " geeks"
# class grandchild(child):
#     str3 = " hi"
# class basic(grandchild):
#     def get_str(self):
#         print(self.str1 + self.str2 +self.str3)
# person = basic()
# person.get_str()  


# # multiple inheritance
# class superclass1:
#     num1 = 5
# class superclass2:
#     num2 = 5
# class subclass(superclass1,superclass2):
#     def addition(self):
#         print(self.num1 + self.num2)
# obj = subclass()
# obj.addition()


# class sup:
#     num1=5
# class sup1:
#     num2=5
# class sub(sup,sup1):
#     def add(self):
#         print(self.num1+self.num2)
# ob=sub()
# ob.add()


class phone:
    def body(self):
        print("hii..")
    def index(self):
        print("noo..")
a=phone()
a.body()
a.index()


class car:
    def body(self,color,brand):
        self.color=color
        print(color)
        self.brand=brand
        print(brand)

    def model(self,hp,power):
        self.hp=hp
        print(hp)
        self.power=power
        print(power)
    
    

c1=car()
c1.body('blue', 'bmw')
c1.model(750, 48)

class Employee:

    def __init__( self,name,age,salary,gender):
         self.name = name
         self.age = age
         self.salary = salary
         self.gender = gender

    def employee_details(self):
         print("Name of employee is ",self.name)
         print("age of employee is ",self.age)
         print("salary of employee is ",self.salary)
         print("gender of employee is ",self.gender)

e1 = Employee('stark', 22, 35000, 'male')
e1.employee_details()


class g():
    def __init__(self,r,t,y,i):
        self.r=r
        self.t=t
        self.y=y
        self.i=i
    def d(self):
        print("d is  R",self.r) 
        print("d is  T",self.t)
        print("d is  U",self.y)
        print("d is  I",self.i)

g1=g("RR",47,10,"uyhgkjhsjjhd")
g1.d()

class phone:
    def make_call(self):
        print("make a call in my phone")
    def playing_game(self):
        print("playing the game ")
p1=phone()
p1.make_call()
p1.playing_game()


def fibo_recu1(n):
    if n==1:
        return 0
    if n==2:
        return 1
    
    return fibo_recu1(n-1) +fibo_recu1(n-2)
n=8
i=1
for i in range(i,n+1):
    print(fibo_recu1(i))

def pali(n):
    s=n[::-1]
    if s==n:
        print("yes")
    else:
        print("not ")
pali("iwerti")