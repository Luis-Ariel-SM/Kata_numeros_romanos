romanos = {'M':1000,
           'D':500,
           'C':100,
           'L':50,
           'X':10,
           'V':5,
           'I':1,
           }

def romano_a_entero(nRomano):

    if nRomano == "":
        return "Error en formato"

    if len(nRomano)>3:
        return "Error en formato"

    entero = 0
    numRepes = 0
    letraAnt = ""
    
    for letra in nRomano:

        if letra == letraAnt and numRepes == 3:
            return "Error en formato"
        elif letra == letraAnt :
            numRepes += 1
        else:
            numRepes = 1   

        if letra in romanos:
            entero += romanos [letra]        
        else:
            return "Error en formato"

        letraAnt = letra

    return entero