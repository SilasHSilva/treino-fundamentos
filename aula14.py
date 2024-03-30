a = 'AAAA'
b = 'BBBBB'
c = 1.2

string = 'b ={nome2} a={nome1} c={nome3} a={nome1}'
formato = string.format(nome1 = a, nome2 = b, nome3 = c)

print(formato)