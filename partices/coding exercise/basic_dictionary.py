# Write Python 3 code in this vscode editor and run it.
# sample dictonary code.
data ={1:'naveen',2:'kiran',3:'rama',4:'hauman'}
print(' type :',type(data))
print("data",data)
for i in data:
    print("data",i,data.get(i))
    
 # convert   two lists into dictonary using dict and  zip   
keys = ['bhargavi','tanvi','roopa']
values = ['html','python','embeeded c']
data = dict(zip(keys,values))
print('data:',data)