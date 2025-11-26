"""
================================================================================
SIMULADO P2 - PROGRAMAÇÃO ORIENTADA A OBJETOS
Professor: Tiago Castro
Turma: 4º Período B - Engenharia de Software
================================================================================

PRINCÍPIO: SINGLE RESPONSIBILITY PRINCIPLE (SRP)
VALOR: 1,0 ponto

O Princípio da Responsabilidade Única estabelece que uma classe deve ter apenas
um motivo para mudar, ou seja, deve ter apenas uma responsabilidade.

================================================================================
"""

# ============================================================================
# EXEMPLO QUE NÃO RESPEITA O SRP
# ============================================================================
# 
# A classe abaixo viola o SRP porque possui múltiplas responsabilidades:
# 1. Gerenciar dados do pedido
# 2. Calcular totais
# 3. Salvar no banco de dados
# 4. Enviar email de confirmação
# 5. Gerar relatório
#
# PROBLEMA: Se precisarmos mudar a forma de envio de email, ou a forma de
# salvar no banco, ou a forma de gerar relatório, teremos que modificar
# a mesma classe, violando o SRP.
#
# ============================================================================

class Pedido:
    def __init__(self, numero, cliente, itens):
        self.numero = numero
        self.cliente = cliente
        self.itens = itens
    
    def calcular_total(self):
        """Calcula o total do pedido"""
        total = 0
        for item in self.itens:
            total += item['preco'] * item['quantidade']
        return total
    
    def salvar_no_banco(self):
        """Salva o pedido no banco de dados"""
        # Simulação de salvamento
        print(f"Salvando pedido {self.numero} no banco de dados...")
        # Código de conexão com banco seria aqui
    
    def enviar_email_confirmacao(self):
        """Envia email de confirmação para o cliente"""
        total = self.calcular_total()
        print(f"Enviando email para {self.cliente} confirmando pedido {self.numero} no valor de R$ {total:.2f}")
        # Código de envio de email seria aqui
    
    def gerar_relatorio(self):
        """Gera relatório do pedido"""
        print(f"Gerando relatório do pedido {self.numero}...")
        # Código de geração de relatório seria aqui



# ============================================================================
# ORIENTAÇÕES PARA CORREÇÃO
# ============================================================================
#
# SUA TAREFA:
# Refatore o código acima aplicando o Princípio da Responsabilidade Única.
#
# PASSO A PASSO:
# 1. Mantenha a classe Pedido apenas com responsabilidade de representar
#    os dados do pedido e calcular o total.
#
# 2. Crie uma classe separada para persistência (ex: PedidoRepository)
#    que será responsável apenas por salvar o pedido no banco.
#
# 3. Crie uma classe separada para comunicação (ex: EmailService)
#    que será responsável apenas por enviar emails.
#
# 4. Crie uma classe separada para relatórios (ex: RelatorioService)
#    que será responsável apenas por gerar relatórios.
#
# 5. Use composição ou injeção de dependência para conectar essas classes.
#
# ============================================================================
# ÁREA PARA SUA IMPLEMENTAÇÃO
# ============================================================================

# TODO: Implemente aqui a baixo a sua solução aplicando o SRP

class Pedido:
    def __init__(self, numero, cliente, itens):
        self.numero = numero
        self.cliente = cliente
        self.itens = itens
    
    def calcular_total(self):
        total = 0
        for item in self.itens:
            total += item['preco'] * item['quantidade']
        return total

class PedidoRepository():

    def salvar_no_banco(self, pedido: Pedido):
        print(f"Salvando pedido {pedido.numero} no banco de dados...")

class EmailService():
    
    def enviar_email_confirmacao(self, pedido: Pedido):
        total = pedido.calcular_total()  
        print(f"Enviando email para {pedido.cliente} confirmando pedido {pedido.numero} no valor de R$ {total:.2f}")  # Corrigir aqui

class RelatorioService():

     def gerar_relatorio(self, pedido: Pedido):
        print(f"Gerando relatório do pedido {pedido.numero}...")  # Corrigir aqui

pedido = Pedido(1, "joao@email.com", [{"preco": 10.0, "quantidade": 2}])
total = pedido.calcular_total()

repository = PedidoRepository()
repository.salvar_no_banco(pedido)

email_service = EmailService()
email_service.enviar_email_confirmacao(pedido)

relatorio_service = RelatorioService()
relatorio_service.gerar_relatorio(pedido)
