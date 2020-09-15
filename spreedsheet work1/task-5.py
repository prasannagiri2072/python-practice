#Display the volume of the sphere.
r = int(input("Input the radious."))

def volume(r):
    pi = 22/7
    volume = 4/3 * pi * r**3
    return volume
print("The volume of the sphere is " , volume(r))
