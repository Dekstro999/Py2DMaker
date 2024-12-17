import random

def Entre(n1,n2):
    n1=n1*1000
    n2=n2*1000
    
    return random.randint(n1, n2)

def clean_widgets(self):
    for widget in self.winfo_children():
        widget.destroy()