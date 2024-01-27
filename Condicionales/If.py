'''''
z = 4
if z % 2 == 0:
    print("z es multiplo de 2")
'''''
'''''
z = int(input("Ingresa un valor entero"))
if z % 2 == 0:
    print("z es multiplo de 2")
else:
    print("z no es multiplo de 2")
'''''    
room = "bed"
area = 14.0
z = int(input("Ingresa un valor entero"))
if room == "kit":
    print("looking around un the kitchen")
elif room == "bed":
        print("looking around in the bedroom")
else:
    print("looking around elsewhere")
    if area > 15:
        print("big place!")
    else:
        print("pretty samll")