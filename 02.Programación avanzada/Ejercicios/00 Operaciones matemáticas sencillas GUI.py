from tkinter import *
from tkinter import ttk

class mainApp(Tk):
    entrada1 = None
    entrada2 = None
    
    __entradaAnt1 = ""
    __entradaAnt2 = ""
    
    def __init__(self):
        Tk.__init__(self)
        self.title("Matemáticas sencillas")
        self.geometry("200x150")
        self.configure(bg='#ECECEC')
        self.resizable(0,0)
        
        self.entrada1 = int()
        self.entrada2 = int()
        self.suma = self.entrada1 + self.entrada2
        self.resta = (self.entrada1) - (self.entrada2)
        self.multi = (self.entrada1) * (self.entrada2)
        self.divide = (self.entrada1) / (self.entrada2)
   
        
        
        self.createLayout()
    
    def createLayout(self):
        self.entrada1 = ttk.Entry(self, textvariable=self.entrada1).place(x=10, y=10)
        self.entrada2 = ttk.Entry(self, textvariable=self.entrada2).place(x=10, y=40)
        self.suma = ttk.Entry(self, textvariable=self.suma).place(x=10, y=70)
        self.resta = ttk.Entry(self, textvariable=self.resta).place(x=10, y=100)
        self.multi = ttk.Entry(self, textvariable=self.multi).place(x=10, y=130)
        self.divide = ttk.Entry(self, textvariable=self.divide).place(x=10, y=140)
        
        
        
        self.rb1 = ttk.Radiobutton(self, text="Fahrenheit", variable=self.tipoUnidad, value="F", command=self.selected).place(x=20, y=70)
        self.rb2 = ttk.Radiobutton(self, text="Celsius", variable=self.tipoUnidad, value="C", command=self.selected).place(x=20, y=95)
    
    def start(self):
        self.mainloop()
        
  
    def selected(self):
        resultado = 0
        toUnidad = self.tipoUnidad.get()
        grados = float(self.temperatura.get())
        
        if toUnidad == 'F':
            resultado = grados * 9/5 + 32
        elif toUnidad == 'C':
            resultado = (grados - 32) * 5/9
        else:
            resultado = grados
            
        self.temperatura.set(resultado)       
     
     
     
if __name__ == '__main__':
    app = mainApp()
    
    app.start()
