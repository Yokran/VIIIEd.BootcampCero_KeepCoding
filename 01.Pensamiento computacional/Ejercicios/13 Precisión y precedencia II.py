#SOLUCIÓN:
strCapital = input("Capital principal...........: ")
strInteres = input("Interés anual...............: ")
strAños =    input("Años de imposición..........: ")
strPeriodo = input("Periodos de imposición anual: ")

capital = float(strCapital)
interes = float(strInteres)/100
años = int(strAños)
periodo = int(strPeriodo)

final = capital *(1 + interes/periodo)**(periodo * años)

print("{:.2f} € invertidos al {:.2f}% durante {} años con {} periodos de imposición por año se transforman en {:.2f} €]".format(capital, interes*100, años, periodo, final))