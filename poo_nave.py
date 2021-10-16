#Declaracion de una clase
#convencion de nombre de clases: La primera letra va en mayuscula y el nombre en singular
class Nave:
    """
    #atributos
    nombre = "Halcon milenario"
    motor_encendido = False
    material = "aluminio"
    combustible = "premium"
    peso_carga = 0
    kilometraje = 0"""
    #metodo contructor que se ejecuta automaticamente en la construccion de un objeto
    def __init__(self):
        #atributos
        self.nombre = input("Como se va a llamar tu nave: ")
        self.motor_encendido = False
        self.material = input("De qué material será tu nave: ")
        self.combustible = input("Cual será el combustible de tu nave: ")
        self.peso_carga = 0
        self.kilometraje = 0

    #metodos
    def volar(self, tiempo):
        print("La nave esta volando...")
        self.kilometraje = self.kilometraje + tiempo*10
    def aterrizar(self, lugar):
        print("La nave esta aterrizando en: "+lugar)
    def encender(self):
        self.motor_encendido = True
    
    def imprimir_obj(self):
        print("Nombre: ", self.nombre)
        print("Material: ", self.material)
        print("Combustible: ", self.combustible)
        print("Kilometraje actual: ", self.kilometraje)
        print("Peso de carga: ", self.peso_carga)


#definicion de un objeto
mi_nave = Nave()
navecita = Nave()
mi_nave.imprimir_obj()
print("-----------------------------")
navecita.imprimir_obj()
#ejecucion de un método
mi_nave.encender()
print("Estado del motor")
if(mi_nave.motor_encendido==True):
    print("El motor esta encendido")
else:
    print("El motor está apagado")
mi_nave.volar(50)



    

    
