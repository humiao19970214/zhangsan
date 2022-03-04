'''
字符串都需要加引号
#元组
a=(1,2,"哈哈",True,"哈哈","嘻嘻","哈哈")
print(a)
print(a[2])

#显示下标当有多个哈哈时,显示的是第一个哈哈的下标
print(a.index("哈哈"))
print(a[1],a[2])

#切片(左闭右开)
print(a[0:4])

#统计值的数量
print(a.count("哈哈"))


#元组里面放元组(二维元组)
b=(a,"哈哈","aaa")
print(b[1])
print(b[0][3])
'''

'''
#数组(和数组的区别是:元组一旦写好就不可以修改,而数组可以)
a=[1,2,"哈哈",True,"哈哈","嘻嘻","哈哈"]
print(a[4])

#增
a.append("append")
print(a)
a.insert(0,"append2")
print(a)

#剪切(pop)
b=a.pop(5)
print(a)
print(b)


#清空
a.clear()
print(a)


#给数组增加多个值extend()
a=[1,2,"哈哈",True,"哈哈","嘻嘻","哈哈"]
xx=["hello","world","!"]
a.extend(xx)
print(a)
print(a+xx)

#删除remove()
a.remove("哈哈")
print(a)
'''


'''
python的语法:
所有的方法都是小括号结尾; 
元组,数组,字典的取值都用中括号;
元组,数组,字典的定义分别是(),[],{}
'''

#字典
'''
字典的特点:
1.字典中的值没有顺序;
2.字典的结构必须是键值对(key:value);

'''
a={
    "name":"张三",
    "age":25,
    0:"李四"
}
#取值
print(a["name"])
#新增
a["high"]="183cm"
print(a)
#修改
a["name"]="王五"
print(a)

#get()取值
print(a.get("name"))

#pop()剪切
print(a.pop("name"))
print(a)
#update()新增或修改
a.update(name=1111)
print(a)

#a.get("")和a[""]的区别：若输入一个空值，a.get("")会输出空值，a[""]会报错
#print(a.get("name1"))
#print(a[name1])


#删除（元组不能修改，所以不能删除）
del a["name"]
print(a)


#课后作业



