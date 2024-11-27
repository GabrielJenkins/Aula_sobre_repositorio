from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoAlertPresentException
import time 

@given(u'entro na página de contato do Instituto Joga Junto')
def step_impl(context):
    context.browser.get("https://www.jogajuntoinstituto.org/#Contato")
    time.sleep(5)  # Aguarda o carregamento da página


@when(u'insiro meus dados no formulário')
def step_impl(context):
    # Preenche os campos do formulário
    context.browser.find_element(By.ID, "nome").send_keys("Gabriel Souza")
    context.browser.find_element(By.ID, "email").send_keys("gabrielQA@hotmail.com")
    context.browser.find_element(By.ID, "assunto").send_keys("Ser facilitador")
    context.browser.find_element(By.ID, "mensagem").send_keys("Olá da turma de QA Avançado, Ilhabela Novembro 2024")
    time.sleep(2)  # Aguarda para simular o preenchimento


@when(u'envio a mensagem "Olá da turma de QA Avançado, Ilhabela Novembro 2024"')
def step_impl(context):
    # Envia o formulário
    enviar_button = context.browser.find_element(By.XPATH, "//button[@type='submit']/p[contains(text(), 'Enviar')]")
    context.browser.execute_script("arguments[0].click();", enviar_button)
    time.sleep(5)  # Aguarda a resposta do envio

    # Trata o alerta de sucesso (se existir)
    try:
        alert = context.browser.switch_to.alert
        print(f"Alerta detectado: {alert.text}")
        alert.accept()  # Fecha o alerta
    except NoAlertPresentException:
        print("Nenhum alerta foi encontrado.")


@then(u'fecho o navegador')
def step_impl(context):
    context.browser.quit()