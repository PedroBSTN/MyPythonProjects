print('comaprador de frase')

s1 = input('primeira frase')
s2 = input('segunda frase')

print(f'Tamanho de "{s1}": {len(s1)} caracteres')
print(f'Tamanho de "{s2}": {len(s2)} caracteres')

if s1 == s2:
    print('as duas sao igauis')
else:
    print('as duas são diferentes')

if len(s1) == len(s2):
    print('tem o mesmo tamanho')
else:
    print('tem tamanhos diferentes')