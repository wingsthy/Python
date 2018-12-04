# Author:wingsthy
# -*- coding:utf-8 -*-
'''
name = input ( "name:")
age = int(input ( "age:"))
job = input ( "job:")
salary = input ( "salary:")
print(type(age))
info=
--------info of %s ----------
Name:%s
Age:%s                                      
Job:%s
Salary:%s
 %(name,name,age,job,salary)
print(info)
'''

age_of_oldboy = 88
age_ = int(input("guess_age is:"))
if age_ == age_of_oldboy:
    print("yes,you are right!")
elif age_ > age_of_oldboy:
    print("think smaller...")
else:
    print("think bigger!!")


