from tools import ProcesarEjercicio


#crear un objecto ejercicio desde su titulo
def crear_objeto():
    ejercicio = ProcesarEjercicio(str(input('introducta un titulo: ')))

    #indicar la version de la API
    ejercicio.set_version(int(input('introduzca la version de la API (2 o 3): ')))

    #indicar el endpoint
    ejercicio.set_endpoint(str(input("introduzca el endpoint: ")))
    ejercicio.set_complete_URL()

    #indicar el archivo json de respuesta
    ejercicio.set_respuesta(str(input("introduzca el nombre del archivo de respuesta: ")))

    return ejercicio


#procesar informacion y crear el archivo txt entregable
def crear_archivo(ejercicio):
    assert isinstance(ejercicio, ProcesarEjercicio)

    ejercicio.guardar_txt()






if __name__ == '__main__':
    crear_archivo(crear_objeto())
