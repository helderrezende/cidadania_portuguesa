import pandas as pd

PATH_EXCEL = "data/Arquivo Central.xlsx"
PATH_EXCEL_MANUAL = "data/Cidadania_manual.xlsx"

def get_acp_data():
    COLUMNS_EXCEL = ['numero_processo', 'year', 
                     'Dt. Recepção (pelo-AR) sab/dom',
                     'Despacho de Aprovação sab/dom',
                     'Data de Conclusão (Assento) sab/dom',
                     'Status', 'Exig & Urg']
    
    acp_excel = pd.read_excel(PATH_EXCEL)
    manual_excel = pd.read_excel(PATH_EXCEL_MANUAL)

    acp_excel = pd.concat([acp_excel, manual_excel], sort=False)
    acp_excel = acp_excel.dropna(subset=["Número do processo"])
    acp_excel['numero_processo'], acp_excel['year'] = acp_excel["Número do processo"].str.split("/").str
    
    acp_excel = acp_excel[COLUMNS_EXCEL].copy()
    
    acp_excel = acp_excel.dropna(subset=['year'])
    
    
    return acp_excel