import sys

class Inna:
    def __str__(self):
        return "siema"
class Klasa:
    def __init__(self,x):
        self.x=x
    def string(self,s):
        return self.x.join(s)

i=Inna()
print(i)
k = Klasa('x')
print(k.string(sys.argv))
