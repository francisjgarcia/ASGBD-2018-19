#!/usr/bin/env python

import os, argparse

parser = argparse.ArgumentParser()
parser.add_argument("-u", required=True, dest="usuario", help="Usuario de PostgreSQL")
parser.add_argument("-H", default="localhost", dest="host", help="IP del equipo remoto")
parser.add_argument("-p", default="5432", dest="puerto", help="Puerto del equipo remoto")
parser.add_argument("-db", required=True, dest="database", help="Nombre de la base de datos")
args = parser.parse_args()
if args.usuario: usuario = "-U "+args.usuario
if args.host: host = "-h "+args.host
if args.puerto: puerto = "-p "+args.puerto
if args.database: database = args.database

print "En el directorio actual tienes los siguientes backups:"
os.system("ls *.sql.gz 2>/dev/null")
backup = raw_input('Backup a recuperar: ')

print "Eliminando la base de datos..."
os.system("dropdb "+usuario+" "+host+" "+puerto+" "+database)

print "Creando la base de datos..."
os.system("createdb "+usuario+" "+host+" "+puerto+" "+database)

print "Descomprimiendo y restaurando backup..."
os.system("gunzip < "+backup+" | psql "+usuario+" "+host+" "+puerto+" -d "+database)