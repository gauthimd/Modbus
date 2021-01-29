#!/usr/bin/python3
# -*- encoding: utf-8 -*-

import time
from pyModbusTCP.client import ModbusClient
from pyModbusTCP import utils
hosts = ["10.11.0.14","10.10.254.2","10.11.0.2"] # Meter, IPC (NAT), IPC (Local)
ports = [502, 30502] #Meter port, IPC port

try:
    print("Connecting to SEL Meter...")
    #c = FloatModbusClient(host = hosts[0], port = ports[0], auto_open=True)
    #if c: print("Connection made...")
    sel = ModbusClient(host=hosts[0], port=ports[0], auto_open=True)
    if sel:print("Connected!")
    while sel.open():
        try:
            #ia = sel.read_input_registers(350,2)
            ia = [0,14]
            print(ia)
            x = bin(ia[1])[2:].zfill(16)
            print(x,type(x))
        except Exception as e:
            print("NOPE",e)
            sel.close()
except:
    print("Shutting down...")
    sel.close()
print("Done")
