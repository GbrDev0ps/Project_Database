import sqlite3
from datetime import datetime
import csv

def insert_data(csv_file):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    
    with open(csv_file, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=';')
        data = []
        
        next(reader)
        
        for line in reader:
            
            col1, col2, col3, col4 = line[0], line[1], line[7], line[8]
            
            col4 = datetime.strptime(col4, '%d/%m/%Y').date()
            
            data.append((col1, col2, col3, col4))
            
        cursor.executemany("INSERT INTO companies (CNPJ_CIA, DENOM_SOCIAL, SIT, DT_INI_SIT) VALUES (?, ?, ?, ?)", data)
    
    conn.commit()
    conn.close()

if __name__ == '__main__':
    # Nome do arquivo CSV a ser importado
    csv_file = 'database/database-companies.csv'
    insert_data(csv_file)
    print(f"Dados do arquivo {csv_file} inseridos com sucesso.")