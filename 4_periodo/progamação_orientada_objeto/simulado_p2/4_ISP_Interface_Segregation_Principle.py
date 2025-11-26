"""
================================================================================
SIMULADO P2 - PROGRAMAÇÃO ORIENTADA A OBJETOS
Professor: Tiago Castro
Turma: 4º Período B - Engenharia de Software
================================================================================

PRINCÍPIO: INTERFACE SEGREGATION PRINCIPLE (ISP)
VALOR: 2,0 pontos

O Princípio de Segregação de Interface estabelece que os clientes não devem
ser forçados a depender de interfaces que não utilizam. É melhor ter várias
interfaces específicas do que uma interface geral "gorda".

================================================================================
"""

# ============================================================================
# EXEMPLO QUE NÃO RESPEITA O ISP
# ============================================================================
# 
# A interface Trabalhador abaixo viola o ISP porque:
# - Força todas as classes que a implementam a ter métodos que podem não
#   fazer sentido para elas
# - Um Humano precisa trabalhar, comer e dormir (faz sentido)
# - Um Robo precisa trabalhar, mas não precisa comer nem dormir
#   (mas é forçado a implementar esses métodos!)
#
# PROBLEMA: Classes são forçadas a implementar métodos que não fazem sentido
# para elas, resultando em implementações vazias ou que lançam exceções.
#
# ============================================================================

from abc import ABC, abstractmethod

class Trabalhador(ABC):
    """
    PROBLEMA: Interface "gorda" que força implementação de métodos
    que podem não fazer sentido para todas as classes.
    """
    @abstractmethod
    def trabalhar(self):
        """Método que faz sentido para todos"""
        pass
    
    @abstractmethod
    def comer(self):
        """Método que NÃO faz sentido para Robo!"""
        pass
    
    @abstractmethod
    def dormir(self):
        """Método que NÃO faz sentido para Robo!"""
        pass


class Humano(Trabalhador):
    """Humano implementa todos os métodos (faz sentido)"""
    def trabalhar(self):
        return "Humano trabalhando..."
    
    def comer(self):
        return "Humano comendo..."
    
    def dormir(self):
        return "Humano dormindo..."


class Robo(Trabalhador):
    """
    PROBLEMA: Robo é forçado a implementar comer() e dormir()
    mesmo que não faça sentido! Isso viola o ISP.
    """
    def trabalhar(self):
        return "Robo trabalhando..."
    
    def comer(self):
        # PROBLEMA: Robo não come! Implementação vazia ou exceção
        raise NotImplementedError("Robos não comem!")
    
    def dormir(self):
        # PROBLEMA: Robo não dorme! Implementação vazia ou exceção
        raise NotImplementedError("Robos não dormem!")


# ============================================================================
# ORIENTAÇÕES PARA CORREÇÃO
# ============================================================================
#
# SUA TAREFA:
# Refatore o código acima aplicando o Princípio de Segregação de Interface.
#
# PASSO A PASSO:
# 1. Quebre a interface Trabalhador em interfaces menores e mais específicas:
#    - Trabalhador (apenas com trabalhar())
#    - SerVivo (com comer() e dormir())
#    - Ou outras interfaces específicas conforme necessário
#
# 2. Faça Humano implementar Trabalhador E SerVivo (ou interfaces equivalentes)
#    já que humanos trabalham, comem e dormem.
#
# 3. Faça Robo implementar APENAS Trabalhador, já que robos só trabalham.
#
# 4. Agora cada classe implementa apenas os métodos que realmente precisa,
#    sem ser forçada a implementar métodos que não fazem sentido.
#
# DICA: Em Python, uma classe pode implementar múltiplas interfaces/herdar
# de múltiplas classes abstratas.
#
# ============================================================================
# ÁREA PARA SUA IMPLEMENTAÇÃO
# ============================================================================

# TODO: Implemente aqui sua solução aplicando o ISP
# 
# Exemplo de uso esperado:
# from abc import ABC, abstractmethod
# 
# # Criar interfaces segregadas (ex: Trabalhador, SerVivo)
# # Humano implementa Trabalhador + SerVivo
# # Robo implementa apenas Trabalhador
# 
# humano = Humano()
# print(humano.trabalhar())  # OK
# print(humano.comer())      # OK
# print(humano.dormir())     # OK
# 
# robo = Robo()
# print(robo.trabalhar())    # OK
# # robo.comer()             # Não existe! (e não deveria existir)
# # robo.dormir()            # Não existe! (e não deveria existir)

