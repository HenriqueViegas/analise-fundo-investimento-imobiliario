from pathlib import Path
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import pandas as pd
import undetected_chromedriver as uc



ROOT_FOLDER = Path(__file__).parent
CHROMEDRIVER_EXEC = ROOT_FOLDER / '/drivers/chromedriver.exe'

# chrome_options = ''
# chrome_service = ''
# chrome_browser = ''
# driver = webdriver.Chrome()

options = webdriver.ChromeOptions() 
options.add_argument("start-maximized")
driver = uc.Chrome(options=options)

#fundos tijolo
# ticker = [
# 'MGLU3','HAPV3','B3SA3','BBDC4','COGN3','MRVE3','PETR4','PCAR3','IFCM3','EMBR3','SOMA3','ABEV3',
# 'PETZ3','ITUB4','RAIZ4','ENEV3','CPLE6','VALE3','OIBR3','AMER3','USIM5','GRND3','CVCB3','BRFS3',
# 'RENT3','ITSA4','CMIG4','LREN3','CPLE3','AZUL4','CIEL3','BBDC3','ANIM3','RADL3','BEEF3','PETR3',
# 'GGBR4','RAIL3','VBBR3','NTCO3','AURE3','ASAI3','SEQL3','CSAN3','BBAS3','CEAB3','CCRO3','VAMO3',
# 'BRAP4','CXSE3','RCSL4','CMIN3','GOAU4','GFSA3','TIMS3','SUZB3','HBSA3','UGPA3','RCSL3','IRBR3',
# 'LWSA3','MRFG3','CSNA3','EQTL3','WEGE3','SLCE3','BHIA3','QUAL3','ELET3','TRPL4','GMAT3','CRFB3',
# 'STBP3','GOLL4','CYRE3','PRIO3','JBSS3','POMO4','MULT3','BRKM5','ONCO3','RDOR3','TOTS3','SBSP3',
# 'EVEN3','ODPV3','BBSE3','SIMH3','TEND3','AZEV4','ARZZ3','ENAT3','VIVA3','MOVI3','CBAV3','JHSF3',
# 'VIVT3','MBLY3','HYPE3','YDUQ3','ALPA4','GUAR3','RRRP3','PSSA3','CSMG3','AERI3','DXCO3','GGPS3',
# 'BRSR6','PGMN3','SRNA3','SMTO3','LJQQ3','USIM3','FLRY3','VULC3','MTRE3','RANI3','ECOR3','TTEN3',
# 'CPFE3','EZTC3','INTB3','EGIE3','ALOS3','BPAN4','HBRE3','KLBN4','SBFG3','DIRR3','SMFT3','CURY3',
# 'NEOE3','RECV3','AESB3','MEAL3','MLAS3','KEPL3','VVEO3','CLSA3','FESA4','SAPR4','ELET6','LIGT3',
# 'ENJU3','CASH3','AMAR3','ZAMP3','MILS3','CSED3','PTBL3','RAPT4','PDGR3','POSI3','TRIS3','SOJA3',
# 'HBOR3','LAVV3','TRAD3','MDIA3','AGRO3','SHUL4','FIQE3','MYPK3','SEER3','PLPL3','BRIT3','ABCB4',
# 'ORVR3','AMBP3','LEVE3','MATD3','ESPA3','OPCT3','CAML3','NGRD3','ETER3','AZEV3','ITUB3','PINE4',
# 'BMGB4','VLID3','CMIG3','SYNE3','TUPY3','POMO3','KLBN3','LUPA3','KRSA3','JALL3','MDNE3','SGPS3',
# 'ARML3','JSLG3','RNEW4','TAEE4','AGXY3','TFCO4','PNVL3','WIZC3','BLAU3','PORT3','FRAS3','BMOB3',
# 'DASA3','SAPR3','LPSB3','PRNR3','TASA4','VITT3','UNIP6','ROMI3','ALPK3','LOGG3','PFRM3','PDTC3',
# 'UCAS3','DESK3','TGMA3','TECN3','TAEE3','AVLL3','VIVR3','RNEW3','MELK3','BMEB4','NINJ3','OIBR4',
# 'BRAP3','EUCA4','GGBR3','WEST3','DEXP3','DMVF3','SANB4','SANB3','TCSA3','INEP3','ITSA3','SHOW3',
# 'CAMB3','RDNI3','GOAU3','CSUD3','ELMD3','CTNM4','INEP4','AALR3','RSID3','TPIS3','BIOM3','CEBR5',
# 'WHRL4','ALUP4','HAGA4','PMAM3','FHER3','CTSA4','BEES3','IGTI3','IGTI3','CEBR6','SNSY5','ALLD3',
# 'LOGN3','BOBR4','LAND3','DOTZ3','COCE5','FRTA3','ENGI4','TASA3','BRKM3','ALUP3','WLMM4','LVTC3',
# 'CRIV4','BRSR3','UNIP3','PINE3','RPMG3','OSXB3','SCAR3','GEPA4','BPAC3','TELB4','BPAC5','EMAE4',
# 'EPAR3','ALPA3','BAHI3','NEXP3','CLSC4','ENGI3','BEES4','BAZA3','EQPA3','JFEN3','RAPT3','CEBR3',
# 'CTSA3','MTSA4','RPAD5','ATMP3','ATOM3','EUCA3','APER3','TEKA4','CRPG5','RPAD6','REDE3','PTNT3',
# 'PTNT4','HAGA3','DOHL4','CGRA4','NUTR3','CRPG6','TRPL3','OFSA3','BSLI3','MWET4','WHRL3','CEEB3',
# 'MGEL4','EALT4','MAPT4','VSTE3','BRIV3','EKTR4','NORD3','SNSY3','BGIP4','CPLE5','MNPR3','CTKA3',
# 'BALM4','CGAS5','FESA3','BRGE7','BRIV4','EALT3','HOOT4','CEDO4','BRGE3','AFLT3','GPAR3','HBTS5',
# 'CGRA3','DTCY3','FRIO3','BNBR3','RSUL4','MNDL3','BMEB3','BGIP3','BMIN4','BRGE5','DEXP4','MERC4',
# 'CLSC3','GEPA3','BSLI4','RPAD3','PLAS3','CRIV3','BMKS3','ESTR4','BRGE6','CTNM3','HETA4','TELB3',
# 'AHEB3','PEAB4','MRSA3B','ELET5','CGAS3','CSRN3','BALM3','IGTI4','IGTI4','BAUH4','MSPA3','MSPA4',
# 'CEDO3','MRSA6B','MRSA5B','LUXM4','TEKA3','BDLL4','MAPT3','PATI4','ENMT4','EQMA3B','BRKM6','CTKA4',
# 'EQPA5','PATI3','ENMT3','BRGE8','JOPA3','TKNO4','USIM6','JOPA4','MOAR3','BMIN3','COCE3','BRSR5','CBEE3',
# 'CEGR3','SOND5','UNIP5','CSRN6','ESTR3','WLMM3','LIPR3','CRPG3','PEAB3','DMFN3','EQPA6','GSHP3','EQPA7',
# 'CSRN5','EKTR3','AHEB5','CALI3','SOND6','CEEB5','DOHL3','CEED4','CEED3','BDLL3','FIEI3','CSAB3','CSAB4',
# 'MEGA3','SQIA3','ALSO3','BRPR3','MTSA3','SLED4','SLED3','AHEB6','VIIA3','MWET3','ENBR3','BOAS3','MODL3',
# 'MERC3','CRDE3','IGBR3','ODER4','PARD3','CASN3','WIZS3','LLIS3','BRML3','DMMO3','GETT3','GETT4','SULA4',
# 'SULA3','CEPE5','TCNO4','TCNO3','CEPE6','BKBR3','MTIG4','BLUT4','BLUT3','MODL4','CARD3','SHUL3','FIGE3',
# 'FNCN3','HETA3','LCAM3','BIDI4','BIDI3','EEEL4','EEEL3','BBRK3','SOND3','CESP6','CESP3','CESP5','ECPR4',
# 'MOSI3','POWE3','ECPR3','GNDI3','LAME4','LAME3','OMGE3','IGTA3','JPSA3','BRDT3','JBDU4','JBDU3','HGTX3',
# 'CCPR3','DTEX3','VVAR3','PNVL4','TESA3','BTOW3','LINX3','BTTL3','GPCP3','GPCP4','SMLS3','MMXM3','BSEV3',
# 'CNTO3','TIET4','TIET3','CORR4','CEPE3','CALI4','SNSY6','CASN4','EMAE3','BPAR3','APTI4','VSPT3','MTIG3',
# 'FIGE4','LUXM3','TKNO3','COCE6','MGEL3','CTSA8','MMAQ4'
# ]

tickers1 = ['BBAS3','BBDC3','ITUB3','ITSA3','SANB4','BPAC5','BPAN4','BMGB4','SQIA3','PETR3','PRIO3']
tickers2 = ['BRKM3','UGPA3','HYPE3','FLRY3','RADL3','PGMN3','HAPV3','ODPV3','QUAL3','OFSA3','PETZ3']
tickers3 = ['LREN3','EZTC3','CYRE3','MRVE3','GFSA3','TCSA3','JBSS3','MRFG3','BRFS3','MDIA3','ABEV3']
tickers4 = ['KLBN4','SUZB3','BBSE3','IRBR3','WIZS3','PSSA3','BRML3','MULT3','VALE3','GGBR4','USIM5']
tickers5 = ['GOAU4','WEGE3','CMIG3','ELET3','EGIE3','ENBR3','ENGI3','EQTL3','TAEE4','CPLE3','TRPL3']
tickers6 = ['MOVI3','CCRO3','ECOR3','RAIL3','SAPR3','SBSP3','VIVT3','TIMS3','SEER3','COGN3','ANIM3']
tickers7 = ['EMBR3','B3SA3','CSAN3','MGLU3','PCAR3','CSNA3','RENT3','CVCB3']
           
# tickers = ['EMBR3','SOMA3']
cabecalho = ['Codigo', 'Nome', 'Segmento', 'Setor', 'Lucro Líquido', 'Receita Líquida', 'Patrimônio Líquido', 'Dívida Líquida', 'Cotação', 'Proventos por Ação', 'Numero de Ações', 'Dividend Yield(%)']
nome_list = []
segmento_list = []
setor_list = []
lucro_liq_list = []
receita_liq_list = []
patrim_liq_list = []
divida_liq_list = []
cotacao_list = []
proventos_list = []
num_acao_list = []
dy_list = []


for ticker in tickers1:
    driver.get("https://statusinvest.com.br/acoes/" + ticker)
    time.sleep(2)
    driver.find_element(By.XPATH, "//*[@id='contabil-section']/div[1]/div/div[2]/div[2]/div[1]/button").click()
    time.sleep(30)
    nome = driver.find_element(By.XPATH, "//*[@id='company-section']/div[1]/div/div[1]/div[2]/h4/span").text
    segmento = driver.find_element(By.XPATH, "//*[@id='company-section']/div[1]/div/div[3]/div/div[3]/div/div/div/a/strong").text
    setor = driver.find_element(By.XPATH, "//*[@id='company-section']/div[1]/div/div[3]/div/div[1]/div/div/div/a/strong").text
    time.sleep(4)
    # receita_liq = driver.find_element(By.XPATH, "//*[@id='contabil-section']/div[1]/div/div[2]//following-sibling:div").text
    # receita_liq = driver.find_element(By.CSS_SELECTOR, ".table-info-body").above({By.CSS_SELECTOR: ".d-block"}).text
    # receita_liq = driver.find_element(By.XPATH, "//*[@id='contabil-section']/div/div[@class='table-info-body']/tbody/tr[1]/td[2]/span").text
    # receita_liq = driver.find_element(By.XPATH, "//*[@id='contabil-section']/div/div/div[2]/div/div/table/tbody/tr/td[2]").text
    receita_liq = driver.find_element(By.XPATH, "//*[@id='contabil-section']/div[1]/div/div[2]/div[1]/div/table/tbody/tr[1]/td[2]/span").text
    time.sleep(4)
    lucro_liq = driver.find_element(By.XPATH, "//*[@id='contabil-section']/div[1]/div/div[2]/div[1]/div[1]/table/tbody/tr[11]/td[2]/span").text
    patrim_liq = driver.find_element(By.XPATH, "//*[@id='company-section']/div[1]/div/div[2]/div[1]/div/div/strong").text
    divida_liq = driver.find_element(By.XPATH, "//*[@id='company-section']/div[1]/div/div[2]/div[6]/div/div/strong").text
    cotacao = driver.find_element(By.XPATH, "//*[@id='main-2']/div[2]/div/div[1]/div/div[1]/div/div[1]/strong").text
    proventos = driver.find_element(By.XPATH, "//*[@id='main-2']/div[2]/div/div[1]/div/div[4]/div/div[2]/div/span[2]").text
    num_acao = driver.find_element(By.XPATH, "//*[@id='company-section']/div[1]/div/div[2]/div[9]/div/div/strong").text
    dy = driver.find_element(By.XPATH, "//*[@id='main-2']/div[2]/div/div[1]/div/div[4]/div/div[1]/strong").text
    print(ticker)
    # receita_liq = float(receita_liq.replace('.', '').replace(',', '.').replace(' M', '')) * 1000000 if ' M' in receita_liq else receita_liq.replace('.', '').replace(',', '.').replace(' B', '') * 1000000000
    # lucro_liq = float(lucro_liq.replace('.', '').replace(',', '.').replace(' M', '')) * 1000000 if ' M' in lucro_liq else lucro_liq.replace('.', '').replace(',', '.').replace(' B', '') * 1000000000
    # print(lucro_liq)
    # divida_liq = 0 if divida_liq == '-' else float(divida_liq.replace('.', ''))
    # dy = 0 if dy == '-' else float(dy.replace(',', '.'))

    nome_list.append(nome)
    segmento_list.append(segmento)
    setor_list.append(setor)
    lucro_liq_list.append(lucro_liq)
    receita_liq_list.append(receita_liq)
    patrim_liq_list.append(patrim_liq)
    divida_liq_list.append(divida_liq)
    cotacao_list.append(cotacao)
    proventos_list.append(proventos)
    num_acao_list.append(num_acao)
    dy_list.append(dy)

    time.sleep(1)


zipped = list(zip(tickers, nome_list, segmento_list, setor_list, lucro_liq_list, receita_liq_list, patrim_liq_list, divida_liq_list, cotacao_list, proventos_list, num_acao_list, dy_list))
df1 = pd.DataFrame(zipped, columns = cabecalho)
df1 = df1[['Codigo', 'Nome', 'Segmento', 'Setor', 'Lucro Líquido', 'Receita Líquida', 'Patrimônio Líquido', 'Dívida Líquida', 'Cotação', 'Proventos por Ação', 'Numero de Ações', 'Dividend Yield(%)']]
print(df1)
df1.to_excel('C:/Users/dagos/OneDrive/Área de Trabalho/acoes.xlsx', sheet_name = 'acoes', index = False)
# Transformando em float

# df['Patrimônio Líquido'] = df['Patrimônio Líquido'].str.replace('.', '').astype(float)
# df['Cotação'] = df['Cotação'].str.replace(',', '.').astype(float)
# df['Proventos por Ação'] = df['Proventos por Ação'].str.replace('R$ ', '').str.replace(',', '.').astype(float)
# df['Numero de Ações'] = df['Numero de Ações'].str.replace('.', '').astype(float)

# #Criando colunas calculadas
# df['P/L'] = round(df['Cotação'] / ((df['Lucro Líquido'] / df['Numero de Ações'])), 2)
# df['P/VPA'] = round(df['Cotação'] / ((df['Patrimônio Líquido'] / df['Numero de Ações'])), 2)
# df['Margem Líquida(%)'] = round(df['Lucro Líquido'] / df['Receita Líquida'], 2) 
# df['ROE(%)'] = round(df['Lucro Líquido'] / df['Patrimônio Líquido'], 2)
# df['Div. Liq/ Patr.Liq(%)'] = round(df['Dívida Líquida'] / df['Patrimônio Líquido'], 2)



# #Reorganiza o cabeçalho
# df = df[['Codigo', 'Nome', 'Segmento', 'Setor', 'Lucro Líquido', 'Receita Líquida', 'Patrimônio Líquido', 'Dívida Líquida', 'Cotação', 'Proventos por Ação', 'Numero de Ações', 'P/L', 'P/VPA', 'Margem Líquida(%)', 'ROE(%)', 'Div. Liq/ Patr.Liq(%)', 'Dividend Yield(%)']]


# #altera o estilo
# def formata_pl(val):
#     if val > 15:
#         color = '#c44764'
#     else:
#         color = '#b1f571'
#     return 'background-color: %s' % color

# def formata_pvpa(val):
#     if val > 2:
#         color = '#c44764'
#     else:
#         color = '#b1f571'
#     return 'background-color: %s' % color

# def formata_margem(val):
#     if val < 0.1:
#         color = '#c44764'
#     else:
#         color = '#b1f571'
#     return 'background-color: %s' % color

# def formata_roe(val):
#     if val < 0.1:
#         color = '#c44764'
#     else:
#         color = '#b1f571'
#     return 'background-color: %s' % color

# def formata_div_liq(val):
#     if val > 0.7:
#         color = '#c44764'
#     else:
#         color = '#b1f571'
#     return 'background-color: %s' % color


# df = df.style.applymap(formata_pl, subset=['P/L'])\
#         .applymap(formata_pvpa, subset=['P/VPA'])\
#         .applymap(formata_margem, subset=['Margem Líquida(%)'])\
#         .applymap(formata_roe, subset=['ROE(%)'])\
#         .applymap(formata_div_liq, subset=['Div. Liq/ Patr.Liq(%)'])




driver.close()




