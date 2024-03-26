# -*- coding: cp1251 -*-

import random
from unicodedata import normalize

def checker1(num):
    if num % 3 == 0: 
        print(" Проверка 3")
    else: 
        print("����� �� ������� �� 3")

while True:
    checker = False
    primaryChoice = input("����� ������� ��� �������� : \n1)\n2)\n3)\n4)\n5) - �����\n����� : ")
    if [num for num in primaryChoice if num not in ".,/*-+1234567890"]: checker = True
    if checker == True:
        print("��� ������")
        break
    primaryChoice = int(primaryChoice)
    
    if primaryChoice == 1:
        print("������� ����� ��� �������� ��� ������� �� 3")
        num = input()
        num = int(num)
        checker1(num)
        
    if primaryChoice == 2:
        print("������� �����, ������� ����� ������ �����")
        
        