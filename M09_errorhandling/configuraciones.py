class Configuraciones:
    def __init__(self, myList):
        self.lista = myList
    
# -------------------------------------------------------------------------------------------------
    def Primos(self):
        for i in self.lista:
            if self.__Primos(i):
                print(f'El número {i} es primo')
            else:
                print(f'El número {i} no es primo')

    def ConversionTemperaturas(self, origen, destino):
        for i in self.lista:
            print(f'{i} {origen} a {destino} es: ', str(self.__ConversionTemperaturas(i, origen, destino)))

# -------------------------------------------------------------------------------------------------

    def __Primos(self, num):  #Obtiene el número primo
        if num < 2:
            return False
        else:
            for i in range(2, num):
                if num % i == 0:
                    return False
            return True
        
    def ModaRepeticiones(self, lista):  #Obtiene que número se repite mas veces
        unicos = []
        repeticiones = []

        if list(lista) == 0:
            return None
        else:
            for value in lista:
                if value in unicos: #Si existe dentro de unicos
                    i = unicos.index(value)
                    repeticiones[i] += 1
                else:   #Si no existe dentro de unicos
                    unicos.append(value)
                    repeticiones.append(1)
        
        moda = unicos[0]    
        maximo = repeticiones[0]

        for index, elementos in enumerate(unicos):        
            if maximo < repeticiones[index]:    #Si el maximo es menor a las repeticiones
                '''
                Si el máximo es menor al valor guardado, se reemplaza.
                '''
                moda = elementos
                maximo = repeticiones[index]

        return moda, maximo
    
    def __ConversionTemperaturas(self, valor, origen, destino):   #Conversor de Temperaturas
        conversion = 0
        if origen == 'Celsius':
            if destino == 'Fahrenheit':
                conversion = 32 + (9/5 * valor)
            elif destino == 'Kelvin':
                conversion = 273.15 + valor
            else:
                return 'Destino ingresado no valido.'
        elif origen == 'Fahrenheit':
            if destino == 'Celsius':
                conversion = 5/9 * (valor - 32)
            elif destino == 'Kelvin':
                conversion = 273.15 + 5/9 * (valor - 32)
            else:
                return 'Destino ingresado no valido.'
        elif origen == 'Kelvin':
            if destino == 'Celsius':
                conversion = valor - 273.15
            elif destino == 'Fahrenheit':
                conversion = 32 + 9/5 * (valor - 273.15)
            else:
                return 'Destino ingresado no valido.'
        else:
            return 'Origen ingresado no valido.'
        
        return round(conversion, 2)
    
    def __Factorial(self, num):   #Obtiene el factorial
        if type(num) != int or num < 0:
            print('Dato ingresado invalido')
        else:
            if num <= 1:
                return 1
            else:
                return num * self.Factorial(num - 1)