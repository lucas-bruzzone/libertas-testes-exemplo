"""
Testes de integração para o sistema bancário
"""

import pytest
import sys
sys.path.insert(0, '.')
from src.banco import ContaBancaria, SistemaBancario


@pytest.fixture
def sistema_bancario():
    """Fixture com sistema bancário configurado"""
    sistema = SistemaBancario()
    sistema.criar_conta("001", 1000)
    sistema.criar_conta("002", 500)
    sistema.criar_conta("003", 0)
    return sistema


class TestSistemaBancario:
    """Testes de integração do sistema bancário"""
    
    def test_criar_conta_nova(self):
        """Testa criação de nova conta"""
        sistema = SistemaBancario()
        conta = sistema.criar_conta("100", 250)
        
        assert conta.numero == "100"
        assert conta.saldo == 250
        assert sistema.obter_conta("100") == conta
    
    def test_criar_conta_duplicada(self):
        """Testa erro ao criar conta duplicada"""
        sistema = SistemaBancario()
        sistema.criar_conta("100", 250)
        
        with pytest.raises(ValueError):
            sistema.criar_conta("100", 300)
    
    def test_transferencia_sucesso(self, sistema_bancario):
        """Testa transferência bem-sucedida"""
        resultado = sistema_bancario.transferir("001", "002", 200)
        
        assert resultado == True
        assert sistema_bancario.contas["001"].saldo == 800
        assert sistema_bancario.contas["002"].saldo == 700
    
    def test_transferencia_saldo_insuficiente(self, sistema_bancario):
        """Testa transferência com saldo insuficiente"""
        resultado = sistema_bancario.transferir("002", "001", 600)
        
        assert resultado == False
        assert sistema_bancario.contas["002"].saldo == 500
        assert sistema_bancario.contas["001"].saldo == 1000
    
    def test_transferencia_conta_inexistente(self, sistema_bancario):
        """Testa transferência para conta inexistente"""
        resultado = sistema_bancario.transferir("001", "999", 100)
        
        assert resultado == False
        assert sistema_bancario.contas["001"].saldo == 1000
    
    def test_transferencia_valor_zero(self, sistema_bancario):
        """Testa transferência de valor zero"""
        resultado = sistema_bancario.transferir("001", "002", 0)
        
        assert resultado == False
        assert sistema_bancario.contas["001"].saldo == 1000
        assert sistema_bancario.contas["002"].saldo == 500
    
    def test_total_depositos(self, sistema_bancario):
        """Testa cálculo do total de depósitos"""
        total_inicial = sistema_bancario.total_depositos()
        assert total_inicial == 1500  # 1000 + 500 + 0
        
        # Após transferência, total deve permanecer o mesmo
        sistema_bancario.transferir("001", "002", 300)
        total_pos_transferencia = sistema_bancario.total_depositos()
        assert total_pos_transferencia == 1500


class TestContaBancaria:
    """Testes unitários da conta bancária"""
    
    def test_deposito_valido(self):
        """Testa depósito válido"""
        conta = ContaBancaria("123", 100)
        resultado = conta.depositar(50)
        
        assert resultado == True
        assert conta.saldo == 150
    
    def test_deposito_invalido(self):
        """Testa depósito inválido"""
        conta = ContaBancaria("123", 100)
        resultado = conta.depositar(-50)
        
        assert resultado == False
        assert conta.saldo == 100
    
    def test_saque_valido(self):
        """Testa saque válido"""
        conta = ContaBancaria("123", 100)
        resultado = conta.sacar(30)
        
        assert resultado == True
        assert conta.saldo == 70
    
    def test_saque_saldo_insuficiente(self):
        """Testa saque com saldo insuficiente"""
        conta = ContaBancaria("123", 100)
        resultado = conta.sacar(150)
        
        assert resultado == False
        assert conta.saldo == 100


# Testes parametrizados
@pytest.mark.parametrize("saldo_inicial,valor_transferencia,sucesso_esperado", [
    (1000, 500, True),
    (1000, 1000, True),
    (1000, 1001, False),
    (500, 600, False),
    (0, 1, False)
])
def test_transferencia_parametrizada(valor_transferencia, sucesso_esperado, saldo_inicial):
    """Testa transferência com diferentes valores"""
    sistema = SistemaBancario()
    sistema.criar_conta("origem", saldo_inicial)
    sistema.criar_conta("destino", 0)
    
    resultado = sistema.transferir("origem", "destino", valor_transferencia)
    assert resultado == sucesso_esperado