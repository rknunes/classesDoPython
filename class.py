class Bolo:
    def __init__(self, sabor, cobertura, tamanho):
        self.sabor = sabor
        self.cobertura = cobertura
        self.tamanho = tamanho

    def assar(self):
        pass

    def comer(self):
        pass

    def apodrecido(self):
        pass

bolo1 = Bolo('chocolate', 'chocolate', 'medio')    
bolo2 = Bolo('laranja', 'creme', 'pequeno')

print(bolo1.sabor)
print(bolo1.tamanho)       

print(bolo2.sabor)
print(bolo2.cobertura)

if bolo1.sabor == bolo2.sabor:
    print('voce tem sabores iguais nos bolos')

else:
    print('os sabores sao diferentes')    