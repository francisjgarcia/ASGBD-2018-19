#!/usr/bin/env python
# -*- coding: utf-8 -*-

import psycopg2

conexion_w = psycopg2.connect(host="192.168.6.2",port=1234,database="postgres", user="postgres", password="bolson")
conexion_r = psycopg2.connect(host="192.168.6.2",port=4321,database="postgres", user="postgres", password="bolson")

cursor_w = conexion_w.cursor()
cursor_r = conexion_r.cursor()

sql0 = "SELECT inet_server_addr();"

try:
    cursor_w.execute(sql0)
    cursor_r.execute(sql0)

    datos_escritura = cursor_w.fetchone()
    datos_lectura = cursor_r.fetchone()

    permiso_escritura = datos_escritura[0]
    permiso_lectura = datos_lectura[0]

    print("Consulta de escritura: "+permiso_escritura)
    print("Consulta de lectura: "+permiso_lectura)

except:
        print "Ha habido un error durante la conexión con alguna base de datos."

conexion_w.close()
conexion_r.close()