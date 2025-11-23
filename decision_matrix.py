# Project 12 - Decision Matrix GUI

# Import libraries
import tkinter as tk
from tkinter import messagebox
import matplotlib
import matplotlib.pyplot as plt

from PIL import Image, ImageTk

class DecisionMatrix:
    def __init__(self, root):
        self.root = root

        # Creating the GUI
        self.root.title('Project 12 - Decision Matrix Generator')
        #self.root.state('zoomed')
        self.root.geometry('900x750')
        self.root.configure(bg='#C0C5A7')

        # Title and logo
        logo = Image.open('title.png')
        logo = logo.resize((400,100))

        logo = ImageTk.PhotoImage(logo)
        logo_show = tk.Label(root, image=logo, bg='#C0C5A7')
        logo_show.image = logo
        logo_show.grid(row=0, column=0)

        # Criteria description
        desc = Image.open('criteria.png')
        desc = desc.resize((800,400))

        desc = ImageTk.PhotoImage(desc)
        desc_show = tk.Label(root, image=desc, bg='#C0C5A7')
        desc_show.image = desc
        desc_show.grid(row=3, column=0, padx=2, pady=2)
    

        # Criteria and alternatives
        self.criteria = ['Cost & Material Efficiency', 'Building Envelope Efficiency', 'Structural Efficiency', 'Constructability', 'Functionality/Flexibility', 'Aesthetics']
        self.alternatives = ['Alternative 1', 'Alternative 2']

        # Creating a frame for the table
        self.table_frame = tk.Frame(root, bg='#C0C5A7', bd=5, relief = 'raised')
        self.table_frame.grid(row=1, column=0, pady=10, padx=10)

        # Storage for scores and weights
        self.score_entries = {}
        self.weight_entries = {}

        # Creating the table headers
        table_headers = tk.Label(self.table_frame, text = 'Alternatives', bg='#C0C5A7',fg='#56623E', font=('Century Gothic',12, 'bold'))
        table_headers.grid(row=2, column=0)

        for j, c in enumerate(self.criteria):
            criterion_name = tk.Label(self.table_frame, text=c, font=('Century Gothic', 10, 'bold'), bg='#C0C5A7', fg='#56623E')
            criterion_name.grid(row=0,column=j+1, padx=5, pady=5)

            e = tk.Entry(self.table_frame, width=5)
            e.grid(row=1, column=j+1, padx=5, pady=5)
            e.insert(0, '1')
            self.weight_entries[c] = e
#
            weight_label = tk.Label(self.table_frame, text='Weight', font=('Century Gothic', 8, 'italic'),bg='#C0C5A7', fg='#56623E')
            weight_label.grid(row=2, column=j+1, padx=5, pady=5)

        # Alternatives and score entries
        for i, alt in enumerate(self.alternatives):
            score_label = tk.Label(self.table_frame, text=alt, font=('Century Gothic', 10, 'bold'),bg='#C0C5A7', fg='#56623E')
            score_label.grid(row=i+3, column=0, padx=5, pady=5)
            for j, c in enumerate(self.criteria):
                t = tk.Entry(self.table_frame, width=5)
                t.grid(row=i+3, column=j+1, padx=5, pady=5)
                t.insert(0, '0')
                self.score_entries[(alt, c)] = t

        # Calculate button
        calc_button = tk.Button(root, text='Calculate & Plot', bg='#56623E',font=('Century Gothic', 10), command=self.calc_plot, fg='white')
        calc_button.grid(row=2, column=0, pady=5)

        # Result label
        self.result_label = tk.Label(root, text='', font=('Century Gothic', 10, 'bold'), bg='#C0C5A7')
      

    def calc_plot(self):

        # Get weights
        try:
            weights = {c: float(e.get()) for c, e in self.weight_entries.items()}
        except ValueError:
            messagebox.showerror('Error', 'Ensure weights are numeric')
            return
        
        # Calculating weighted scores
        total_scores = {}
        for alt in self.alternatives:
            score = 0
            for c in self.criteria:
                try:
                    s = float(self.score_entries[(alt, c)].get())
                    score += s * weights[c]
                except ValueError:
                    messagebox.showerror('Error', 'All scores must be numeric')
                    return
                
            total_scores[alt] = score

        # Show best choice
        best_alt = max(total_scores.items(), key=lambda x:x[1])[0]
        self.result_label.config(text=f"\nThe best decision is: {best_alt} (Weighted Score: {total_scores[best_alt]:.2f})")
        self.result_label.grid(row=11, column=1)

        # Plot graph
        plt.figure(figsize=(10, 5))
        plt.bar(total_scores.keys(), total_scores.values(), color=['#a1a7cc', '#8c0000'])
        plt.ylabel('Weighted Score')
        plt.title('Decision Matrix Results')
        plt.ylim(0, max(total_scores.values())*1.2)

        for i , (alt, score) in enumerate(total_scores.items()):
            plt.text(i, score + 0.05*max(total_scores.values()), f"{score:.2f}", ha='center')
        plt.show()
                                



if __name__ == '__main__':
    root = tk.Tk()
    app = DecisionMatrix(root)
    root.mainloop()
