#!/usr/bin/python3
# -*- encoding: utf-8 -*-

import time, datetime
from pyModbusTCP.client import ModbusClient
from pyModbusTCP import utils
hosts = ["10.11.0.14","10.10.254.2","10.11.0.2"] # Meter, IPC (NAT), IPC (Local)
ports = [502, 30502] #Meter port, IPC port

class FloatModbusClient(ModbusClient):   #This class was needed to allow writing floats
    def read_float(self, address, number=1):
        reg_1 = self.read_holding_registers(address, number * 2)
        if reg_1:
            print(reg_1)
            return [utils.decode_ieee(f) for f in utils.word_list_to_long(reg_1)]
        else:
            return None

    def write_float(self, address, floats_list):
        b32_1 = [utils.encode_ieee(f) for f in floats_list]
        b16_1 = utils.long_list_to_word(b32_1)
        return self.write_multiple_registers(address, b16_1)

#First open a connection to the SEL meter
try:
    print("Connecting to SEL Meter...")
    sel = ModbusClient(host=hosts[0], port=ports[0], auto_open=True)
    if sel.open():
        print("Connected to SEL!\n")
    else:
        print("Error connecting to SEL Meter")
except: 
    print("Error connecting to SEL Meter")
    print("Aborting")
    sel.close()

#Second, open a connection to the IPC modbus server
try:
    print("Connecting using Float Client...")
    c = FloatModbusClient(host=hosts[1], port=ports[1], auto_open=True)
    if c: print("Connection made...")
except:
    print("Error connecting to IPC...")
    c.close()

#Once both connections are made, the main loop can run
if sel and c: print("Beginning main loop...")
while True:
    try:
        start = datetime.datetime.now()
        w = sel.read_input_registers(370,2)
        w3 = -1*float(w[1]/100)
        c.write_float(174,[w3])
        end = datetime.datetime.now()
        print("W3 is",w3,"\n","Time delta is",end - start,"secs")
    except Exception as e: print("Somethings jacked",e)
sel.close()
c.close()
print("Connections closed. Complete")
