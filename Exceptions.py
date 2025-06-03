try:
    age = int(input("Enter your age: "))
    print('Age:',age)
    income = 7000000
    risk = income/age
except ValueError:
    print("Invalid value")
except ZeroDivisionError:
    print("Age cannot be Zero.")