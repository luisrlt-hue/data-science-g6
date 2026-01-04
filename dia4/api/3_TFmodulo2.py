import requests
from tabulate import tabulate
import mysql.connector



URL = 'https://restcountries.com/v3.1/region/America'

response = requests.get(URL)
if response.status_code == 200:
    data = response.json()  
    rows = []
    
    for pais in data:  
        nombre = pais['name']['common'] 
        capital = pais.get('capital',['Sin capital'] )
        if capital and isinstance(capital, list):
            capital= capital[0]
        else:
            capital= 'Sin capital'
            
        region= pais.get('region')
        poblacion= pais.get('population',0)
        rows.append([nombre, capital, region, poblacion])
    
    headers = ['Nombre', 'Capital', 'Region', 'Poblacion']
    print(tabulate(rows, headers, tablefmt='grid'))
    
    #cargamos data en  la base de datos
    connection= mysql.connector.connect(
        host='localhost',
        user='root',    
        password='root',
        database='db_g6')
    
    if connection.is_connected():
        cursor= connection.cursor()
        cursor.execute(
        """
            CREATE TABLE IF NOT EXISTS paises(
            id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
            Nombre VARCHAR(255) NOT NULL,
            Capital VARCHAR(255) NOT NULL,
            Region VARCHAR(255),
            Poblacion BIGINT
            );
            """
        )
        #insertamos los datos
        for fila in rows:
            cursor.execute(
                """
                INSERT INTO paises (Nombre, Capital, Region, Poblacion)
                VALUES (%s, %s, %s, %s);
                """,
                fila
            )
            
        connection.commit()
        connection.close()
        print(F'Datos insertados correctamente en la base de datos.')
    else:
        print('Error al conectar a la base de datos.')
        
        
else:
    print(f'Error en la solicitud: {response.status_code}')

    
    

