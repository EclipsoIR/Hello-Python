class Car :
    def __init__(self,brand,model):# Aqui lo que estamos haciendo es el contructor de la clase
        # self.brand = brand
        # self.model=model
        self.brand_model =f"{brand} {model}"
        self.__model = model # Aqui estamos haciendo la variblae model privada
        
    
    
    def funciona(self,bool:bool):
        if (bool):
            print(f"El coche {self.brand_model} esta funcionando")
        else:
            print(f"El coche {self.brand_model} no esta funcionando")

    # Vamos a crear una funcion que lo que haga es retornar el modelo porque como lo hemos puesto privado no se puede devolver
    def get_model (self):
        return self.__model

my_car = Car("Kia","Rio")
print(my_car)
# print(my_car.brand,my_car.model)
print(my_car.brand_model)
my_car.funciona(True)

my_othercar = Car("Kia","Sportage")

print(my_othercar.brand_model)

# LO que hacemos aqui es setear el nuevo brand_model de myother_car
my_othercar.brand_model="BMW M2"

print(my_othercar.brand_model)

# print(my_car.__model) #Esto peta porque la variable __model es privada


print(my_car.get_model())

my_car.__model="PRueba" #No peta pero no escribe el modelo porque la variable es privada 

print(my_car.get_model())