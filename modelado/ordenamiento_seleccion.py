class OrdenamientoSeleccion(object):
    """docstring for OrdenamiendoSeleccion"""
    
    # metodo que ordena el arreglo usando el ordenamiento por selección
    def Ordenar(self, mas_pequenio):
        # for que itera a traves de datos.len - 1 elementos
        for x in range(0, len(mas_pequenio)-1):
            #primer indice del resto del arreglo
            mas_peque = x 
            #for que itera para buscar el indice del elemento mas pequeño
            for l in range(x + 1, len(mas_pequenio)):
                #if para hacer la comparacion 
                if mas_pequenio[l] < mas_pequenio[mas_peque]:
                    #mas peque es igual al indice l
                    mas_peque = l
            #if intercambia el elemento mas pequeño en la posicion
            if mas_peque != x:
                # Temporal toma el valor de mas pequenio
                temporal = mas_pequenio[x]
                #mas pequenio toma el valor de mas pequinio en la posicion mas peque
                mas_pequenio[x] = mas_pequenio[mas_peque]
                #mas pequenio en la posicion mas peque es igual a temporal
                mas_pequenio[mas_peque] = temporal
        #retornamos mas peqenio
        return mas_pequenio
    # metodo ayudante para intercambiar los valores de dos elementos
    def Insercion(self, mas_pequenio):
        #for que itera a traves del arreglo
        for x in range(1, len(mas_pequenio)):
            #almacena primero en auxiliar 
            aux = mas_pequenio[x]
            #sustituye posi por aux
            posi = x
            #While para la condicion 
            while posi > 0 and mas_pequenio[posi - 1] > aux:
                mas_pequenio[pos] = mas_pequenio[posi - 1]
                posi = posi -1
            mas_pequenio[posi] = aux
        # retornamos mas pequenio
        return mas_pequenio