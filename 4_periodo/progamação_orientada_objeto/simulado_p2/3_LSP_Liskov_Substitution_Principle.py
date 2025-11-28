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

from abc import ABC, abstractmethod

class FormaGeometrica(ABC):

    @abstractmethod
    def calcula_areas(self):
        pass

class Retangulo(FormaGeometrica):

    def __init__(self, largura, altura):
        self._largura = largura
        self._altura = altura
    
    def set_largura(self, largura):
        self._largura = largura
    
    def set_altura(self, altura):
        self._altura = altura
    

    def set_largura_e_altura(self, largura, altura):
        self._largura = largura
        self._altura = altura
        self._altura = altura
    
    def get_largura(self):
        return self._largura
    
    def get_altura(self):
        return self._altura
    
    def calcular_area(self):
        return self._largura * self._altura

class Quadrado(FormaGeometrica):
    
    def __init__(self, lado):
        self._lado = lado
        
    def set_lado(self, lado):
        self._lado = lado
    
    def get_lado(self):
        return self._lado
    
    def calcular_area(self):
        return self._lado * self._lado

# Exemplo de uso esperado:
# from abc import ABC, abstractmethod
# 
# # Criar classe abstrata FormaGeometrica
# # Fazer Retangulo herdar de FormaGeometrica
# # Fazer Quadrado herdar de FormaGeometrica (não de Retangulo!)
# 
def dobrar_tamanho(forma: FormaGeometrica):
    """
    Esta função funciona com QUALQUER FormaGeometrica.
    Não precisa saber se é Retangulo ou Quadrado!
    """
    area_original = forma.calcular_area()
    
    # Para Retangulo, dobra largura e altura separadamente
    if isinstance(forma, Retangulo):
        forma.set_largura(forma.get_largura() * 2)
        forma.set_altura(forma.get_altura() * 2)
    # Para Quadrado, dobra o lado
    elif isinstance(forma, Quadrado):
        forma.set_lado(forma.get_lado() * 2)
    
    area_nova = forma.calcular_area()
    return area_nova
    area_nova = forma.calcular_area()
    return area_nova

def calcular_area_total(formas: list[FormaGeometrica]):
    """
    Outro exemplo: função que calcula área total de várias formas.
    Funciona com qualquer combinação de FormaGeometrica!
    """
    total = 0
    for forma in formas:
        total += forma.calcular_area()
    return total


# ============================================================================
# TESTES
# ============================================================================

if __name__ == "__main__":
    # Teste com Retangulo
    r = Retangulo(5, 4)
    print(f"Retangulo original: {r.get_largura()}x{r.get_altura()} = área {r.calcular_area()}")
    area_dobrada = dobrar_tamanho(r)
    print(f"Retangulo dobrado: {r.get_largura()}x{r.get_altura()} = área {area_dobrada}")
    print(f"Esperado: 80 (10 * 8)\n")
    
    # Teste com Quadrado
    q = Quadrado(5)
    print(f"Quadrado original: lado {q.get_lado()} = área {q.calcular_area()}")
    area_dobrada = dobrar_tamanho(q)
    print(f"Quadrado dobrado: lado {q.get_lado()} = área {area_dobrada}")
    print(f"Esperado: 100 (10 * 10)\n")
    
    # Teste com lista mista (polimorfismo)
    formas = [
        Retangulo(3, 4),
        Quadrado(5),
        Retangulo(2, 6)
    ]
    area_total = calcular_area_total(formas)
    print(f"Área total de {len(formas)} formas: {area_total}")
    print(f"Esperado: 12 + 25 + 12 = 49")


