"""
================================================================================
SIMULADO P2 - PROGRAMAÇÃO ORIENTADA A OBJETOS
Professor: Tiago Castro
Turma: 4º Período B - Engenharia de Software
================================================================================

PRINCÍPIO: DEPENDENCY INVERSION PRINCIPLE (DIP)
VALOR: 3,0 pontos

O Princípio de Inversão de Dependência estabelece que:
1. Módulos de alto nível não devem depender de módulos de baixo nível.
   Ambos devem depender de abstrações.
2. Abstrações não devem depender de detalhes. Detalhes devem depender
   de abstrações.

================================================================================
"""

# ============================================================================
# EXEMPLO QUE NÃO RESPEITA O DIP
# ============================================================================
# 
# O código abaixo viola o DIP porque:
# - A classe NotificacaoService (alto nível) depende diretamente de
#   EmailService e SMSService (baixo nível/concretas)
# - Se quisermos adicionar um novo tipo de notificação (ex: WhatsApp),
#   precisamos MODIFICAR NotificacaoService
# - NotificacaoService está acoplado a implementações concretas, não a abstrações
#
# PROBLEMA: Alto acoplamento, difícil de testar, difícil de estender.
#
# ============================================================================

class EmailService:
    """Serviço concreto para envio de emails"""
    def enviar_email(self, destinatario, mensagem):
        print(f"Enviando email para {destinatario}: {mensagem}")
        # Código real de envio de email aqui


class SMSService:
    """Serviço concreto para envio de SMS"""
    def enviar_sms(self, numero, mensagem):
        print(f"Enviando SMS para {numero}: {mensagem}")
        # Código real de envio de SMS aqui


class NotificacaoService:
    """
    PROBLEMA: Esta classe depende diretamente de classes concretas
    (EmailService e SMSService), violando o DIP.
    
    Se quisermos adicionar WhatsApp, Push Notification, etc,
    precisamos MODIFICAR esta classe!
    """
    def __init__(self):
        # PROBLEMA: Dependência direta de classes concretas
        self.email_service = EmailService()
        self.sms_service = SMSService()
    
    def notificar_por_email(self, destinatario, mensagem):
        """Notifica por email"""
        self.email_service.enviar_email(destinatario, mensagem)
    
    def notificar_por_sms(self, numero, mensagem):
        """Notifica por SMS"""
        self.sms_service.enviar_sms(numero, mensagem)
    
    def notificar_todos(self, email, telefone, mensagem):
        """Notifica por todos os canais"""
        self.notificar_por_email(email, mensagem)
        self.notificar_por_sms(telefone, mensagem)


# Exemplo de uso (problema):
# notificacao = NotificacaoService()
# notificacao.notificar_por_email("user@email.com", "Olá!")
# notificacao.notificar_por_sms("123456789", "Olá!")


# ============================================================================
# ORIENTAÇÕES PARA CORREÇÃO
# ============================================================================
#
# SUA TAREFA:
# Refatore o código acima aplicando o Princípio de Inversão de Dependência.
#
# PASSO A PASSO:
# 1. Crie uma interface/abstração (usando ABC) chamada Notificador ou
#    CanalNotificacao que define o método enviar() ou notificar().
#
# 2. Faça EmailService e SMSService implementarem essa interface.
#    Cada um deve ter seu próprio método de envio, mas seguindo o contrato.
#
# 3. Modifique NotificacaoService para:
#    - Receber uma lista de notificadores (ou um único notificador) via
#      construtor (INJEÇÃO DE DEPENDÊNCIA)
#    - Depender da abstração (interface), não das implementações concretas
#
# 4. Agora, para adicionar um novo canal (ex: WhatsAppService), você só precisa:
#    - Criar a classe WhatsAppService implementando a interface
#    - Passar uma instância para NotificacaoService
#    - SEM MODIFICAR NotificacaoService!
#
# 5. Isso também facilita testes: você pode criar um MockNotificador
#    para testar NotificacaoService sem depender de serviços reais.
#
# DICA: Use injeção de dependência no construtor de NotificacaoService.
#
# ============================================================================
# ÁREA PARA SUA IMPLEMENTAÇÃO
# ============================================================================

# TODO: Implemente aqui sua solução aplicando o DIP
# 
# Exemplo de uso esperado:
# from abc import ABC, abstractmethod
# 
# # Criar interface Notificador
# # Fazer EmailService implementar Notificador
# # Fazer SMSService implementar Notificador
# # Modificar NotificacaoService para receber notificadores via construtor
# 
# # Uso com injeção de dependência:
# email_service = EmailService()
# sms_service = SMSService()
# 
# notificacao = NotificacaoService([email_service, sms_service])
# notificacao.notificar("user@email.com", "123456789", "Mensagem importante")
# 
# # Para adicionar novo canal, apenas criar e injetar:
# # whatsapp_service = WhatsAppService()
# # notificacao2 = NotificacaoService([email_service, sms_service, whatsapp_service])

