# importacion del modulo
import psycopg2

#conexion a base de datos
conexion=psycopg2.connect(user='postgres',
                          password='12345678910',  
                          host='localhost',
                          port='5432',
                          database='Python')

# utilizar cursor
cursor=conexion.cursor()

# crear sentencia sql
sql='INSERT INTO personas (id_persona,pers_nombre,pers_apellido,edad) VALUES(%s,%s,%s,%s)'

# solicitud de datos al usuario
id_persona=input('ingrese el identificador:')
pers_nombre=input('ingrese el nombre: ')
pers_apellido=input('ingrese el apellido: ')
edad=input('ingrese la edad: ')

# recoleccion de datos
datos=(id_persona,pers_nombre,pers_apellido,edad)

# hacer uso del metodo execute
cursor.execute(sql,datos)

# guardar registro
conexion.commit()

# registro insertados
registros=cursor.rowcount

# mostrar mensaje
print(f'registro insertado: {registros}')

# cerrar conexiones
cursor.close()
conexion.close()