###############################################################################
# g3.py - 3d framework module - 2020
#
# Riccardo Soldini - riccardo.soldini@gmail.com
###############################################################################


class Point3D:
    def __init__(self, X=0, Y=0, Z=0):
        self._X=X
        self._Y=Y
        self._Z=Z

    @property
    def X(self):
        return self._X
    @X.setter
    def X(self, X):
        self._X = X

    @property
    def Y(self):
        return self._Y
    @Y.setter
    def Y(self, Y):
        self._Y = Y

    @property
    def Z(self):
        return self._Z
    @Z.setter
    def Z(self, Z):
        self._Z = Z


class Vector3D(Point3D):
    def __init__(self, X=0, Y=0, Z=0):
        self._X=X
        self._Y=Y
        self._Z=Z

    def __add__(self,v):
        return Vector3D(self._X+v._X,
                        self._Y+v._Y,
                        self._Z+v._Z)

class Plane:
    def __init__(self,Point=Point3D(),Normal=Vector3D(0,0,1)):
        self.Point=Point
        self.Normal=Normal

    def __str__(self):
        s='Plane in ('
        s+=str(self.Point._X)+','
        s+=str(self.Point._Y)+','
        s+=str(self.Point._Z)+') at normal ('
        s+=str(self.Normal._X)+','
        s+=str(self.Normal._Y)+','
        s+=str(self.Normal._Z)+')'
        return s



def PlaneFrom3Points(p1,p2,p3):
    a1 = p2._X - p1._X
    b1 = p2._Y - p1._Y
    c1 = p2._Z - p1._Z
    a2 = p3._X - p1._X
    b2 = p3._Y - p1._Y
    c2 = p3._Z - p1._Z
    a = b1 * c2 - b2 * c1
    b = a2 * c1 - a1 * c2
    c = a1 * b2 - b1 * a2
    d = (- a * p1._X - b * p1._Y - c * p1._Z)
    return Plane(p1,Vector3D(a,b,c))
