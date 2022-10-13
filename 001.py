# 1.	Напишите программу, которая принимает на вход цифру, обозначающую день недели,
#  и проверяет, является ли этот день выходным.



x = int(input("Enter number "))
if x == 6 or x == 7 or x % 6 == 0 or x % 7 == 0:
    print("It`s weekend")
else:
    print("Its not weekend")