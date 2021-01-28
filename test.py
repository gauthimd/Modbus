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
    sel = ModbusClient(host=hosts[0], port=ports[0], auto_open=True)
    if sel:print("Connected!")
    while sel.open():
        try:
            ia = sel.read_input_registers(350,2)
            #print(ia)
            IA = int('0b'+bin(ia[0])[2:]+bin(ia[1])[2:],2)/100.0
            print("IA is",IA,"Amps")
            ib = sel.read_input_registers(352,2)
            IB = int('0b'+bin(ib[0])[2:]+bin(ib[1])[2:],2)/100.0
            print("IB is",IB,"Amps")
            ic = sel.read_input_registers(354,2)
            IC = int('0b'+bin(ic[0])[2:]+bin(ic[1])[2:],2)/100.0
            print("IC is",IC,"Amps")
            w3 = sel.read_input_registers(370,2)
            W3 = int('0b'+bin(w3[0])[2:]+bin(w3[1])[2:],2)/100.0
            print("W3 is",W3,"kW\n")
            '''
            u3 = sel.read_input_registers(372,2)
            U3 = int('0b'+bin(u3[0])[2:]+bin(u3[1])[2:],2)/100.0
            print("U3 is",U3,"kVA")
            q3 = sel.read_input_registers(374,2)
            Q3 = int('0b'+bin(q3[0])[2:]+bin(q3[1])[2:],2)/100.0
            print("Q3 is",Q3,"kVAR\n")
            '''
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
