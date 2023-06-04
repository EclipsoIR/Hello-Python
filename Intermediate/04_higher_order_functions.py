# Clase en vídeo: https://youtu.be/TbcEqkabAWU?t=10172

### Higher Order Functions ###

from functools import reduce


def sum_one(value):
    return value + 1


def sum_five(value):
    return value + 5

# Lo que haces a esta funcion es pasarle 3 parametros 2 son numeros y el utltimo parametro es una funcion que luego la llamas dentro para que se ejecute con esos numeros
def sum_two_values_and_add_value(first_value:float, second_value:int, f_sum):
    return f_sum(first_value + second_value)


print(sum_two_values_and_add_value(5, 2, sum_one))
print(sum_two_values_and_add_value(5, 2, sum_five))

### Closures ###


def sum_ten(original_value):
    def add(value):
        return value + 10 + original_value
    return add


add_closure = sum_ten(1)
print(add_closure(5))
print((sum_ten(5))(1))
print(sum_ten(5)(1))


### Built-in Higher Order Functions ###

numbers = [2, 5, 10, 21, 3, 30]

# Map


def multiply_two(number):
    return number * 2

# print(map(multiply_two, numbers)) si haces esto te devuelve un objeto por eso lo pasa a lista abajo para poder imprimirlo 

print(list(map(multiply_two, numbers)))
print(list(map(lambda number: number * 2, numbers)))

# Filter


def filter_greater_than_ten(number):
    if number > 10:
        return True
    return False


print(list(filter(filter_greater_than_ten, numbers)))
print(list(filter(lambda number: number > 10, numbers)))


# Prueba mia de filtrar primero los numeros y luego multiplicar eso numeros


print(list(map(lambda number : number*2,filter(lambda number : number>15,numbers))))


# Vamos a hacer algo parecido pero en el filtro vamos a poner una lambda con un condicional el filter siempre quiere un true o false 

print(list(map(lambda number : number*2,filter(lambda number : True if "2" in str(number) else False,numbers))))

print(list(filter(lambda number : True if "2" in str(number) else False,numbers)))

# Si quieres pasarle dos listas al filter como se haria ?? 

# numeros2 = [3,34,2]

# print(list(filter(lambda number_1,number_2 : True if ("2" in str(number_1) & "3" in str(number_2)) else False,numbers,numeros2)))


# Reduce

# Lo que hace esto es suma los dos primeros se lo almacena y le suma el siguiente numero osea 2+5 = 7 + 10 = 17 + 21 = 38 +3 = 41 +30 = 71  
def sum_two_values(first_value, second_value):
    return first_value + second_value


print(reduce(sum_two_values, numbers))


print(reduce(lambda number1, number2 : number1*number2, numbers))
