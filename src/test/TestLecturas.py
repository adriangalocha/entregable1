'''
@author: Galocha
'''




from lecturas.lecturas import ejercicio6, ejercicio7, ejercicio8, longitud_promedio_lineas




if __name__ == '__main__':
  
    
    ubicacion:str = 'C/Users/Galocha/git/proyecto-laboratorio-python-adriangalocha/src/ficheros1'
    fichero:str = '/lin_quijote.txt'
    cad:str = 'Quijote'
    print(ejercicio6(ubicacion+fichero, cad))
    print(ejercicio7(ubicacion+fichero, cad))
    print(ejercicio8(ubicacion+fichero))
    
    ubicacion:str = 'C/Users/Galocha/git/proyecto-laboratorio-python-adriangalocha/src/ficheros1'
    fichero:str = '/palabras_ramdon.csv'
    print(longitud_promedio_lineas(ubicacion+fichero))
    
    
    
    