def iterator_colours():
    colours=['red', 'green', 'blue', 'yellow', 'purple', 'orange']
    for colour in colours:
        print(colour)
    
def iterator_colours_next():
    colours=['red', 'green', 'blue', 'yellow', 'purple', 'orange']
    it = iter(colours)
    # printing the iterator object
    for i in range(len(colours)):
        print("next iterator ",next(it))

def iterator_calling():
    iterator_colours()
    iterator_colours_next()
    

iterator_calling()


def keyword_nonlocal():
    a =6
    print("a=", a)
    def keyword_inner():
        nonlocal a
        a = 90
        a += 5
        print("a=", a)
    keyword_inner()
    print("a=", a)
keyword_nonlocal()