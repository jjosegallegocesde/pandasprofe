from data.listado import listado
from data.aleatorio import crearEmpleados
import pandas as pd
from crearTabla import crearTabla

# selección, filtrado, agrupación y transformación de datos encontrar valores atípicos, identificar tendencias, y buscar patrones en los datos
#Estadísticas básicas: Pandas tiene métodos integrados para calcular estadísticas básicas como la media, mediana, desviación estándar, varianza, máximo, mínimo, y cuartiles de una lista de datos
#

tabla=pd.DataFrame(listado, columns=['nombre','edad'])
#print(tabla)

tabla2=pd.read_csv("./data/empleados.csv")

empleados=crearEmpleados()

tabla3=pd.DataFrame(empleados)
datos = pd.DataFrame([165, 170, 158, 172, 175, 168, 163, 169, 166, 174, 180],columns=['estaturas'])


'''jovenes=tabla2[tabla2["edad"]<28]
filtro = tabla2[(tabla2['edad'] < 28) & (tabla2['cargo'] == 'analista1')]
jovenes2 = tabla2.query('edad < 28')
filtro2=tabla2.query('edad < 28 and cargo == "analista1"')
print(filtro)'''

crearTabla(tabla3,"tabla3")
crearTabla(tabla2,"tabla2")






'''moda = datos['estaturas'].mode()
media = datos['estaturas'].mean()
mediana = datos['estaturas'].median()
desviacion_estandar = datos['estaturas'].std()'''


'''print("\n")
print(tabla2.head())

print("\n")
print(tabla2.tail())

print("\n")
print(tabla2.info())

print("\n")
print(tabla2['salario'].sum())

print("\n")
print(tabla2[['nombres','salario']])'''

