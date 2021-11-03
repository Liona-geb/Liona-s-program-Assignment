City_name=["Oakland","Atlanta","New York City","Seattle","Memphis","Miami","Boston","Los Angeles","Denver","New Orleans"]
print(City_name)

Kpop_groups=["BTS","BlackPink","Twice","Itzy","TXT","Got7","EXO","Ateez","NCT","ENHYPEN"]
print(Kpop_groups)

US_cities=City_name[1]
print(US_cities)

US_cities=City_name[0:7]
print(US_cities)

Groups=Kpop_groups[0:4]
print(Groups)

Groups=Kpop_groups[0:1],City_name[0:1]
print(Groups)

City_name[0]="San Fransisco"
print(City_name)

City_name[2]="Brooklyn"
print(City_name)

City_name[7]="Hollywood"
print(City_name)

City_name[5]="Tampa"
print(City_name)

City_name.append("Oakland")
print(City_name)

City_name.extend(["New York city","Los Angeles"])
print(City_name)

City_name.insert(0,"Miami")
print(City_name)

del City_name[0]
City_name.pop(3)
City_name.remove("Denver")
print(City_name)