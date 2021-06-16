#Lab 3

#Slide 3 
Food_price = {"Chicken": 1.59, "Beef": 1.99, "Cheese": 1.00, "Milk": 2.50}
#Slide 4
NBA_players = {"Lebron James": 23, "Kevin Durant": 35, "Stephen Curry": 30, "Damian Lillard": 0}
People_PhoneNumber = {"Bob": 5103591287, "Jeff": 3295124395, "Bill": 9843274578, "Jones": 8173287433}
#Slide 6 
Chicken_price = Food_price["Chicken"]
print(Chicken_price)
Beef_price = Food_price["Beef"]
print(Beef_price)
Cheese_price = Food_price["Cheese"]
print(Cheese_price)
Milk_price = Food_price["Milk"]
print(Milk_price)
#Slide 7
Bob_PhoneNumber = People_PhoneNumber["Bob"]
print(Bob_PhoneNumber)
Jeff_PhoneNumber = People_PhoneNumber["Jeff"]
print(Jeff_PhoneNumber)
Bill_PhoneNumber = People_PhoneNumber["Bill"]
print(Bill_PhoneNumber)
Jones_PhoneNumber = People_PhoneNumber["Jones"]
print(Jones_PhoneNumber)
#Slide 9 
Shoe_amount = {"Jordan_13": 1, "Yeezy": 8, "Foamposite": 10, "Air_Max": 5,  "SB_Dunk": 20}
#Slide 10
Shoe_amount["Jordan_13"] = 5
Jordan_13_amount = Shoe_amount["Jordan_13"]
print(Jordan_13_amount)
Shoe_amount["Yeezy"] = 13
Yeezy_amount = Shoe_amount["Yeezy"]
print(Yeezy_amount)
Shoe_amount["Foamposite"] = 14
Foamposite_amount = Shoe_amount["Foamposite"]
print(Foamposite_amount)
Shoe_amount["Air_Max"] = 9
Air_Max_amount = Shoe_amount["Air_Max"]
print(Air_Max_amount)
Shoe_amount["SB_Dunk"] = 22
SB_Dunk_amount = Shoe_amount["SB_Dunk"]
print(SB_Dunk_amount)
#Slide 11
Food_price1 = {"Turkey": 2.53, "Rib": 3.54, "Bean": 1.09}
Food_price.update(Food_price1)
print(Food_price)
NBA_players1 = {"Dude": 5, "Jen": 12, "Cool": 35}
NBA_players.update(NBA_players1)
print(NBA_players)
People_PhoneNumber1 = {"Sam": 3245498883, "Ben": 4133285489, "Jill": 4135482390}
People_PhoneNumber.update(People_PhoneNumber1)
print(People_PhoneNumber)
Shoe_amount1 = {"Nikes": 20, "Jordans": 10, "Flip_Flops": 35}
Shoe_amount.update(Shoe_amount1)
print(Shoe_amount)
#Slide 12 
del Food_price["Bean"]
del Food_price["Beef"]
print(Food_price)
del NBA_players["Dude"]
del NBA_players["Cool"]
print(NBA_players)
del People_PhoneNumber["Sam"]
del People_PhoneNumber["Bob"]
print(People_PhoneNumber)
del Shoe_amount["Nikes"]
del Shoe_amount["Yeezy"]
print(Shoe_amount)