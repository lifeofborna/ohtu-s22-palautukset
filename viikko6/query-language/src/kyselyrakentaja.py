from matchers import *

class Kyselyrakentaja:
    def __init__(self):
        self.olio = []
    
    def playsIn(self, team):
        self.olio.append(PlaysIn(team))

    def hasAtleast(self, value, what):
        self.olio.append(HasAtLeast(value,what))

    def hasFewerThan(self,value,what):
        self.olio.append(HasFewerThan(value,what))

    def oneOf(self, m1,m2):
        condition1 = True
        condition2 = True
        for x in m1:
            if Or(x):
                condition1 = True
            else: condition1 = False
        for x in m2:
            if Or(x):
                condition2 = True
            else: condition2 =False
            
        if condition1:
            for x in m1:
                self.olio.append(x)
            return self.olio


        if condition2:
            for x in m2:
                self.olio.append(x)
            return self.olio

    def build(self):
        if len(self.olio) == 0:
            return All()
        return self.olio