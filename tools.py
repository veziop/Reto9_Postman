import json

class ProcesarEjercicio:
    dir_respuestas = 'respuestas\\'

    def __init__(self, titulo):
        self.titulo = titulo

    def set_endpoint(self, endpoint):
        self.endpoint = endpoint

    def set_respuesta(self, respuesta):
        self.respuesta = self.dir_respuestas + respuesta

    def eliminar_espacios(self):
        return self.titulo.replace(' ', '_')

    def guardar_txt(self):
        with open(self.respuesta, encoding='utf-8') as f:
            data = json.load(f)

        data = json.dumps(data, indent=4)

        with open(f'ejercicio_{self.eliminar_espacios()}.txt', 'w') as f:
            f.write(f'Ejercio "{self.titulo}"\n\n')
            f.write(f'Endpoint: {self.endpoint}\n\n')
            f.write(data)
