#Name: Daniyar Kakimbekov
#Student ID: 201856966


def gcd(n1, n2): 
    try:
        if n1 == 0 and n2 == 0:
            raise ArithmeticError( "gcd(0,0) does not exist")
        elif n1 == 0:
            return n2
        return gcd(n2%n1, n1)     
    except ArithmeticError:
        pass

from numbers import *

class Rational( Number ) :
    def __init__( self, num, denom = 1 ) :
        if not isinstance( num, Integral ) :
            raise TypeError( "Rational: numerator {} must be Integral".
            format( num ))
        if not isinstance( denom, Integral ) :
            raise TypeError( "Rational: denominator {} must be Integral".
            format( denom ))
        self.num = num
        self.denom = denom
        self.normalize()

    def normalize(self):
        self.num , self.denom = self.num // (gcd(self.num, self.denom)), self.denom // (gcd(self.num, self.denom))
       
    def __repr__(self):
        return "{}, {}".format(self.num,self.denom)

    def __str__(self):
        if self.num <0 and self.denum == 1:
            return "{}".format(-self.num)
        elif self.denom == 1:
            return "{}".format(self.num)
        elif self.denom == -1:
            return "{}".format(-self.num)   
        return"{} / {}".format(self.num,self.denom)

    def __neg__(self):
        return Rational((self.num*-1))

    def __add__(self, other):
        if not isinstance(self, Rational):
            self = Rational(self[0], self[1])
        if not isinstance(other, Rational):
            other = Rational(other[0], other[1])
        return Rational((self.num*other.denom + other.num * self.denom), self.denom*other.denom)

    def __sub__(self,other):
        if not isinstance(self, Rational):
            self = Rational(self[0], self[1])
        if not isinstance(other, Rational):
            other = Rational(other[0], other[1])
        return Rational((self.num*other.denom - other.num * self.denom), self.denom*other.denom)

    def __radd__( self, other ) :
        if not isinstance(other, Rational):
            other = Rational(other[0], other[1])
        if not isinstance(self, Rational):
            self = Rational(self[0], self[1])
        return Rational((self.num*other.denom + other.num * self.denom), self.denom*other.denom)

    def __rsub__( self, other ) :
        if not isinstance(other, Rational):
            other = Rational(other[0], other[1])
        if not isinstance(self, Rational):
            self = Rational(self[0], self[1])   
        return Rational((self.num*other.denom + other.num * self.denom), self.denom*other.denom) 

    def __mul__( self, other ) :
        if not isinstance(other, Rational):
            other = Rational(other[0], other[1])
        return Rational(self.num*other.num, self.denom*other.denom)

    def __truediv__( self, other ) :
        if not isinstance(other, Rational):
            other = Rational(other[0], other[1])
        return Rational(self.num * other.denom, self.denom * other.num)

    def __eq__( self, other ):
        if not isinstance(other, Rational):
            other = Rational(other[0], other[1])
        if self.num == other.num and self.denom == other.denom:
            return True
        else :
            return False

    def __ne__( self, other ) :
        if not isinstance(other, Rational):
            other = Rational(other[0], other[1])
        if self.num == other.num and self.denom == other.denom:
            return False
        else :
            return True

    def __lt__( self, other ) :
        if not isinstance(other, Rational):
            other = Rational(other[0], other[1])
        if self.num / self.denom < other.num / other.denom:
            return True
        else : 
            return False

    def __gt__( self, other ) :
        if not isinstance(other, Rational):
            other = Rational(other[0], other[1])
        if self.num / self.denom < other.num / other.denom:
            return False
        else : 
            return True

    def __le__( self, other ) :
        if not isinstance(other, Rational):
            other = Rational(other[0], other[1])
        if self.num / self.denom <= other.num / other.denom:
            return True
        else : 
            return False

    def __ge__( self, other ) :
        if not isinstance(other, Rational):
            other = Rational(other[0], other[1])
        if self.num / self.denom >= other.num / other.denom:
            return True
        else : 
            return False

    def getfloat( self ) :
        return self. num / self. denom

