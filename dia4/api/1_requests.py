import requests
from tabulate import tabulate

URL='https://randomuser.me/api/?results=5'

response = requests.get(URL)
print(response.status_code)

if response.status_code == 200:
    print('conexion a api exitosa')
    data=response.json()
    rows=[]
    
    for dict_user in data['results']:
        nombre=dict_user['name']['first'] + ' ' + dict_user['name']['last'] 
        pais=dict_user['location']['country']
        email=dict_user['email']
        telefono=dict_user['phone']
        foto=dict_user['picture']['large']
        rows.append([nombre, pais, email, telefono, foto])
        
    headers=['Nombre', 'Pais', 'Email', 'Telefono', 'Foto']
    print(tabulate(rows,headers,tablefmt='grid'))
    
    
        
else:
    print(f'error {response.status_code}')
    
    
    


