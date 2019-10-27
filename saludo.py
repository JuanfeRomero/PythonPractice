class Saludo:
    def saludo(self):
        self
        saludos = {0: "",
                   1: 'mundo',
                   2: 'fede',
                   3: 'aloh'
                   }
        if self == -1:
            print('saliendo')
        elif self != -1 and (int(self) < 0 or int(self) > 3):
            print('numero no valido')
        else:
            print('hola ' + saludos[self] + "!")
    myNum = -5
    while myNum != -1:
        print("elegi que saludar: 0 a 3, -1 para salir")
        myNum = int(input())
        saludo(myNum)
