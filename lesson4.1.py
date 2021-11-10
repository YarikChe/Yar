# class ACLass:
    
#     attr = 10

#     def method(self, x):
#         print(x)

# a_object = ACLass()
# print(a_object.attr)
# a_object.method(150)


# class Point:

#     def __init__(self, x, y, z):
#         self.coord = (x, y, z)

#     def __repr__(self):
#         return f'Point {self.coord}'

# class Line:

#     def __init__(self, p1, p2):
#         self.point_1 = p1
#         self.point_2 = p2

#     def __del__(self):
#         print(f'Line({self.point_1} -------{self.point_2})')

# p1 = Point(1, 2, 3)
# p2 = Point(4, 5, 6)

# l = Line(p1, p2)
# del l
# print('Конец программы')

# ---------------------------------------------------------

# class Rectangle:
    

#     def __new__(cls, *args, **kwargs):
#         print('Hello from new')
#         return super().__new__(cls)

#     def __init__(self, width, height):
#         print('Hello from init')
#         self.width = width
#         self.height = height
#         print(id(self))


# r = Rectangle(10, 20)
# r2 = Rectangle(10, 20)




# class Rectangle:

#     default_color = 'green'
    
#     def __init__(self, width, height):
#         print('Hello from init')
#         self.width = width
#         self.height = height

# print(Rectangle.default_color)
# Rectangle.default_color = 'red'
# Rectangle.width = 10
# print(Rectangle.width)

# r1 = Rectangle(10, 20)
# # r1.default_color = 'yellow'
# print(r1.default_color)
# r2 = Rectangle(10, 20)
# print(r2.default_color)


# class Rectangle:

#     default_color = 'green'
    
#     def __init__(self, width, height):
    
#         self.__width = width
#         self.__height = height

#     def get_square(self):
#         return self.__width * self.__height

# r1 = Rectangle(20, 30)

# print(r1.get_square())



#-----------------------------------


# class Rectangle:
    
#     def __init__(self, width, height):
#         self.__width = width
#         self.__height = height
    
#     def get_width(self):
#         return self.__width
    
#     def get_height(self):
#         return self.__height
    
#     def set_width(self, w):
#         self.__width = w
    
#     def set_height(self, h):
#         self.__height = h

#     def get_square(self):
#         return self.__width * self.__height
    
    

# r1 = Rectangle(30, 20)
# r1.set_height(-15)
# # print(r1.__width, r1.__height)
# print(r1.get_height())
# print(r1.get_width())
# print(r1.get_square())

# class Rectangle:
#     def __init__(self, width, height):
#         self.__width = width
#         self.__height = height
    
#     @property
#     def width(self):
#         return self.__width
    
#     @property
#     def height(self):
#         return self.__height
    
#     @width.setter
#     def width(self, w):
#         if w>0:
#             self.__width = w
    
#     @height.setter
#     def height(self, h):
#         if h>0:
#             self.__height = h

#     def get_square(self):
#         return self.__width * self.__height
    

# r1 = Rectangle(30, 20)
# # r1.set_height(-15)
# r1.width = 10000
# print(r1.height)
# print(r1.width)

# print(r1.area())

class Animal:

    def __init__(self, name, color, voice):
        self.__name = name
        self.__color = color
        self.__voice = voice
    
    def __repr__(self):
        return f'{self.__name} in {self.__color}'
    
    def say(self):
        print(self.__voice)

lion = Animal('lion', 'yellow', 'RRRRR')
hourse = Animal('hourse', 'brown', 'IGGGGGG')
cat = Animal('cat', 'grey', 'meow')
animals_list = [lion, hourse, cat]
for animal in animals_list:
    print(animal)
    animal.say()