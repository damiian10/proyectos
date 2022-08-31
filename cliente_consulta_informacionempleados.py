import requests

def raya():
    print('---------------------------------------------------------------------')
    return

url = 'http://45.90.108.154/fake-api/employee/api/v1/employees'

response = requests.get(url)
#print(response)
data = response.json()
#print(data)
empleados = data['data']
salarios = data['data']
edades = data['data']
ids= data['data']


print()
print('\033[34m')
raya()
print('            ANÁLISIS DE DATOS EMPLEADOS EMPRESA XYZ                      ' )
raya()

print()
print('LA DATA DE LOS EMPLEADOS ES : ')
print(empleados)

def listar_empleados(url):
    empleados = requests.get(url)
    empleados = empleados.json()
    #print(empleados)
    #print(empleados['data'])
    #print()

    # IDS DE LOS EMPLEADOS
    #print(empleados['data'][14]['id'])
    id_edad_menor = empleados['data'][14]['id']
    id_edad_mayor = empleados['data'][2]['id']
    id_salariomax = empleados['data'][16]['id']
    id_salariomin = empleados['data'][23]['id']

    #NOMBRES DE LOS EMPLEADOS
    #print(empleados['data'][14]['employee_name'])
    nombre_edad_menor = empleados['data'][14]['employee_name']
    nombre_edad_mayor = empleados['data'][2]['employee_name']
    nombre_salario_maximo = empleados['data'][16]['employee_name']
    nombre_salario_minimo = empleados['data'][23]['employee_name']

    #SALARIOS DE LOS EMPLEADOS
    #print(empleados['data'][14]['employee_salary'])
    salario_maximo = empleados['data'][16]['employee_salary']
    salario_minimo = empleados['data'][23]['employee_salary']

    #EDAD DE LOS EMPEADOS
    #print(empleados['data'][14]['employee_age'])
    edad_menor = empleados['data'][14]['employee_age']
    edad_mayor = empleados['data'][2]['employee_age']
    #for empleado in empleados:
        #print(empleados['data'])

    print('\033[31m')
    print (f'EDAD MENOR DE LOS EMPLEADOS' )
    print('\033[34m')
    print (f'La edad menor de todos los empleados es : *  {edad_menor}  *  ')
    print (f'Nombre del empleado de la edad minima   : *  {nombre_edad_menor}  *  ')
    print (f'El codigo (id) del empleado es          : *  {id_edad_menor}    * ')
    raya()
    print()
    print('\033[31m')
    print(f'EDAD MAYOR DE LOS EMPLEADOS')
    print('\033[34m')
    print(f'La edad menor de todos los empleados es : *  {edad_mayor}  *  ')
    print(f'Nombre del empleado de la edad minima   : *  {nombre_edad_mayor}  *  ')
    print(f'El codigo (id) del empleado es          : *  {id_edad_mayor}    * ')
    raya()
    print()
    print('\033[31m')
    print(f'SALARIO MAXIMO DE LOS EMPLEADOS')
    print('\033[34m')
    print(f'El salario maximo de todos los empleados es : *  {salario_maximo}  *  ')
    print(f'Nombre del empleado con salario maximo      : *  {nombre_salario_maximo}  *  ')
    print(f'El codigo (id) del empleado es              : *  {id_salariomax}    * ')
    raya()
    print()
    print('\033[31m')
    print(f'SALARIO MINIMO DE LOS EMPLEADOS')
    print('\033[34m')
    print(f'El salario minimo de todos los empleados es : *  {salario_minimo}  *  ')
    print(f'Nombre del empleado con salario minimo      : *  {nombre_salario_minimo}  *  ')
    print(f'El codigo (id) del empleado es              : *  {id_salariomin}    * ')


def detalle_empleados(empleo):
    ruta_pais = 'http://45.90.108.154/fake-api/employee/api/v1/employees' + empleo
    empleo = requests.get(ruta_pais)
    empleo = empleo.json()


for id in ids:
    ids= id['id']
    #print(ids)
#print('El numero de personas son:', ids)

for empleado in empleados:
    nombres= empleado['employee_name']
    #print(nombres)
raya()
print('\033[34m')
print('EL NUMERO DE EMPLEADOS DE LA EMPRESA XYZ ES  :   ', ids )
raya()
print()

for salario in salarios:
    salarios= salario['employee_salary']
    #print(salarios)

for edad in edades:
    edades= edad['employee_age']
    #print(edades)

if __name__=='__main__':
    url= 'http://45.90.108.154/fake-api/employee/api/v1/employees'
    listar_empleados(url)
    detalle_empleados('')



