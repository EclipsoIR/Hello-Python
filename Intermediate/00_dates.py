# Clase en vídeo: https://youtu.be/TbcEqkabAWU

### Dates ###

# Date time

from datetime import timedelta
from datetime import date
from datetime import time
from datetime import datetime



pruebaAntonio = datetime.today()
print("Esta si ",pruebaAntonio.day)
now = datetime.now()


def print_date(date:date):
    print(date.year)
    print(date.month)
    print(date.day)
    print(date.hour)
    print(date.minute)
    print(date.second)
    print(date.timestamp()) # Es lo que se utiliza para guarda fechas en bases de datos es una forma de guardar fechas en un formato estandar.
    


print_date(now)

year_2023 = datetime(2023, 1, 1)

print("Nuevos Datos")
print_date(year_2023)

# Time

current_time = time(21, 6, 0)
print(current_time.hour)
print(current_time.minute)
print(current_time.second)

# Esto no funciona no es como el datetime.now() a la forma del time tienes que definirlo antes como esta arriba
# print("Prueba mia")
# print(time.hour)
# print(time.minute)
# print(time.second)


# Date


current_date = date.today() # Con esto estas inicializando la variable a el dia de hoy
print(current_date.year)
print(current_date.month)
print(current_date.day)

current_date = date(2022, 10, 6)
print("DATE")
print(current_date.year)
print(current_date.month)
print(current_date.day)

current_date = date(current_date.year,
                    current_date.month + 1, current_date.day)

print(current_date.month)

# Operaciones con fechas

diff = year_2023 - now
print(diff)

diff = year_2023.date() - current_date
print(diff)

# Timedelta


start_timedelta = timedelta(200, 100, 100, weeks=10)
end_timedelta = timedelta(300, 100, 100, weeks=13) 

print(end_timedelta - start_timedelta)
print(end_timedelta + start_timedelta)
