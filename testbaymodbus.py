#!/usr/bin/python3
IPs = ["10.10.254.2","10.11.0.14"]
ports = [30502,502]
devs = ["Y.Cube","SEL Meter"]
import time
from pyModbusTCP.client import ModbusClient
try:
    print("Connecting to Y.Cube IPC...")
    yq = ModbusClient(host=IPs[0], port=ports[0], auto_open=True)
    if yq.open():
        print("Connected to Y.Cube")
    sel = ModbusClient(host=IPs[1], port=ports[1], auto_open=True)
    if sel.open():
        print("Connected to SEL Meter")
except: 
    print("Error connecting")
    yq.close()
    sel.close()
try:
    while yq.open() and sel.open():
        m1 = sel.read_holding_registers(370,2)/100
        print("Meter value: ", m1)
        yq.write_single_register(174, m1)
        time.sleep(5)
except:
    print("Aborting")
    yq.close()
    sel.close()
