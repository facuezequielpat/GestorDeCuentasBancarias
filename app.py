from flask import Flask , render_template, request, redirect, url_for, flash
"""Flask: Este módulo es la base de Flask y se utiliza para crear instancias de la aplicación Flask.
render_template: Se utiliza para renderizar plantillas HTML en la aplicación Flask.
request: Permite acceder a los datos enviados por el cliente, como formularios y parámetros de URL.
redirect: Se utiliza para redirigir a los usuarios a otra URL dentro de la aplicación.
url_for: Genera URLs para funciones de vista dentro de la aplicación Flask.
flash: Se utiliza para mostrar mensajes flash, que son mensajes temporales que se muestran al usuario 
en la próxima solicitud."""
from flask_mysqldb import MySQL

app= Flask(__name__)#al crear una instancia de la clase Flask con Flask(__name__)
#, estás proporcionando a Flask el nombre del módulo actual como el "nombre de paquete".

#MYSQL connection
app.config['MYSQL_HOST']='localhost'#localhost = anfitrion local
app.config['MYSQL_USER']='root'#root = raiz
app.config['MYSQL_PASWOORD']=''
app.config['MYSQL_DB']='banco'
mysql=MySQL(app)#estás pasando tu aplicación Flask app como parámetro al constructor de la clase MySQL.
#Esto se hace para configurar la conexión de la base de datos dentro de tu aplicación Flask.

app.secret_key='mysecretkey'#La clave secreta se utiliza para proteger datos sensibles
#como las sesiones de usuario y otros datos almacenados en cookies.
#Debe ser suficientemente compleja para evitar que sea adivinada fácilmente por terceros.
@app.route('/')
def Index():
    cursor=mysql.connection.cursor()# conecta el cursor
    cursor.execute(
                    """SELECT p.dni,p.nombre,p.apellido,
                    d.deposito,d.retiro,d.saldo, d.fechaIngreso FROM persona p INNER JOIN dep_ret d ON p.dni=d.dni_dep_ret""")
    respuesta = cursor.fetchall()
    return render_template('Index.html', usuarios=respuesta)

@app.route('/Registrar_usuario', methods=['POST'])
def agregar():
    if request.method == 'POST':
        dni_correcto=True
        while dni_correcto:
            dni=request.form['dni']
            if dni.isnumeric():
                if len(dni)==8:
                    dni_correcto= False
                else:
                    flash("El dni debe tener 8 digitos")
                    return redirect(url_for('Index'))
            elif dni.isalnum():
                flash("El dni no debe ser alfanumerico")
                return redirect(url_for('Index'))
            else:
                flash("Ingrese Dni valido, no es numerico")
                return redirect(url_for('Index'))
        nombre=request.form['nombre']
        apellido= request.form['apellido']
        deposito=float(request.form['deposito'])
        retiro= float(request.form['retiro'])
        x=True
        while x:
            if retiro <= deposito:
                x=False
            else:
                flash("El retiro debe ser menor que el deposito")
                return redirect(url_for('Index'))
        saldo=deposito-retiro
        cursor=mysql.connection.cursor()
        sql_persona = "INSERT INTO persona (dni, nombre, apellido) VALUES (%s,%s,%s)"
        sql_dep_ret = "INSERT INTO dep_ret (deposito, retiro, saldo, dni_dep_ret, fechaIngreso) VALUES (%s, %s,%s, %s,CURRENT_TIMESTAMP())"
        cursor.execute(sql_persona, (dni, nombre, apellido,))
        cursor.execute(sql_dep_ret, (deposito, retiro, saldo, dni,))
        mysql.connection.commit()
        flash('Usuario registrado')
        return redirect(url_for('Index'))

        


@app.route('/Mostrar_usuario')
def mostrar():
    return 'Mostrar Usuario'

@app.route('/Buscar_usuario')
def buscar():
    return'Buscar usuario'

@app.route('/Seleccionar_usuario/<dni>')
def seleccionar_usuario(dni):
    cursor = mysql.connection.cursor()
    sql="""SELECT p.dni,p.nombre,p.apellido
                FROM persona p  
                WHERE p.dni= %s;"""# Corregir este codigo, por que al hacer editar todo, se mantiene el saldo anterior.
    cursor.execute(sql,(dni,))
    data=cursor.fetchone()
    return render_template('editarUsuario.html', usuario=data)

@app.route('/Editar_todo/<dni>', methods=['POST'])
def editar_todo(dni):
    if request.method=='POST':
        cursor = mysql.connection.cursor()
        cursor.execute(
            """SELECT p.dni,p.nombre,p.apellido,
            d.deposito,d.retiro,d.saldo,d.fechaIngreso 
            FROM persona p INNER JOIN dep_ret d 
            ON p.dni=d.dni_dep_ret 
            WHERE p.dni= %s;""", (dni,))
        usuario = cursor.fetchone()
        if usuario:
            su='seleccionar_usuario'
            dni_correcto=True
            while dni_correcto:
                if dni.isnumeric():
                    if len(dni)==8:
                        dni_correcto= False
                    else:
                        flash("El dni debe tener 8 digitos")
                        return redirect(url_for(su,dni=dni))
                elif dni.isalnum():
                    flash("El dni no debe ser alfanumerico")
                    return redirect(url_for(su,dni=dni))
                else:
                    flash("Ingrese Dni valido, no es numerico")
                    return redirect(url_for(su, dni=dni))   
            nombre=request.form['nombre']
            apellido= request.form['apellido']
            deposito=float(request.form['deposito'])
            deposito+=float(usuario[3])
            retiro= float(request.form['retiro'])
            retiro+=float(usuario[4])
            saldo=deposito-retiro
            x=True
            while x:
                if retiro <= deposito:
                    x=False
                else:
                    flash("El retiro debe ser menor que el deposito")
                    return redirect(url_for(su, dni=dni))
            sql='''UPDATE persona p, dep_ret d SET nombre=%s, apellido=%s, 
                    deposito = %s, retiro = %s,
                    saldo= %s,fechaIngreso = CURRENT_TIMESTAMP()
                    WHERE p.dni= %s AND d.dni_dep_ret= %s'''
            cursor.execute(sql,(nombre,apellido,deposito,retiro,saldo,dni,dni))
            mysql.connection.commit()
            flash('Se ha editado el usuario')
            return redirect(url_for('Index'))

@app.route('/Eliminar_usuario/<string:dni>', methods=['POST', 'GET'])
def eliminar(dni):
    cursor = mysql.connection.cursor()
    sql_dep_ret = "DELETE FROM dep_ret WHERE dni_dep_ret= {0};"
    #sql_bitacora = "DELETE FROM bitacoraTrigger WHERE dni_bitacora= {0};"
    sql_persona = "DELETE FROM persona WHERE dni= {0};" 
    cursor.execute(sql_dep_ret.format(dni))
    #cursor.execute(sql_bitacora.format(dni))
    cursor.execute(sql_persona.format(dni))
    mysql.connection.commit()
    flash('La cuenta a sido eliminada')
    return redirect(url_for('Index'))
@app.route('/Historial/<dni>')
def historial_dni(dni):
        cursor=mysql.connection.cursor()
        sql='SELECT * FROM bitacoraTrigger WHERE consulta_hecha LIKE "%{0}%";'
        cursor.execute(sql.format(dni))
        respuesta = cursor.fetchall()
        return render_template('historial.html', usuarios = respuesta) 

if __name__ == '__main__':# Si lo que se esta ejecutando es el archivo principal
    app.run(port=3000,debug=True)

