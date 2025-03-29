log = '''
                      ___.                       .__    .__                                            __                
  _____   ____   _____\_ |__   ___________  _____|  |__ |__|_____     ____ ______   ________________ _/  |_  ___________ 
 /     \_/ __ \ /     \| __ \_/ __ \_  __ \/  ___/  |  \|  \____ \   /  _ \\____ \_/ __ \_  __ \__  \\   __\/  _ \_  __ \
|  Y Y  \  ___/|  Y Y  \ \_\ \  ___/|  | \/\___ \|   Y  \  |  |_> > (  <_> )  |_> >  ___/|  | \// __ \|  | (  <_> )  | \/
|__|_|  /\___  >__|_|  /___  /\___  >__|  /____  >___|  /__|   __/   \____/|   __/ \___  >__|  (____  /__|  \____/|__|   
      \/     \/      \/    \/     \/           \/     \/   |__|            |__|        \/           \/                   
'''
print(log)

def membershipOperator(string1):
    print("y" in string1)
    print("y" not in string1)


def list_mem():
    list1 = [1, 2, 3, 4, 5]
    print(f"{1 in list1} is in list")
    print(f"{6 in list1} is not in list")
    for i in list1:
        print(i, end=" ")
        print(f"{i} is in list")


string1 = input("enter the String : ").lower()

membershipOperator(string1)
list_mem()
