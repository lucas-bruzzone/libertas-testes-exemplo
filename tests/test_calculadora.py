"""
Testes unitários para a classe Calculadora
"""

import pytest
import sys
sys.path.insert(0, '.')
from src.calculadora import Calculadora


class TestCalculadora:
    """Classe de testes para Calculadora"""
    
    def setup_method(self):
        """Executado antes de cada teste"""
        self.calc = Calculadora()
    
    def test_soma_positivos(self):
        """Testa soma de números positivos"""
        assert self.calc.soma(2, 3) == 5
    
    def test_soma_negativos(self):
        """Testa soma de números negativos"""
        assert self.calc.soma(-2, -3) == -5
    
    def test_soma_zero(self):
        """Testa soma com zero"""
        assert self.calc.soma(5, 0) == 5
        assert self.calc.soma(0, 0) == 0
    
    def test_subtracao_normal(self):
        """Testa subtração normal"""
        assert self.calc.subtracao(10, 3) == 7
        assert self.calc.subtracao(5, 8) == -3
    
    def test_multiplicacao_normal(self):
        """Testa multiplicação normal"""
        assert self.calc.multiplicacao(3, 4) == 12
        assert self.calc.multiplicacao(-2, 5) == -10
    
    def test_divisao_normal(self):
        """Testa divisão normal"""
        assert self.calc.divisao(10, 2) == 5.0
        assert self.calc.divisao(15, 3) == 5.0
    
    def test_divisao_por_zero(self):
        """Testa exceção de divisão por zero"""
        with pytest.raises(ZeroDivisionError):
            self.calc.divisao(10, 0)


# Fixture para reutilização
@pytest.fixture
def calculadora():
    """Fixture que retorna uma instância de Calculadora"""
    return Calculadora()


def test_operacoes_com_fixture(calculadora):
    """Exemplo usando fixture"""
    assert calculadora.soma(1, 2) == 3


# Teste parametrizado
@pytest.mark.parametrize("a,b,esperado", [
    (2, 3, 5),
    (-1, 1, 0),
    (0, 0, 0),
    (100, -50, 50),
    (-10, -5, -15)
])
def test_soma_parametrizada(calculadora, a, b, esperado):
    """Testa soma com múltiplos valores"""
    assert calculadora.soma(a, b) == esperado


@pytest.mark.parametrize("a,b,esperado", [
    (10, 2, 5.0),
    (20, 4, 5.0),
    (15, 3, 5.0),
    (100, 10, 10.0)
])
def test_divisao_parametrizada(calculadora, a, b, esperado):
    """Testa divisão com múltiplos valores"""
    assert calculadora.divisao(a, b) == esperado