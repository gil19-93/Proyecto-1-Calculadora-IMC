print('''Buenos dias 
Solicitare algunos datos personales para poder generar tu ficha medica
Ten mucha paciencia en el proceso
''')
nombre = input('Introduce tu nombre: ')
apellido = input('Introduce tu apellido paterno: ')
apellido2 = input('Introduce tu apellido materno: ')
edad = int(input('Introduce tu edad: '))
sangre = str(input('Tipo de sangre: '))
peso = int(input('Introduce tu peso en Kg: '))
estatura = float(input('Introduce tu estatura en Mt: '))
correo = (input('Introduce tu correo electronico: '))
numero = int(input('Introduce tu telefono: '))
print(str(sangre))

imc = (peso / (estatura **2))

print('''
++Ficha Medica++
''')
print('Nombre completo:' + nombre, apellido, apellido2)
print('Edad: ' + str(edad))
print('Tipo de sangre: ' + str(sangre))
print('Peso: ' + str(peso))
print('Estatura: ' + str(estatura))
print('I.M.C.: ' + '{:.2f}'.format(imc))
print('Correo electronico: ' + correo)
print('Numero de contacto: ' + str(numero))

final = (input('Ficha completada'))
