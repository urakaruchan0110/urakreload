#!/usr/bin/python
# -*- coding: utf-8 -*-

import subprocess
#---------------------------------------------------------Dibujo
print "-------------------------------------------------------------"
print " ██╗   ██╗██████╗ ██████╗  █████╗ ████████╗███████╗██████╗   "
print " ██║   ██║██╔══██╗██╔══██╗██╔══██╗╚══██╔══╝██╔════╝██╔══██╗  "
print " ██║   ██║██████╔╝██║  ██║███████║   ██║   █████╗  ██████╔╝  "
print " ██║   ██║██╔═══╝ ██║  ██║██╔══██║   ██║   ██╔══╝  ██╔══██╗  "
print " ╚██████╔╝██║     ██████╔╝██║  ██║   ██║   ███████╗██║  ██║  "
print "  ╚═════╝ ╚═╝     ╚═════╝ ╚═╝  ╚═╝   ╚═╝   ╚══════╝╚═╝  ╚═╝  "
print "-------------------------------------------------------------"

#-------------------------------------------------------Preguntas
print "Instalar"
print "Descargar"
print "Borrar"
print "Todo"
#------------------------------------------------------Variables
yo = raw_input()
u = "Descargar"
i = "Instalar"
rm = "Borrar"
up = "Todo"
#--------------------------------------------------------------Borrar
if( yo == rm):
	print "se borraran archivos basura"
	subprocess.call(["sudo","apt-get","autoremove"])
#--------------------------------------------------------------Descargar Actualizaciones
if(yo == u):
	print "se descargaran actualizaciones"
	subprocess.call(["sudo","apt-get","update"])
#---------------------------------------------------------------Instalar Actualizaciones

if(yo == i):
	print "Se instalaran las Actualizaciones"
	subprocess.call(["sudo","apt-get","upgrade"])
else:
	print "ERROR"
#------------------------------------------------------------------------
if(yo == up):
	print "Se actualizara todo el sistema"
	subprocess.call(["apt-get","update"])
	subprocess.call(["apt-get","upgrade"])
	subprocess.call(["apt-get","dist-upgrade"])
	subprocess.call(["sudo","apt-get","autoremove"])
