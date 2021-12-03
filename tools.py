import json

class ProcesarEjercicio:
    dir_respuestas = 'respuestas_json\\'
    dir_entregables = 'entregables\\'

    def __init__(self, titulo):
        self.titulo = titulo
        self.nombre_archivo = self.procesar_nombre_archivo()

    def set_version(self, version):
        self.version = version

    def set_endpoint(self, endpoint):
        self.endpoint = endpoint

    def set_complete_URL(self):
        if self.version == 2:
            URL = 'https://restcountries.com/v2'
        else:
            URL = 'https://restcountries.com/v3.1'

        self.complete_URL = URL + self.endpoint

    def set_respuesta(self, respuesta):
        self.respuesta = self.dir_respuestas + respuesta

    def eliminar_espacios(self):
        return self.titulo.replace(' ', '_')

    def procesar_nombre_archivo(self):
        return f'{self.dir_entregables}ejercicio_{self.eliminar_espacios()}.txt'

    def guardar_txt(self):
        with open(self.respuesta, encoding='utf-8') as f:
            data = json.load(f)

        data = json.dumps(data, indent=4)

        with open(self.nombre_archivo, 'w') as f:
            f.write(f'Ejercicio "{self.titulo}"\n\n')
            f.write(f'Endpoint: {self.endpoint}\nURL completo: {self.complete_URL}\n\n')
            f.write(f'Respuesta en JSON:\n{data}')
