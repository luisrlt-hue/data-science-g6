import requests

API_URL = 'https://apiperu.dev/api/ruc'
TOKEN = '22af9c82fc51e180cf597cc2b49e620197950f57a161216e3a2ff72ac91fa612'

data_request = {
  "ruc":"20117592899"
}

headers = {
    "Authorization": f"Bearer {TOKEN}",
    "Content-Type": "application/json"
}

response = requests.post(API_URL, json=data_request, headers=headers)

if response.status_code == 200:
    data=response.json()['data']
    print("="*50)
    print(f'RUC : {data['ruc']}')
    print(f'Razon Social : {data["nombre_o_razon_social"]}')
    print(f'Dirección : {data["direccion"]}')
    print(f'Distrito : {data["distrito"]}')
    print(f'Provincia : {data["provincia"]}')
    print(f'Departamento : {data["departamento"]}')
    print(f'ubigeo : {data["ubigeo_sunat"]}')
    
    