# Project 12 - Decision Matrix GUI

# Import libraries
import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt

class DecisionMatrix:
    def __init__(self, root):
        self.root = root

        # Creating the GUI
        self.root.title('Project 12 - Decision Matrix Generator')
        self.root.geometry('1350x600')
        self.root.configure(bg='#FAF3CD')

        # Title and logo
    
        self.title = tk.Label(root, text='Decision Matrix', font=('Century Gothic', 25), bg='#FAF3CD', width=50)
        self.title.grid(row=0, column=1)

        self.logo = tk.PhotoImage(file='logo.png')
        logo_show = tk.Label(root, image=self.logo)
        logo_show.grid(row=0, column=0)

        # Criteria and alternatives
        self.criteria = ['Structural Performance', 'Cost', 'Constructability', 'Sustainability', 'Safety Compliance', 'Aesthetics']
        self.alternatives = ['Alternative 1', 'Alternative 2']

        # Creating a frame for the table
        self.table_frame = tk.Frame(root, bg='#FAF3CD', bd=5, relief = 'raised')
        self.table_frame.grid(row=1, column=1, columnspan=2, pady=30, padx=30)

        # Storage for scores and weights
        self.score_entries = {}
        self.weight_entries = {}

        # Creating the table headers
        table_headers = tk.Label(self.table_frame, text = 'Alternatives', bg='#FAF3CD', font=('Century Gothic',12, 'bold'))
        table_headers.grid(row=2, column=0)

        for j, c in enumerate(self.criteria):
            criterion_name = tk.Label(self.table_frame, text=c, font=('Century Gothic', 10), bg='#FAF3CD')
            criterion_name.grid(row=0,column=j+1, padx=5, pady=5)

            e = tk.Entry(self.table_frame, width=5)
            e.grid(row=1, column=j+1, padx=5, pady=2)
            e.insert(0, '1')
            self.weight_entries[c] = e

            weight_label = tk.Label(self.table_frame, text='Weight', font=('Century Gothic', 8),bg='#FAF3CD')
            weight_label.grid(row=2, column=j+1, padx=5, pady=2)

        # Alternatives and score entries
        for i, alt in enumerate(self.alternatives):
            score_label = tk.Label(self.table_frame, text=alt, font=('Century Gothic', 10),bg='#FAF3CD')
            score_label.grid(row=i+3, column=0, padx=5, pady=5)
            for j, c in enumerate(self.criteria):
                t = tk.Entry(self.table_frame, width=5)
                t.grid(row=i+3, column=j+1, padx=5, pady=5)
                t.insert(0, '0')
                self.score_entries[(alt, c)] = t

        # Calculate button
        calc_button = tk.Button(root, text='Calculate & Plot', bg='#FAF3CD',font=('Century Gothic', 10), command=self.calc_plot)
        calc_button.grid(row=7, column=1)

        # Result label
        self.result_label = tk.Label(root, text='', font=('Century Gothic', 10, 'bold'), bg='#FAF3CD')
        #elf.result_label.pack(pady=10)

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
        self.result_label.config(text=f"The best decision is: {best_alt} (Weighted Score: {total_scores[best_alt]:.2f})")
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