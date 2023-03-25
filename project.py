def computeRectangleWallsArea():
    global length, width, height
    length = int(input("Enter the length of the room in feet:\n "))
    width = int(input("Enter the width of the room in feet:\n "))
    height = int(input("Enter the height of the room in feet:\n "))
    return length, width, height


def computeCustomWallsArea():
    global wallcount
    wallcount = int(input("How many walls are there in the room\n"))
    wallslist = []
    for i in range(wallcount):
        height = int(input("Enter the height of wall {} in feet\n ".format(i + 1)))
        length = int(input("Enter the length of wall {} in feet\n ".format(i + 1)))
        a = height * length
        wallslist.append(a)
    x = sum(wallslist)
    return x


def computeSquareWallsArea():
    global length
    length = int(input("Enter the length of the room in feet:\n "))
    return length


def calculateRectangleArea():
    a = (length + width)
    b = 2 * height
    c = a * b
    return c


def computeSquareArea():
    a = length * length
    b = a * 4
    return b


def computeWindowsDoorsArea():
    global count
    count = int(input("How many windows and doors does the room contain?\n "))
    b = []
    for i in range(count):
        count1 = int(input("Enter window/door length for window/door {} in feet\n ".format(i + 1)))
        count2 = int(input("Enter window/door length for window/door {} in feet\n ".format(i + 1)))
        a = count1 * count2
        b.append(a)
    x = sum(b)

    return x
    

def computeGallons():
    e = d / 350
    return e


def computePaintPrice():
    f = e * 42
    return f


def computeRoomArea():
    g = ("For Room: {0:}, the area to be painted is {1:.2f} square ft and will require {2:.2f} gallons to paint. This will cost the customer ${3:.2f} ".format(i + 1, d, e, f))
    return g


print("Welcome to Shiny Paint Company for indoor painting!")
room_count = (int(input("How many Rooms do you want to paint:\n ")))
print("Thank you")
#variable contains overall calculations for area,gallon,money
overall_area = []
overall_gallons = []
overall_money = []
#iteration for each rooms and the functions 
for i in range(room_count):
    print("Room: {}".format(i + 1))
    shape = (int(input("Select the shape of the room:\n1 - Rectangular\n2 - Square\n3 - Custom (more or less than 4 walls, all square or rectangles)\n ")))
    if shape == 1: #rectangle option
        computeRectangleWallsArea()
        b = calculateRectangleArea()
    elif shape == 2: #square option
        computeSquareWallsArea()
        b = computeSquareArea()
    elif shape == 3: #custom option
        b = computeCustomWallsArea()
    #c,d,e,f,g --> are the varaible containing all of the fucntions and calculation on area, windows and door,money, and gallon
    c = computeWindowsDoorsArea()
    d = b - c
    overall_area.append(d)
    e = computeGallons()
    overall_gallons.append(e)
    f = computePaintPrice()
    overall_money.append(f)
    g = computeRoomArea()
    print(g)
    continue
#calcualtion of the all the items in the overall variables
x = sum(overall_area)
y = sum(overall_gallons)
z = sum(overall_money)
print("Area to be painted is {0:.2f} square ft and will require {1:.2f} gallons to paint. This will cost the customer ${2:.2f} ".format(x, y, z))





        
            





        
            