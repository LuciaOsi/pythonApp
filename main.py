from Phone import Phone
'''
phoneE = Phone("phoneE", 4, 3)
print(phoneE.calculate_total_price())

# You can add a property that it is not define in the class
phoneE.has_cover = True

# Shows all the attributes of the class level --> {'__module__': 'Phone', 'pay_rate': 0.8, '__init__': <function
# Phone.__init__ at 0x7f5afa95adc0>, 'calculate_total_price': <function Phone.calculate_total_price at
# 0x7f5afa95ae50>, '__dict__': <attribute '__dict__' of 'Phone' objects>, '__weakref__': <attribute '__weakref__' of
# 'Phone' objects>, '__doc__': None}
print(Phone.__dict__)
# Shows all the attributes of the instance level -->  {'name': 'empty_phone', 'price': 4, 'quantity': 3}
print(phoneE.__dict__)

# For this item i want a different discount
phoneE.pay_rate = 0.7
print(Phone.pay_rate)
print(phoneE.apply_discount())
print(phoneE.price)
'''

'''
phone1 = Phone("phone1", 100, 1)
phone2 = Phone("phone2", 1000, 3)
phone3 = Phone("phone3", 10, 5)
phone4 = Phone("phone4", 50, 5)
phone5 = Phone("phone5", 75, 5)

# Returns all the items
for phone in Phone.get_all:
    print(phone)

# Creates a csv.file
file = open("phones.csv", "w")
file.write("name,price,quantity")
file.write("\nphone1, 100, 1")
file.write("\nphone2, 1000, 3")
file.write("\nphone3, 10, 5")
file.write("\nphone4, 50, 5")
file.write("\nphone5, 75, 5")
file.close()
'''

# Import phones from csv and creates them
# Class method
'''
Phone.get_from_csv()
print(Phone.get_all)
'''

# Static method
phoneR = Phone('phoneX', 12, 23)
print(phoneR.is_integer(6.3))
print(Phone.is_integer(6.3))
print(Phone.is_integer(6.0))
