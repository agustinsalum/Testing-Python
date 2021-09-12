
class Pila:
     def __init__(self):
         self.items = []

     def estaVacia(self):
         return self.items == []

     def incluir(self, item):
         self.items.append(item)

     def extraer(self):
         return self.items.pop()

     def inspeccionar(self):
         return self.items[len(self.items)-1]

     def tamano(self):
         return len(self.items)
	

def crear():
	miPila = Pila()
	return miPila.tamano()

def agregar():
	miPila = Pila()
	miPila.incluir(5)
	return miPila.inspeccionar()

def ultimoElemento():
	miPila = Pila()
	miPila.incluir(5)
	miPila.incluir(8)
	miPila.incluir(9)
	return miPila.inspeccionar()

def eliminarTope():
	miPila = Pila()
	miPila.incluir(5)
	miPila.incluir(8)
	miPila.incluir(9)
	miPila.extraer()
	return miPila.inspeccionar()
