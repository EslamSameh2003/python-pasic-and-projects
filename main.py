from math import * #module or library
from datetime import date
name = 'eslam'
age =  20
num =-2
print(name.replace("eslam","samer"))
print("my age is " + str(age)) #مينفعش تطبع جمله مع int علشان كده حولنا age ل string
print (name.index("a"))
print(abs(num))
print(abs(pow(num,7)))
print(max(4,8,54,565,78,87,98*87))
print(round(3.4))
#/////////// input  ///////////
"""
v=input("your name : ")
age2=str(input("your age is "))
print( "hello mr: " + v + " and age is : "+ age2)
"""
#/////////////CALCULATOR////////
"""
n1=int(input("num1 = "))
n2=int(input("num2 = "))
sum= n1+n2
print(sum)
"""
# //////LIST//////
f=["eslam","mahmoud","hi","samer","ahmed"]
number=[1,7,3,7,5,10,56]
print(f[0])
print(f[1:2])
print(f[1:])
print(f[:-1])
print(f[-1:])
f.append(2)   # بتضيف index  الاخر
f.insert(1,"hi")   # بتضع اللي انت عايزه ف list وفي مكان معين
print(f)
f.remove("mahmoud")   # بتحذف ال index اللي انت عيزه
print(f)
f.pop()    # بتحذف اخر index
print(f)
i=f.pop()  # بتوريك اخر index تم حذفه
print(i)
print( f.index("hi")) # بتوريك مكان اللي انت عايزه ف list
print (f.count("hi"))  # بتوريك عدد الكلام اللي موجود
f.sort() # ترتيب ال index حسب الحروف او الارقام
print(f)
number.sort()
print(number)
k=f.copy()
print(k)
f.clear()  # بتحذف محتوى list كلها
print(f)
# ////////////// Tuples /////////
cordinate=(4,5)   # ال value لا تتغير
print(cordinate)
# //////////////////// args متغيرات  ///////////
# زي ال tuple
def sum(*args): # بتعمل براميترات زي ما انت عايز وقت الرن تيم
    result = 0
    for x in args:
        result+=x
    return result

print(sum(4,7,4,5,8,5,7,5,8,4,6,58,1000000000))

#////////////////////////// kwargs ( key ward arguments ) ///////////////
# بتعمل زي ال dectionary
# هيجمع ال values اللي ما بداخل ال key ward argument
def use_kwargs(**kwargs):
    result=""
    for x in kwargs.values():
        result+=x
    return result
print(use_kwargs(e="eslam",s=" samer",a=" ahmed"))

def use_args_and_kwargs(x,y,*args,option=True,**kwargs):
    print(x,y)
    print(args)
    print(option)
    print(kwargs)

x=use_args_and_kwargs(4,5,"1 arg","2 arg",option=True,e="eslam",s="samer",m="mahmoud")
print(x)
#//////////////////// unpacking ////////////////////////////////////
# بتوريك اللي جوه ال list بس من غير اقواس
print("///////// unpacking ///////")
list=[1,2,3]
print(list)
print(*list) #unpacking
#//////////////// unpacking with args(tuples)/////
def sum_args_with_unpacking(*args):
    sum=0
    for x in args:
        sum+=1
    return sum
list1=[1,2,3,4,5,6]
list2=[1,2,3,4,5,6]
list3=[1,2,3,4,5,6]
print(sum_args_with_unpacking(*list1,*list2,*list3))
#////////////////
a,*b,c=list1
print(a) # a=1
print(b) # b=[2,3,4,5]
print(c) # c=6
merge_list=(*list1,*list2)    # بتضع اكتر من lists  ف list واحده(بتدمجهم)
print(merge_list)
#//////////////// unpacking with kwargs(dictionary) ////////////
dic1={"a":1,"b":2}
dic2={"c":3,"d":4}
merge_dictionary={**dic1,**dic2}
print(merge_dictionary)
str=[*"eslamsameh","eslam"]
print(str)
# ///////////////// function ///////////////////////////////
# def + func_name():
     # indentation   مسافه فارغه
""""
def input_name():
    na=input("what's your name ")
    print("my name is " + na)
input_name()
def input_name(na,age):
    print("my name is " + na+ " and my age is "+str(age))
input_name("eslam",20)
"""
# return statement
def muliple(nu):
    m=nu*nu
    return m
mu=muliple(5)
print(mu)
#///////////////// Conditions ////////////////////////////////
# and / or / and not / ==
is_hungry=False
wants_to_eat=True

if    is_hungry == wants_to_eat:
    print ("eat")
elif  is_hungry and not wants_to_eat:
    print (" eat to live")
elif  not is_hungry and wants_to_eat:
    print("i will kill you")
else:
    print("not eat")
# ////////////// Comparisons Operators/////////
# > / < / >= / <= / == / !=

def max_num(num1,num2,num3):
    if num1>=num2 and num1>=num3:
        return num1
    elif num2>=num1 and num2>=num3:
        return num2
    else:
        return num3
print(max_num(54,7,4))
#///////////////// Dictionaries ///////////
# بتستخدم طريقة الkey :value يعني كل قيمة ليها المفتاح بتاعها
convert ={
    "jan":"january",
    "fab":"faburary",
    "mar":"march"
}
print(convert["jan"])
print(convert.get("mar","aug is not here"))
#////////////////// Loops //////////////////////////////
#/// while ///////
i=1
while i<=10:
    i += 1
    if i==6:
        continue  # تعمل على skip للحاجه اللي انا عيزها
        break     # بتخرجني خالص
    print(i)
else:
    print ("end loop")

#////// for ///////////
for x in "samer":
    print(x)

name ="ali"
for x in name:
    print(x)

for x in range(10): # بتعد من 0 ل 9
    print(x)
for x in range(22,25):
    print(x)
buddies=["eslam","samer","ahmed"]
print(len(buddies))   # بتوريك عدد ال list
print(len("nknlknkjnkn"))   # بتوريك عدد ال اللي انت كتبه

for x in range(len(buddies)):
    print(x)
for x in range(len(buddies)):
    print(buddies[x])

for s in range(10):
    if s % 2==0:
        print("num of even = " , s)
    else:
        print("num of odd = " , s)
#////////////////////// 2 Diminial array and listed loops/////////////////
list=[
    [1,2,3],
    [4,5,6],
    [7,8,9]

]
for i in list:
    for j in i:
        print(j)
#/////////////////// Error(try except)//////////////

'''''
try:
    numb=int(input("input num"))
    print(numb)
except :       # defult
    print("not number")

try:
  #  x=10/0
    v=input()
    print(v)
except ValueError as err:   # special
    print(err)
except ZeroDivisionError as err1:
    print (err1)
    '''
#////////////////// Reading Files ///////////////////
# open("file name.extenition ","mode literal")
#work_file = open('file.txt','r')
#for i in work_file.readlines():
 #   print(i)

#work_file.close()
#////////////////////////// Writing Files///////////
'''
r : تقرأ الملف
r+: بتقرا وتضيف  اللي موجود ف اول سطر
a : بتضيف كلام ف اخر الملف ولة الملف مش موجود ممكن تنشأه
a+: بتقرا وتضيف ع اللي موجود ف اخر السطر
w : بتمسح اللي موجود وتكتب من اول خالص
w+: بتقرا وتمسح اللي موجود وتكتب من اول خالص

'''
#work_file = open('file.txt','a')
#print(work_file.write("eslam\n"))
#work_file.close()
#////////////////////////// Python Classes & Objects /////////////
from Employee import employee

e1=employee ("eslam",20)
print(e1.name,e1.age)
#//////////////////////////////inheritence//////////////
from Doctor import doctor
from familydoctor import family_doctor

d1=doctor()
d1.stydied_yers()
d1.paid_who()
d2=family_doctor()
d2.work_where()
d2.paid_who()
#//////////////////////////////////////////////////
# encapsulation
# هي تحتوي ع getter and setter ال getter هو انك بمقدورك ان تغير وتضع مافيه اما setter فقط ان ترى ماحدث دون ولا تستطيع التغيير
#///////////////////////
#abstraction
# وظيفتها انك ترى الشكل العام للحاجه ولاتعلم مايحدث ما بداخلها مثل العربية تتحرك ولكن هل تعلم ما يحدث لكس تتحرك ؟؟؟
#ويستخدم ف تقسبم التاسك حيث لاتهتم بما يحدث لباقي الكود فقط اهتم ب الجزء المطلوب منك
#وتنقسم الي interface and implementation
#interface طريقة من خللها اقدر اخد اواعرف معلومه من كلاس تاني من غير ما اعرف طريقة عمل الكلاس كله
#وهي طريقة للتحدث بين الكلاس
#implementation
# هي كريقة لمعرفة مابداخل الكلاس وكبف يعمل
#//////////////////////////////////////////////practice//////////
class Student:
    no_of_student=0 # class attribute
    def __init__(self,name="none",age=0,course="none"):  #constructor
        self.__name = name    # ( __ ) -> private
        self.__age = age
        self.__course = course
        Student.no_of_student+=1
    def descripe(self):      # inistance method
        print(f"my name is {self.__name} and my age is {self.__age} and my course is {self.__course} ")
        #print("my name is {} and my age is {} and my course is {}".format(self.__name,self.__age,self.__course))
    def set_name(self,new_name):
        self.__name=new_name

    def get_name(self):
        return self.__name
#///////////////// class method ///////////////////
#@classmethod  بتقدر تعدل ع class attribute
    @classmethod #decorator
    def inittfrombearthtear(cls, name, birth_year):
        return cls(name, date.today().year - birth_year) # بترجعلك الاسم و عمرك

#//////// opjects /////////////
s1=Student("Ahmed",45,"Cs")
s2=Student.inittfrombearthtear("Eslam",2003)
#s1.set_name("samer")
#//////// print ///////////////
#print(s1.get_name())
s1.descripe()
s2.descripe()
#////////////////////////// static method ///////////////
