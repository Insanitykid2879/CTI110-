Python 3.11.3 (tags/v3.11.3:f3909b8, Apr  4 2023, 23:49:59) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> print("This program calculates and displays travel expenses")
... a= int(input('Enter Budget:'))
... b= (input('Enter your travel destination:'))
... c= int(input('How much do you think you will spend on gas?'))
... d= int(input('Approximately, how much will you need for accomodation/hotel?'))
... e= int(input('Last, how much will you need for food?:'))
... 
... print("\n------------Travel Expenses------------")
... print("Location:"      +b)
... print("${:.2f}".format(a))
... print("${:.2f}".format(c))
... print("${:.2f}".format(d))
... print("${:.2f}".format(e))
... 
... r= a-c-d-e
... print("\n---------------------------------------")
... 
... print("Remaining balance:","${:.2f}".format(r))
