#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 22 13:12:00 2021

@author: alrier
"""

import mysql.connector

def crear_conexion(nombre_host, usuario, contrasena, basedatos):
    conexion = None
    try:
        conexion = mysql.connector.connect(
                host = nombre_host,
                user = usuario,
                passwd = contrasena,
                database = basedatos
                )
        print('Conexión realizada satisfactoriamente')
    except Error as e:
        print("Error al establecer conexión: ",e)
    
    return conexion

conexion=crear_conexion('34.122.51.150','alvaroriverae','alvaroriverae','alvaroriverae')