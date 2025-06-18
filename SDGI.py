lista_productos=[]
#producto={"nombre":nombre,"precio":precio,"cantidad":stock,"codigo":codigo}
#Codigo tiene que tener 3 validaciones:
#El codigo debe tener un minimo de 5 caracteres
#El codigo debe tener al menos 2 mayusculas
#El codigo debe tener al menos un numero
opcion="0"

"""
Sacar las funciones del while [x]
Cambiar las listas para crear el producto por un diccionario []
Agregar un codigo al diccionario de producto []
Agregar una lista para almacenar los diccionarios del producto []
Modificar las funciones para almacenar los diccionarios de los productos []
Agregar las funciones faltantes []
    Actualizar cantidad/precio []
    Mostrar Inventario completo []
    Eliminar productos []
"""
def validarcodigo(codigo):
    contador_mayusculas=0
    contador_numeros=0
    for l in codigo:
        if l.isupper():#Si es el caracter esta en mayuscula
            contador_mayusculas+=1
        if l.isnumeric():#Si el caracter es un numero
            contador_numeros+=1

    if contador_mayusculas<2:
        print("El codigo debe tener al menos dos mayusculas")
        return False                                                                                                                                    
    elif contador_numeros==0:
        print("El codigo debe tener al menos un numero")
        return False
    elif len(codigo) <5:
        print("El codigo debe tener al menos 5 caracteres")    
        return False
    else:
        return True                


def solicitarProducto():
        nombre=input("Ingrese el nombre del producto: ")
        while True:
            codigo=input("Ingrese el codigo de producto: ")
            if validarcodigo(codigo)==True:
                print("Codigo correcto")
                break
            else:
                print("El codigo es incorrecto, debe volver a ingresarlo")


        try:
            stock=int(input("Ingrese el stock del producto: "))
            precio=int(input("Ingrese el precio del producto: "))
            
            if stock<0 or precio <0:
                raise ValueError
                
            else:
                producto=[nombre,precio,stock,codigo]
                return producto

        except ValueError:
            print("Debe ingresar valores enteros positivos")
    
def guardarProducto(nombre,precio,stock,codigo):
    #producto={"nombre":nombre,"precio":precio,"cantidad":stock,"codigo":codigo}
    productobuscado=buscarProducto(codigo)
    if productobuscado!= None:
            print("Ese producto ya fue registrado")
            return False 

    producto={"nombre":nombre,"precio":precio,"cantidad":stock,"codigo":codigo}
    lista_productos.append(producto)
    return True     



def buscarProducto(codigo):
    for producto in lista_productos:
        if codigo == producto["codigo"]:
            return producto
    
    return None


def mostrarproducto(codigo):
    productobuscado = buscarProducto(codigo)
    if productobuscado!= None:
        print("-"*60)
        print(f"cod: {productobuscado[codigo]} \tNombre: {productobuscado[nombre]} \t Precio: ${productobuscado[precio]} \t Stock: {productobuscado[stock]} unidades")
        print("-"*60)
        #return [nombre,precio,stock]
    #Print("No existe un producto con ese nombre")

while opcion!="6":
    print("1.- Agregar producto")
    print("2.- Buscar producto")
    print("3.- Actualizar cantidad/precio")
    print("4.- Mostrar inventario completo")
    print("5.- Eliminar producto")
    print("6.- Salir")

    opcion=input("Ingrese la opción que desea(1-6): ")

    def solicitarProducto():
        nombre=input("Ingrese el nombre del producto: ")
        try:
            stock=int(input("Ingrese el stock del producto: "))
            precio=int(input("Ingrese el precio del producto: "))
            
            if stock<0 or precio <0:
                raise ValueError
                
            else:
                producto=[nombre,precio,stock]
                return producto

        except ValueError:
            print("Debe ingresar valores enteros positivos")
    

            
        else:
            print("No existe un producto con ese nombre")
    
    match opcion:

        case "1":
            nuevoProducto=solicitarProducto()
            if nuevoProducto!= None:
                guardarProducto(nuevoProducto[0],nuevoProducto[1],nuevoProducto[2])
        case "2":
            nombreProducto=input("Ingrese el nombre del producto a buscar: ")
            buscarProducto(nombreProducto)

