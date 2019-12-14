a = float(input('Digite o comprimento do segmento a: '))
b = float(input('Digite o comprimento do segmento b: '))
c = float(input('Digite o comprimento do segmento c: '))

if a < (b + c) and b < (a + c) and c < (a + b):
    print('É possível a formação de um triângulo do tipo ', end='')
    if a == b == c:
        print('equilátero')
    elif a == b or c == b or a == c:
        print('isóceles')
    elif a != b != c:
        print('escaleno')
else:
    print('Não é possível a formação de um triângulo!')