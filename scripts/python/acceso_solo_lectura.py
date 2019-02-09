#!/usr/bin/env python
# -*- coding: utf-8 -*-

import psycopg2

conexion_r = psycopg2.connect(host="192.168.8.53",port=4321,database="dbpolitecnico", user="frodo", password="bolson")

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

except:
    print "Ha habido un error, probablemente no exista la tabla que has indicado."

conexion_r.close()
