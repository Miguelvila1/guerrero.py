import random
class guerrero:
    def __init__(self, nombre,vida,fuerza,precision,velocidad,defensa):
        self.nombre = nombre
        self.vida=vida
        self.fuerza=fuerza
        self.precision=precision
        self.velocidad=velocidad
        self.defensa=defensa
    def golpear(self,g):
        if(random.random() <= self.precision - g.velocidad / 100):
            g.vida -= max([(self.fuerza - g.defensa) + random.randrange(-10,11),1])
            print("golpe certerode",self.nombre)
        else:
            print(g.nombre,"esquiva el golpe") 
def simular_batalla(j1 , j2):
    golpeador , receptor = j1,j2
    if(j1.velocidad < j2.velocidad):
            golpeador, receptor =j1, j2
    while(j1.vida > 0 and j2.vida > 0):
        print("\n" + j1.nombre, j1.vida, "vs", j2.vida, j2.nombre)
        golpeador.golpear(receptor)
        golpeador, receptor = receptor, golpeador  
        print("\n", + j1.nombre, j1.vida, "vs", j2.vida, j2.nombre)
        print("ganador", receptor.nombre)
superman=guerrero('superman', 100,50,80,30,20)
goku=guerrero('goku', 1000,600,800,400,67)
chuck=guerrero('chuck norris', 100, 70,75,40,15)
simular_batalla(goku, superman)
