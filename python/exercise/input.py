age = input("please input your age:")

print("你输入的年龄是：" + age)

age = int(age)

if age < 6 : 
   print("幼儿园") 
elif (age >= 6 and age < 12) :  
   print("小学生")
elif (age >= 12 and age < 18) :  
   print("中学生")
elif (age >= 18 and age < 22) :  
   print("大学生")  
else :  
   print("I don't know.") 