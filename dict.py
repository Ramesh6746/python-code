# # d={'r':1,'a':2,'m':3,'e':4,'s':5,'h':6}
# # print((d))
# # d=d.keys()

# # print(d)
# # d=d.values()
# # print(d)
# # for i in d:
# #     if i.keys:
# #         print((i))



# dict1 = {"a1":10,"b2":20,"c3":30} 
# for k,v in dict1.items():

#     dict1[k]= v*3
# print(dict1)


# dict2 = {'b1':12,'b2':23,'b3':34}
# for k,v in dict2.items():
#     print(k) 

# user ={
#     'name':'ramesh',
#     'age': 22,
#     'fav1': 'msd',
#     'fav': 'stark',

# }
# print((user))

# print(user['fav1'])

# if 'name1' in user:
#     print('present')
# else:
#     print('not present')

# for i in user.items():
#     print(i)
# # values method
# user_values =user.keys()
# print(user_values)
# # item method
# for i , j in user.items():
#     print(f"key is {i} and values {j}")
    
# # Add & delete DATA
# user['f_song'] = ['song1','song2','song3','sdf']
# print(user)
# # pop item
# pop_item = user.pop('f_song')
# print(pop_item)
# # update 
user={}
more_info = {'static':'haryana','hobbies':['coding','reading','playing cricket']}
user.update(more_info)
print(user)

# # framkeys . method  
d = dict.fromkeys((1,11,6,7,8,99,0),('unkown'))
print(d)

# # Get method


# d1 = d.copy()
# print(d1)

dict1 = {"a1":10,"b2":20,"c3":30} 
for k ,v in dict1.items():
    dict1[k]=v*4
print(dict1)
dict1 = {"a1":10,"b2":20,"c3":30}
for k,v in dict1.items():
    print(v)

print(dict1['b2'])
if 'a13' in dict1:
    print('present')
else:
    print('n0ot present')

a=dict.fromkeys(('unknown'),(1,2,3,4,5,6,7,8))
print(a)

d={'a':2,'b':3}
for k ,v in d.items():
    d[k]=v*2
print(d)

d={'suresh':456,'monu':786,'kishore':244,'john':234}
#u_id=input("enter the key :")
u_id='mon'
if u_id in d.keys():
    print('key is present in the dict')
    print("Value",":",d[u_id])
else:
    print("does not present ")


d={'suresh':456,'monu':786,'kishore':244,'john':234}
d1={'suresh1':456,'monu1':786,'kishore1':244,'john1':234}
d.update(d1)
print(d)


d={'suresh':456,'monu':786,'kishore':244,'john':234}
for k,v in d.items():
    d[k]=v*2
print(d)

d=dict.fromkeys((1,2,3,4,4,5,6,6,7),('unkoun'))
print(d)


