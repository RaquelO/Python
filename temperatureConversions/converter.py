#declare class
class Temperature :
    def __init__(self) :#initialize and set ftemp to 1.0
        self.ftemp = 1.0

    #mutator function to overwrite value of ftemp with argument passed to it
    def settemperature(self, ftempin) :
        self.ftemp = ftempin

    #accessor function that returns value of ftemp
    def gettemperature(self) :
        return self.ftemp

    #accessor function to return calculated celsius temperature conversion
    def tocelsius(self) :
        return ((self.ftemp - 32) * (5/9))

    #accessor function to return calculated kelvin temperature conversion
    def tokelvin(self) :
        return ((self.ftemp + 459.67) * (5/9))
