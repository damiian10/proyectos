import requests

def raya():
    print('--------------------------------------------------------------------------')
    return

url = 'https://dummy.restapiexample.com/api/v1/employees'

response = requests.get(url , headers= {'User-Agent':'insomnia/2022.1.1'})
#print(response)
data = response.json()
#print(data)
#empleados = data['data']
#salarios = data['data']
#edades = data['data']
ids= data['data']

print()
print('\033[35m')
raya()
print('          🔎  ANÁLISIS DE DATOS EMPLEADOS EMPRESA XYZ👨‍💻   🔍                     ' )
raya()

def listar_empleados(url):
    empleados = requests.get(url , headers= {'User-Agent':'insomnia/2022.1.1'})
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
    salariostotales = sum((empleados['data'][0]['employee_salary'],empleados['data'][1]['employee_salary'],empleados['data'][2]['employee_salary'],empleados['data'][3]['employee_salary'],empleados['data'][4]['employee_salary'],empleados['data'][5]['employee_salary'],empleados['data'][6]['employee_salary'],empleados['data'][7]['employee_salary'],empleados['data'][8]['employee_salary'],empleados['data'][9]['employee_salary'],empleados['data'][10]['employee_salary'],
                           empleados['data'][11]['employee_salary'],empleados['data'][12]['employee_salary'],empleados['data'][13]['employee_salary'],empleados['data'][14]['employee_salary'],empleados['data'][15]['employee_salary'],empleados['data'][16]['employee_salary'],empleados['data'][17]['employee_salary'],empleados['data'][18]['employee_salary'],empleados['data'][19]['employee_salary'],empleados['data'][20]['employee_salary'],
                           empleados['data'][21]['employee_salary'],empleados['data'][22]['employee_salary'],empleados['data'][23]['employee_salary'])) / 24
    #print(round(salariostotales, 2))

    #EDAD DE LOS EMPLEADOS
    #print(empleados['data'][14]['employee_age'])
    edad_menor = empleados['data'][14]['employee_age']
    edad_mayor = empleados['data'][2]['employee_age']
    edadestotales = sum((empleados['data'][0]['employee_age'], empleados['data'][1]['employee_age'],empleados['data'][2]['employee_age'], empleados['data'][3]['employee_age'],empleados['data'][4]['employee_age'], empleados['data'][5]['employee_age'],empleados['data'][6]['employee_age'], empleados['data'][7]['employee_age'],empleados['data'][8]['employee_age'], empleados['data'][9]['employee_age'],empleados['data'][10]['employee_age'],
                           empleados['data'][11]['employee_age'], empleados['data'][12]['employee_age'],empleados['data'][13]['employee_age'], empleados['data'][14]['employee_age'],empleados['data'][15]['employee_age'], empleados['data'][16]['employee_age'],empleados['data'][17]['employee_age'], empleados['data'][18]['employee_age'],empleados['data'][19]['employee_age'], empleados['data'][20]['employee_age'],
                           empleados['data'][21]['employee_age'], empleados['data'][22]['employee_age'],empleados['data'][23]['employee_age'])) / 24
    #print(edadestotales)

    print('\033[31m')
    print('LA DATA DE LOS EMPLEADOS ES 🖥️📁 : ')
    print(empleados)
    raya()
    print()
    print (f'LA EDAD MENOR DE LOS EMPLEADOS' )
    print('\033[34m')
    print (f'LA EDAD MAYOR DE TODOS LOS EMPLEADOS ES  : *  {edad_menor}  *  ')
    print (f'NOMBRE DEL EMPLEADO DE LA EDAD MINIMA ES : *  {nombre_edad_menor}  *  ')
    print (f'EL CÓDIGO (ID) DEL EMLPLEADO ES          : *  {id_edad_menor}    * ')
    raya()
    print()
    print('\033[31m')
    print(f'LA EDAD MAYOR DE LOS EMPLEADOS')
    print('\033[34m')
    print(f'LA EDAD MAYOR DE TODOS LOS EMPLEADOS  ES  : *  {edad_mayor}  *  ')
    print(f'NOMBRE DEL EMPLEADO DE LA EDAD MAXIMA ES  : *  {nombre_edad_mayor}  *  ')
    print(f'EL CÓDIGO (ID) DEL EMLPLEADO ES           : *  {id_edad_mayor}    * ')
    raya()
    print()
    print('\033[31m')
    print(f'SALARIO MAXIMO DE LOS EMPLEADOS💰')
    print('\033[34m')
    print(f'EL SALARIO MAXIMO DE TODOS LOS EMPLEADOS ES : *  {salario_maximo}💲  *  ')
    print(f'NOMBRE DEL EMPLEADO CON SALARIO MAXIMO  ES  : *  {nombre_salario_maximo}  *  ')
    print(f'EL CÓDIGO (ID) DEL EMLPLEADO ES             : *  {id_salariomax}    * ')
    raya()
    print()
    print('\033[31m')
    print(f'SALARIO MINIMO DE LOS EMPLEADOS💰')
    print('\033[34m')
    print(f'EL SALARIO MINIMO DE TODOS LOS EMPLEADOS ES : *  {salario_minimo}💲  *  ')
    print(f'NOMBRE DEL EMPLEADO CON SALARIO MINIMO      : *  {nombre_salario_minimo}  *  ')
    print(f'EL CÓDIGO (ID) DEL EMLPLEADO ES             : *  {id_salariomin}    * ')
    raya()
    print()
    print('\033[31m')
    print(f'PROMEDIO DE LOS SALARIOS TOTALES💵 ')
    print('\033[34m')
    print(f'EL SALARIO PROMEDIO DE TODOS LOS EMPLEADOS ES  : *  {round(salariostotales, 2)}💲 *  ')
    raya()
    print()
    print('\033[31m')
    print(f'PROMEDIO DE LAS EDADES TOTALES ')
    print('\033[34m')
    print(f'EL PROMEDIO DE EDAD DE TODOS LOS EMPLEADOS ES  : *  {round(edadestotales, 2)} *  ')
    raya()

for id in ids:
    ids= id['id']
    #print(ids)
#print('El numero de personas son:', ids)

#for empleado in empleados:
#    nombres= empleado['employee_name']
    #print(nombres)

print('\033[34m')
raya()
print(f'EL NUMERO DE EMPLEADOS DE LA EMPRESA XYZ ES 🧑  :    EXISTEN {ids} EMPLEADOS' )
raya()
print()

#for salario in salarios:
#    salarios= salario['employee_salary']
    #print(salarios)

#for edad in edades:
#    edades= edad['employee_age']
    #print(edades)

if __name__=='__main__':
    url= 'https://dummy.restapiexample.com/api/v1/employees'
    listar_empleados(url)




