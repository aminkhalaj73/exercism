from __future__ import division
from fractions import gcd
class Rational(object):
    def __init__(self, numer, denom):
        if denom == 0 :
            raise Exception("wrong value for denom")
        
        _gcd = gcd(numer , denom)
        self.numer = numer / _gcd
        self.denom = denom / _gcd


    def __eq__(self, other):
        return self.numer == other.numer and self.denom == other.denom

    def __repr__(self):
        return '{}/{}'.format(self.numer, self.denom)

    def __add__(self, other):
        numer = self.numer * other.denom + other.numer * self.denom
        denom = self.denom * other.denom
        return Rational(numer , denom)


    def __sub__(self, other):
        numer = self.numer * other.denom - other.numer * self.denom
        denom = self.denom * other.denom
        return Rational(numer , denom)

    def __mul__(self, other):
        numer = self.numer * other.numer
        denom = self.denom * other.denom
        return Rational(numer , denom)

    def __truediv__(self, other):
        numer = self.numer * other.denom
        denom = self.denom * other.numer
        return Rational(numer , denom)

    def __abs__(self):
        numer = abs(self.numer)
        denom = abs(self.denom)
        return Rational(numer , denom)

    def __pow__(self, power):

        if power < 0 :
            absolute_pow = abs(power)
            numer = self.denom ** absolute_pow
            denom = self.numer ** absolute_pow
            return Rational(numer , denom)
        elif power == 0 :
            numer = 1
            denom = 1
            return Rational(numer , denom)
        else:
            numer = self.numer ** power
            denom = self.denom ** power
            return Rational(numer , denom)


    def __rpow__(self, base):
        return (abs(base) ** self.numer) ** (1 / self.denom)
