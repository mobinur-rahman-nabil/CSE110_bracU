# -*- coding: utf-8 -*-
"""cse110_Assignment_5_List.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1x0mU-1Qzdj3n9GFmMsB-0FsOROUnQyFI
"""

#task1
list1=[]
for i in range(5):
  n=int(input("enter: "))
  list1.append(n)
  print("Number in the list",list1)

#task2
user_input=input("Enter your numbers: ")
list1=[int(x.strip()) for x in user_input.split(",")]

if len(list1)>=4:
  new_list=list1[2:-2:1]
  print(new_list)
else:
  print("Not Possible")
print(len(list1))

#task3
user_input=input("Enter your number:")
list1=[int(x.strip()) for x in user_input.split(",")]
list2=[]
list1.reverse()
print(f"printing value from the reverse order \n {list1}")

#task3 for exact assignment output
list1=[]

for i in range(5):
  n=int(input())
  list1.append(n)

print(f"printing value from the reverse order: {list1[::-1]}")

#task4 with hardcode as assignment
list1=[9, 25, 1, 36]
list2=[]
for i in list1:
  list2.append(i**2)
print(list2)

#task4 with builtin
# Given list
given_list = [1, 2, 3, 4, 5, 6, 7]

# Use list comprehension to square each item in the list
squared_list = [x ** 2 for x in given_list] # how does that shit works !!

# Print the squared list
print(squared_list)

#task5
given_list=["","my","name","","is","Nabil","isn't it","?"," "]

'''#we will not remove elements from the main list because when loop
starts the first blank string "" get removed which was 0 indexed and then "name" which was 1
indexed but after getting the first 0 indexed element removed,1 indexed "my" becomes 0 indexed after reomving.
for next time when the loop runs it automatically counts from 1 index and it will cut "my"=index0

so we will itterate in main list loop but will cut from duplicate list '''
dup_list=given_list[:]
modified_list=[]
for i in given_list: #?
  if i=="":
    dup_list.remove(i)
  else:
    modified_list.append(i)

print(f"Original List: {given_list}","\n",f"Modified List: {modified_list}")

#task6

user_input=input("enter input sperated by comma: ")
list1=[int(x.strip()) for x in user_input.split(",")]


maximum=0
index=0
for i in list1:
  if i>maximum:
    maximum=i

  elif i<maximum:
    continue
for j in range(len(list1)):
  if list1[j]==maximum:
    index=j
print("My List: ",list1)
print("Largest number in the list is",maximum,"which was found at index",index)

#task6
user_input=input()
list1=[int(x.strip()) for x in user_input.split(",")]
maximum=0
index=0
for i in list1:
  if i>maximum:
    maximum=i
    continue
  else:
    pass
for j in range(len(list1)):
  if list1[j]==maximum:
    index=j
print(f"My  List: {list1}")
print(f'Largest number in the list is {maximum} which was found at index {index}')

#task7'
'''Use built in list functions here'''
list1=[1,4,7,5,2,44]
new_list=[]
list2=[6,1,3,9,1]


for i in list1:
  if list1[-1]!=i:
    new_list.append(i)
  else:
    for j in list2:
      new_list.append(j)
print(new_list)

# task7
"""method 2"""
list1 = [1, 4, 7, 5, 2, 44]
list2 = [6, 1, 3, 9, 1]

# Check if list1 is not empty
if list1:
    # Replace the last element of list1 with elements from list2
    list1[-1:] = list2 #this is how to replace the last element of a list by another whole list

# Print the modified list1
print(list1)

'''list1.remove(list1[-1])'''
'''remove list1[-1] and update list1 then list1.extend(list2)'''

#task8
list_one = [1, 2, 3, 4, 5, 6, 7, 8, 9]
list_two = [10, 11, 12, -13, -14, -15, -16]
new_list=[]
for i in list_one:
  if i%2==0:
    new_list.append(i)
  else:
    continue
for j in list_two:
  if j%2==0:
    new_list.append(j)
  else:
    continue

print(new_list)

#task9
user_input = input("write a string: ")
string = [int(x) for x in user_input.split()] # figure out this line with and without strip()
modified_list=[]
for i in string:
  if i%2!=0:
    modified_list.append(i)
  else:
    continue
print("Original List: ",string)
print("Modified List: ",modified_list)

#task10
user_input=input("enter string: ")
numbers=[int(x.strip()) for x in user_input.split(",")]
'''why strip()matters here'''

'''# why not string=[int(x) for x in user_input.split(",")]?'''
modified_list=[]

for i in numbers:
  if i not in modified_list:
    modified_list.append(i)

print("Input list:", numbers)
print("Modified list:", modified_list)

#task11
List_one = [1, 4, 3, 2, 6]
List_two = [5, 7, 9, 8, 0]
-
for i in List_one:
  for j in List_two:
    if i==j:
      print(True)
      break
    elif List_one[len(List_one)-1]!=List_two[len(List_one)-1]:
      print(False)
  continue
  '''fix this code'''

#tuple writing method
tuple1=(2,3,4,5,6,"f")  #bracket is not necessary to write tuple
tuple2=1,2,4,5,6,"d"
print(tuple1)
print(tuple2)



