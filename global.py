_a=1
_b=2
def add():
    global _a  #引用全局变量_a
    _a=3
    return ("_a+_b=",_a+_b)

def sub():
    #print("_a=%d" % _a)
    global _b #引用全局变量_b
    _b=4
    return ("_a-_b=",_a-_b)

print(add())
print(sub())


i=1
print(type(i))

l=99999999990
print(type(l))

f=1.2
print(type(f))

b=True
print(type(b))

c=7+8j
print(type(c))


#单引号
str1='python'
#单引号中使用双引号
str2='"python"'
#双引号中使用单引号
str3="'python'"
#三单引号
str4='''python'''
#三单引号中间使用双引号
str5='''"python"'''
#三单引号中有换行符
str6='''hello
python'''
#三双引号中有换行符
str7="""hello
python"""

print("str1: {0}".format(str1))
print("str2: {0}".format(str2))
print("str3: {0}".format(str3))
print("str4: {0}".format(str4))
print("str5: {0}".format(str5))
print("str6: {0}".format(str6))
print("str7: {0}".format(str6))


str='''he say: "hello world!" '''
print(str)

str8="he say:'hello,world!'"
print(str8)

print("1 + 1 = ", 1 + 1)
print("2 - 1 = ", 2 - 1)
print("2 * 3 = ", 2 * 3)
print("4 / 2 = ", 4 / 2)
print("1 / 2 = ", 1 / 2)
print("1 / 2 = ", 1.0 / 2.0)
print("3 % 2 = ", 3 % 2)
print("2 ^ 3 = ", 2 ** 3)

print("1 + 2 < 3 - 1 => ",1 + 2 < 3 - 1)
print("1 + 2 <= 3 > 5 % 2 =>",1 + 2 <= 3 > 5 % 2)


#控制语句
#if条件语句
#x=int(input("x:"))
#x=x+1
#print(x)

#a=input("a:")
#b=input("b:")
#if a>b:
#    print(a,">",b)
#else:
#    print(a,"<",b)
 


#score=int(input("score:"))  #input输出的是字符串类型，需要使用int（）转换成int
#if (score>90) and (score<=100):
#   print("优秀")
#elif (score>80) and (score<=90):
#    print("良好")
#elif (score>=60) and (score<=80):
#    print("及格")
#else:
#    print("不及格")


x=1
y=2
operator='/'
result={
    "+":x+y,
    "-":x-y,
    "*":x*y,
    "/":x/y
}

print(result.get(operator))

#num=input('输入几个数字：').split(',')
#print(num)


for x in range(-1,2):
    if x>0:
        print("正数：",x)
    elif x==0:
        print("零:",x)
    else:
        print("负数:",x)
print("循环结束")


#x=int(input("请输入数字:"))#如果不加int（），x为str，y为int,x和y不能进行比较
#print(type(x))
#y=0
#flag=0
#for y in range(100):
#   if x==y:
#        flag=1
#        print("找到了")
#        break
#if flag==0:
#    print("没有找到")


#xrange()
#x=xrange(8)
#print(x)


s1=("apple")
print(s1[0])
s2=("apple",)
print(s2[0])

tuple=("apple","banana","grape","orange")
print(tuple[-1])    #"orange"
print(tuple[-2])    #"grape"   
tuple2=tuple[1:3]   #("banana","grape")
tuple3=tuple[0:-2]  #("apple","banana","grape")
tuple4=tuple[2:-2]  #()
print(tuple2)
print(tuple3)
print(tuple4)



fruit1=("apple","banana")
fruit2=("grape","orange")
tuple=(fruit1,fruit2)
print(tuple)
print(tuple[0][0])
print(tuple[0][1])
print(tuple[1][0])
print(tuple[1][1])


tuple=("banana",101,True,(11,"as"))
a,b,c,d=tuple
print(a,b,c,d)


tuple=(("apple","banana"),("grape",'orange'),('watermelon',),('grapefruit',))
for i in range(len(tuple)):
    print("tuple[%d]:" % i,"",)
    for j in range(len(tuple[i])):
        print(tuple[i][j],"",)


#tuple=(("apple","banana"),("grape",
#'orange'),('watermelon',),('grapefruit',))
#k=0 
#for a in map(None,tuple):
#    print("tuple[%d]:" % k)
#    for x in a:
#        print(x)
#    k=k+1
#

    list=['apple','banana','grape','orange']
    print(list)
    print(list[2])
    list.append("watermelon")
    list.insert(1,"grapefruit")
    print(list)
    list.remove("grape")
    print(list)
    #list.remove("a")
    print(list.pop())
    print(list)

    list1=["apple","banana"]
    list2=["grape","orange"]
    list1.extend(list2)
    print(list1)
    list3=["watermelon"]
    list1=list1+list3
    print(list1)
    list1+=["grapefruit"]
    print(list1)
    list1=["apple","banana"]*2
    print(list1)

    list=["apple","banana","apple"]
    print(list)

    tuple1=(11,11,11)
    print(tuple1)

    list=["orange","banana","grape","apple"]
    print(list.index("grape"))
    print(list.index("orange"))
    print("apple" in list)

    list.sort()
    print(list)
    list.reverse()
    print(list)

   


    dict={"a":"apple","b":"banana","g":"grape","o":"orange"}
    print(dict)
    print(dict["a"])

    dict={"a":"apple","b":"banana","g":"grape","o":"orange"}
    dict["w"]="watermelon"
    del(dict["a"])
    dict["g"]="grapefruit"
    print(dict.pop("b"))
    print(dict)
    dict.clear()
    print(dict)

    dict={"a":"apple","b":"banana","g":"grape","o":"orange"}
    for k in dict:
        print("dict[%s]:" % k,dict[k])
    print(dict.items())

    dict={"a":"apple","b":"banana","g":"grape","o":"orange"}
    print(dict.items())
    for k,v in dict.items():
        print("dict[%s]: %s"  % (k,v))


    dict={"a":("apple",),"bo":{"b":"banana","o":"orange"},"g":["grape","grapefruit"]}
    print(dict["a"])        #('apple',)
    print(dict["a"][0])     #apple
    print(dict["bo"])       #{"b":"banana","o":"orange"}
    print(dict["bo"]["o"])  #orange
    print(dict["g"])        #["grape","grapefruit"]
    print(dict["g"][1])     #grapefruit

    dict={"a":"apple","b":"banana","g":"grape","o":"orange"}
    print(dict.keys())
    print(dict.values())
    print(dict.get("a","pink"))
    print(dict.get("e"))

    dict1={1:"1",2:"2",3:"3"}
    print(dict1)
    dict2={5:'5',6:'6'}
    dict1.update(dict2)
    print(dict1)

    dict={}
    dict.setdefault("a")
    print(dict)
    dict.setdefault("b","banana")
    print(dict)

    dict={"a":"apple","b":"banana","g":"grape","o":"orange"}
    dict.pop("b")
    print(dict)
    dict6=dict.copy()
    print(dict6)

    dict={"a":"apple","b":"grape","c":"orange","d":"banana"}
    print(dict)
    print(sorted(dict.items(),key=lambda d:d[0]))
    print(sorted(dict.items(),key=lambda d:d[1]))
    dict8=dict
    print(dict8)


    dict={"a":"apple","b":"grape"}
    dict2={"c":"orange","d":"banana"}
    dict2=dict.copy()
    print(dict2)

    import copy
    dict={"a":"apple","b":{"g":"grape","o":"orange"}}
    dict2=copy.deepcopy(dict)
    print("dict2:",dict2)
    dict3=copy.copy(dict)
    print("dict3:",dict3)
    dict2["b"]["g"]="orange"
    print(dict)
    dict3["b"]["g"]="orange"
    print(dict)


    