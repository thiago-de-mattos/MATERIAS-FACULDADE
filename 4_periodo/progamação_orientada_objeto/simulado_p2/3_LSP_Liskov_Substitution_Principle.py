"""
================================================================================
SIMULADO P2 - PROGRAMAÇÃO ORIENTADA A OBJETOS
Professor: Tiago Castro
Turma: 4º Período B - Engenharia de Software
================================================================================

PRINCÍPIO: LISKOV SUBSTITUTION PRINCIPLE (LSP)
VALOR: 1,0 ponto

O Princípio de Substituição de Liskov estabelece que objetos de uma superclasse
devem ser substituíveis por objetos de suas subclasses sem quebrar a aplicação.
Ou seja, as subclasses devem poder ser usadas no lugar de suas classes base
sem alterar o comportamento esperado.

================================================================================
"""

# ============================================================================
# EXEMPLO QUE NÃO RESPEITA O LSP
# ============================================================================
# 
# O código abaixo viola o LSP porque:
# - A classe Retangulo define que largura e altura podem ser alteradas
#   independentemente
# - A classe Quadrado herda de Retangulo, mas força largura == altura
# - Quando tentamos usar Quadrado no lugar de Retangulo, o comportamento
#   esperado é quebrado (ao setar largura, altura também muda)
#
# PROBLEMA: Código que funciona com Retangulo pode quebrar quando recebe
# um Quadrado, violando o princípio de substituição.
#
# ============================================================================

class Retangulo:
    def __init__(self, largura, altura):
        self._largura = largura
        self._altura = altura
    
    def set_largura(self, largura):
        """Define a largura do retângulo"""
        self._largura = largura
    
    def set_altura(self, altura):
        """Define a altura do retângulo"""
        self._altura = altura
    
    def get_largura(self):
        return self._largura
    
    def get_altura(self):
        return self._altura
    
    def calcular_area(self):
        """Calcula a área do retângulo"""
        return self._largura * self._altura


class Quadrado(Retangulo):
    """
    PROBLEMA: Quadrado herda de Retangulo, mas viola o contrato.
    Ao setar largura, também altera altura, quebrando o comportamento esperado.
    """
    def __init__(self, lado):
        super().__init__(lado, lado)
    
    def set_largura(self, largura):
        """Ao setar largura, também altera altura (viola LSP!)"""
        self._largura = largura
        self._altura = largura  # PROBLEMA: comportamento inesperado!
    
    def set_altura(self, altura):
        """Ao setar altura, também altera largura (viola LSP!)"""
        self._largura = altura  # PROBLEMA: comportamento inesperado!
        self._altura = altura


# Exemplo que demonstra o problema:
# def dobrar_tamanho(retangulo: Retangulo):
#     """Função que espera um Retangulo e dobra seu tamanho"""
#     retangulo.set_largura(retangulo.get_largura() * 2)
#     retangulo.set_altura(retangulo.get_altura() * 2)
#     return retangulo.calcular_area()
# 
# # Funciona corretamente com Retangulo:
# r = Retangulo(5, 4)
# area = dobrar_tamanho(r)  # Esperado: 80 (10 * 8)
# 
# # Mas quebra com Quadrado (viola LSP):
# q = Quadrado(5)
# area = dobrar_tamanho(q)  # Resultado incorreto! (10 * 10 = 100, mas deveria ser 80)


# ============================================================================
# ORIENTAÇÕES PARA CORREÇÃO
# ============================================================================
#
# SUA TAREFA:
# Refatore o código acima aplicando o Princípio de Substituição de Liskov.
#
# PASSO A PASSO:
# 1. Crie uma classe abstrata FormaGeometrica (usando ABC) que define
#    o método calcular_area() como abstrato.
#
# 2. Faça Retangulo e Quadrado herdarem diretamente de FormaGeometrica,
#    não um do outro.
#
# 3. Cada classe deve implementar calcular_area() de forma independente.
#
# 4. Se necessário, crie métodos específicos para cada forma (ex: metodo set_lado
#    para Quadrado, metodo set_largura_e_altura para Retangulo).
#
# 5. Agora, qualquer função que receba FormaGeometrica pode trabalhar
#    tanto com Retangulo quanto com Quadrado sem problemas!
#
# DICA: Use o módulo abc do Python para criar classes abstratas.
#
# ============================================================================
# ÁREA PARA SUA IMPLEMENTAÇÃO
# ============================================================================

# TODO: Implemente aqui sua solução aplicando o LSP
# 
# Exemplo de uso esperado:
# from abc import ABC, abstractmethod
# 
# # Criar classe abstrata FormaGeometrica
# # Fazer Retangulo herdar de FormaGeometrica
# # Fazer Quadrado herdar de FormaGeometrica (não de Retangulo!)
# 
def dobrar_tamanho(forma: FormaGeometrica):
#     # Esta função deve funcionar com qualquer FormaGeometrica
#     # sem precisar saber se é Retangulo ou Quadrado
     pass
# 
# r = Retangulo(5, 4)
# q = Quadrado(5)
# 
# # Ambos devem funcionar corretamente:
# area_r = dobrar_tamanho(r)
# area_q = dobrar_tamanho(q)

