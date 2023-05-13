# Write a Python program which accepts a sequence of comma-separated numbers from user and generate a list and a tuple with those numbers.
num = input("Enter the comma seperated number: ")
list1 = num.split(',')
print(list1)
print(tuple(list1))