# Concatenação
# Conversão

#print('1' + 12) - é necessário converter o dado para dar certo 
print('1' + str(12)) #conversão de int para str
print(int('1') + 12) #conversão de str para int

print(int('1'), type(int('1')))
print(bool('   ')) #true pois possui informação
print(bool("")) #false pois não possui informação
print(bool(True == False))
print(bool(False == False))
print(bool(bool('') == bool(' '))) # Comparação de tipos