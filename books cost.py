books={
    "Harry Potter And The Philosophers Stone":"£7.99",
    "Harry Potter And The Chamber Of Secrets":"8.99",
    "Harry Potter And The Prisoner Of Azcaban":"6.99",
    "Harry Potter And The Goblet Of Fire": "12.99",
    "Harry Potter And The Order Of The Pheonix":"14.99",
    "Harry Potter And The Half-Blood Prince":"11.99",
    "Harry Potter And The Deathly Hallows (part 1)":"10.99",
    "Harry Potter And The Deathly Hallows (part 2)":"10.99"
}
books.items()
# how to check if a key exist in the dictionaries or not, 
if "Harry Potter And The Philosophers Stone" in books:
    print ("Yes it is available")
# change a value,
books ["Harry Potter And The Chamber Of Secrets"]="8.99"
print (books)
# change a key value pair, adding a key-value pair,
books ["Harry Potter And The Deathly Hallows (part 2)"]="10.99" 
# delete from dictionaries, 
del (books) ["Harry Potter And The Chamber Of Secrets"]
# looping through the values in the dictionaries.
for key,value in books.items():
    print (key,value)#access items, 
print (books["Harry Potter And The Goblet Of Fire"])
print (books["Harry Potter And The Deathly Hallows (part 1)"])
#get keys, 
print (books.keys())
# get values,
print (books.values())
# list of key value pairs, 
print ()