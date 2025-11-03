# Project 12 - Decision Matrix GUI

# Import libraries
import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt

class DecisionMatrix:
    def __init__(self, root):
        self.root = root

        # Creating the GUI
        self.root.title('Decision Matrix Generator')
        self.root.geometry('1350x600')
        self.root.configure(bg='#FAF3CD')

        # Title and logo
        self.logo = tk.PhotoImage(file='logo.png')
        logo_show = tk.Label(root, image=self.logo)



if __name__ == '__main__':
    root = tk.Tk()
    app = DecisionMatrix(root)
    root.mainloop()