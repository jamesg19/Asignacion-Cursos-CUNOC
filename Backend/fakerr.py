from faker import Faker

fake = Faker()

nombres_aleatorios = [fake.name() for _ in range(500)]

# Imprimir los nombres aleatorios generados
for nombre in nombres_aleatorios:
    # sustituir espacio en blanco por coma
    #print(nombre.replace(' ', ','))
    # eliminar texto despues de encontrar espacio en blanco
    print(nombre.split(' ')[1])
    #print(fake.name())
