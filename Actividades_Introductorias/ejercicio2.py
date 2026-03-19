#Equivalencia a partir de segundos
UNA_HORA = int(3600)
UN_MINUTO = int(60)
tiempo = int(input("Ingrese una cantidad de Segundos: "))

if tiempo != 0:
    horas = tiempo // UNA_HORA
    minutos = (tiempo % UNA_HORA) // 60
    segundos = tiempo % 60

    print (f"{tiempo} equivale a {horas} hora(s), {minutos} minuto(s), y {segundos} segundo(s).")
else:
    print ('Ingreso 0')


    
