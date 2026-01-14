# Name: Tyler Jones
# Course: CS 1160 
# Assignment: Project 02 
# Filename: project02.py 
# Brief Description: Expense Pie Chart. 

import matplotlib.pyplot as plt

with open("expenses.txt", "w") as file:
    rent = float(input("Enter your monthly rent expense: "))
    gas = float(input("Enter your monthly gas expense: "))
    food = float(input("Enter your monthly food expense: "))
    clothing = float(input("Enter your monthly clothing expense: "))
    car_payment = float(input("Enter your monthly car payment expense: "))
    misc = float(input("Enter your monthly miscellaneous expense: "))
    
    file.write(f'Rent: {rent}\n')
    file.write(f'Gas: {gas}\n')
    file.write(f'Food: {food}\n')
    file.write(f'Clothing: {clothing}\n')
    file.write(f'Car Payment: {car_payment}\n')
    file.write(f'Miscellaneous: {misc}\n')

with open("expenses.txt", "r") as file:
    catagories = []
    amounts = []
    for line in file:
        category, amount = line.strip().split(":")
        catagories.append(category)
        amounts.append(float(amount))

    plt.figure(figsize=(8, 8))
    plt.pie(amounts, labels=catagories, autopct='%1.1f%%', startangle=140)
    plt.title('Monthly Expenses Distribution')
    plt.show()

