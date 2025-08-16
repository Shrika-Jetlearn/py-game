menu={
    "monday":"kale",
    "tuesday":"quiona",
    "wednesday":"salmon",
    "thursday":"bagel",
    "friday":"yoghurt",
    "saturday":"broccoli",

}
#access items, 
print (menu["wednesday"])
print (menu["saturday"])
#get keys, 
print (menu.keys())
# get values,
print (menu.values())
# list of key value pairs, 
print (menu.items())
# how to check if a key exist in the dictionaries or not, 
if "wednesday" in menu:
    print ("Yes it is available")
# change a value,
menu ["friday"]="bagel"
print (menu)
# change a key value pair, adding a key-value pair,
menu ["sunday"]="egg fried rice" 
# delete from dictionaries, 
del (menu["tuesday"])
# looping through the values in the dictionaries.
for key,value in menu.items():
    print (key,value)