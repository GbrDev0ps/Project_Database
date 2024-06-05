import tkinter as tk
import sqlite3
from tkinter import messagebox
from tkinter import ttk
from datetime import datetime


def query_data(start_date=None, end_date=None):
    conn = sqlite3.connect('database.db', detect_types=sqlite3.PARSE_DECLTYPES)
    cursor = conn.cursor()
    
    if start_date:
        try:
            start_date = datetime.strptime(start_date, '%d/%m/%Y').date()
        except ValueError as e:
            raise ValueError(f"Formato de data inicial inválido: {e}")
    
    if end_date:
        try:
            end_date = datetime.strptime(end_date, '%d/%m/%Y').date()
        except ValueError as e:
            raise ValueError(f"Formato de data final inválido: {e}")
    
    if start_date and end_date:
        if start_date == end_date:
            cursor.execute('''
            SELECT CNPJ_CIA, DENOM_SOCIAL, SIT FROM companies
            WHERE DT_INI_SIT = ?
            ORDER BY DT_INI_SIT DESC
            ''', (start_date,))
        else:
            cursor.execute('''
            SELECT CNPJ_CIA, DENOM_SOCIAL, SIT FROM companies
            WHERE DT_INI_SIT BETWEEN ? AND ?
            ORDER BY DT_INI_SIT DESC
            ''', (start_date, end_date))
    elif start_date:
        cursor.execute('''
        SELECT CNPJ_CIA, DENOM_SOCIAL, SIT FROM companies
        WHERE DT_INI_SIT >= ?
        ORDER BY DT_INI_SIT DESC
        ''', (start_date,))
    elif end_date:
            cursor.execute('''
            SELECT CNPJ_CIA, DENOM_SOCIAL, SIT FROM companies
            WHERE DT_INI_SIT <= ?
            ORDER BY DT_INI_SIT DESC
            ''', (end_date,))

            
            
            
    result = cursor.fetchall()
    conn.close()
    
    return result

def display_results(result):
    result_window = tk.Toplevel(root)
    result_window.title("Resultados da Consulta")
    
    tree = ttk.Treeview(result_window, columns=('CNPJ_CIA', 'DENOM_SOCIAL', 'SIT'), show='headings')
    tree.heading('CNPJ_CIA', text='CNPJ')
    tree.heading('DENOM_SOCIAL', text='Nome')
    tree.heading('SIT', text='Situação')
    
    for row in result:
        tree.insert('', tk.END, values=row)
    
    tree.pack(expand=True, fill='both')
    
    scrollbar = ttk.Scrollbar(result_window, orient=tk.VERTICAL, command=tree.yview)
    tree.configure(yscroll=scrollbar.set)
    scrollbar.pack(side='right', fill='y')

def on_query():
    start_date = entry_start_date.get()
    end_date = entry_end_date.get()
    
    try:
        result = query_data(start_date, end_date)
        if result:
            display_results(result)
        else:
            messagebox.showinfo("Resultados da Consulta", "Nenhum resultado encontrado.")
    except ValueError as e:
        messagebox.showerror("Erro", f"Formato de data inválido: {e}")
    except sqlite3.Error as e:
        messagebox.showerror("Erro", f"Erro no banco de daods: {e}")
        
root = tk.Tk()
root.title("Consulta de Companhias Abertas")

root.minsize(500, 300)

frame = tk.Frame(root, padx=20, pady=20)
frame.grid(row=0, column=0, padx=10, pady=10)

tk.Label(frame, text="Data Inicial (dd/mm/yyyy):", font=('Arial', 14)).grid(row=0, column=0, padx=10, pady=10, sticky='e')
entry_start_date = tk.Entry(frame, font=('Arial', 14))
entry_start_date.grid(row=0, column=1, padx=10, pady=10)

tk.Label(frame, text="Data Final (dd/mm/yyyy):", font=('Arial', 14)).grid(row=1, column=0, padx=10, pady=10, sticky='e')
entry_end_date = tk.Entry(frame, font=('Arial', 14))
entry_end_date.grid(row=1, column=1, padx=10, pady=10)

tk.Button(frame, text="Consultar", command=on_query, font=('Arial', 14)).grid(row=2, column=0, columnspan=2, pady=20)

root.mainloop()