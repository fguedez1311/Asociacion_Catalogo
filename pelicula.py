import pickle
class Pelicula:
    def __init__(self,titulo,duracion,lanzamiento):

        self.titulo=titulo
        self.duracion=duracion
        self.lanzamiento=lanzamiento
    def __str__(self):
        return '{} {}'.format(self.titulo,self.lanzamiento)
    def buscar(self,filtro):
        return filtro in self.titulo
class Catalogo:
    def __init__(self):
        self.peliculas=[]
    def nueva_pelicula(self,titulo,duracion,lanzamiento):
        self.peliculas.append(Pelicula(titulo,duracion,lanzamiento))
        self.guardar()
    def guardar(self):
        fichero=open('catalogo.pckl','wb')
        pickle.dump(self.peliculas,fichero)
        fichero.close()
        del(fichero)
    def cargar(self):
        fichero = open('catalogo.pckl', 'ab+')
        fichero.seek(0)
        self.peliculas=pickle.load(fichero)
        fichero.close()
    def mostrar_peliculas(self):
        for pelicula in self.peliculas:
            print(pelicula)
c=Catalogo()
c.nueva_pelicula("El Padrino",175,1972)
c.nueva_pelicula("El Padrino 2",200,2020)
c.cargar()
c.mostrar_peliculas()