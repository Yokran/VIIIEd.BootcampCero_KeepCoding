def ordinal(n):
  ordinals = ('primero', 'segundo', 'tercero', 'cuarto', 'quinto', 'sexto', 'séptimo', 'octavo', 'noveno', 'décimo', 'undécimo', 'duodécimo')
  
  if n > 0 and n <= 12:
    return ordinals[n-1]
  else:
    return ''
  
if __name__ == '__main__':
  for i in range(1,13):
    print("{:2d} -> {}".format(i, ordinal(i)))