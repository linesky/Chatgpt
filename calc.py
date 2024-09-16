
import tkinter as tk
from tkinter import messagebox

def calculate(operation):
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        
        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            if num2 == 0:
                raise ValueError("Divisão por zero")
            result = num1 / num2
        
        entry_result.delete(0, tk.END)
        entry_result.insert(0, str(result))
    except ValueError as e:
        messagebox.showerror("Erro", str(e))

# Criando a janela principal
root = tk.Tk()
root.title("Calculadora Simples")
root.configure(bg='black')
# Criando e posicionando as caixas de texto
label1 = tk.Label(root, bg='black', fg='white',text="n:")
label1.grid(row=0, column=0, padx=10, pady=10)
entry1 = tk.Entry(root,bg='black', fg='white')
entry1.grid(row=0, column=1, padx=10, pady=10)

label2 = tk.Label(root,bg='black', fg='white', text="n:")
label2.grid(row=1, column=0, padx=10, pady=10)
entry2 = tk.Entry(root,bg='black', fg='white')
entry2.grid(row=1, column=1, padx=10, pady=10)

label_result = tk.Label(root, bg='black', fg='white', text="nn:")
label_result.grid(row=2, column=0, padx=10, pady=10)
entry_result = tk.Entry(root,bg='black', fg='white')
entry_result.grid(row=2,column=1, padx=10, pady=10)

# Funções de cálculo para cada operação
button_add = tk.Button(root, text="+", bg='black', fg='white', command=lambda: calculate('+'))
button_add.grid(row=3, column=0, padx=5, pady=5)

button_subtract = tk.Button(root, text="-", bg='black', fg='white', command=lambda: calculate('-'))
button_subtract.grid(row=3, column=1, padx=5, pady=5)

button_multiply = tk.Button(root, text="*", bg='black', fg='white', command=lambda: calculate('*'))
button_multiply.grid(row=3, column=2, padx=5, pady=5)

button_divide = tk.Button(root, text="/", bg='black', fg='white', command=lambda: calculate('/'))
button_divide.grid(row=3, column=3, padx=5, pady=5)

# Rodando a janela principal
root.mainloop()
