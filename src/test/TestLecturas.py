'''
@author: Galocha
'''




from lecturas.lecturas import ejercicio6, ejercicio7, ejercicio8, longitud_promedio_lineas




if __name__ == '__main__':
 

    print(f'El número de veces que aparece la palabra Quijote es:')
    print(ejercicio6('../resources/lin_quijote.txt', ' ', 'Quijote'))
    print()
  
    print(f'Las líneas que tienes la palabra Quijote son:')
    print(ejercicio7('../resources/lin_quijote.txt', 'Quijote'))
    print()
    
    print(ejercicio8('../resources/lin_quijote.txt'))
    print()
    
    print(longitud_promedio_lineas('../resources/lin_quijote.txt'))
  

    
    