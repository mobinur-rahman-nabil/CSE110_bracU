# -*- coding: utf-8 -*-
"""CSE110_Assignment_2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1otgOk-UhDtxmgQku8yVGLc8OutchO7mi
"""

#task1
import math
radius=int(input())
circumference=2*math.pi*radius
area=math.pi*(radius**2)
print("Area is", area,"\n"+"Circumference is", circumference)

#try

#try

#task4
a=int(input())
b=int(input())
if a>b:
  print(a-b)
else:
  print(b-a)

#task5
a=int(input())
if a%2==0:
  print("The number is even")
else:
  print("The number is odd")

#mutiple , things code
a=int(input())
if a%2==0 or a%5==0:
  print(a)
else:
  print("Not a multiple of 2 OR 5")

#task6
a=int(input())
if a%2==0 or a%5==0:
  print(a)
else:
  print("Not a multiple of 2 OR 5")

#task7
a=int(input())
if a%2==0 and a%5==0:
  print("Multiple of 2 and 5 both")
elif (a%2==0 or a%5==0) and not (a%2==0 and a%5==0):
  print(a)
else:
  print("Not a multiple we want")

#task8
try

#task9
given_seconds=int(input())
hour=given_seconds//3600
remainder1=given_seconds%3600
minutes=remainder1//60
seconds=remainder1%60
print("Hour:",hour,"Minutes:",minutes,"seconds:", seconds)

#task10
hour=int(input())

if 0<=hour<=168:
  if hour<=40:
    print(200*hour)
  elif hour>40:
    print(8000+300*(hour-40))
elif hour>168:
  print("Impossible to work more than 168 hours weekly")
else:
  print("Hour cannot be negative")

#task11
#try its easier

#task12

hour=int(input())
if 0<=hour<=23: #learn this f"{}" and how it works and also for this nested condition where did i put that
  if 4<=hour<=6:
    meal="Breakfast"
  elif 12<=hour<=13:
    meal="Lunch"
  elif 16<=hour<=17:
    meal="Snacks"
  elif 19<=hour<=20:
    meal="Dinner"
  else:
    meal="Patience is virtue"
  print(f"{meal}.")
else:
  print("Wrong time")

#task13
#try

#task14-task19
#try

#task20
a=int(input())
if a%2!=0 and a%5!=0:
  print(a)
else:
  print("No")

#task21
a=int(input())
if a%2!=0 or b%5!=0:
  print(a)
else:
  print("No")

#task22
canvas=int(input())
tubes=int(input())
canvas_p=120
tubes_p=75
total_money=canvas*canvas_p+tubes*tubes_p

if 0<=total_money<=299:
  discount="No Discount"
elif 300<=total_money<=499:
  discount=10
elif 500<=total_money<=749: #you cant use string"" to addition"
  discount=20
elif 750<=total_money<=999:
  discount=50
elif total_money>=1000:
  discount=150
with_discount=total_money-discount
print("Previous total:",total_money)
print(f"New total after discount: {with_discount}")