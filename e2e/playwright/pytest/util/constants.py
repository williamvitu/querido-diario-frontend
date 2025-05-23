
class Constants():

  URL_QD_CATARSE = "https://www.catarse.me/queridodiario-okbr"
  URL_QD_APOIE =  "https://ok.org.br/apoie/"
  URL_QD_ORG = "https://ok.org.br/"
  URL_QD_DOCUMENTACAO = "https://docs.queridodiario.ok.org.br/pt-br/latest/"
  URL_REPOSITORIOS_GITHUB = "https://github.com/orgs/okfn-brasil/repositories?q=querido-diario"
  URL_REPOSITORIO_RASPADORES = "https://github.com/okfn-brasil/querido-diario"
  URL_REPOSITORIO_PROCESSAMENTO_DADOS = "https://github.com/okfn-brasil/querido-diario-data-processing"
  URL_REPOSITORIO_FRONTEND= "https://github.com/okfn-brasil/querido-diario-frontend"
  URL_CONVITE_DISCORD="https://discord.com/invite/mxHGPq8rdY"
  URL_RELATORIO_TECNICO="https://querido-diario-static.nyc3.cdn.digitaloceanspaces.com/documents/reports/1o-relatorio-tecnico-atividades.pdf"

  TEXT_SETUP_MODULE = "[SETUP] Starting Setup for file:"
  TEXT_TEARDOWN_MODULE = "[SETUP] Starting Teardown for file:"
  TEXT_SETUP_SCENARIO = "[SETUP] Starting Setup for test function:"
  TEXT_TEARDOWN_SCENARIO = "[SETUP] Starting Teardown for test function:"

  CIDADES_POR_REGIAO = {
    "Norte": [
      "Jaru (RO)", "Manaus (AM)", "Boa Vista (RR)", "Belém (PA)", "Garrafão do Norte (PA)",
      "Santana do Araguaia (PA)", "Macapá (AP)", "Santana (AP)", "Tartarugalzinho (AP)",
      "Aguiarnópolis (TO)", "Aparecida do Rio Negro (TO)", "Araguaína (TO)",
      "Axixá do Tocantins (TO)", "Campos Lindos (TO)", "Caseara (TO)", "Centenário (TO)",
      "Divinópolis do Tocantins (TO)", "Goiatins (TO)", "Gurupi (TO)",
      "Lagoa da Confusão (TO)", "Lagoa do Tocantins (TO)", "Miracema do Tocantins (TO)",
      "Muricilândia (TO)", "Nazaré (TO)", "Peixe (TO)", "Ponte Alta do Tocantins (TO)",
      "Pugmil (TO)", "Recursolândia (TO)", "Sampaio (TO)", "Santa Fé do Araguaia (TO)",
      "Talismã (TO)", "Palmas (TO)", "Tocantínia (TO)", "Tocantinópolis (TO)", "Tupirama (TO)"
    ],
    "Nordeste": [
      "Afonso Cunha (MA)", "Aldeias Altas (MA)", "Anajatuba (MA)", "Axixá (MA)",
      "Bacabal (MA)", "Bacuri (MA)", "Boa Vista do Gurupi (MA)", "Bom Jardim (MA)"
    ],
    "Centro-Oeste": [
      "Bela Vista (MS)", "Campo Grande (MS)", "Corumbá (MS)", "Costa Rica (MS)",
      "Deodápolis (MS)", "Glória de Dourados (MS)", "Inocência (MS)", "Maracaju (MS)",
      "Paranhos (MS)", "Rio Brilhante (MS)", "Cotriguaçu (MT)", "Cuiabá (MT)", "Rondonópolis (MT)",
      "Aparecida de Goiânia (GO)", "Goiânia (GO)", "Brasília (DF)"
    ],
    "Sudeste": [
      "Belo Horizonte (MG)", "Betim (MG)", "Campo Belo (MG)", "Candeias (MG)",
      "Carmo da Cachoeira (MG)", "Carmo do Rio Claro (MG)", "Contagem (MG)"
    ],
    "Sul": [
      "Antônio Olinto (PR)", "Apucarana (PR)", "Cafelândia (PR)", "Cafezal do Sul (PR)",
      "Campo Largo (PR)", "Campo Mourão (PR)", "Carambeí (PR)", "Castro (PR)", "Corbélia (PR)"
    ]
    }

  ESTADOS_POR_REGIAO = {
    "Norte": [("Acre", "AC"), ("Amapá", "AP"), ("Amazonas", "AM"), ("Pará", "PA"), ("Rondônia", "RO"),
              ("Roraima", "RR"), ("Tocantins", "TO")],

    "Nordeste": [("Alagoas", "AL"), ("Bahia", "BA"), ("Ceará", "CE"), ("Maranhão", "MA"), ("Paraíba", "PB"),
                 ("Pernambuco", "PE"), ("Piauí", "PI"), ("Rio Grande do Norte", "RN"), ("Sergipe", "SE")],

    "Centro-Oeste": [("Goiás", "GO"), ("Mato Grosso", "MT"), ("Mato Grosso do Sul", "MS"), ("Distrito Federal", "DF")],

    "Sudeste": [("Espírito Santo", "ES"), ("Minas Gerais", "MG"), ("Rio de Janeiro", "RJ"), ("São Paulo", "SP")],

    "Sul": [("Paraná", "PR"), ("Rio Grande do Sul", "RS"), ("Santa Catarina", "SC")]
  }

