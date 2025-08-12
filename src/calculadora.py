"""
Classe Calculadora para demonstração de testes unitários
"""

class Calculadora:
    """Classe que implementa operações matemáticas básicas"""
    
    def soma(self, a, b):
        """Retorna a soma de dois números"""
        return a + b
    
    def subtracao(self, a, b):
        """Retorna a subtração de dois números"""
        return a - b
    
    def multiplicacao(self, a, b):
        """Retorna a multiplicação de dois números"""
        return a * b
    
    def divisao(self, a, b):
        """Retorna a divisão de dois números"""
        if b == 0:
            raise ZeroDivisionError("Divisão por zero não é permitida")
        return a / b