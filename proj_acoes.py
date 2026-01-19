from pathlib import Path
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import pandas as pd
import undetected_chromedriver as uc



ROOT_FOLDER = Path(__file__).parent
CHROMEDRIVER_EXEC = ROOT_FOLDER / '/drivers/chromedriver.exe'

options = webdriver.ChromeOptions() 
options.add_argument("start-maximized")
driver = uc.Chrome(options=options)

# tickers1 = ['BBAS3','BBDC3','ITUB3','ITSA3','SANB4','BPAC5','BPAN4','BMGB4','SQIA3','PETR3','PRIO3']
# tickers2 = ['BRKM3','UGPA3','HYPE3','FLRY3','RADL3','PGMN3','HAPV3','ODPV3','QUAL3','OFSA3','PETZ3']
# tickers3 = ['LREN3','EZTC3','CYRE3','MRVE3','GFSA3','TCSA3','JBSS3','MRFG3','BRFS3','MDIA3','ABEV3']
tickers4 = ['KLBN4','SUZB3','BBSE3','IRBR3']
tickers45 = ['PSSA3','BRML3','MULT3','VALE3','GGBR4','USIM5']
tickers5 = ['GOAU4','WEGE3','CMIG3','ELET3','EGIE3','ENBR3','ENGI3','EQTL3','TAEE4','CPLE3','TRPL3']
tickers6 = ['MOVI3','CCRO3','ECOR3','RAIL3','SAPR3','SBSP3','VIVT3','TIMS3','SEER3','COGN3','ANIM3']
tickers7 = ['EMBR3','B3SA3','CSAN3','MGLU3','PCAR3','CSNA3','RENT3','CVCB3']
           
# # tickers = ['EMBR3','SOMA3']
cabecalho = ['Codigo', 'Nome', 'Segmento', 'Setor', 'Lucro Líquido', 'Receita Líquida', 'Patrimônio Líquido', 'Dívida Líquida', 'Cotação', 'Proventos por Ação', 'Numero de Ações', 'Dividend Yield(%)']
# nome_list = []
# segmento_list = []
# setor_list = []
# lucro_liq_list = []
# receita_liq_list = []
# patrim_liq_list = []
# divida_liq_list = []
# cotacao_list = []
# proventos_list = []
# num_acao_list = []
# dy_list = []

# #tickers1
# for ticker in tickers1:
#     driver.get("https://statusinvest.com.br/acoes/" + ticker)
#     time.sleep(2)
#     driver.find_element(By.XPATH, "//*[@id='contabil-section']/div[1]/div/div[2]/div[2]/div[1]/button").click()
#     time.sleep(30)
#     nome = driver.find_element(By.XPATH, "//*[@id='company-section']/div[1]/div/div[1]/div[2]/h4/span").text
#     segmento = driver.find_element(By.XPATH, "//*[@id='company-section']/div[1]/div/div[3]/div/div[3]/div/div/div/a/strong").text
#     setor = driver.find_element(By.XPATH, "//*[@id='company-section']/div[1]/div/div[3]/div/div[1]/div/div/div/a/strong").text
#     time.sleep(4)

#     receita_liq = driver.find_element(By.XPATH, "//*[@id='contabil-section']/div[1]/div/div[2]/div[1]/div/table/tbody/tr[1]/td[2]/span").text
#     time.sleep(4)
#     lucro_liq = driver.find_element(By.XPATH, "//*[@id='contabil-section']/div[1]/div/div[2]/div[1]/div[1]/table/tbody/tr[11]/td[2]/span").text
#     patrim_liq = driver.find_element(By.XPATH, "//*[@id='company-section']/div[1]/div/div[2]/div[1]/div/div/strong").text
#     divida_liq = driver.find_element(By.XPATH, "//*[@id='company-section']/div[1]/div/div[2]/div[6]/div/div/strong").text
#     cotacao = driver.find_element(By.XPATH, "//*[@id='main-2']/div[2]/div/div[1]/div/div[1]/div/div[1]/strong").text
#     proventos = driver.find_element(By.XPATH, "//*[@id='main-2']/div[2]/div/div[1]/div/div[4]/div/div[2]/div/span[2]").text
#     num_acao = driver.find_element(By.XPATH, "//*[@id='company-section']/div[1]/div/div[2]/div[9]/div/div/strong").text
#     dy = driver.find_element(By.XPATH, "//*[@id='main-2']/div[2]/div/div[1]/div/div[4]/div/div[1]/strong").text

#     nome_list.append(nome)
#     segmento_list.append(segmento)
#     setor_list.append(setor)
#     lucro_liq_list.append(lucro_liq)
#     receita_liq_list.append(receita_liq)
#     patrim_liq_list.append(patrim_liq)
#     divida_liq_list.append(divida_liq)
#     cotacao_list.append(cotacao)
#     proventos_list.append(proventos)
#     num_acao_list.append(num_acao)
#     dy_list.append(dy)

#     time.sleep(1)


# zipped = list(zip(tickers1, nome_list, segmento_list, setor_list, lucro_liq_list, receita_liq_list, patrim_liq_list, divida_liq_list, cotacao_list, proventos_list, num_acao_list, dy_list))
# df1 = pd.DataFrame(zipped, columns = cabecalho)
# df1 = df1[['Codigo', 'Nome', 'Segmento', 'Setor', 'Lucro Líquido', 'Receita Líquida', 'Patrimônio Líquido', 'Dívida Líquida', 'Cotação', 'Proventos por Ação', 'Numero de Ações', 'Dividend Yield(%)']]
# print(df1)
# df1.to_excel('C:/Users/dagos/OneDrive/Área de Trabalho/acoes1.xlsx', sheet_name = 'acoes', index = False)

# #tickers2
# nome_list = []
# segmento_list = []
# setor_list = []
# lucro_liq_list = []
# receita_liq_list = []
# patrim_liq_list = []
# divida_liq_list = []
# cotacao_list = []
# proventos_list = []
# num_acao_list = []
# dy_list = []
# for ticker in tickers2:
#     driver.get("https://statusinvest.com.br/acoes/" + ticker)
#     time.sleep(2)
#     driver.find_element(By.XPATH, "//*[@id='contabil-section']/div[1]/div/div[2]/div[2]/div[1]/button").click()
#     time.sleep(30)
#     nome = driver.find_element(By.XPATH, "//*[@id='company-section']/div[1]/div/div[1]/div[2]/h4/span").text
#     segmento = driver.find_element(By.XPATH, "//*[@id='company-section']/div[1]/div/div[3]/div/div[3]/div/div/div/a/strong").text
#     setor = driver.find_element(By.XPATH, "//*[@id='company-section']/div[1]/div/div[3]/div/div[1]/div/div/div/a/strong").text
#     time.sleep(4)

#     receita_liq = driver.find_element(By.XPATH, "//*[@id='contabil-section']/div[1]/div/div[2]/div[1]/div/table/tbody/tr[1]/td[2]/span").text
#     time.sleep(4)
#     lucro_liq = driver.find_element(By.XPATH, "//*[@id='contabil-section']/div[1]/div/div[2]/div[1]/div[1]/table/tbody/tr[11]/td[2]/span").text
#     patrim_liq = driver.find_element(By.XPATH, "//*[@id='company-section']/div[1]/div/div[2]/div[1]/div/div/strong").text
#     divida_liq = driver.find_element(By.XPATH, "//*[@id='company-section']/div[1]/div/div[2]/div[6]/div/div/strong").text
#     cotacao = driver.find_element(By.XPATH, "//*[@id='main-2']/div[2]/div/div[1]/div/div[1]/div/div[1]/strong").text
#     proventos = driver.find_element(By.XPATH, "//*[@id='main-2']/div[2]/div/div[1]/div/div[4]/div/div[2]/div/span[2]").text
#     num_acao = driver.find_element(By.XPATH, "//*[@id='company-section']/div[1]/div/div[2]/div[9]/div/div/strong").text
#     dy = driver.find_element(By.XPATH, "//*[@id='main-2']/div[2]/div/div[1]/div/div[4]/div/div[1]/strong").text

#     nome_list.append(nome)
#     segmento_list.append(segmento)
#     setor_list.append(setor)
#     lucro_liq_list.append(lucro_liq)
#     receita_liq_list.append(receita_liq)
#     patrim_liq_list.append(patrim_liq)
#     divida_liq_list.append(divida_liq)
#     cotacao_list.append(cotacao)
#     proventos_list.append(proventos)
#     num_acao_list.append(num_acao)
#     dy_list.append(dy)

#     time.sleep(1)

# zipped = list(zip(tickers2, nome_list, segmento_list, setor_list, lucro_liq_list, receita_liq_list, patrim_liq_list, divida_liq_list, cotacao_list, proventos_list, num_acao_list, dy_list))
# df2 = pd.DataFrame(zipped, columns = cabecalho)
# df2 = df2[['Codigo', 'Nome', 'Segmento', 'Setor', 'Lucro Líquido', 'Receita Líquida', 'Patrimônio Líquido', 'Dívida Líquida', 'Cotação', 'Proventos por Ação', 'Numero de Ações', 'Dividend Yield(%)']]
# print(df2)
# df2.to_excel('C:/Users/dagos/OneDrive/Área de Trabalho/acoes2.xlsx', sheet_name = 'acoes', index = False)

# #tickers3
# nome_list = []
# segmento_list = []
# setor_list = []
# lucro_liq_list = []
# receita_liq_list = []
# patrim_liq_list = []
# divida_liq_list = []
# cotacao_list = []
# proventos_list = []
# num_acao_list = []
# dy_list = []
# for ticker in tickers3:
#     driver.get("https://statusinvest.com.br/acoes/" + ticker)
#     time.sleep(2)
#     driver.find_element(By.XPATH, "//*[@id='contabil-section']/div[1]/div/div[2]/div[2]/div[1]/button").click()
#     time.sleep(30)
#     nome = driver.find_element(By.XPATH, "//*[@id='company-section']/div[1]/div/div[1]/div[2]/h4/span").text
#     segmento = driver.find_element(By.XPATH, "//*[@id='company-section']/div[1]/div/div[3]/div/div[3]/div/div/div/a/strong").text
#     setor = driver.find_element(By.XPATH, "//*[@id='company-section']/div[1]/div/div[3]/div/div[1]/div/div/div/a/strong").text
#     time.sleep(4)

#     receita_liq = driver.find_element(By.XPATH, "//*[@id='contabil-section']/div[1]/div/div[2]/div[1]/div/table/tbody/tr[1]/td[2]/span").text
#     time.sleep(4)
#     lucro_liq = driver.find_element(By.XPATH, "//*[@id='contabil-section']/div[1]/div/div[2]/div[1]/div[1]/table/tbody/tr[11]/td[2]/span").text
#     patrim_liq = driver.find_element(By.XPATH, "//*[@id='company-section']/div[1]/div/div[2]/div[1]/div/div/strong").text
#     divida_liq = driver.find_element(By.XPATH, "//*[@id='company-section']/div[1]/div/div[2]/div[6]/div/div/strong").text
#     cotacao = driver.find_element(By.XPATH, "//*[@id='main-2']/div[2]/div/div[1]/div/div[1]/div/div[1]/strong").text
#     proventos = driver.find_element(By.XPATH, "//*[@id='main-2']/div[2]/div/div[1]/div/div[4]/div/div[2]/div/span[2]").text
#     num_acao = driver.find_element(By.XPATH, "//*[@id='company-section']/div[1]/div/div[2]/div[9]/div/div/strong").text
#     dy = driver.find_element(By.XPATH, "//*[@id='main-2']/div[2]/div/div[1]/div/div[4]/div/div[1]/strong").text


#     nome_list.append(nome)
#     segmento_list.append(segmento)
#     setor_list.append(setor)
#     lucro_liq_list.append(lucro_liq)
#     receita_liq_list.append(receita_liq)
#     patrim_liq_list.append(patrim_liq)
#     divida_liq_list.append(divida_liq)
#     cotacao_list.append(cotacao)
#     proventos_list.append(proventos)
#     num_acao_list.append(num_acao)
#     dy_list.append(dy)

#     time.sleep(1)

# zipped = list(zip(tickers3, nome_list, segmento_list, setor_list, lucro_liq_list, receita_liq_list, patrim_liq_list, divida_liq_list, cotacao_list, proventos_list, num_acao_list, dy_list))
# df3 = pd.DataFrame(zipped, columns = cabecalho)
# df3 = df3[['Codigo', 'Nome', 'Segmento', 'Setor', 'Lucro Líquido', 'Receita Líquida', 'Patrimônio Líquido', 'Dívida Líquida', 'Cotação', 'Proventos por Ação', 'Numero de Ações', 'Dividend Yield(%)']]
# print(df3)
# df3.to_excel('C:/Users/dagos/OneDrive/Área de Trabalho/acoes3.xlsx', sheet_name = 'acoes', index = False)

# #tickers4
# nome_list = []
# segmento_list = []
# setor_list = []
# lucro_liq_list = []
# receita_liq_list = []
# patrim_liq_list = []
# divida_liq_list = []
# cotacao_list = []
# proventos_list = []
# num_acao_list = []
# dy_list = []
# for ticker in tickers4:
#     driver.get("https://statusinvest.com.br/acoes/" + ticker)
#     time.sleep(6)
#     driver.find_element(By.XPATH, "//*[@id='contabil-section']/div[1]/div/div[2]/div[2]/div[1]/button").click()
#     time.sleep(30)
#     nome = driver.find_element(By.XPATH, "//*[@id='company-section']/div[1]/div/div[1]/div[2]/h4/span").text
#     segmento = driver.find_element(By.XPATH, "//*[@id='company-section']/div[1]/div/div[3]/div/div[3]/div/div/div/a/strong").text
#     setor = driver.find_element(By.XPATH, "//*[@id='company-section']/div[1]/div/div[3]/div/div[1]/div/div/div/a/strong").text
#     time.sleep(4)

#     receita_liq = driver.find_element(By.XPATH, "//*[@id='contabil-section']/div[1]/div/div[2]/div[1]/div/table/tbody/tr[1]/td[2]/span").text
#     time.sleep(4)
#     lucro_liq = driver.find_element(By.XPATH, "//*[@id='contabil-section']/div[1]/div/div[2]/div[1]/div[1]/table/tbody/tr[11]/td[2]/span").text
#     patrim_liq = driver.find_element(By.XPATH, "//*[@id='company-section']/div[1]/div/div[2]/div[1]/div/div/strong").text
#     divida_liq = driver.find_element(By.XPATH, "//*[@id='company-section']/div[1]/div/div[2]/div[6]/div/div/strong").text
#     cotacao = driver.find_element(By.XPATH, "//*[@id='main-2']/div[2]/div/div[1]/div/div[1]/div/div[1]/strong").text
#     proventos = driver.find_element(By.XPATH, "//*[@id='main-2']/div[2]/div/div[1]/div/div[4]/div/div[2]/div/span[2]").text
#     num_acao = driver.find_element(By.XPATH, "//*[@id='company-section']/div[1]/div/div[2]/div[9]/div/div/strong").text
#     dy = driver.find_element(By.XPATH, "//*[@id='main-2']/div[2]/div/div[1]/div/div[4]/div/div[1]/strong").text
#     print(ticker)

#     nome_list.append(nome)
#     segmento_list.append(segmento)
#     setor_list.append(setor)
#     lucro_liq_list.append(lucro_liq)
#     receita_liq_list.append(receita_liq)
#     patrim_liq_list.append(patrim_liq)
#     divida_liq_list.append(divida_liq)
#     cotacao_list.append(cotacao)
#     proventos_list.append(proventos)
#     num_acao_list.append(num_acao)
#     dy_list.append(dy)

#     time.sleep(1)

# zipped = list(zip(tickers4, nome_list, segmento_list, setor_list, lucro_liq_list, receita_liq_list, patrim_liq_list, divida_liq_list, cotacao_list, proventos_list, num_acao_list, dy_list))
# df4 = pd.DataFrame(zipped, columns = cabecalho)
# df4 = df4[['Codigo', 'Nome', 'Segmento', 'Setor', 'Lucro Líquido', 'Receita Líquida', 'Patrimônio Líquido', 'Dívida Líquida', 'Cotação', 'Proventos por Ação', 'Numero de Ações', 'Dividend Yield(%)']]
# print(df4)
# df4.to_excel('C:/Users/dagos/OneDrive/Área de Trabalho/acoes4.xlsx', sheet_name = 'acoes', index = False)

# #tickers45
# nome_list = []
# segmento_list = []
# setor_list = []
# lucro_liq_list = []
# receita_liq_list = []
# patrim_liq_list = []
# divida_liq_list = []
# cotacao_list = []
# proventos_list = []
# num_acao_list = []
# dy_list = []
# for ticker in tickers45:
#     driver.get("https://statusinvest.com.br/acoes/" + ticker)
#     time.sleep(4)
#     driver.find_element(By.XPATH, "//*[@id='contabil-section']/div[1]/div/div[2]/div[2]/div[1]/button").click()
#     time.sleep(30)
#     nome = driver.find_element(By.XPATH, "//*[@id='company-section']/div[1]/div/div[1]/div[2]/h4/span").text
#     segmento = driver.find_element(By.XPATH, "//*[@id='company-section']/div[1]/div/div[3]/div/div[3]/div/div/div/a/strong").text
#     setor = driver.find_element(By.XPATH, "//*[@id='company-section']/div[1]/div/div[3]/div/div[1]/div/div/div/a/strong").text
#     time.sleep(4)

#     receita_liq = driver.find_element(By.XPATH, "//*[@id='contabil-section']/div[1]/div/div[2]/div[1]/div/table/tbody/tr[1]/td[2]/span").text
#     time.sleep(4)
#     lucro_liq = driver.find_element(By.XPATH, "//*[@id='contabil-section']/div[1]/div/div[2]/div[1]/div[1]/table/tbody/tr[11]/td[2]/span").text
#     patrim_liq = driver.find_element(By.XPATH, "//*[@id='company-section']/div[1]/div/div[2]/div[1]/div/div/strong").text
#     divida_liq = driver.find_element(By.XPATH, "//*[@id='company-section']/div[1]/div/div[2]/div[6]/div/div/strong").text
#     cotacao = driver.find_element(By.XPATH, "//*[@id='main-2']/div[2]/div/div[1]/div/div[1]/div/div[1]/strong").text
#     proventos = driver.find_element(By.XPATH, "//*[@id='main-2']/div[2]/div/div[1]/div/div[4]/div/div[2]/div/span[2]").text
#     num_acao = driver.find_element(By.XPATH, "//*[@id='company-section']/div[1]/div/div[2]/div[9]/div/div/strong").text
#     dy = driver.find_element(By.XPATH, "//*[@id='main-2']/div[2]/div/div[1]/div/div[4]/div/div[1]/strong").text


#     nome_list.append(nome)
#     segmento_list.append(segmento)
#     setor_list.append(setor)
#     lucro_liq_list.append(lucro_liq)
#     receita_liq_list.append(receita_liq)
#     patrim_liq_list.append(patrim_liq)
#     divida_liq_list.append(divida_liq)
#     cotacao_list.append(cotacao)
#     proventos_list.append(proventos)
#     num_acao_list.append(num_acao)
#     dy_list.append(dy)

#     time.sleep(1)

# zipped = list(zip(tickers45, nome_list, segmento_list, setor_list, lucro_liq_list, receita_liq_list, patrim_liq_list, divida_liq_list, cotacao_list, proventos_list, num_acao_list, dy_list))
# df45 = pd.DataFrame(zipped, columns = cabecalho)
# df45 = df45[['Codigo', 'Nome', 'Segmento', 'Setor', 'Lucro Líquido', 'Receita Líquida', 'Patrimônio Líquido', 'Dívida Líquida', 'Cotação', 'Proventos por Ação', 'Numero de Ações', 'Dividend Yield(%)']]
# print(df45)
# df45.to_excel('C:/Users/dagos/OneDrive/Área de Trabalho/acoes45.xlsx', sheet_name = 'acoes', index = False)


# #tickers5
# nome_list = []
# segmento_list = []
# setor_list = []
# lucro_liq_list = []
# receita_liq_list = []
# patrim_liq_list = []
# divida_liq_list = []
# cotacao_list = []
# proventos_list = []
# num_acao_list = []
# dy_list = []
# for ticker in tickers5:
#     driver.get("https://statusinvest.com.br/acoes/" + ticker)
#     time.sleep(2)
#     driver.find_element(By.XPATH, "//*[@id='contabil-section']/div[1]/div/div[2]/div[2]/div[1]/button").click()
#     time.sleep(30)
#     nome = driver.find_element(By.XPATH, "//*[@id='company-section']/div[1]/div/div[1]/div[2]/h4/span").text
#     segmento = driver.find_element(By.XPATH, "//*[@id='company-section']/div[1]/div/div[3]/div/div[3]/div/div/div/a/strong").text
#     setor = driver.find_element(By.XPATH, "//*[@id='company-section']/div[1]/div/div[3]/div/div[1]/div/div/div/a/strong").text
#     time.sleep(4)

#     receita_liq = driver.find_element(By.XPATH, "//*[@id='contabil-section']/div[1]/div/div[2]/div[1]/div/table/tbody/tr[1]/td[2]/span").text
#     time.sleep(4)
#     lucro_liq = driver.find_element(By.XPATH, "//*[@id='contabil-section']/div[1]/div/div[2]/div[1]/div[1]/table/tbody/tr[11]/td[2]/span").text
#     patrim_liq = driver.find_element(By.XPATH, "//*[@id='company-section']/div[1]/div/div[2]/div[1]/div/div/strong").text
#     divida_liq = driver.find_element(By.XPATH, "//*[@id='company-section']/div[1]/div/div[2]/div[6]/div/div/strong").text
#     cotacao = driver.find_element(By.XPATH, "//*[@id='main-2']/div[2]/div/div[1]/div/div[1]/div/div[1]/strong").text
#     proventos = driver.find_element(By.XPATH, "//*[@id='main-2']/div[2]/div/div[1]/div/div[4]/div/div[2]/div/span[2]").text
#     num_acao = driver.find_element(By.XPATH, "//*[@id='company-section']/div[1]/div/div[2]/div[9]/div/div/strong").text
#     dy = driver.find_element(By.XPATH, "//*[@id='main-2']/div[2]/div/div[1]/div/div[4]/div/div[1]/strong").text


#     nome_list.append(nome)
#     segmento_list.append(segmento)
#     setor_list.append(setor)
#     lucro_liq_list.append(lucro_liq)
#     receita_liq_list.append(receita_liq)
#     patrim_liq_list.append(patrim_liq)
#     divida_liq_list.append(divida_liq)
#     cotacao_list.append(cotacao)
#     proventos_list.append(proventos)
#     num_acao_list.append(num_acao)
#     dy_list.append(dy)

#     time.sleep(1)

# zipped = list(zip(tickers5, nome_list, segmento_list, setor_list, lucro_liq_list, receita_liq_list, patrim_liq_list, divida_liq_list, cotacao_list, proventos_list, num_acao_list, dy_list))
# df5 = pd.DataFrame(zipped, columns = cabecalho)
# df5 = df5[['Codigo', 'Nome', 'Segmento', 'Setor', 'Lucro Líquido', 'Receita Líquida', 'Patrimônio Líquido', 'Dívida Líquida', 'Cotação', 'Proventos por Ação', 'Numero de Ações', 'Dividend Yield(%)']]
# print(df5)
# df5.to_excel('C:/Users/dagos/OneDrive/Área de Trabalho/acoes5.xlsx', sheet_name = 'acoes', index = False)


# #tickers6
# nome_list = []
# segmento_list = []
# setor_list = []
# lucro_liq_list = []
# receita_liq_list = []
# patrim_liq_list = []
# divida_liq_list = []
# cotacao_list = []
# proventos_list = []
# num_acao_list = []
# dy_list = []
# for ticker in tickers6:
#     driver.get("https://statusinvest.com.br/acoes/" + ticker)
#     time.sleep(2)
#     driver.find_element(By.XPATH, "//*[@id='contabil-section']/div[1]/div/div[2]/div[2]/div[1]/button").click()
#     time.sleep(30)
#     nome = driver.find_element(By.XPATH, "//*[@id='company-section']/div[1]/div/div[1]/div[2]/h4/span").text
#     segmento = driver.find_element(By.XPATH, "//*[@id='company-section']/div[1]/div/div[3]/div/div[3]/div/div/div/a/strong").text
#     setor = driver.find_element(By.XPATH, "//*[@id='company-section']/div[1]/div/div[3]/div/div[1]/div/div/div/a/strong").text
#     time.sleep(4)

#     receita_liq = driver.find_element(By.XPATH, "//*[@id='contabil-section']/div[1]/div/div[2]/div[1]/div/table/tbody/tr[1]/td[2]/span").text
#     time.sleep(4)
#     lucro_liq = driver.find_element(By.XPATH, "//*[@id='contabil-section']/div[1]/div/div[2]/div[1]/div[1]/table/tbody/tr[11]/td[2]/span").text
#     patrim_liq = driver.find_element(By.XPATH, "//*[@id='company-section']/div[1]/div/div[2]/div[1]/div/div/strong").text
#     divida_liq = driver.find_element(By.XPATH, "//*[@id='company-section']/div[1]/div/div[2]/div[6]/div/div/strong").text
#     cotacao = driver.find_element(By.XPATH, "//*[@id='main-2']/div[2]/div/div[1]/div/div[1]/div/div[1]/strong").text
#     proventos = driver.find_element(By.XPATH, "//*[@id='main-2']/div[2]/div/div[1]/div/div[4]/div/div[2]/div/span[2]").text
#     num_acao = driver.find_element(By.XPATH, "//*[@id='company-section']/div[1]/div/div[2]/div[9]/div/div/strong").text
#     dy = driver.find_element(By.XPATH, "//*[@id='main-2']/div[2]/div/div[1]/div/div[4]/div/div[1]/strong").text


#     nome_list.append(nome)
#     segmento_list.append(segmento)
#     setor_list.append(setor)
#     lucro_liq_list.append(lucro_liq)
#     receita_liq_list.append(receita_liq)
#     patrim_liq_list.append(patrim_liq)
#     divida_liq_list.append(divida_liq)
#     cotacao_list.append(cotacao)
#     proventos_list.append(proventos)
#     num_acao_list.append(num_acao)
#     dy_list.append(dy)

#     time.sleep(1)

# zipped = list(zip(tickers6, nome_list, segmento_list, setor_list, lucro_liq_list, receita_liq_list, patrim_liq_list, divida_liq_list, cotacao_list, proventos_list, num_acao_list, dy_list))
# df6 = pd.DataFrame(zipped, columns = cabecalho)
# df6 = df6[['Codigo', 'Nome', 'Segmento', 'Setor', 'Lucro Líquido', 'Receita Líquida', 'Patrimônio Líquido', 'Dívida Líquida', 'Cotação', 'Proventos por Ação', 'Numero de Ações', 'Dividend Yield(%)']]
# print(df6)
# df6.to_excel('C:/Users/dagos/OneDrive/Área de Trabalho/acoes6.xlsx', sheet_name = 'acoes', index = False)


# #tickers7
# nome_list = []
# segmento_list = []
# setor_list = []
# lucro_liq_list = []
# receita_liq_list = []
# patrim_liq_list = []
# divida_liq_list = []
# cotacao_list = []
# proventos_list = []
# num_acao_list = []
# dy_list = []
# for ticker in tickers7:
#     driver.get("https://statusinvest.com.br/acoes/" + ticker)
#     time.sleep(2)
#     driver.find_element(By.XPATH, "//*[@id='contabil-section']/div[1]/div/div[2]/div[2]/div[1]/button").click()
#     time.sleep(30)
#     nome = driver.find_element(By.XPATH, "//*[@id='company-section']/div[1]/div/div[1]/div[2]/h4/span").text
#     segmento = driver.find_element(By.XPATH, "//*[@id='company-section']/div[1]/div/div[3]/div/div[3]/div/div/div/a/strong").text
#     setor = driver.find_element(By.XPATH, "//*[@id='company-section']/div[1]/div/div[3]/div/div[1]/div/div/div/a/strong").text
#     time.sleep(4)

#     receita_liq = driver.find_element(By.XPATH, "//*[@id='contabil-section']/div[1]/div/div[2]/div[1]/div/table/tbody/tr[1]/td[2]/span").text
#     time.sleep(4)
#     lucro_liq = driver.find_element(By.XPATH, "//*[@id='contabil-section']/div[1]/div/div[2]/div[1]/div[1]/table/tbody/tr[11]/td[2]/span").text
#     patrim_liq = driver.find_element(By.XPATH, "//*[@id='company-section']/div[1]/div/div[2]/div[1]/div/div/strong").text
#     divida_liq = driver.find_element(By.XPATH, "//*[@id='company-section']/div[1]/div/div[2]/div[6]/div/div/strong").text
#     cotacao = driver.find_element(By.XPATH, "//*[@id='main-2']/div[2]/div/div[1]/div/div[1]/div/div[1]/strong").text
#     proventos = driver.find_element(By.XPATH, "//*[@id='main-2']/div[2]/div/div[1]/div/div[4]/div/div[2]/div/span[2]").text
#     num_acao = driver.find_element(By.XPATH, "//*[@id='company-section']/div[1]/div/div[2]/div[9]/div/div/strong").text
#     dy = driver.find_element(By.XPATH, "//*[@id='main-2']/div[2]/div/div[1]/div/div[4]/div/div[1]/strong").text


#     nome_list.append(nome)
#     segmento_list.append(segmento)
#     setor_list.append(setor)
#     lucro_liq_list.append(lucro_liq)
#     receita_liq_list.append(receita_liq)
#     patrim_liq_list.append(patrim_liq)
#     divida_liq_list.append(divida_liq)
#     cotacao_list.append(cotacao)
#     proventos_list.append(proventos)
#     num_acao_list.append(num_acao)
#     dy_list.append(dy)

#     time.sleep(1)

# zipped = list(zip(tickers7, nome_list, segmento_list, setor_list, lucro_liq_list, receita_liq_list, patrim_liq_list, divida_liq_list, cotacao_list, proventos_list, num_acao_list, dy_list))
# df7 = pd.DataFrame(zipped, columns = cabecalho)
# df7 = df7[['Codigo', 'Nome', 'Segmento', 'Setor', 'Lucro Líquido', 'Receita Líquida', 'Patrimônio Líquido', 'Dívida Líquida', 'Cotação', 'Proventos por Ação', 'Numero de Ações', 'Dividend Yield(%)']]
# print(df7)
# df7.to_excel('C:/Users/dagos/OneDrive/Área de Trabalho/acoes7.xlsx', sheet_name = 'acoes', index = False)

# df_consol = pd.merge(df1, df2, df3, df4, df45, df5, df6, df7 how = 'outer')
df1 = pd.read_excel('C:/Users/dagos/OneDrive/Área de Trabalho/acoes1.xlsx')
df2 = pd.read_excel('C:/Users/dagos/OneDrive/Área de Trabalho/acoes2.xlsx')
df3 = pd.read_excel('C:/Users/dagos/OneDrive/Área de Trabalho/acoes3.xlsx')
df4 = pd.read_excel('C:/Users/dagos/OneDrive/Área de Trabalho/acoes4.xlsx')
df45 = pd.read_excel('C:/Users/dagos/OneDrive/Área de Trabalho/acoes45.xlsx')
df5 = pd.read_excel('C:/Users/dagos/OneDrive/Área de Trabalho/acoes5.xlsx')
df6 = pd.read_excel('C:/Users/dagos/OneDrive/Área de Trabalho/acoes6.xlsx')
df7 = pd.read_excel('C:/Users/dagos/OneDrive/Área de Trabalho/acoes7.xlsx')

df_consol = pd.concat([df1, df2, df3, df4, df45, df5, df6, df7])
df_consol.to_excel('C:/Users/dagos/OneDrive/Área de Trabalho/acoes_consol.xlsx', sheet_name = 'acoes', index = False)

# driver.close()