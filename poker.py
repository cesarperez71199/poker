import random

#Inicia la clase 
class Baraja:
    
#Constructor que especifica los val0res del mazo con "valores" y "palos" del mismo
    def __init__(self):
        self.mazo = []
        self.palos = ["Corazones", "Diamantes", "Picas", "Tréboles"]
        self.valores = ["As", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        self.crear_mazo()
        

#Metodo que crea un mazo barajeado con "valores" y "palos"
    def crear_mazo(self):
        self.mazo = [(valor, palo) for valor in self.valores for palo in self.palos]
        
        random.shuffle(self.mazo)    #Barajea los valores de la lista 


#Metodo que comprueba si hay las cartas suficientes y va eliminando del mazo (pop())
#la utlima carta hasta quedar con 5 guardandolas en "mano"
    def repartir_mano(self, num_cartas):
        if num_cartas > len(self.mazo):
            print("No hay suficientes cartas en el mazo.")
            return []
        
        mano = [self.mazo.pop() for _ in range(num_cartas)]
        return mano
    

#Metodo que definira las manos de los jugadores
    def evaluar_mano(self, mano):
        valores = [carta[0] for carta in mano] #se guardaran los "valores" que haya en
                                                #carta recorriendo los espacios de mano(5) 
                                                
       
        palos = [carta[1] for carta in mano]    #se guardaran los "palos" que haya en
                                                #carta recorriendo los espacios de mano(5) 


#Parte que definira los juegos que corresponden a cada mano
        if self.es_escalera_real(valores, palos):
            return "Escalera Real"
        elif self.es_escalera_color(valores, palos):
            return "Escalera de Color"
        elif self.es_poker(valores):
            return "Poker"
        elif self.es_full(valores):
            return "Full"
        elif self.es_color(palos):
            return "Color"
        elif self.es_escalera(valores):
            return "Escalera"
        elif self.es_trio(valores):
            return "Trio"
        elif self.es_doble_pareja(valores):
            return "Doble Pareja"
        elif self.es_pareja(valores):
            return "Pareja"
        else:
            return "Carta Alta"
        
#Metodos que definiran el comportamiento de los juegos de manos 

#Metodo que comprueba si la mano es escalera real
    def es_escalera_real(self, valores, palos):
        return set(valores) == set(["10", "J", "Q", "K", "As"]) and len(set(palos)) == 1
    

#Metodo que comprueba si es escalera color
    def es_escalera_color(self, valores, palos):
        return self.es_escalera(valores) and len(set(palos)) == 1


#Metodo que comprueba si es poker
    def es_poker(self, valores):
        for valor in set(valores):
            if valores.count(valor) == 4:
                return True
        return False
    

#Metodo que comprueba si es full
    def es_full(self, valores):
        return set(valores) == 3 and len(set(valores)) == 3
    
    
#Metodo que comprueba si es color
    def es_color(self, palos):
        return len(set(palos)) == 1


#Metodo que comprueba si es escalera
    def es_escalera(self, valores):
        valores_ordenados = sorted(valores, key=lambda x: self.valores.index(x))
        for i in range(len(valores_ordenados) - 1):
            if self.valores.index(valores_ordenados[i]) + 1 != self.valores.index(valores_ordenados[i + 1]):
                return False
        return True
    
    

#Metodo que comprueba si es trio 
    def es_trio(self, valores):
        for valor in set(valores):
            if valores.count(valor) == 3:
                return True
        return False


#Metodo que comprueba si son dobles pares
    def es_doble_pareja(self, valores):
        return len(set(valores)) == 3 and len([valor for valor in set(valores) if valores.count(valor) == 2]) == 2


#Metodo que comprueba si son pares
    def es_pareja(self, valores):
        return len(set(valores)) == 4
    


#Metodo que define al gandor 
    def obtener_ganador(self, manos):
        evaluaciones = [self.evaluar_mano(mano) for mano in manos]
        puntajes = [self.obtener_puntaje(evaluacion) for evaluacion in evaluaciones]
        max_puntaje = max(puntajes)
        ganadores = [i for i, puntaje in enumerate(puntajes) if puntaje == max_puntaje]
        
        if len(ganadores) == 1:
            return f"¡Jugador {ganadores[0] + 1} es el ganador con {evaluaciones[ganadores[0]]}!"
        else:
            ganadores_str = ", ".join([str(ganador + 1) for ganador in ganadores])
            return f"¡Hay un empate entre los jugadores {ganadores_str}!"



#Escala de relevancia que determina que juego es mejor
    def obtener_puntaje(self, evaluacion):
        puntajes = {
            "Carta Alta": 0,
            "Pareja": 1,
            "Doble Pareja": 2,
            "Trio": 3,
            "Escalera": 4,
            "Color": 5,
            "Full": 6,
            "Poker": 7,
            "Escalera de Color": 8,
            "Escalera Real": 9
        }
        return puntajes[evaluacion]

# Llamado de los metodos 
baraja = Baraja()
mano_jugador1 = baraja.repartir_mano(5)
mano_jugador2 = baraja.repartir_mano(5)
mano_jugador3 = baraja.repartir_mano(5)

manos = [mano_jugador1, mano_jugador2, mano_jugador3]

for i, mano in enumerate(manos):
    print(f"Jugador {i + 1}: {mano}")
    evaluacion = baraja.evaluar_mano(mano)
    print(f"Evaluación: {evaluacion}")

ganador = baraja.obtener_ganador(manos)
print(ganador)
 
    
