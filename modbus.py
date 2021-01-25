#!/usr/bin/python3
import time
from pyModbusTCP.client import ModbusClient
hosts = ["10.19.176.237","10.11.0.14","10.10.254.2"]
ports = [502, 30502]
try:
    print("Connecting to SEL 735...")
    c = ModbusClient(host=hosts[1], port=ports[0], auto_open=True)
    if c.open():
        print("Connected to meter!")
    else:
        print("Error connecting to meter")
except: 
    print("Error connecting to host")
if not c.host(hosts[1]):
    print("Error connecting to host")
if not c.port(ports[0]):
    print("Port error")
try:
    print("Connecting to Y.Cube IPC Modbus Server...")
    c = ModbusClient(host=hosts[2], port=ports[1], auto_open=True)
    if c.open():
        print("Connected to Y.CUbe!")
    else:
        print("Error connecting to Y.Cube")
except: 
    print("Error connecting to host")
if not c.host(hosts[2]):
    print("Error connecting to host")
if not c.port(ports[1]):
    print("Port error")
try:
    while c.open():
#       regs = c.read_holding_registers(205)
        regs = c.read_holding_registers(370,2)
        print(regs[0])
        time.sleep(5)
except:
    print("Aborting")
    c.close()
c.close()
