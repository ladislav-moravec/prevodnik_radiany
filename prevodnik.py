import math

class Prevodnik():
    #Obsahuje pomocné metody pro převod mezi radiány a stupni

    #Převede radiány na stupně
    @staticmethod
    def radiany_na_stupne(radiany):
        return math.degrees(radiany)

    #Převede stupně na radiány
    @staticmethod
    def stupne_na_radiany(stupne):
        return math.radians(stupne)