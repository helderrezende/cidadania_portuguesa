import pandas as pd
import requests
from bs4 import BeautifulSoup

def get_bs4_html(senha_acesso):
    payload = {'SenhaAcesso': senha_acesso}

    r = requests.post("https://nacionalidade.justica.gov.pt/Home/GetEstadoProcessoAjax", data=payload)
    soup = BeautifulSoup(r.text, 'html.parser')
    
    return soup

def get_info_processo(soup):
    info_dict = {}
    
    numero_processo = soup.find(id='bloc1').text
    
    get_status = soup.find('section', class_='step-indicator')
    last_status = get_status.find_all(class_='active1')[-1].find("div").text
    requerente = soup.find('div', attrs={'style': 'color:#335779; font-size:1.3em;'}).text
    local = soup.find('div', attrs={'style': 'font-weight: bold;'}).text
    
    info_dict['numero_processo'] = numero_processo
    info_dict['last_status'] = last_status
    info_dict['requerente'] = requerente
    info_dict['local'] = local
    
    return info_dict