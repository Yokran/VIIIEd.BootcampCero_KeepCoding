for codigo in range(32, 127):
    print("'{}': {:3d}".format(chr(codigo), codigo), end="\t")
    if codigo % 4 == 3:
        print("")
    
    