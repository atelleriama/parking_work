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

root = tk.Tk()
root.title("Smart Parking Access Control")
root.geometry("350x280")

label_title = tk.Label(root, text="Smart Parking Dashboard", font=("Arial", 16, "bold"))
label_title.pack(pady=10)
label_cars = tk.Label(root, text="Cars inside: ---", font=("Arial", 13))
label_cars.pack(pady=5)
label_total = tk.Label(root, text="Total spaces: ---", font=("Arial", 13))
label_total.pack(pady=5)
label_free = tk.Label(root, text="Free spaces: ---", font=("Arial", 13))
label_free.pack(pady=5)
label_air = tk.Label(root, text="Air quality: ---", font=("Arial", 13))
label_air.pack(pady=5)
label_gate = tk.Label(root, text="Gate status: ---", font=("Arial", 13, "bold"))
label_gate.pack(pady=10)