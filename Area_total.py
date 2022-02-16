
def rectangle(bs , ss):
    area = bs * ss
    environment = (2 * bs) + (2 * ss)
    print('area: ' , area ,'environment: ' , environment )

def square(side):
    area = side** 2
    environment = 4 * side
    print('area: ' , area , 'environment: ' , environment)

def triangle(barycentric , height , leg , otherside):
    environmente = 3 * barycentric
    environmenti = (2 * leg) + (barycentric)
    environmentd = barycentric + leg + otherside
    t = input('''wich type of triangle do you want to calculate?select one
e for equilateral triangle
i for isosceles triangle
d for different triangle =''')
    if t == 'e':
        print('environment: ' , environmente)
    if t == 'i':
        print('environment: ' , environmenti)
    if t == 'd':
        print('environment: ' , environmentd)
    area = barycentric * height / 2
    print('area: ' , area)

def trapezius(bb , sb , height , leg):
    area = (bb + sb / 2) * height
    environment = bb + sb + (2*leg)
    print('area: ', area)
    print('environment: ' ,environment)

def circle(radius):
    pi = 3.14159265
    area = pi * radius ** 2
    environment = 2 * pi * radius
    print('area: ' , area , 'environment: ' , environment)

def hexagon(side):
    area = 3 * 1.7320508076 * side ** 2 / 2
    environment = 6 * side
    print('area: ' , area)
    print('environment: ' , environment)

def sphere(radius):
    pi= 3.14159265
    volume = (4 * pi * radius ** 3)/3 
    print('volume: ' , volume)
    area = 4 * pi * radius ** 2
    print('area: ' , area)

def cylindrical(radius , height):
    pi= 3.14159265
    area = ((2 * pi * radius ** 2) + (height * (2 * pi * radius)))
    print('area: ' , area)
    volume = pi * radius ** 2 * height
    print ('volume: ' , volume)

def pyramid(height , side_of_base):
    print('if it is square pyramid:') 
    a = side_of_base * side_of_base
    volume = (a * height) / 3
    print('volume: ' , volume)


    print('if it is triangular pyramid:')
    h = int(input('provide the height of base: '))
    a1 = (h * side_of_base) / 2
    volume1 = a1 * height / 3
    print('volume: ' , volume1) 
    
   


# about program import your library
    
    
    
       
       
                 
    
    
    
    
    
    




