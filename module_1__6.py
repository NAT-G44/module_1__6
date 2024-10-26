my_dict={"Даша":2001, "Катя":2002, "Соня":2003}
print(my_dict)
print(my_dict["Даша"])
my_dict["Оля"]=2004
my_dict["Ира"]=2005
print(my_dict.update({"Оля":2004,"Ира":2005}))
del my_dict["Катя"]
print(my_dict)

my_set={1,"one",3,4,2,"one",5,3,"two"}
print(my_set)
my_set.add(25)
my_set.add("five")
my_set.discard(2)
print(my_set)
