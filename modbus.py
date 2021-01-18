#!/usr/bin/python3
import time
from pyModbusTCP.client import ModbusClient
try:
    print("Connecting to SEL 735...")
    c = ModbusClient(host="10.19.176.237", port=502, auto_open=True)
    if c.open():
        print("Connected!")
    else:
        print("Error connecting")
except: 
    print("Error connecting to host")
if not c.host("10.19.176.237"):
    print("Error connecting to host")
if not c.port(502):
    print("Port error")
try:
    while c.open():
        regs = c.read_holding_registers(205)
        print(regs[0])
        time.sleep(5)
except:
    print("Aborting")
    c.close()
c.close()
