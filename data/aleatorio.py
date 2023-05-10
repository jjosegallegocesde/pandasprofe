from faker import Faker
import random


def crearEmpleados():

    # Crear una instancia de la clase Faker
    faker = Faker()

    # Crear una lista vacía para almacenar los empleados
    empleados = []

    # Generar 1000 empleados aleatorios
    for i in range(1000):
        # Generar un nombre aleatorio
        nombre = faker.name()
        
        # Generar un cargo aleatorio
        cargo = faker.job()
        
        # Generar un salario aleatorio entre 1000 y 5000
        salario = random.randint(1000, 5000)
        
        # Generar un valor booleano aleatorio para el campo de deudas
        tiene_deudas = random.randint(0, 1)
        
        # Agregar los datos del empleado a la lista de empleados
        empleados.append({
            'nombre': nombre,
            'cargo': cargo,
            'salario': salario,
            'tiene_deudas': bool(tiene_deudas)
        })

    return empleados
