import requests

#define atributos
payload = {"name" : "Aang","allies":"Gyatso"}

#Comando GET
r = requests.get('https://last-airbender-api.fly.dev/api/v1/characters',payload)

#Imprimir texto
print(r.text)

print(r.url)