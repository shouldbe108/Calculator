# -*- coding: utf-8 -*-
"""
Created on Sun Aug 14 18:26:25 2022

@author: atpax
"""

import tkinter as tk
LARGE_FONT_STYLE = ("arial", 40, "bold")
SMALL_FONT_STYLE = ("Arial", 16 )
LIGHT_GRAY = "#F5F5F5"
LABEL_COLOR = "#25265E"
WHITE = "#FFFFFF"

class Calculator:
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry("375x667")
        self.window.resizable(0,0)
        self.window.title("calculator")
        
        self.total_expression = "0"
        self.current_expression = "0"
        
    #two frams for buttons and display
        self.display_frame = self.create_display_frame()
        
        
        self.total_label=self.create_display_labels()
        self.label= self.create_display_labels()
        
        self.digits ={
            7: (1,1), 8: (1,2), 9: (1,3),
            4: (2,1), 5: (2,2), 6: (2,3),
            1: (3,1), 2: (3,2), 3: (3,3),
            0: (4,2), '.': (4,1)   
            
            
        }
        
        
        self.buttons_frame = self.create_buttons_frame()
        self.create_digit_buttons()
        
    def create_display_labels(self):
        total_label=tk.Label(self.display_frame, text=self.total_expression, anchor=tk.E, bg=LIGHT_GRAY, fg=LABEL_COLOR, padx=24, font=SMALL_FONT_STYLE) #anchor positions text to the East
        total_label.pack(expand=True, fill='both')
        return total_label
    
    def create_display_labels(self):
        label=tk.Label(self.display_frame, text=self.current_expression, anchor=tk.E, bg=LIGHT_GRAY, fg=LABEL_COLOR, padx=24, font=LARGE_FONT_STYLE) #anchor positions text to the East
        label.pack(expand=True, fill='both') 
        return label
        
    def create_display_frame(self):
        frame = tk.Frame(self.window, height=221, bg=LIGHT_GRAY)
        frame.pack(expand=True, fill="both")
        return frame
    
    def create_digit_buttons(self):
        for digit, grid_value in self.digits.items():
            button = tk.Button(self.buttons_frame, text=str(digit), bg=WHITE, fg=LABEL_COLOR)
            button.grid(row=grid_value[0], column=grid_value[1],sticky=tk.NSEW)
    def create_buttons_frame(self):
        frame = tk.Frame(self.window)
        frame.pack(expand=True, fill="both")
        return frame
    
    
    def run(self):
        self.window.mainloop()
    
if __name__ == "__main__":
    calc = Calculator()
    calc.run() #these lines of code only run when program is run from the terminal.
    