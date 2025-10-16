str_length = input ("please type length: \n")
str_width = input ("please type width: \n")
str_meter = input("How much for 1 meter? \n")
length = float (str_length)
width = float (str_width)
meter = float (str_meter)
area = length * width
str_area=str(area)
print("The total area is : " + str_area)
total_price = area * meter
str_total_price =str(total_price)
print("Give the buy : " + "$" + str_total_price )
#حل اخر واسهل جدااا جدااا عن طريق , بدل+لانها بتقدر تجمع النصوص المختلفة
str_length = input ("please type length: \n")
str_width = input ("please type width: \n")
str_meter = input("How much for 1 meter? \n")
length = float (str_length)
width = float (str_width)
meter = float (str_meter)
area = length * width
print("The total area is : ", area)
total_price = area * meter
print("Give the buy : " + "$" , total_price )