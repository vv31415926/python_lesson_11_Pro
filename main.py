'''
1. Выполнить задание уровня light
2. Реализовать собственный класс с использованием магических методов (не менее 10-ти).
'''
from __future__ import division
class Point2D:
    def __init__(self,x,y):
        self.coord = [x,y]

    def module(self, coord ):
        return round(   ( self.coord[0]*self.coord[0]+self.coord[1]*self.coord[1] )**0.5, 2   )

    def __str__(self):
        return f' точка с координатами: x={self.coord[0]}, y={self.coord[1]}, длинна вектора:{self.module(self.coord)}\n'

    def __eq__( self, other ):
        return self.module( self.coord) == other.module( other.coord)

    def __lt__( self, other ):
        return self.module( self.coord) < other.module( other.coord)

    def __gt__( self, other ):
        return self.module( self.coord ) > other.module( other.coord)

    def __le__( self, other ):
        return self.module( self.coord) <= other.module( other.coord)

    def __ge__( self, other ):
        return self.module( self.coord) >= other.module( other.coord)

    def __add__(self, other):
        p = Point2D( self.coord[0]+other.coord[0], self.coord[1]+other.coord[1] )
        return p

    def __abs__(self):
        return self.module( self.coord )

    def __sub__(self, other):
        p = Point2D(self.coord[0] - other.coord[0], self.coord[1] - other.coord[1])
        return p

    def __mul__(self, other):
        if isinstance( other, Point2D):
            p = Point2D(self.coord[0] * other.coord[0], self.coord[1] * other.coord[1])
        else:
            p = Point2D(self.coord[0] * other, self.coord[1] * other)
        return p

    def __truediv__(self, other):
        if isinstance( other, Point2D):
            if other.coord[0] != 0 and other.coord[1] != 0:
                p = Point2D(   self.coord[0] / other.coord[0], self.coord[1] / other.coord[1]   )
            else:
                p = Point2D( 0,0 )
        else:
            if other != 0 :
                p = Point2D(self.coord[0] / other, self.coord[1] / other)
            else:
                p = Point2D( 0,0 )
        return p

if __name__ == '__main__':
    point1 = Point2D( 5,5 )
    point2 = Point2D(1, 2)
    point3 = Point2D(5, 5)

    print( point1, point2, point3 )
    print( 'точка1 = точка2:',point1 == point2, ',    точка1 = точка3:',point1 == point3 )
    print( 'точка1 < точка2:',point1 < point2, ',    точка1 < точка3:',point1 < point3)
    print('точка1 > точка2:', point1 > point2, ',    точка1 > точка3:', point1 > point3)
    print('точка1 <= точка2:', point1 <= point2, ',    точка1 <= точка3:', point1 <= point3)
    print('точка1 >= точка2:', point1 >= point2, ',    точка1 >= точка3:', point1 >= point3)

    print( 'Сумма точек 1 и 2:',point1+point2 )

    print( 'Модуль точки 1:',abs(point1), ', Модуль точки 2:', abs(point2), ', Модуль точки 3:', abs(point3))

    print('разность точек 1 и 2:', point1 - point2)

    print('умножение точек 1 и 2:', point1 * point2)
    print('умножение точек 1 на 5:', point1*5)

    print('деление точек 1 и 2:', point1 / point2 )
    print('деление точек 1 на 2:', point1/2 )



