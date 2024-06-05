import sqlite3

def create_datebase():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS companies (
        CNPJ_CIA TEXT,
        DENOM_SOCIAL TEXT,
        SIT TEXT,
        DT_INI_SIT DATE               
)    
''')
    
    conn.commit()
    conn.close()
    
if __name__ == '__main__':
    create_datebase()