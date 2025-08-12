"""
Sistema bancário para demonstração de testes de integração
"""

class ContaBancaria:
    """Classe que representa uma conta bancária"""
    
    def __init__(self, numero, saldo_inicial=0):
        """Inicializa conta com número e saldo"""
        self.numero = numero
        self.saldo = saldo_inicial
    
    def depositar(self, valor):
        """Deposita valor na conta"""
        if valor > 0:
            self.saldo += valor
            return True
        return False
    
    def sacar(self, valor):
        """Saca valor da conta se houver saldo suficiente"""
        if 0 < valor <= self.saldo:
            self.saldo -= valor
            return True
        return False
    
    def consultar_saldo(self):
        """Retorna o saldo atual"""
        return self.saldo


class SistemaBancario:
    """Sistema que gerencia múltiplas contas bancárias"""
    
    def __init__(self):
        """Inicializa sistema com dicionário vazio de contas"""
        self.contas = {}
    
    def criar_conta(self, numero, saldo_inicial=0):
        """Cria nova conta no sistema"""
        if numero in self.contas:
            raise ValueError(f"Conta {numero} já existe")
        
        conta = ContaBancaria(numero, saldo_inicial)
        self.contas[numero] = conta
        return conta
    
    def obter_conta(self, numero):
        """Retorna conta pelo número"""
        return self.contas.get(numero)
    
    def transferir(self, origem, destino, valor):
        """Transfere valor entre contas"""
        conta_origem = self.contas.get(origem)
        conta_destino = self.contas.get(destino)
        
        if not conta_origem or not conta_destino:
            return False
        
        if conta_origem.sacar(valor):
            conta_destino.depositar(valor)
            return True
        return False
    
    def total_depositos(self):
        """Calcula total de dinheiro no sistema"""
        return sum(conta.saldo for conta in self.contas.values())