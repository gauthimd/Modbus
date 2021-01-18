#!/usr/bin/python3
IP = ["10.11.0.2","10.11.0.12","10.11.0.13"]
port = [30502,502,502]
dev = ["Y.Cube","SEL Meter 1", "SEL Meter 2"]
import time
from pyModbusTCP.client import ModbusClient
try:
    print("Connecting to Y.Cube IPC...")
    yq = ModbusClient(host="10.11.0.2", port=30502, auto_open=True)
    if yq.open():
        print("Connected to Y.Cube")
    sel1 = ModbusClient(host="10.11.0.12", port=502, auto_open=True)
    if sel1.open():
        print("Connected to SEL Meter 1")
    sel2 = ModbusClient(host="10.11.0.13", port=502, auto_open=True)
    if sel2.open():
        print("Connected to SEL Meter 2")
except: 
    print("Error connecting")
    yq.close()
    sel1.close()
    sel2.close()
try:
    while yq.open() and sel1.open() and sel2.open():
        m1 = sel1.read_holding_registers(370,2)/100
        print("Meter 1 value: ", m1)
        m2 = sel2.read_holding_registers(370,2)/100
        print("Meter 2 value: ", m2)
        total = m1 + m2
        print("Total: ", total)
        yq.write_single_register(174, total)
        time.sleep(5)
except:
    print("Aborting")
    yq.close()
    sel1.close()
    sel2.close()
