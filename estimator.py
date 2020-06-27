import pandas as pd
import numpy as np


def calc_despacho_estimate(data):
    desp_data = data[data['Status'] == "Despacho"].copy()
    desp_data = desp_data.sort_values('Despacho de Aprovação sab/dom')
    desp_data = desp_data.dropna(subset=["Despacho de Aprovação sab/dom"])
    desp_data = desp_data.reset_index(drop=True)
    desp_data = desp_data[desp_data['Exig & Urg'] != "exi"]
    
    diff_days_mask = (desp_data['Despacho de Aprovação sab/dom'] - desp_data['Dt. Recepção (pelo-AR) sab/dom'])
    desp_data['diff_days'] = diff_days_mask.dt.days
    
    # removing outlines...
    desp_data = desp_data[np.abs(desp_data['diff_days'] - desp_data['diff_days'].rolling(20).mean()) <= (2*desp_data['diff_days'].std())]
    
    desp_data = desp_data.reset_index(drop=True)
    
    
    # calculing ewma mean...
    desp_data['ewma_mean_diff_days'] = desp_data['diff_days'].ewm(span=20, min_periods=0,
                                                                  adjust=False, ignore_na=False).mean()
    
    
    return desp_data