import json
import os

RUTA_RECURSOS = "data/recursos.json"
RUTA_COMBATES = "data/combates.json"

def guardar_combates(combates):           
    data = {
        "combates": combates
    }
    with open(RUTA_COMBATES, "w") as f:
        json.dump(data, f, indent=4)

def cargar_combates():             
    if not os.path.exists(RUTA_COMBATES):
        return
    try:
        with open(RUTA_COMBATES, "r") as f:
            combates = json.load(f)   
            combates = combates.get("combates")
            return combates
    except Exception as e:
        print(f'Error al cargar datos: {e}')
        
def cargar_recursos():       
    if not os.path.exists(RUTA_RECURSOS):
        return
    try:
        with open(RUTA_RECURSOS, "r") as f:
            data = json.load(f)
            return data
    except Exception as e:
        print(f'Error al cargar datos: {e}')