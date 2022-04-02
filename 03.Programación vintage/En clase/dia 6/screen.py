def clear():
    print("\033[2J")

def locate(line, column):
    print("\033[{};{}H".format(line, column), end="")

def clearline(line=None, column=None):
    if line is not None and column is not None:
        locate(line, column)
    elif line is not None:
        locate(line, 1)
    print("\033[K", end="")
    
def Print(cadena, line, column, delEnd=False):
    
    locate(line, column)
    if delEnd:
        clearline()
    print(cadena, end="")

def Input(msg, line, column, delEnd=True):
    locate(line, column)
    if delEnd:
        clearline()
    return input(msg)

def Format(style, colorText=37, colorBack=40):
    print("\033[{};{};{}m".format(style, colorText, colorBack))

def Reset():
    Format(0, 37, 40)