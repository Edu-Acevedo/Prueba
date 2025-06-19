opcion = 0
turistas = {"001": ["John Doe", "Estados Unidos", "12-01-2024"],
            "002": ["Emily Smith", "Estados Unidos", "23-03-2024"],
            "012": ["Julian Martinez", "Argentina", "19-09-2023"],
            "014": ["Agustin Morales", "Argentina", "28-03-2024"],
            "005": ["Carlos Garcia", "Mexico", "10-05-2024"],
            "006": ["Maria Lopez", "Mexico", "08-12-2023"],
            "007": ["Joao Silva", "Brasil", "20-06-2024"],
            "003": ["Michael Brown", "Estados Unidos", "05-07-2023"],
            "004": ["Jessica Davis", "Estados Unidos", "15-11-2024"],
            "008": ["Ana Santos", "Brasil", "03-10-2023"],
            "010": ["Martin Fernandez", "Argentina", "13-02-2023"],
            "011": ["Sofia Gomez", "Argentina", "07-04-2024"],
        }



#def Turistas_por_pais(pais):
    
 #   for elemento in turistas.values():
 #       if elemento[1].upper()==str(pais).upper():
 #           print(f"nombre: {elemento[0]}")

#Turistas_por_pais(nacion)

def Turistas_por_mes(mes=None,pais=None):
    fecha_random = "12-03-2020"
    mes=fecha_random.split("-")[1]
    print(f"mes: {mes}")


Turistas_por_mes()    


   


#while True:
#    try:
#        print("***MENU PRINCIPAL***\n1_ Turistas Por Pais\n2_ Turistas Por Mes\n3_ Eliminar Turista\n4_ Salir")

 #       opcion = input("Ingrese una opcion valida 1-4: ")
#    except ValueError:
  #      print("Ingrese un valor entero disponible")

#    match opcion:
 #       case "1":
  #          nacion = input("")
