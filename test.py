'''
Created on 7/4/2016

@author: suarez
'''

import requests
import json
import uuid, datetime
import hashlib, binascii
from bson.json_util import loads

def insert_ticket(ticket, nombre_estacionamiento):
    url = "http://localhost:8000/insert_ticket/"
    headers = {'content-type': 'application/json'}
    # Data a enviar
    data = {
        'num_ticket': ticket,
        'hora_entrada': str(datetime.datetime.utcnow()),
        'nombre_estacionamiento': nombre_estacionamiento,
        'pago_hecho': False
    }
    # Request POST
    r = requests.post(url, data=json.dumps(data), headers=headers)
    print(r.text)


def pago_ticket(num_ticket):
    url = "http://localhost:8000/pagar_ticket/"
    headers = {'content-type': 'application/json'}
    # Data a enviar
    data = {
        'num_ticket': num_ticket,
    }
    r = requests.post(url, data=json.dumps(data), headers=headers)
    print(r.text)

def crear_cajero(usuario, password, nombre, apellido, cedula, telefono, nivel, cargo, direccion):
    cashier = {
        'usuario': usuario,
        'password': password,
        'nombre_cajero': nombre,
        'apellido_cajero': apellido,
        'cedula_cajero': cedula,
        'telefono': telefono,
        'nivel_cajero': nivel,
        'cargo_cajero': cargo,
        'direccion_cajero': direccion,
    }
    print(cashier)
    url = "http://localhost:8000/create_cashier/"
    headers = {'content-type': 'application/json'}
    r = requests.post(url, data=json.dumps(cashier), headers=headers)
    print(r.text)


def delete_cajero(username):
    cashier = {
        'usuario': username,
    }
    print(cashier)
    url = "http://localhost:8000/delete_cashier/"
    headers = {'content-type': 'application/json'}
    r = requests.post(url, data=json.dumps(cashier), headers=headers)
    print(r.text)


def verificar_password(username, password):
    cashier = {
        'usuario': username,
        'password': password,
    }
    print(cashier)
    url = "http://localhost:8000/verif_password/"
    headers = {'content-type': 'application/json'}
    r = requests.post(url, data=json.dumps(cashier), headers=headers)
    print(r.text)


def add_operacion(ticket, tipo_opera, num_taquilla, nombre_estacio, cajero, pago_hecho, monto_pago):
    operacion = {
        'ticket': ticket,
        'tipo_operacion': tipo_opera,
        'num_taquilla': num_taquilla,
        'nombre_estacionamiento': nombre_estacio,
        'cajero': cajero,
        'pago_hecho': pago_hecho,
        'monto_pago': monto_pago,
    }
    print(operacion)
    url = "http://localhost:8000/add_operation/"
    headers = {'content-type': 'application/json'}
    r = requests.post(url, data=json.dumps(operacion), headers=headers)
    print(r.text)


def get_operaciones_fecha(fecha_inicial, fecha_final):
    filtro = {
        'fecha_inicial': fecha_inicial,
        'fecha_final': fecha_final,
    }
    print(filtro)
    url = "http://localhost:8000/get_ope_fecha/"
    headers = {'content-type': 'application/json'}
    r = requests.post(url, data=json.dumps(filtro), headers=headers)
    j = loads(r.json())
    for docs in j:
        print docs


def add_estacionamiento(nombre, puestos, descripcion, direccion, fraccion, menos_tres, mas_tres, iva):
    estacionamiento = {
                        'nombre': nombre,
                        'puestos': puestos,
                        'descripcion':descripcion,
                        'direccion': direccion,
                        'fraccion': fraccion,
                        'menos_tres': menos_tres,
                        'mas_tres':mas_tres,
                        'iva': iva,
                         }
    print(estacionamiento)
    url = "http://localhost:8000/add_estaciona/"
    headers = {'content-type': 'application/json'}
    r = requests.post(url, data=json.dumps(estacionamiento), headers=headers)
    print(r.text)


#agregar estacionamiento
add_estacionamiento('estacionamiento prueba',250,'estacio de prueba para verq tal','El marques',4.25,12.0,12.0,15)
#Operaciobes por feccha
#d = datetime.datetime.utcnow() - datetime.timedelta(days=2)
#get_operaciones_fecha(str(d), str(datetime.datetime.utcnow()))
#add_operacion('123456789','operacion prueba',15,'Estacionamiento Gary','Gary Suarez',True,250.456)
#verificar_password('suarezgary','19965282')
# delete_cajero('suarezgary')
#crear_cajero('suarezgary','19965282','gary','suarez','19965282','0414-3961758',4,'cajero','el marques, calle macareo')


#insert_ticket(123456789012,'Estacionamiento Gary')
#pago_ticket(123456789012)