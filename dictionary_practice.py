dict_name={"Chicken":1.59,"Beef":1.99,"Cheese":1.00,"Milk":2.50}
print(dict_name)

NBA_players = {"Lebron James": 23, "Kevin Durant": 35, "Stephen Curry": 30, "Damian Lillard": 0}
print(NBA_players)

Steph_jersey=NBA_players["Stephen Curry"]
print(Steph_jersey)
groceries=dict_name
Chicken_price=groceries["Chicken"]
print(Chicken_price)
Beef_price=groceries["Beef"]
Cheese_price=groceries["Cheese"]
Milk_price=groceries["Milk"]
print(Beef_price)
print(Cheese_price)
print(Milk_price)
Steph_jersey=NBA_players["Lebron James"]
print(Steph_jersey)

NBA_players["Lebron James"]=6
print(NBA_players)

Shoe_name={"Jordan 13":1,"Yeezy":8,"Foamposite":10,"Air Max":5,"SB Dunk":20}
print(Shoe_name)

Purchased_shoes=Shoe_name["SB Dunk"]
print(Purchased_shoes)
Shoe_name["SB Dunk"]=16
print(Shoe_name)

Returned_shoes=Shoe_name["Yeezy"]
print(Returned_shoes)
Shoe_name["Yeezy"]=9
print(Shoe_name)

Shoe_name["Jordan 13"]=8
Shoe_name["Yeezy"]=15
Shoe_name["Foamposite"]=17
Shoe_name["Air Max"]=12
Shoe_name["SB Dunk"]=27
print(Shoe_name)

Shoe_name["Jordan 13"]=5
Shoe_name["Yeezy"]=12
Shoe_name["Foamposite"]=14
Shoe_name["Air Max"]=9
Shoe_name["SB Dunk"]=24
print(Shoe_name)

NBA_players["Luka Doncic"] = 77 
print(NBA_players)
Shoe_name["Converse"]=25
print(Shoe_name)

del NBA_players["Kevin Durant"]
print(NBA_players)

del Shoe_name["Air Max"]
print(Shoe_name)