# we write two programs
# to create address book and write some records into it
# read this book
book ={}
book ['tom']={
    'name':"tom",
    "address":"1 red street,NY",
    'PHONE': 67899089887
}
book ['bon']={
    'name':"bon",
    "address":"1 red street,NY",
    'PHONE': 23447567
}

# import json in built function
import json
s = json.dumps(book,indent= 4)
#print("string :",s)
#write the json file
with open(r"C:\Users\gandl\Downloads\git_bhargavi_gudur\BasicPythonConcepts\json\data\data.txt","w") as f:
   data = f.write(s)

print("data:",data)
#read the json file
with open(r"C:\Users\gandl\Downloads\git_bhargavi_gudur\BasicPythonConcepts\json\data\data.txt","r") as f:
   data = json.load(f)

print("data:",data)
