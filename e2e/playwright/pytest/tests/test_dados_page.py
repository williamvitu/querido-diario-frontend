import pytest
import random
import logging
from playwright.sync_api  import Page, expect, Browser
from  util.constants      import Constants as c
from  pages.page_dados    import DadosPage

"""
Este arquivo executa testes E2E
Testes são executados na Página -> https://queridodiario.ok.org.br/dados

"""
@pytest.fixture(scope="function")
def dados_page(browser_context) ->DadosPage:
  dados_page = DadosPage(browser_context)
  dados_page.page.goto("/dados")
  # dados_page.wait_main_fields()
  return dados_page

@pytest.fixture(scope="function", autouse=True)
def before_after_each(request):
  test_case_name = request.node.name
  logging.info(c.TEXT_SETUP_SCENARIO)

  yield
  logging.info(c.TEXT_TEARDOWN_SCENARIO)


@pytest.mark.pagina_dados
@pytest.mark.parametrize("regiao_brasil", ["Norte", "Nordeste","Sul", "Sudeste", "Centro-Oeste"] )
def test_buscar_diario_oficial_por_estado_regioes_brasil(dados_page: DadosPage, regiao_brasil):
  """
           Cenário de teste:
            Busca por dados de cada região do Brasil em uma seleção aleatória dos Estados do Brasil.

            Obs: Este cenário considera apenas estados que a ferramenta está apta
   """

  # Escolhe um estado aleatoriamente baseado na região do brasil em que o estado reside
  estado, acronimo_estado = random.choice(c.ESTADOS_POR_REGIAO[regiao_brasil])

  # Estado com o texto completo Ex: "São Paulo (SP)"
  estado_completo =  f"{estado} ({acronimo_estado})"

  # Preenche o campo "Estado"
  dados_page.fill_estado_input(estado)
  # Clica na opção do dropdown
  dados_page.click_on_estado_dropdown(estado_completo)
  # Clica no botao "Pesquisar"
  dados_page.click_on_pesquisar_button()

  resultado_busca = dados_page.page.get_by_test_id(dados_page.label_resultado_busca)
  expect(resultado_busca).to_be_visible()
  expect(resultado_busca).to_have_text(f"Diários Oficiais agregados de {acronimo_estado}")

@pytest.mark.pagina_dados
@pytest.mark.parametrize("municipio_estado", [("Paulínia","SP"), ("Campo Largo","PR"), ("Jaru","RO"), ("Afonso Cunha","MA"), ("Bela Vista", "MS")])
def test_buscar_diario_oficial_por_municipio(dados_page: DadosPage, municipio_estado):
  """
           Cenário de teste:
            Busca por dados de um município em um estado que reside em cada região do Brasil

            Obs: Por enquanto, este cenário está com os municípios hardcoded, a ideia é aumentar o escopo desse teste.
   """
  # Escolhe um estado aleatoriamente baseado na região do brasil em que o estado reside
  municipio, estado = municipio_estado

  municipio_estado_completo = f"{municipio} ({estado})"

  # Preenche o campo "Estado"
  dados_page.fill_municipio_input(municipio)
  # Clica na opção do dropdown
  dados_page.click_on_municipio_dropdown(municipio_estado_completo)
  # # Clica no botao "Pesquisar"
  dados_page.click_on_pesquisar_button()

  resultado_busca = dados_page.page.get_by_test_id(dados_page.label_resultado_busca)
  expect(resultado_busca).to_be_visible()
  expect(resultado_busca).to_have_text(f"Diários Oficiais agregados de {municipio_estado_completo}")


@pytest.mark.pagina_dados
def test_buscar_diario_oficial_inexistente(dados_page: DadosPage):
  """
           Cenário de teste:
            Este cenário busca por um estado que não existe, verificando se a mensagem de 'empty state' (Quando não há retorno da busca) está funcionando.

            Obs: Este cenário considera apenas estados que a ferramenta está apta
   """
  # Preenche o campo "Estado" com um texto de um estado que não existe
  dados_page.fill_estado_input("Testing")
  # Clica no botão "Pesquisar"
  dados_page.click_on_pesquisar_button()

  # Resultado esperado tela de "empty state"
  expect(dados_page.page.get_by_text("Sua pesquisa não encontrou nenhum conteúdo correspondente")).to_be_visible()


