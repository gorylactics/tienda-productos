class Producto:
    def __init__(self, nombre , precio , categoria):
        self.nombre = nombre
        self.precio = precio
        self.categoria = categoria
        self.id = 1
    
    # def identificador(self ,  identificador):
    #     for index in self.id:
    #         self.id += 1

    def actualizarPrecio(self , impuesto , incrementado):
        if incrementado == True:
            self.precio += (self.precio * impuesto)
        else:
            self.precio -= (self.precio * impuesto)
    def impresion(self):
        return f'Id: {self.id}\nProducto: {self.nombre}\nCategoria: {self.categoria}\nPrecio: {self.precio}'

if __name__ == '__main__':
    platano = Producto('Platano', 100 , 'Frutas')
    print(platano.impresion())
    platano.actualizarPrecio(0.20 , True)
    print(platano.precio)
    platano.actualizarPrecio(0.20 , False)
    print(platano.precio)

    platano2 = Producto('avion' , 100 , 'vehiculo')
    print(platano2.impresion())

# print(locals())