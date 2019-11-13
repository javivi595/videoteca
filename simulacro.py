#JAVIER DURAN DIAZ

#METODOS 
listapeliculas=[]

def listar():
    #Listar todas las peliculas
    for a in range(len(listapeliculas)):
        if listapeliculas[a][2]>0:
            print("ID: {}, Pelicula: {}, Director: {}, Genero: {}, Año: {}, Duracion: {}, estado disponible".format(a+1,listapeliculas[a][1],listapeliculas[a][2],listapeliculas[a][3],listapeliculas[a][4],listapeliculas[a][5]) )
        else:    
            print("ID: {}, Pelicula: {}, Director: {}, Genero: {}, Año: {}, Duracion: {}, estado no disponible".format(a+1,listapeliculas[a][1],listapeliculas[a][2],listapeliculas[a][3],listapeliculas[a][4],listapeliculas[a][5])) 


def añadir():
    tit=input("Introduce el titulo: ")
    dire=input("Introduce el director: ")
    cop=int(input("Introduce las copias que añades: "))
    gen=input("Introduce el genero: ")
    añ=int(input("Introduce el año de la pelicula: "))
    dur=int(input("Introduce duracion: "))
    listapeliculas.append([cop,tit,dire,gen,añ,dur])
    print("La pelicula {} ha sido añadida en el puesto {}.".format(tit,len(listapeliculas)))

def reservar():
    listar()
    #RESERVA
    reserva=int(input("Introdcue el ID de la pelicula que desea reservar: "))
    if reserva>(len(listapeliculas)+1):
        if listapeliculas[reserva-1][2]>0:
            print("Pelicula reservada")
            listapeliculas[reserva-1][2]-=1
        else:
            print("Pelicula no disponible")
    else:
        print("ID incorrecta")
        
#BUSCADOR

def buscar():
    print("¿Que tipo de busqueda desea realizar?")
    print("1)Titulo")
    print("2)Director")
    print("3)Genero")
    print("4)Año")
    print("5)Duracion")
    
    opcion=int(input(""))
    busq=input("Introduce el texto de busqueda:")
    busqueda(opcion,busq)
    
         
        
def busqueda(x, busq):
    
    for a in range(len(listapeliculas)):
        cadena="".join(map(str,listapeliculas[a][x]))
        c=cadena.find(busq)
        contador=0
        if c!=-1:
             print("ID: {}, Pelicula: {}, Director: {}, Genero: {}, Año: {}, Duracion: {}".format(a+1,listapeliculas[a][1],listapeliculas[a][2],listapeliculas[a][3],listapeliculas[a][4],listapeliculas[a][5]) )
             contador+=1
    if contador==0:
        print("No se ha encontrado tu pelicula")




#menu

entrada=0
while entrada != 4:
    print("\n\nMENU DE VIDEOCLUB")
    print("ELIGE UNA OPCION")
    print(" 1.Añadir pelicula \n 2.Reservar pelicula \n 3.Buscar peliculas \n 4.Salir")
    entrada=int(input("Introduce tu opcion: "))
    #AÑADIR PELICULA
    if entrada==1:       
        añadir()
    #Reservar pelicula    
    elif entrada==2:
        reservar()
    #Buscar peliculas
    elif entrada==3:
        buscar()
    #SALIR
    elif entrada!=4:
        print("Opcion incorrecta")

#Mensaje despedida
print("Gracias por su visita")
        