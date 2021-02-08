#Furkan Surucu

name_surname= input("Please enter your name and surname: ")
height= float(input("Please enter your heigth in meters: "))
weight= float(input("Please enter your weigth: "))
mass_index = round(weight/(height**2),2)

print("Dear {},\nYour body mass index:".format(name_surname),mass_index)
if mass_index < 25:
    print("Normal")
elif mass_index < 30 and mass_index >=25:
    print("Overweight")
elif mass_index < 40 and mass_index >=30:
    print("Obese")
else:
    print("Extremely Rotund")
