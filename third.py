

#lists
l=[1,2]
print l
print "1. append \n 2. insert at a location \n 3. remove one element \n 4.pop a element\n 5. reverse\n 6. sort\n 7.exit 8.display"

a=raw_input("enter ur choice")
while(a!=7):
    print l
    fun[a]()
    a=int(raw_input("enter ur choice"))

fun={
        '1':append(),
        '2':insert(),
        '3':remove(),
        '4':pop(),
        '5':reverse(),
        '6':sort(),
    }
def append():
    l.append(4)
def insert():
    l.insert(2,3)
def remove():
    l.remove(2)
def pop():
    l.pop(0)
def reverse():
    l.reverse()
def sort():
    l.sort()