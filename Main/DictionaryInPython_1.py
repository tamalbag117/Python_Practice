# Dictionary is nothing but key value pairs
d1 = {}  # ---->blank dictionary
# check type
print(type(d1))
d2 = {"Miko": "Honey", "SujoyDA": "Puchki", "Rajo": "Gajo", "Lucifer": {1: "Fire", 2: "Fly"}}
print(d2)
# quarry
print(d2["Miko"])
print(d2["Lucifer"])
print(d2["Lucifer"][2])
d2["Rangan"] = "pallu"  # add item to dictionary
print(d2)
del d2["Lucifer"][1]  # delete element from list
print(d2)
d3 = d2.copy()  # copy content of one dictionary to another
d3["Crimson Red"] = {1: "curly firefly", 2: "mota gorila"}
d3["Lucifer"][3] = str(108)
d3["Lucifer"].update({4: "butterfly"})   # prefer .update over others
print(d2)
print(d3)
# key value print
print(d2.keys())
# items print ---> print key value pair
print(d2.items())
print(d3["Lucifer"].items())
