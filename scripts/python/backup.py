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
os.system("pg_dump "+host+" "+usuario+" "+puerto+" "+database+" | gzip > "+database+"_$(date +%Y-%m-%d).sql.gz")