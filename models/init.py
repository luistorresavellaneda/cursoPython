from models.clientes import Clientes
cliente = Clientes('Luis', 'Torres', edad='23')
cliente.edad='22'
print(cliente.edad)
print(cliente.nombres)