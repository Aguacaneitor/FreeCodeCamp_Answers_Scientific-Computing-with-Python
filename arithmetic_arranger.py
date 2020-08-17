
def checkFloat(number):
    try:
        int(number)
        return False
    except:
        return True

def arithmetic_arranger(problems):
    ejecutar = True
    arranged_problems = ""
    numerosSup = []
    numerosInf = []
    operadores = []
    longitudNumeros = []
    if len(problems) > 5:
        arranged_problems = "Error: Too many problems."
        ejecutar =  False
    if ejecutar:
        for operacion in problems:
            partes = operacion.split()
            if partes[1] not in ('+','-'):
                arranged_problems = "Error: Operator must be '+' or '-'."
                ejecutar = False
                break
            else:
                operadores.append(partes[1])
            if len(partes[0]) >= 5 or len(partes[2]) >= 5:
                    arranged_problems = "Error: Numbers cannot be more than four digits."
                    ejecutar = False
                    break
            if not checkFloat(partes[0]):
                numerosSup.append(partes[0])
                longitudNumeros.append(len(partes[0]))
            else:
                arranged_problems = "Error: Numbers must only contain digits"
                ejecutar = False
                break
            if not checkFloat(partes[2]):
                numerosInf.append(partes[2])
                if len(partes[2]) > longitudNumeros[-1]:
                    longitudNumeros[-1] = len(partes[2])
            else:
                arranged_problems = "Error: Numbers must only contain digits"
                ejecutar = False
                break
    if ejecutar:
        resultados = []
        for i in range(0,len(longitudNumeros)):
            if operadores[i] in ('+'):
                resultados.append(int(numerosSup[i])+int(numerosInf[i]))
            else:
                resultados.append(int(numerosSup[i])-int(numerosInf[i]))
        for i in range(0,len(longitudNumeros)):
            arranged_problems += "  "
            diferencia = len(numerosInf[i]) - len(numerosSup[i])
            if diferencia > 0:
                for j in range(0,diferencia):
                    arranged_problems += " "
            arranged_problems += numerosSup[i]
            if i < (len(longitudNumeros)-1): arranged_problems += "    "

        
        arranged_problems += "\n"

        for i in range(0,len(longitudNumeros)):
            arranged_problems += operadores[i]+" "
            diferencia = len(numerosSup[i]) - len(numerosInf[i]) 
            if diferencia > 0:
                for j in range(0,diferencia):
                    arranged_problems += " "
            arranged_problems += numerosInf[i]
            if i < (len(longitudNumeros)-1): arranged_problems += "    "

        arranged_problems += "\n"

        for i in range(0,len(longitudNumeros)):
            arranged_problems += "--"
            for j in range(0,longitudNumeros[i]):
                arranged_problems += "-"
            if i < (len(longitudNumeros)-1): arranged_problems += "    "
        
        arranged_problems += "\n"

        for i in range(0,len(longitudNumeros)):
            diferencia = (longitudNumeros[i]+2) - len(str(resultados[i])) 
            if diferencia > 0:
                for j in range(0,diferencia):
                    arranged_problems += " "
            arranged_problems += str(resultados[i])
            if i < (len(longitudNumeros)-1): arranged_problems += "    "
        
    return arranged_problems


esperado = "    3      3801      45      123\n+ 855    -    2    + 43    +  49\n-----    ------    ----    -----" 
prueba = arithmetic_arranger(["3 + 855", "3801 - 2", "45 + 43", "123 + 49"])
if prueba == esperado:
    print("Bien")
else:
    print("Mal",prueba,sep="\n")