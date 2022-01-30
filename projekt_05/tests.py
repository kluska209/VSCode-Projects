import numpy as np
from bokeh.models import ColumnDataSource, DataTable, TableColumn, HTMLTemplateFormatter, Div
from openpyxl.workbook import Workbook
from openpyxl import load_workbook
import os
from collections import defaultdict
from bokeh.plotting import figure
from bokeh.palettes import all_palettes
import transmittance

def calculate_ratio(data1, data2):

    trans1 = data1['trans_avg']
    trans2 = data2['trans_avg']
    results = []

    for i in range(4):
        results.append(trans1[i]/trans2[i])

    return {'mm': data1['mm'], 'ratio': results}

print(calculate_ratio(transmittance.avg_castrol_trans['niebieska'], transmittance.avg_castrol_trans['czerwona']))
