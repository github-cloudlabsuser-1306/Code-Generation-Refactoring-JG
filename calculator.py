# Create a basic calculator
# that can perform addition, subtraction,
# multiplication, and division
# as well as take input and display results
# Import the necessary libraries
import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog
from tkinter import ttk
import math
import re
import os
import sys
import logging
import time
import random
import datetime
import json
import requests
import urllib.parse
import urllib.request
import urllib.error
import xml.etree.ElementTree as ET
import csv
import sqlite3

# Set up logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
# Set up the main window

class Calculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Calculator")
        self.geometry("400x600")
        self.resizable(False, False)
        self.create_widgets()

    def create_widgets(self):
        # Create the display
        self.display = tk.Entry(self, width=16, font=('Arial', 24), bd=10, insertwidth=2, justify='right')
        self.display.grid(row=0, column=0, columnspan=4)

        # Create the buttons
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+'
        ]

        row_val = 1
        col_val = 0
        for button in buttons:
            action = lambda x=button: self.click(x)
            tk.Button(self, text=button, padx=20, pady=20, font=('Arial', 18), command=action).grid(row=row_val, column=col_val)
            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1

        # Create the clear button
        tk.Button(self, text='C', padx=20, pady=20, font=('Arial', 18), command=self.clear).grid(row=row_val, column=0)

    def click(self, button):
        # Handle button clicks
        if button == '=':
            try:
                result = str(eval(self.display.get()))
                self.display.delete(0, tk.END)
                self.display.insert(0, result)
            except Exception as e:
                messagebox.showerror("Error", "Invalid input")
                logging.error("Error evaluating expression: %s", e)
        elif button == 'C':
            self.clear()
        else:
            self.display.insert(tk.END, button)

    def clear(self):
        # Clear the display
        self.display.delete(0, tk.END)

if __name__ == "__main__":
    calculator = Calculator()
    calculator.mainloop()