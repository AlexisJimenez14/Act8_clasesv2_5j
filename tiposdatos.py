print(" Clase V2 Alexis Fabian Jimenez Jimenez")
#zona de clase
class Datos:
    # el constructor funcion
    def __init__(self,estatura,peso):
        self.estatura = estatura
        self.peso = peso
    def mostrar_datos(self):
        print(f"estatura: {self.estatura} mts,peso {self.peso}")

    def mi_lista(self):
        animales_miticos=["hydra","quimera","dragon","wyverm"]
        print(animales_miticos)
        for x in animales_miticos:
            print(x)
    def mi_tupla(self):
        hermanos=("juan","pedro","pablo","diego","daniel")
        print(hermanos)
        for x in hermanos:
            print(x)
    def mi_set(self):
        chiles={"habanero","aji","rocoto","jalapeño","morron"}
        print(chiles)
        for x in chiles:
            print(x)
            
    def mi_diccionario(self):
        iphone={
            "iphone ":"9/1/2007",
            "iphone 6":"19/9/2014",
            "iphone x":"3/11/2017",
            "iphone 12 ":"23/10/2022"
        }
        print(iphone)
        for x in iphone:
            print(x, iphone[x])
    

#creacion del objeto
info= Datos(1.66,70.5)

# utilizando objetos
info.mostrar_datos()
print("bestias miticas Alexis Jimenez -listas")
info.mi_lista()
print("hermanos Alexis Jimenez -tupla")
info.mi_tupla()
print("chiles Alexis Jimenez -set")
info.mi_set()
print("iphone s Alexis Jimenez -diccionario")
info.mi_diccionario()
