from tkinter import *

class graphic_interface:
    
    def __init__(self):
        
        self.root = Tk()
        
        self.frm_information = Frame(self.root, pady=10, padx=10)
        self.frm_information.pack()
        
        self.lbl_first_number = Label(self.frm_information, text="Enter first number: ")
        self.lbl_first_number.grid(row=0, column=0)
        self.lbl_first_number.config(font=('Verdana', 10))
        
        self.var_first_number = StringVar()
        self.ent_first_number = Entry(self.frm_information, textvariable = self.var_first_number)
        self.ent_first_number.grid(row=1, column=0)
        self.ent_first_number.config(font=('Verdana', 12), justify='center')
        
        self.lbl_second_number = Label(self.frm_information, text="Enter second number: ")
        self.lbl_second_number.grid(row=2, column=0)
        self.lbl_second_number.config(font=('Verdana', 10))
        
        self.var_second_number = StringVar()
        self.ent_second_number = Entry(self.frm_information, textvariable = self.var_second_number)
        self.ent_second_number.grid(row=3, column=0, pady=(0,10))
        self.ent_second_number.config(font=('Verdana', 12), justify='center')
        
        self.var_result_number = StringVar()
        self.ent_result = Entry(self.frm_information, textvariable = self.var_result_number)
        self.ent_result.grid(row=6, column=0)
        self.ent_result.config(font=('Verdana', 14), justify='center')
        
        self.btn_to_add = Button(self.frm_information, text='Addition', command = lambda:self.sumarNumeros())
        self.btn_to_add.grid(row=4, column=0)
        self.btn_to_add.config(font=('Verdana', 12))
        
        self.lbl_result = Label(self.frm_information, text='The result is: ')
        self.lbl_result.grid(row=5, column=0, pady=(10,5))
        self.lbl_result.config(font=('Verdana', 10))
                
        
        self.root.mainloop()
  
  
        
    def sumarNumeros(self):
        numero1 = self.var_first_number.get()
        numero2 = self.var_second_number.get()
        self.var_first_number.set('')
        self.var_second_number.set('')
        
        try:    
            num1 = float(numero1)
            num2 = float(numero2)   
            resultadoSuma = num1 + num2 
            
            self.var_result_number.set(resultadoSuma)
            self.lbl_result['text'] = "Addition. The result is: "
            return resultadoSuma
        
        except ValueError as err:
            self.lbl_result['text'] = "Addition is no possible "
            self.var_result_number.set('')
            raise 
        
        
        




    
        
  
