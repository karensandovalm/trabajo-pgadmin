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

# sentencia sql
sql='DELETE FROM personas WHERE id_persona=%s'

# solicitar dato al usuraio
idpersona=input('ingrese el id del registro a eliminar: ')

# metodo execute
cursor.execute(sql,idpersona)

# guardar cambios
conexion.commit()

# conteo de registro eliminado
registro_eliminado=cursor.rowcount

# mensaje al usuario
print(f'registros eliminados: {registro_eliminado}')

# cerrar conexiones
cursor.close()
conexion.close()