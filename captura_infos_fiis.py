from pathlib import Path
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import pandas as pd
import numpy as np

ROOT_FOLDER = Path(__file__).parent
CHROMEDRIVER_EXEC = ROOT_FOLDER / '/drivers/chromedriver.exe'

chrome_options = ''
chrome_service = ''
chrome_browser = ''



driver = webdriver.Chrome()

#fundos tijolo
'''Observar sempre a atualização dos códigos dos ativos'''
fundos = ['XPIN11','XPLG11','XPPR11','RECT11','XPML11','BPML11','BTLG11','ALZR11','TRXF11','HSLG11','VISC11','VILG11', \
          'VINO11','HGLG11','HGPO11','HGRE11','HGRU11','CTXT11','RBVA11','RBED11','KNRI11','VTLT11', \
            'CBOP11','BRCO11','GGRC11','HSML11','HGBS11','NEWL11','QAGR11','OULG11'] #antigo

# fundos = ['XPML11', 'HGLG11', 'KNRI11', 'BTLG11', 'VISC11', 'XPLG11', 'TRXF11', 'PVBI11', 'HGBS11', 'BRCR11', 'HSML11', 'ALZR11', 
#             'GGRC11', 'RBVA11', 'GARE11', 'RBRP11', 'PATC11', 'PATL11', 'RBRL11', 'TEPP11', 'FVPQ11', 'LVBI11', 'HGRE11', 'RBRF11', 
#             'JSRE11', 'BCFF11', 'HFOF11', 'XPPR11', 'VILG11', 'RECR11', 'BTCR11', 'BARI11', 'MORE11', 'SNCI11', 'BLMG11', 'FAMB11', 
#             'FATN11', 'FEXC11', 'FVPQ11', 'FUND11', 'HGPO11', 'HGRU11', 'HTMX11', 'IRDM11', 'JSRE11', 'MALL11', 'MATV11', 'MGCR11', 
#             'MGLG11', 'MORC11', 'PATC11', 'PATL11', 'PLCR11', 'RBRP11', 'RBRR11', 'RBRY11', 'RECT11', 'RECR11', 'RZTR11', 'SADI11', 
#             'SDIL11', 'SNCI11', 'SPVJ11', 'TEPP11', 'TRXF11', 'VILG11', 'VISC11', 'XPML11', 'XPLG11', 'XPPR11']
# cabecalho = ['Codigo', 'Adm', 'Segmento', 'Ultimo Rendimento', 'Valor Patrimonial da Cota', 'Cotação', 'P/VPC', 'Vacancia(%)']
cabecalho = ['Codigo', 'Adm', 'Segmento', 'Ultimo Rendimento', 'Valor Patrimonial da Cota', 'Cotação', 'P/VPC'] #igual o de cima só que retirado vacancia pois deu erro
adm_list = []
segmento_list = []
ult_rend_list = []
vlr_patr_list = []
cotacao_list = []
dy_list = []
pvpc_list = []
# vacancia_list = [] #retirado a vacancia pois deu erro

for fundo in fundos:
    driver.get("https://fiis.com.br/" + fundo)
    time.sleep(2)
    adm = driver.find_element(By.XPATH, "//*[@id='carbon_fields_fiis_informations-2']/div[1]/div[1]/p").text
    segmento = driver.find_element(By.XPATH, "//*[@id='carbon_fields_fiis_informations-2']/div[3]/p[7]/b").text
    ult_rend = driver.find_element(By.XPATH, "//*[@id='carbon_fields_fiis_header-2']/div/div/div[1]/div[2]/div/div[2]/p[1]/b").text
    vlr_patr = driver.find_element(By.XPATH, "//*[@id='carbon_fields_fiis_quotations_chart-2']/div[2]/div[3]/p[1]/b").text
    cotacao = driver.find_element(By.XPATH, "//*[@id='carbon_fields_fiis_quotations_chart-2']/div[1]/div[2]/div[1]/div[1]/span[2]").text
    pvpc = driver.find_element(By.XPATH, "//*[@id='carbon_fields_fiis_header-2']/div/div/div[1]/div[2]/div/div[4]/p[1]/b").text
    
    adm_list.append(adm)
    segmento_list.append(segmento)
    ult_rend_list.append(ult_rend)
    vlr_patr_list.append(vlr_patr)
    cotacao_list.append(cotacao)
    pvpc_list.append(pvpc)

    time.sleep(1)

import undetected_chromedriver as uc
options = webdriver.ChromeOptions() 
options.add_argument("start-maximized")
driver = uc.Chrome(options=options)

# for fundo in fundos: #retirado a vacancia pois deu erro
#     driver.get("https://www.clubefii.com.br/fiis/" + fundo)
#     time.sleep(3)
#     vacancia = driver.find_element(By.CSS_SELECTOR, "#vacancia > div.info > div:nth-child(1) > strong:nth-child(3)").text
#     vacancia_list.append(vacancia)

# zipped = list(zip(fundos, adm_list, segmento_list, ult_rend_list, vlr_patr_list, cotacao_list, pvpc_list, vacancia_list))
zipped = list(zip(fundos, adm_list, segmento_list, ult_rend_list, vlr_patr_list, cotacao_list, pvpc_list)) #igual o de cima só que retirado vacancia pois deu erro
df = pd.DataFrame(zipped, columns = cabecalho)

# Transformando em float
df['Ultimo Rendimento'] = df['Ultimo Rendimento'].apply(lambda x: float(x.split()[0].replace(',', '.')))
df['Valor Patrimonial da Cota'] = df['Valor Patrimonial da Cota'].apply(lambda x: float(x.split()[0].replace(',', '.')))
df['Cotação'] = df['Cotação'].apply(lambda x: float(x.split()[0].replace(',', '.')))
df['DY do Período(%)'] = round((df['Ultimo Rendimento'] / df['Cotação']) * 100, 2)
df['P/VPC'] = df['P/VPC'].apply(lambda x: float(x.split()[0].replace(',', '.')))
# df['Vacancia(%)'] = df['Vacancia(%)'].apply(lambda x: float(x.split()[0].replace('%', '').replace(',', '.'))) #retirado a vacancia pois deu erro

#Reorganiza o cabeçalho
# df = df[['Codigo', 'Adm', 'Segmento', 'Ultimo Rendimento', 'Valor Patrimonial da Cota', 'Cotação', 'DY do Período(%)', 'P/VPC', 'Vacancia(%)']]
df = df[['Codigo', 'Adm', 'Segmento', 'Ultimo Rendimento', 'Valor Patrimonial da Cota', 'Cotação', 'DY do Período(%)', 'P/VPC']] #igual o de cima só que retirado vacancia pois deu erro
print(df)

#altera o estilo
def formata_dy(val):
    if val < 0.5:
        color = '#c44764'
    else:
        color = '#4b9e2f'
    return 'background-color: %s' % color

def formata_pvpc(val):
    if val > 1.3:
        color = '#c44764'
    else:
        color = '#4b9e2f'
    return 'background-color: %s' % color

def formata_vacancia(val):
    if val > 10:
        color = '#c44764'
    else:
        color = '#4b9e2f'
    return 'background-color: %s' % color


# df = df.style.applymap(formata_dy, subset=['DY do Período(%)'])\
#         .applymap(formata_pvpc, subset=['P/VPC'])\
#         .applymap(formata_vacancia, subset=['Vacancia(%)'])

df = df.style.applymap(formata_dy, subset=['DY do Período(%)'])\
        .applymap(formata_pvpc, subset=['P/VPC']) #igual o de cima só que retirado vacancia pois deu erro

df.to_excel('C:/Users/dagos/OneDrive/Área de Trabalho/fundo_tijolo.xlsx', sheet_name = 'Fundos_tijolo', index = False)


#fundos de papel
'''Observar sempre a atualização dos códigos dos ativos'''

fundos_papel = ['TORD11','HCTR11','DEVA11','SARE11','BCRI11','IRDM11','URPR11',\
          'RECR11','GCFF11','BARI11','FEXC11','BTCR11','BCFF11','CPFF11','CPTS11','RBRR11',\
            'VRTA11','HGFF11','XPCI11','BCIA11','XPSF11','KNIP11','RBHY11','CVBI11','RVBI11','TGAR11',\
            'KNCR11','KNHY11','HGCR11','MXRF11'] #antigo
# fundos_papel = ['KNCR11', 'VRTA11', 'HCRI11', 'CPTS11', 'MXRF11', 'RBRR11', 'DEVA11', 'OUJP11', 'BCRI11', 
#                 'KNSC11', 'VGIR11', 'RZAK11', 'IRDM11', 'RECR11', 'BTCR11', 'BARI11', 'MORE11', 'SNCI11', 
#                 'BLMG11', 'FAMB11', 'FATN11', 'FEXC11', 'FUND11', 'MATV11', 'MGCR11', 'MGLG11', 'MORC11', 
#                 'PLCR11', 'RBRY11', 'RECT11', 'RZTR11', 'SADI11', 'SDIL11', 'SPVJ11']
cabecalho = ['Codigo', 'Adm', 'Segmento', 'Ultimo Rendimento', 'Valor Patrimonial da Cota', 'Cotação', 'P/VPC']
adm_list_papel = []
segmento_list_papel = []
ult_rend_list_papel = []
vlr_patr_list_papel = []
cotacao_list_papel = []
dy_list_papel = []
pvpc_list_papel = []

for fundo in fundos_papel:
    driver.get("https://fiis.com.br/" + fundo)
    time.sleep(2)
    adm = driver.find_element(By.XPATH, "//*[@id='carbon_fields_fiis_informations-2']/div[1]/div[1]/p").text
    segmento = driver.find_element(By.XPATH, "//*[@id='carbon_fields_fiis_informations-2']/div[3]/p[7]/b").text
    ult_rend = driver.find_element(By.XPATH, "//*[@id='carbon_fields_fiis_header-2']/div/div/div[1]/div[2]/div/div[2]/p[1]/b").text
    vlr_patr = driver.find_element(By.XPATH, "//*[@id='carbon_fields_fiis_quotations_chart-2']/div[2]/div[3]/p[1]/b").text
    cotacao = driver.find_element(By.XPATH, "//*[@id='carbon_fields_fiis_quotations_chart-2']/div[1]/div[2]/div[1]/div[1]/span[2]").text
    pvpc = driver.find_element(By.XPATH, "//*[@id='carbon_fields_fiis_header-2']/div/div/div[1]/div[2]/div/div[4]/p[1]/b").text
    
    adm_list_papel.append(adm)
    segmento_list_papel.append(segmento)
    ult_rend_list_papel.append(ult_rend)
    vlr_patr_list_papel.append(vlr_patr)
    cotacao_list_papel.append(cotacao)
    pvpc_list_papel.append(pvpc)

    time.sleep(1)



zipped = list(zip(fundos_papel, adm_list_papel, segmento_list_papel, ult_rend_list_papel, vlr_patr_list_papel, cotacao_list_papel, pvpc_list_papel))
df2 = pd.DataFrame(zipped, columns = cabecalho)

# Transformando em float
df2['Ultimo Rendimento'] = df2['Ultimo Rendimento'].apply(lambda x: float(x.split()[0].replace(',', '.')))
df2['Valor Patrimonial da Cota'] = df2['Valor Patrimonial da Cota'].apply(lambda x: float(x.split()[0].replace(',', '.')))
df2['Cotação'] = df2['Cotação'].apply(lambda x: float(x.split()[0].replace(',', '.')))
df2['DY do Período(%)'] = round((df2['Ultimo Rendimento'] / df2['Cotação']) * 100, 2)
df2['P/VPC'] = df2['P/VPC'].apply(lambda x: float(x.split()[0].replace(',', '.')))

#Reorganiza o cabeçalho
df2 = df2[['Codigo', 'Adm', 'Segmento', 'Ultimo Rendimento', 'Valor Patrimonial da Cota', 'Cotação', 'DY do Período(%)', 'P/VPC']]
print(df2)
#altera o estilo
def formata_dy(val):
    if val < 0.5:
        color = '#c44764'
    else:
        color = '#4b9e2f'
    return 'background-color: %s' % color

def formata_pvpc(val):
    if val > 1.3:
        color = '#c44764'
    else:
        color = '#4b9e2f'
    return 'background-color: %s' % color


df2 = df2.style.applymap(formata_dy, subset=['DY do Período(%)'])\
        .applymap(formata_pvpc, subset=['P/VPC'])


df2.to_excel('C:/Users/dagos/OneDrive/Área de Trabalho/fundo_papel.xlsx', sheet_name = 'Fundos_papel', index = False)

driver.close()




