# -*- coding: cp1251 -*-

from unicodedata import normalize

import random

def checker1(num):
    if num % 3 == 0: 
        print("Число делится на 3")
    else: 
        print("Число не делится на 3")

while True:
    a = 0
   
    checker = False
    primaryChoice = input("Выбор задания для проверки : \n1)\n2)\n3)\n4)\n5) - Выход\nВыбор : ")
    if [num for num in primaryChoice if num not in ".,/*-+1234567890"]: checker = True
    if checker == True:
        print("Так нельзя")
        break
    primaryChoice = int(primaryChoice)
    
    if primaryChoice == 1:
        print("Введите число для проверки для деления на 3")
        num = input()
        num = int(num)
        checker1(num)
        
    if primaryChoice == 2:
        print("Введите число, которое будет делить сотню")
        
        