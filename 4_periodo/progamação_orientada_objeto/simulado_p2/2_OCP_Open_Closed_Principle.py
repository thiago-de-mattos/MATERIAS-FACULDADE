"""
================================================================================
SIMULADO P2 - PROGRAMAÇÃO ORIENTADA A OBJETOS
Professor: Tiago Castro
Turma: 4º Período B - Engenharia de Software
================================================================================

PRINCÍPIO: OPEN/CLOSED PRINCIPLE (OCP)
VALOR: 1,0 ponto

O Princípio Aberto/Fechado estabelece que entidades de software devem estar
abertas para extensão, mas fechadas para modificação. Isso significa que você
deve ser capaz de adicionar novas funcionalidades sem modificar o código existente.

================================================================================
"""

# ============================================================================
# EXEMPLO QUE NÃO RESPEITA O OCP
# ============================================================================
# 
# A classe CalculadoraDesconto abaixo viola o OCP porque:
# - Toda vez que precisamos adicionar um novo tipo de desconto, temos que
#   MODIFICAR a classe existente (adicionar um novo if/elif)
# - Isso viola o princípio "fechado para modificação"
#
# PROBLEMA: Se amanhã precisarmos adicionar desconto para estudante, idoso,
# ou qualquer outro tipo, teremos que alterar o método calcular_desconto,
# aumentando o risco de quebrar código que já funciona.
#
# ============================================================================

class CalculadoraDesconto:
    def calcular_desconto(self, valor, tipo_cliente):
        """
        Calcula desconto baseado no tipo de cliente.
        
        PROBLEMA: Toda vez que adicionamos um novo tipo, precisamos
        modificar este método!
        """
        if tipo_cliente == "VIP":
            return valor * 0.20  # 20% de desconto
        elif tipo_cliente == "PREMIUM":
            return valor * 0.15  # 15% de desconto
        elif tipo_cliente == "REGULAR":
            return valor * 0.05  # 5% de desconto
        else:
            return 0


# Exemplo de uso (problema):
# calc = CalculadoraDesconto()
# desconto = calc.calcular_desconto(1000, "VIP")  # Retorna 200


# ============================================================================
# ORIENTAÇÕES PARA CORREÇÃO
# ============================================================================
#
# SUA TAREFA:
# Refatore o código acima aplicando o Princípio Aberto/Fechado.
#
# PASSO A PASSO:
# 1. Crie uma classe abstrata ou interface (usando ABC do Python) chamada
#    DescontoStrategy ou similar que define o método calcular_desconto.
#
# 2. Crie classes concretas para cada tipo de desconto:
#    - DescontoVIP
#    - DescontoPremium
#    - DescontoRegular
#    Cada uma implementando a estratégia de desconto específica.
#
# 3. Modifique a CalculadoraDesconto para receber uma estratégia de desconto
#    ao invés de um tipo de cliente como string.
#
# 4. Agora, para adicionar um novo tipo de desconto (ex: DescontoEstudante),
#    você só precisa criar uma nova classe sem modificar as existentes!
#
# DICA: Use o módulo abc do Python para criar classes abstratas.
#
# ============================================================================
# ÁREA PARA SUA IMPLEMENTAÇÃO
# ============================================================================

# TODO: Implemente aqui sua solução aplicando o OCP

from abc import ABC,  abstractmethod

class DescontoStrategy(ABC):

    @abstractmethod
    def calcular_desconto(self, valor):
        pass
 
class DescontoVIP(DescontoStrategy):
    
    def calcular_desconto(self, valor):
        return valor * 0.20

class DescontoPremium(DescontoStrategy):
    def calcular_desconto(self, valor):
        return valor * 0.15

class DescontoRegular(DescontoStrategy):
    def calcular_desconto(self, valor):
        return valor * 0.05

class CalculadoraDesconto():
    
    def __init__(self, estrategia: DescontoStrategy ):
        self.estrategia = estrategia
        
    def calcular_desconto(self):
        return self.estrategia

# Exemplo de uso esperado:
# from abc import ABC, abstractmethod
# 
# # Definir interface/estratégia abstrata
# # Criar classes concretas para cada tipo de desconto
# # Modificar CalculadoraDesconto para usar estratégias
# 
# calc = CalculadoraDesconto(DescontoVIP())
# desconto = calc.calcular_desconto(1000)  # Retorna 200
# 
# # Para adicionar novo tipo, apenas criar nova classe:
# # calc2 = CalculadoraDesconto(DescontoEstudante())
# # desconto2 = calc2.calcular_desconto(1000)

