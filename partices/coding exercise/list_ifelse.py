#list python program using list
indian =["samosa","dal","naan"]
chinese =["momo","noddles","fried rice","kimchi"]
italiian =["pizza","pasta","risotto"]

dish = input("enter a dish name :")

if dish in indian:
    print("indian",indian,dish)
elif dish in chinese:
    print("chinese",chinese,dish)
elif dish in italiian:
    print("italiian",italiian,dish)
else :
    print("based on the little knowlege cusian in dish: ",dish)

