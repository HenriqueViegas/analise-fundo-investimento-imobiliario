import os
import glob
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd


'''Apagar arquivos na pasta download'''

caminho_da_pasta = os.path.join(os.getcwd(), 'downloads')

# Percorre os itens dentro do diretório downloads
for item in os.listdir(caminho_da_pasta):
    caminho_completo_arquivo = os.path.join(caminho_da_pasta, item)
    if os.path.isfile(caminho_completo_arquivo) and (item.endswith('.xls') or item.endswith('.xlsx') or item.endswith('.csv')):
        try:
            os.remove(caminho_completo_arquivo)
            print(f'*** Arquivo {item} removido com sucesso ***')
        except OSError as e:
            print(f'*** Erro ao apagar o arquivo {item}: {e.strerror} ***')


'''Configuração do chromedriver'''

# Pasta onde os downloads são salvos
diretorio_downloads = os.path.join(os.getcwd(), "downloads")
if not os.path.exists(diretorio_downloads):
    os.makedirs(diretorio_downloads)

chrome_options = webdriver.ChromeOptions()
prefs = {"download.default_directory": diretorio_downloads}
chrome_options.add_experimental_option("prefs", prefs)


''''Inicia o driver - status invest'''
# chrome_options.add_argument("--headless")  # Roda sem abrir a janela (mais rápido)
# chrome_options.add_argument("--no-sandbox")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
wait = WebDriverWait(driver, 15)

try:
    url = 'https://statusinvest.com.br/fundos-imobiliarios/busca-avancada'
    driver.get(url)

    # Clicar no botão "BUSCAR" - Utilizado XPath
    btn_buscar = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="main-2"]/div[3]/div/div/div/button[2]')))
    btn_buscar.click()
    print("*** Busca realizada... ***")

    # Clicar no botão "DOWNLOAD" - Utilizado XPath
    btn_download = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="main-2"]/div[4]/div/div[1]/div[2]/a')))
    btn_download.click()
    print(f"*** Download iniciado! O arquivo será salvo em: {caminho_da_pasta} ***")

    # Pequena espera apenas para garantir que o download comece antes de fechar
    import time
    time.sleep(3)

finally:
    driver.quit()


''''Leitura e tratamento do arquivo baixado'''
arquivo_csv = glob.glob(os.path.join(caminho_da_pasta, '*.csv'))

if not arquivo_csv:
  print('*** Nenhum arquivo encontrado na pasta ***')
else:
  if len(arquivo_csv) > 1:
          print(f"*** Atenção: há {len(arquivo_csv)} arquivos CSV na pasta. Usando o primeiro encontrado. ***")

  arquivo_csv = arquivo_csv[0]
  print(f"*** Tentando ler o arquivo: {arquivo_csv} ***")

  try:
      df = pd.read_csv(arquivo_csv, sep=";", encoding="cp1252")
      print("*** Arquivo lido com sucesso! ***")
      
      
      df = df[['TICKER', 'PRECO', 'ULTIMO DIVIDENDO', 'DY', 'VALOR PATRIMONIAL COTA', 'P/VP', 'PATRIMONIO', 'PERCENTUAL EM CAIXA', 'N COTISTAS']]

  except Exception as e:
      print(f"*** Erro ao ler o arquivo {arquivo_csv}: {e} ***")



'''Captura infos do site de FIIS - complemento de informações com CNPJ, Segmento e administrador'''
''''Inicia o driver'''

chrome_options.add_argument("--headless")  # Roda sem abrir a janela (mais rápido)
chrome_options.add_argument("--no-sandbox")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
wait = WebDriverWait(driver, 5)


'''Captura os dados principais dos FIIs'''
dados_finais = []

try:
    print("Acessando a lista de fundos...")
    url_base = 'https://fiis.com.br/'
    driver.get(url_base + 'lista-de-fundos-imobiliarios/')

    # Exemplo com os 5 primeiros para teste
    for fundo in df['TICKER']:
        try:
            print(f"Coletando: {fundo}...")
            if "Página não encontrada" in driver.page_source:
                print(f"Página inválida para {fundo}")
                continue

            driver.get(url_base + fundo.lower() + '/')
            cnpj = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="carbon_fields_fiis_informations-2"]/div[3]/p[1]/b'))).text
            segmento = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="carbon_fields_fiis_informations-2"]/div[3]/p[7]/b'))).text 
            adm = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'informations__adm__name'))).text
            dados_finais.append({
                'TICKER': fundo,
                'SEGMENTO': segmento,
                'CNPJ': cnpj,
                'ADMINISTRADOR': adm
            })    

        except Exception as e:
            print(f"Erro ao processar {fundo}: {e}")
            continue  
finally:
    driver.quit()   
df_complementar = pd.DataFrame(dados_finais)

df_final = pd.merge(df, df_complementar, on="TICKER")
df_final.to_excel(caminho_da_pasta + '_analise_completa_fii.xlsx', index=False)

'''Conversão e limpeza de dados'''
df_final = df_final[~df_final["N COTISTAS"].isnull()]

# Corrige separadores de milhar e decimal
colunas_float = ["PRECO", "ULTIMO DIVIDENDO", "DY", "VALOR PATRIMONIAL COTA", "P/VP", "PATRIMONIO", "PERCENTUAL EM CAIXA"]

df_final[colunas_float] = (
    df_final[colunas_float].replace(r"\.", "", regex=True).replace(r",", ".", regex=True)  .astype(float)
)

df_final["N COTISTAS"] = (
    df_final["N COTISTAS"].replace(r"\.", "", regex=True).replace(r",", ".", regex=True).astype(float).astype(int)
)

# Seleciona os fundos de acordo com os critérios bases
# DY do período > 0,005 e P/VPC < 1,3
df_final = df_final[(df_final["PRECO"] != 0) & (df_final["PATRIMONIO"] != 0)]
df_final = df_final[(df_final["ULTIMO DIVIDENDO"] / df_final["VALOR PATRIMONIAL COTA"] > 0.005) & (df_final["P/VP"] < 1.3)]
df_final["DY DO PERIODO"] = df_final["ULTIMO DIVIDENDO"] / df_final["VALOR PATRIMONIAL COTA"] #Cria coluna para demonstrar o valor do DY do período

'''ordenação de coluna e linhas'''
ordem = ["TICKER", "CNPJ", "DY DO PERIODO", "P/VP", "PRECO", "ULTIMO DIVIDENDO", "DY", "VALOR PATRIMONIAL COTA", "PATRIMONIO", "PERCENTUAL EM CAIXA", "N COTISTAS", "SEGMENTO", "ADMINISTRADOR"]
df_final = df_final[ordem]

df_final = df_final.sort_values(by=["DY DO PERIODO", "P/VP"], ascending=[False, True])

df_final.to_excel(caminho_da_pasta + '_filtro_fundos_elegiveis.xlsx', index=False)

# aprimorar o merge
# identificar quais fundos possuem os melhores parâmetros