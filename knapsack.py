class Knapsack:
    def __init__(self, monedas):
        self._monedas = monedas

    def f(self, cromosoma):
        dinero = 0
        for i in range(len(cromosoma)):
            if cromosoma[i]:
                if i == len(cromosoma)-1:
                    if cromosoma[i - 1]:
                        break
                elif i == 0:
                    if cromosoma[i + 1]:
                        break
                elif cromosoma[i - 1] or cromosoma[i + 1]:
                        break
                dinero = dinero + self._monedas[i]   
        return dinero

