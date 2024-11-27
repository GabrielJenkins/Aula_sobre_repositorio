Feature: Formulário de Contato
  Para validar o formulário de contato do site do Instituto Joga Junto
  Como um usuário
  Quero acessar o formulário, aceitar os cookies, preencher meus dados e enviar uma mensagem com sucesso

  Scenario: Enviar mensagem
    Given entro na página de contato do Instituto Joga Junto
    When insiro meus dados no formulário
    And envio a mensagem "Olá da turma de QA Avançado, Ilhabela Novembro 2024"
    Then fecho o navegador