# class Human:
#   def __init__(self):
#     self.eyes = 2
#     self.nose = 1
#   def flirt(self):
#     print("I can flirt.")
# class child(Human):
#   def __init__(self,name):
#     super().__init__()
#     self.name = name
#   def eat(self):
#     print("I can eat.")
#   def work(self):
#     super().work()
#     print("I cannot work.")
# res = child("Pyanshu")
# res.work()
# print(res.eyes)

# l = input("Enter any Word: ")
# h = []
# for i in l:
#     if i in "AEIOUaeiou":
#         h.append(i)
#     else:
#         pass
# print(h)

# n = float(input("Enter your marks: "))                                                       #Turnary Operator
# print("Grade A+")if n>=90 else print("Grade B")if n>=80 else print("Grade C")if n>=70 else print("Fail")

# list1 = ["M", "na", "i", "Ke"]
# list2 = ["y", "me", "s", "lly"]
# combined = [a + b for a, b in zip(list1, list2)]
# print(combined) 

# mumber = [10,20,30,40,50,30,20,40]
# s = set(mumber)
# print(s)

# s = set()
# s1 = {}                                                 #Empty set and dictionary
# print(type(s))
# print(type(s1))

# s = {"Pyanshu","Harry potter","Hitler"}                 #Accessing items of set
# for i in s:
#     print(i)

# s = {"Pyanshu","Harry potter","Hitler"}                 #Checking if an item is in set
# print("Hitler" in s)

# s = {"Pyanshu","Harry potter","Hitler"}
# s.add("Putin")
# s.update(["Trump","Biden"])                             #Adding element in set by add() and update()
# print(s)

# color = {'Red','Yellow','Blue','Black','White','Orange','Green'}
# color.remove("Yellow")
# print(color)                                            #Deleting Element by using remove(), discard(), pop()
# color.discard("White")
# print(color)
# delete = color.pop()
# print(delete)

# h = "Pyanshu \nShaw"
# print(h)

# CP = float(input("Enter the Cost Price: "))
# SP = float(input("Enter the Selling Price: "))
# if CP < SP:
#     print("Profit Earned by",SP-CP,"rupees")
# elif CP == SP:
#     print("No Profit No Loss")
# else:
#     print("Loss Earned by",CP-SP,"rupees")

import pandas as pd
dada = pd.read_csv("Note.csv")
print(dada)