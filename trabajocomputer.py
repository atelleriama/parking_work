# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import time
import csv
import tkinter as tk
from datetime import datetime
import serial

PORT = "COM4"
BAUD = 9600

arduino = serial.Serial(PORT, BAUD)
time.sleep(2)

ruta_archivo = r"G:\My Drive\2 CURSO\Computer Science\trabajocomputer\parking_data.csv"
file = open(ruta_archivo, "w", newline="")
writer = csv.writer(file)
writer.writerow(["Time", "Cars_inside", "Total_spaces", "Free_spaces", "Air_value", "Gate_status"])
