def doble (n):
    return n * 2



class Persona ():

    def __init__ (self, nombre, edad): # self solo existe en el ambito de esta funcion. Nombre y edad son como parametros de entradas. Cada self es local y unico de su funcion.
        self.nombre = nombre # Esto es un atributo de esta funcion u objeto. Los atributos de la clase siempre se crean en el 1ero metodo de la clase
        self.edad = edad
       

    def __repr__(yomismo): # Ejemplo de como funciona el self, aqui siempre se refieren a la instancia pero el hueco es local
        return 'Me llamo {} y tengo {} años'. format(yomismo.nombre, yomismo.edad)
     
    

luis = Persona ('Luis', 19) # luis es una instancia de la clase Persona, es como una copia con otros valores en los atributos (name: luis - edad: 19)
# en esta instancia ya python informa internamente el atributo self, por eso no se utiliza fuera del ambito de Persona.
print (doble(luis.edad)) # Aqui se invoca a la funcion "doble" y como parametro se le mete la instancia con el atributo de la edad

# resultado = 38
