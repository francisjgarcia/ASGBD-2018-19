#!/usr/bin/env python
# -*- coding: utf-8 -*-

import psycopg2

conexion_w = psycopg2.connect(host="192.168.6.2",port=1234,database="dbpolitecnico", user="postgres", password="bolson")
conexion_r = psycopg2.connect(host="192.168.6.2",port=4321,database="dbpolitecnico", user="postgres", password="bolson")

cursor_w = conexion_w.cursor()
cursor_r = conexion_r.cursor()

sql0 = "SELECT inet_server_addr();"
sql1 = "SELECT COUNT(1) FROM tbalumnos;"
sql2 = "SELECT * FROM tbalumnos;"

try:
        cursor_r.execute(sql0)
        servidor = cursor_r.fetchone()
        print "Estás conectándote y leyendo los datos del servidor %s"%servidor
        cursor_r.execute(sql1)
        datos = cursor_r.fetchone()
        print "Hay %d alumnos registrados en la base de datos:"%datos
        cursor_r.execute(sql2)
        resultados = cursor_r.fetchall()
        for registro in resultados:
            username = registro[1]
            edad = registro[2]
            print "%s (%s años),"%(username,edad),

        print "\nVas a insertar un nuevo alumno en la tabla tbalumnos"

        nombre = raw_input('Nombre del alumno: ')
        edad = int(raw_input('Edad del alumno: '))
        sql3 = "INSERT INTO tbalumnos (nombre,edad) VALUES('%s',%d);"%(nombre,edad)

        try:
            cursor_w.execute(sql0)
            servidor = cursor_w.fetchone()
            cursor_w.execute(sql3)
            conexion_w.commit()
            print "El alumno %s con %d años ha sido añadido satisfactoriamente"%(nombre, edad),
            print "en el servidor %s"%servidor
        except:
            conexion_w.rollback()
            print "Ha habido un error a la hora de insertar los datos."

except:
    print "Ha habido un error, probablemente no exista la tabla que has indicado."

conexion_w.close()
conexion_r.close()
