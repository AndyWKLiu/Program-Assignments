#Slide 15
City_list = ["Oakland", "Atlanta", "New_York_City", "Seattle", "Memphis", "Miami", "Boston", "Los_Angeles", "Denver", "New_Orleans"]
print(City_list)

#Slide 16
Name_list = ["Andy", "Jen", "Bob", "Jason", "Jack", "Jackson", "Huaxi", "Yun", "Barry", "Oliver"]
print(Name_list)

#Slide 17

#for City_list
print(City_list[0])
print(City_list[2])
print(City_list[7])

#for Name_list
print(Name_list[0])
print(Name_list[1])
print(Name_list[3])

#Slide 19
four_cities = City_list[0 : 4]
print(four_cities)
four_names = Name_list[5 : 9]
print(four_names)

#Slide 20
City_list[0] = "San Francisco"
City_list[2] = "Brooklyn"
City_list[7] = "Hollywood"
City_list[5] = "Tampa"
print(City_list)

#Slide 22
City_list.append("New Jersey")
City_list.extend(["Santa Cruz", "Selma", "Chicago"])
City_list.insert(7, "Washington, D.C.")
print(City_list)

#Slide 23
City_list.append("Oakland")
City_list.extend(["New York City", "Los Angeles"])
City_list.insert(0, "Miami")
print(City_list)

#Slide 26
City_list.pop(4)
City_list.remove("Miami")
print(City_list)
element = City_list.clear()
print(element)