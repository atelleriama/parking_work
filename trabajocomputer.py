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

def update_data():
    """
    Reads incoming serial data from the Arduino, parses parking system values,
    updates the GUI labels, and logs the data into a CSV file.

    Expected data format (comma-separated):
        cars, total_spaces, free_spaces, air_value, gate_status

    The function is called periodically every 500 ms using Tkinter's event loop.
    """
    try:
        if arduino.in_waiting > 0:
            line = arduino.readline().decode(errors="ignore").strip()
            data = line.split(",")

            if len(data) == 5:
                cars, total, free, air, gate = data
                now = datetime.now().strftime("%H:%M:%S")

                label_cars.config(text="Cars inside: " + cars)
                label_total.config(text="Total spaces: " + total)
                label_free.config(text="Free spaces: " + free)
                label_air.config(text="Air quality: " + air)
                label_gate.config(text="Gate status: " + gate)

                writer.writerow([now, cars, total, free, air, gate])
                file.flush()

    except Exception as e:
        label_gate.config(text="Error reading Arduino")

    root.after(500, update_data)

def close_app():
    """
   Safely closes the application by releasing all resources.

   This function:
   - Closes the CSV file to ensure all data is properly saved.
   - Closes the serial connection to the Arduino.
   - Destroys the Tkinter window and stops the GUI loop.

   It is triggered when the user attempts to close the window.
   """
    file.close()
    arduino.close()
    root.destroy()

root.protocol("WM_DELETE_WINDOW", close_app)

update_data()
root.mainloop()
