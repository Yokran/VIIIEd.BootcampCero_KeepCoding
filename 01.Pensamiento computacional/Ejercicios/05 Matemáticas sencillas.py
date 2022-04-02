strN01 = input("Introduce el primer número ")
strN02 = input("Introduce el segundo número ")

N01 = int(strN01)
N02 = int(strN02)

suma = N01 + N02
resta = N01 - N02
producto = N01 * N02
division = N01 / N02

print(N01, "+", N02, "=", suma, N01, "-", N02, "=", resta)


#SOLUCIÓN

strOp1 = input("Introduce un número: ")
strOp2 = input("Introduce un segundo número:" )

op1 = float(strOp1)
op2 = float(strOp2)

print("{} + {} = {}\n{} - {} = {}\n{} · {} = {}\n{} / {} = {}\n".format(op1, op2, op1+op2, op1, op2, op1-op2, op1, op2, op1*op2, op1, op2, op1/op2))