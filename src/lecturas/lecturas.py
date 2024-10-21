'''
@author: Galocha
'''

from typing import Optional




def ejercicio6(fichero:str, sep:str, cad:str) -> int: 
    res:int = 0
    try:
        with open(fichero, mode = 'r', encoding='utf-8') as f:
            contenido = f.read()
            res = contenido.split(sep).count(cad)
        return res
    except IOError as e:
        print(f'Error al intentar leer el archivo {e}')
        return res


def ejercicio7(fichero:str, cad:str) -> list[str]:
    ls = []
    try:
        with open(fichero, mode='r', encoding='utf-8') as f:
            for linea in f:
                if cad in linea:
                    ls.append(linea.strip())
            return ls
    except IOError as e:
        print(f'Error al intentar abrir el archivo {e}')
        return ls
    
def ejercicio8(fichero:str) -> list[str]:
    palabras_unicas = set()
    ls:list[str] = []
    try:
        with open(fichero, mode='r', encoding='utf-8') as f:
            for linea in f:
                palabras:list[str] = linea.split()
                for palabra in palabras:
                    palabras_unicas.add(palabra)
        return list(palabras_unicas)
    except IOError as e:
        print(f'Error al intentar leer el archivo {e}')
        return ls
    
def longitud_promedio_lineas(file_path: str) -> Optional[float]:
    try:
        with open(file_path, mode='r', encoding='utf-8') as f:
            lineas = f.readlines()
            if not lineas:
                return None
            longitudes:list[int] = [len(linea.strip().split(' ')) for linea in lineas]
            longitud_media:float = sum(longitudes) / len(longitudes)
            return longitud_media
    except IOError as e:
        print(f'Error al intentar abrir el archivo {e}')
        return None 
    
    
    