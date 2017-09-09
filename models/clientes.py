class Clientes(object):
    estado_cuenta = None

    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

    def __len__(self):
        return self.cliente

    def __str__(self):
        #return self.nombre + ' ' + self.apellido
        #return ' '.join((self.nombre, self.apellido),)
        #dato = ' Cliente: %s %s' % (self.nombre, self.apellido)
        return self.getNombres()

    def getNombres(self):
        return ' '.join((self.nombre, self.apellido), )

    @property
    def nombres(self):
        return ' '.join((self.nombre, self.apellido), )

if __file__ == '__main__':
    cliente = Clientes('Luis', 'Torres', edad='23')
    print(cliente.edad)
    print(cliente.nombres, len(cliente))

    cliente.edad='22'