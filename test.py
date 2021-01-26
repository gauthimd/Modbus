#!/usr/bin/python3
# -*- encoding: utf-8 -*-

import time
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
try:
    print("Connecting to SEL Meter...")
    #c = FloatModbusClient(host = hosts[0], port = ports[0], auto_open=True)
    #if c: print("Connection made...")
    sel = ModbusClient(host=hosts[0], port=ports[0], auto_open=True)
    if sel:print("Connected!")
    while sel.open():
        try:
            ia = sel.read_input_registers(350,2)
            print("IA is",float(ia[1]/100),"Amps")
            ib = sel.read_input_registers(352,2)
            print("IB is",float(ib[1]/100),"Amps")
            ic = sel.read_input_registers(354,2)
            print("IC is",float(ic[1]/100),"Amps\n")
            w3 = sel.read_input_registers(370,2)
            print("W3 is",float(w3[1]/100),"kW")
            u3 = sel.read_input_registers(372,2)
            print("U3 is",float(u3[1]/100),"kVA")
            q3 = sel.read_input_registers(374,2)
            print("Q3 is",float(q3[1]/100),"kVAR\n")
            time.sleep(2)
        except Exception as e: 
            print("NOPE",e)
            sel.close()
except: 
    print("Aborting")
    sel.close()
print("Disconnecting from meter")
sel.close()
'''
try:
    print("Connecting using Float Client...")
    c = FloatModbusClient(host = hosts[1], port = ports[1], auto_open=True)
    if c: print("Connection made...")
    c.write_float(174,[0.0])
    c.close()
    print("Register written ")
except Exception as e: print(e)
'''
