

# ctrl+k+c --> comment
# ctrl+k+u --> uncomment



# \x + hex vlaue --> convert hex value to character
# \r carriage return --> replace number with ch in thesame  
#

#////////////////////////////////



print("\x45")

print("eslam\nsameh \rmorsy")

string = 'My web\nsite is Latracal \rSolution'
print(string)

print("eslam 'sameh'")

#////////////////////////////////////////
# method string

# len() --> to know number of character 

print(len("Eslam")); 

# strip() --> remove spaces from right and left
# rstrip() --> remove spaces from right 
# lstrip() --> remove spaces from  leftr 

st1="   eslam sameh  " 

print(st1.strip())
print(st1.rstrip())
print(st1.lstrip())
st2="####eslam sameh#######" 
print(st2.strip("#"))
print(st2.rstrip("#"))
print(st2.lstrip("#"))

# title() --> make all alpha from sart word capital
# capitalize() --> make all alpha from sart word capital

st3="eslam sameh and 3xion"
print(st3.title())
print(st3.capitalize())

# zfill()--> add 0 to make patern for num of digits

c,d,e= "1","11","1111"

print(c.zfill(2))
print(d.zfill(3))
print(e.zfill(5))

# uper()
# lower()
st4,st5="eslam","AXION"
print(st4.upper())
print(st5.lower())


#split () --> make a satatment to a list (array)
print("///split ////// ")
st6="eslam sameh morsy"
print(st6.split())
print(st6.split())
st7="eslam-sameh-morsy-asas-asas-asas"
print(st7.split("-",1))
print(st7.rsplit("-",3))

#center()

st8=" eslam "
print(st8.center(10))
print(st8.center(10,"&"))


#count("name for search")
#count("name for search",startIndex,Endindex)


st9="axion is a neck name for eslam in hunting,axion is famous"
print(st9.count("axion"))
print(st9.count("axion",0,30))

#swapecase() --> I->i, e->E
st10="Axion is a Neck name for Eslam in Hunting,axion is Famous"
print(st10.swapcase())

#startswith()-> is this start with(CH)
#endswith() -->is this end with(CH)

print(st10.startswith("i"))
print(st10.startswith("A"))
print(st10.startswith("a"))
print(st10.startswith("N",11,15))
print(st10.endswith("s"))

# index("ch",start,end)

st11="fdkjgdfkjfdjkjdlfk"
print(st11.index("f"))
print(st11.index("f",1,7))
print(st11.index("j"))

# find("ch",start,end)

st11="fdkjgdfkjfdjkjdlfk"
print(st11.find("f"))
print(st11.find("f",1,5))
print(st11.find("j"))


#rjust()
#ljust()

st12="eslam"
print(st12.rjust(8,"#"))
print(st12.ljust(7,"$"))

#splitlines()
st13='''line1
line2
line3
'''
print(st13.splitlines())

st14= "eslam\tsameh\tmorsy"
print(st14.expandtabs(5))

#istitle(),islower(),isspace(),isidentifier(),isalpha(), -> check is true or false

#replace(old value, newvalue ,count)

st15="axion is now is nothing but in future he will be everything"

print(st15.replace("axion","eslam",1))


# join(iterable)--> collect all in a list together

st16=["eslam","sameh","morsy"]
print("_".join(st16))

#//////////////////////////////////////////////////

#   string formatting

name="eslam"
age=20
rank=10
# placeholder [ %s --> string , %d --> number , %f --> float ] 

print("my name is %s and my age is %d and rank is %f" %  ( name , age , rank) )
# control floating
print("%.2f" %(rank))

# new way
print("my name is {} and my age is {} and rank is {}".format(name,age,rank)  )
print("my name is {:s} and my age is {:d} and rank is {:f}".format(name,age,rank)  )

# control floating
print("{:.2f}" .format(rank))

# format money
n=1654654654
print("{:_d}" .format(n))

# arrange formating

a,b,c= 10,20,30

print("number : {1} {2}   {0} ".format(a,b,c))

print("number : {1:2f} {2:d}  {0} ".format(a,b,c))

# new format
print(f"my name is {name} and my age is {age} and rank is {rank}")



#complex num

complex_num=4+5j

print(f" number ={complex_num} ")
print(f" number ={complex_num.real} ")
print(f" number ={complex_num.imag} ")

#convert number 

# int to float or complex 

print(float(20))
print(complex(20))


# float to int or complex

print(int(10.00))
print(complex(10))

#/////////////////////////////////
# list 

list_one=[1,2,3,4,5]

list_one.append(7)
print(list_one)

list_one.index(1)
print(list_one)

print(list_one[5])


# extend()

list_2=[1,2,3,4,5]
list_3=['e','c']

list_2.extend(list_3)
print(list_2)

#remove()

list_4=[1,2,3,4,5,3]

list_4.remove(3)
print(list_4)


#sort()
list_5=[1,2,3,4,5,-1,0,-2]

list_5.sort()
print(list_5)

list_5.sort(reverse=True)
print(list_5)


# reverse()
list_6=[1,2,3,4,5,"eslam",-1]
list_6.reverse()
print(list_6)

# clear ()
list_7=[1,2,3,4,5,"eslam",-1]

list_7.clear()
print(list_7)

# copy ()
list_7.append(2)

list_8=list_7.copy()
list_7.append(3)
print(list_8)

# count()

list_9=[4,5,4,5,0,5,9,9,8,8] ; print(list_9.count(4))

#index()
print(list_9.index(0))

# insert()
list_9.insert(0,'eslam')

print(list_9)

# pop()
print(list_9.pop(0))

#///////////////////////////////
# tuple


tuple_1=('e','s',1,2,4)
tuple_2='e','s'
print(type(tuple_1))
print(type(tuple_2))

print(tuple_1[3])
 
# len()
tuple_3=('e','s',1,2,4)

print(len(tuple_3))

# repeat --> repeat a list  

tuple_3=('e','s',1,2,4)

print(tuple_3 * 2 )


#///////////////////////////////////////
#  set is like tuble and list 

# is not ordered an not indexed

set_1={1,2,3,4,5}
#print(set_1[0])

# it can't be slicing 

#print(set_1[0:3])

# unhashable type: 'list'

#set_2={1,2,3,4,5,[1,2,3,4]}
#print(set_2)

set_3={1,2,3,4,5,(1,2,3,4)}
print(set_3)

# is unique
set_4={1,2,3,4,5,1,2}
print(set_4)

#union ()

set_4={1,2,3,4,5,1,2}
set_5={7,8,9}
print(set_4 | set_5 )
print(set_4.union(set_5))

# update

set_6={1,2,3,"x"}
print(set_6)
set_7={"e","s"}

set_6.update(set_7)
print(set_6)

#difference()

set_8={1,2,3,"x"}
set_9={"e","s",2,1}
print(set_8.difference(set_9)) # set_8 - set_9



# difference_update()

set_8={1,2,3,"x"}
set_9={"e","s",2,1}
set_8.difference_update(set_9) # set_8 - set_9
print(set_8)


# intersection () & -> التقاطع ما بين الاتنين
# intersection_update () 

# symmetric_difference() i ^ j --> الحاجه اللي مش موجوده ف الاتنين
# symmetric_difference_update()

#/////////////////////////////
#dictionary

dic_1={
    "name":"eslam",
    "age":"22",
    "skills":["dfdf","dfdf","dfdfd"]
    
}

print(dic_1)

print(dic_1["age"])

print(dic_1.keys())
print(dic_1.values())

dic_2={ 

    "lang":{
        "one":"java",
        "two":"js"

    },
    "tools":{
        "one":"burp",
        "two":"nmap"
    }  
}

print(dic_2["lang"]['one'])


dic_3={

    "dic1":dic_1,
    "dic2":dic_2
}


print(dic_3)


dic_3['name']='eslam'

print(dic_3)


dic_4={

    "name":'ffff',
}


dic_4['name']='eslam'

print(dic_4)

dic_4.update({"co":"eg"})
print(dic_4)


dic_4.setdefault("age",0)

print(dic_4)


# items()


dic_5={

    "name":'ffff',
}


allitem=dic_5.items()
dic_5 ['age']=33

print(allitem)

#fromkeys()

dic_6=('e','h','n','b',)

key_dic6='k'

print(dict.fromkeys(  dic_6 , key_dic6 ))

#/////////////////////////////////////

# input()


#data=input("what is your name ?  ")

#print(f"hello, {data} ") # new

#print("hello  %s "% (data)) # old
#print("hello  {:s} ".format (data)) # old 

#data=data.strip().capitalize()
#print(f"hello, {data} ")


#///////////////////////////////////////////////////
  # pract

'''
name=input("enter your name ? ")
age=int(input("enter your age ? "))
email=input("enter  email ? ")

print(f"My name is {name.lower()} , And my Email is {email.lower()}")
ch=email.index("@")

print(email[0:ch])

print(email[ch+1:])

#//////////////////////////////////////////////////////////////////
print("//"*50); # if elif else

n1,n2,n3=map(int,input("Enter 3 num :").split())

if n1==n2 and n1==n3 and n2==n3 :
    print("is Equal")

elif n1>n2 and n1>n3 :
    print(f"{n1} is bigger")

else:
    print("is difference")

# short if    ternary operator
# <value_if_true> if <condition> else <value_if_false>


print("is Equal" if n1==n2 and n1==n3 and n2==n3 else (f"{n1} is bigger  "if n1>n2 and n1>n3  else "is difference" ))

'''
#/////////////////////////////////////////////
print(50*"*")

# mempership operator 

name="eslam"
print("e"in name) # --> ده معناه هل e ف name


print("n" in name)

if "k" in name:
    print("yes")
else:
    print("no")

# admin=["admin","eslam","axion"]

# login=input("Enter name : ").split

# if login in admin:
#     print("is admin ")
# else :
#     print("is not ")

#/////////////////////////////////////////

print(50*"*") 

# loops


# while 
n=1
while n <= 10:
    print(n)
    n+=1 # n=n+1
else:
    print("finish")


list_10=["e","s","l","a","m"]

print(list_10)
a=0
while a < len(list_10):
    print(f"{a+1} {list_10[a]}")
    a+=1

# for loop
print(50*"*")

list_11=[2,5,7,5,6,8,9]

for i in list_11:
    if i%2==0:
        print(f"{i,list_11.index(i)} is even")
    else:
        print(f"{i,list_11.index(i) } is odd")
    
    
myrange=range(0,100)

for i in myrange:
    print(f"{i}".zfill(2))

print(50*"*")


dic_7={
    "one":"10",
    "two":"20",
    "three":"30",
    "four":"40",
    "five":"50"
}

print(dic_7.items())
print(dic_7["one"])

print(dic_7.get("one"))

for i in dic_7:
    print(i,dic_7[i])

#////////////////////////////////////////////
print(50*"*")


num =[1,2,3,4,8,5,4,56,8]

for i in num :
    if i ==8:
        continue
    print(i)

print(10*"*","break",10*"*")

for i in num :
    if i ==8:
        break
    print(i)


print(10*"*","pass",10*"*")

for i in num :
    if i ==8:
        pass
    print(i)

#////////////////////////////////////
print(50*"*")


dic_8={
    "one":"10",
    "two":"20",
    "three":"30",
    "four":"40",
    "five":"50"
}

for dic_keys,dic_values in dic_8.items():
    print(f"{dic_keys} --> {dic_values} ")

print(50*"*")

dic_10={ 

    "lang":{
        "one":"java",
        "two":"js"

    },
    "tools":{
        "one":"burp",
        "two":"nmap"
    }  
}

for dic_keys,dic_values in dic_10.items():
    print(f"{dic_keys} :  ")
    for child_keys,child_values in dic_values.items():
        print(f"{child_keys} : {child_values} ")


#///////////////////////////////////////////////////
print(50*"*")

def name_func():
    print("hi")


name_func()



def name_func2():
    return 2*2

print(name_func2())



def name_func3(a,b): # a,b are parameters
    return a*b

result=name_func3(5,8) # 5,8 are argumesnts
print(result)


# func packing , unpacking argument *arg

list_12=[4,5,6,7] 
print(list_12)
print(*list_12) # unpacking


def name_func3(n1,n2,n3):
    list_13=[n1,n2,n3]
    for i in list_13:
        print(i)


name_func3('ahmed','axion','eslam')



def name_func3(*list_13): # here u can add parameters if u want 
    
    for i in list_13:
        print(i)


name_func3('ahmed','axion','eslam',"sameh")







