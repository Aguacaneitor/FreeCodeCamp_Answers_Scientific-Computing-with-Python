import re

def valor_del_dia(day_of_week):
    dia_numerico = 0
    dia = day_of_week.lower()
    if dia == "monday":
        dia_numerico = 1
    elif dia == "tuesday":
        dia_numerico = 2
    elif dia == "wednesday":
        dia_numerico = 3
    elif dia == "thursday":
        dia_numerico = 4
    elif dia == "friday":
        dia_numerico = 5
    elif dia == "saturday":
        dia_numerico = 6
    elif dia == "sunday":
        dia_numerico = 7
    return dia_numerico

def obtener_dia(dia_numerico):
    dia = ""    
    if dia_numerico == 1:
        dia = "monday"
    elif dia_numerico == 2:
        dia = "tuesday"
    elif dia_numerico == 3:
        dia = "wednesday"
    elif dia_numerico == 4:
        dia = "thursday"
    elif dia_numerico == 5:
        dia = "friday"
    elif dia_numerico == 6:
        dia = "saturday"
    elif dia_numerico == 7:
        dia = "sunday"
    return dia.capitalize()

def add_time(start, duration, day_of_week=""):
    partes = start.split()
    formato_hora_inicial = partes[1]
    formato_hora_final = formato_hora_inicial
    dias_trascurridos = 0
    hora_inicial = int(re.findall("^([0-9]+):", start)[0])
    minutos_inicial = int(re.findall("^[0-9]+:([0-9]+)", start)[0])
    hora_aumentar = int(re.findall("^([0-9]+):", duration)[0])
    minutos_aumentar = int(re.findall("^[0-9]+:([0-9]+)", duration)[0])
    minutos_finales = minutos_inicial + minutos_aumentar
    if minutos_finales >= 60:
        hora_aumentar += (minutos_finales//60)
        minutos_finales %= 60
    hora_final = hora_inicial + hora_aumentar
    contador = hora_final//12
    if contador > 0:
        divisor = hora_final/12 
        if (hora_final % 12 > 0): 
            hora_final = int(hora_final%12)
        else: 
            hora_final = int(hora_final // divisor)
        for i in range (0,contador):
            if formato_hora_final == "AM":
                formato_hora_final = "PM"
            else:
                formato_hora_final = "AM"
                dias_trascurridos += 1

    #if hora_final < 10: hora_final = "0"+str(hora_final)
    if minutos_finales < 10: minutos_finales = "0"+str(minutos_finales)
    new_time = str(hora_final)+":"+str(minutos_finales)+" "+formato_hora_final

    if day_of_week != "":
        dia_inicial = valor_del_dia(day_of_week)
        dia_final = dia_inicial + dias_trascurridos
        if dia_final > 7:
            dia_calcular =  dia_final%7
            dia_final_texto = obtener_dia(dia_calcular)
        else: 
            dia_final_texto =  obtener_dia(dia_final)
        new_time += ", "+ dia_final_texto
    if dias_trascurridos == 1 : new_time += " (next day)"
    elif dias_trascurridos > 1: new_time += " ("+ str(dias_trascurridos) +" days later)"
    return new_time

esperado = "12:05 PM"
calculado = add_time("11:40 AM", "0:25")
if calculado == esperado:
    print("bien")
else: 
    print("Mal")
    print(calculado)