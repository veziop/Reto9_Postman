import json

file = 'all_response.json'

dir_resp = 'respuestas_json\\'


with open(dir_resp + file, encoding='utf-8') as f:
    data = json.load(f)

data = json.dumps(data, indent=4)

with open('ejercicio_ejemplo.txt', 'w', encoding='utf-8') as f:
    f.write('Ejercicio X\n\n')
    f.write(str(data))
