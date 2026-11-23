import requests

url = "https://api.open-meteo.com/v1/forecast"
params = {"latitude": 41.65, "longitude": -0.88,
          "daily": "temperature_2m_max", "timezone": "Europe/Madrid"}
datos = requests.get(url, params=params).json()

dias = datos["daily"]["time"]                    # lista
maximas = datos["daily"]["temperature_2m_max"]   # lista

for dia, t in zip(dias, maximas):
    print(dia, t)
print("Día más caluroso:", dias[maximas.index(max(maximas))])

for dia in dias:
    print(dia)
    
for m in maximas:
    print(m)
    
print("La temperatura mínima será el día: ", dias[maximas.index(min(maximas))], " con: ", min(maximas), " grados.")