from openpyxl.workbook import Workbook
from openpyxl import load_workbook
import os
from bokeh.plotting import figure
from bokeh.palettes import all_palettes

def import_data(file_n, colx, coly, cell_n):
    wb = load_workbook(os.getcwd()+file_n)
    ws = wb.active

    range_x = ws[colx+'2':colx+'2049']
    x = []
    range_y = ws[coly+'2':coly+'2049']
    y = []

    for cell in range_x:
        for e in cell:
            x.append(e.value)

    if cell_n == None:
        for cell in range_y:
            for e in cell:
                y.append(e.value)
    else:
        for cell in range_y:
            for e in cell:
                y.append(e.value/ws[cell_n].value) #normalizuję dane

    data = {'x': x, 'y': y}
    return data

#pobieram dane o źródle światła białego
white_spectra = import_data('\\white_source.xlsx', 'A', 'B', 'B645')

#pobieram dane o diodach LED
red_spectrum = import_data('\\LED.xlsx', 'A', 'B', 'B876')
orange_spectrum = import_data('\\LED.xlsx', 'E', 'F', 'F746')
yellow_spectrum = import_data('\\LED.xlsx', 'I', 'J', 'J687')
green_spectrum = import_data('\\LED.xlsx', 'M', 'N', 'N637')
blue_spectrum = import_data('\\LED.xlsx', 'Q', 'R', 'R329')

#pobieram dane o olejach 
diesel_abs = import_data('\\diesel.xlsx', 'A', 'B', None)
engine_castrol_abs = import_data('\\engine_castrol.xlsx', 'A', 'B', None)
engine_abs = import_data('\\engine.xlsx', 'A', 'B', None)
machine_abs = import_data('\\machine.xlsx', 'A', 'B', None)
gear_abs = import_data('\\gear.xlsx', 'A', 'B', None)
olive_abs = import_data('\\olive.xlsx', 'A', 'B', None)
rapeseed_abs = import_data('\\rapeseed.xlsx', 'A', 'B', None)
sunflower_abs = import_data('\\sunflower.xlsx', 'A', 'B', None)

diesel_trans = import_data('\\diesel.xlsx', 'E', 'F', None)
engine_castrol_trans = import_data('\\engine_castrol.xlsx', 'E', 'F', None)
engine_trans = import_data('\\engine.xlsx', 'E', 'F', None)
machine_trans = import_data('\\machine.xlsx', 'E', 'F', None)
gear_trans = import_data('\\gear.xlsx', 'E', 'F', None)
olive_trans = import_data('\\olive.xlsx', 'E', 'F', None)
rapeseed_trans = import_data('\\rapeseed.xlsx', 'E', 'F', None)
sunflower_trans = import_data('\\sunflower.xlsx', 'E', 'F', None)

def set_fig_properties(fig):
    fig.background_fill_color = all_palettes['Greys'][9][7]
    fig.ygrid.grid_line_color = all_palettes['Greys'][9][6]
    fig.xgrid.grid_line_color = all_palettes['Greys'][9][6]
    fig.title.text_font_size = '16px'
    fig.title.text_font = 'Calibri Light'
    fig.yaxis.axis_label_text_font_size = '14px'
    fig.xaxis.axis_label_text_font_size = '14px'
    fig.yaxis.axis_label_text_font = 'Calibri Light'
    fig.xaxis.axis_label_text_font = 'Calibri Light'

#tworzę wykres źródła światła białego
fig_white = figure(x_range = (300,900), x_axis_label = 'Wavelength [nm]', y_axis_label = 'Light intensity [a.u.]',
             title = 'White light source spectrum', width = 900, height = 580)
set_fig_properties(fig_white)

white_line = fig_white.line('x', 'y', source = white_spectra, name = 'white_line', color = all_palettes['Dark2'][6][5])
white_patch = fig_white.patch('x', source = white_spectra, name = 'white_patch', color = all_palettes['Dark2'][6][5], alpha = 0.2)

#tworzę wykres diod LED
fig_LED = figure(x_range = (400,750), x_axis_label = 'Wavelength [nm]', y_axis_label = 'Light intensity [a.u.]',
             title = 'LED diodes\' spectra', width = 900, height = 580)
set_fig_properties(fig_LED)

red_line = fig_LED.line('x', 'y', source = red_spectrum, name = 'red_line', legend_label = 'RED', color = all_palettes['Spectral'][11][10])
red_patch = fig_LED.patch('x', source = red_spectrum, name = 'red_patch', legend_label = 'RED', color = all_palettes['Spectral'][11][10], alpha = 0.2)
orange_line = fig_LED.line('x', 'y', source = orange_spectrum, name = 'orange_line', legend_label = 'ORANGE', color = all_palettes['Set2'][6][1])
orange_patch = fig_LED.patch('x', source = orange_spectrum, name = 'orange_patch', legend_label = 'ORANGE', color = all_palettes['Set2'][6][1], alpha = 0.2)
yellow_line = fig_LED.line('x', 'y', source = yellow_spectrum, name = 'yellow_line', legend_label = 'YELLOW', color = all_palettes['Set2'][6][5])
yellow_patch = fig_LED.patch('x', source = yellow_spectrum, name = 'yellow_patch', legend_label = 'YELLOW', color = all_palettes['Set2'][6][5], alpha = 0.2)
green_line = fig_LED.line('x', 'y', source = green_spectrum, name = 'green_line', legend_label = 'GREEN', color = all_palettes['PuBuGn'][5][0])
green_patch = fig_LED.patch('x', source = green_spectrum, name = 'green_patch', legend_label = 'GREEN',color = all_palettes['PuBuGn'][5][0], alpha = 0.2)
blue_line = fig_LED.line('x', 'y', source = blue_spectrum, name = 'blue_line', legend_label = 'BLUE', color = all_palettes['Spectral'][11][1])
blue_patch = fig_LED.patch('x', source = blue_spectrum, name = 'blue_patch', legend_label = 'BLUE', color = all_palettes['Spectral'][11][1], alpha = 0.2)

fig_LED.legend.click_policy = "hide"

#tworzę wykres dla widm absorpcyjnych
fig_abs = figure(x_range = (400,800), x_axis_label = 'Wavelength [nm]', y_axis_label = 'Absorbance [OD]',
             title = 'Oil\'s absorption spectrum', width = 900, height = 296)
set_fig_properties(fig_abs)

diesel_abs_line = fig_abs.line('x', 'y', source = diesel_abs, name = 'diesel_abs_line', legend_label = 'DIESEL', color = all_palettes['Set2'][3][2])
engine_castrol_abs_line = fig_abs.line('x', 'y', source = engine_castrol_abs, name = 'engine_castrol_abs_line', legend_label = 'ENGINE_CASTROL', color = all_palettes['Set2'][3][1])
engine_abs_line = fig_abs.line('x', 'y', source = engine_abs, name = 'engine_abs_line', legend_label = 'ENGINE', color = all_palettes['Set2'][3][0])
machine_abs_line = fig_abs.line('x', 'y', source = machine_abs, name = 'machine_abs_line', legend_label = 'MACHINE', color = all_palettes['Set2'][4][3])
gear_abs_line = fig_abs.line('x', 'y', source = gear_abs, name = 'gear_abs_line', legend_label = 'GEAR', color = all_palettes['Set3'][12][3])
olive_abs_line = fig_abs.line('x', 'y', source = olive_abs, name = 'olive_abs_line', legend_label = 'OLIVE', color = all_palettes['Set3'][12][4])
rapeseed_abs_line = fig_abs.line('x', 'y', source = rapeseed_abs, name = 'rapeseed_abs_line', legend_label = 'RAPESEED', color = all_palettes['Set3'][12][0])
sunflower_abs_line = fig_abs.line('x', 'y', source = sunflower_abs, name = 'sunflower_abs_line', legend_label = 'SUNFLOWER', color = all_palettes['Set3'][12][7])

fig_abs.legend.visible = False 

#tworzę wykres dla widm transmisyjnych
fig_trans = figure(x_range = (400,800), y_range = (-10, 100), x_axis_label = 'Wavelength [nm]', y_axis_label = 'Transmitance [%]',
             title = 'Oil\'s transmission spectrum', width = 900, height = 296)
set_fig_properties(fig_trans)

diesel_trans_line = fig_trans.line('x', 'y', source = diesel_trans, name = 'diesel_trans_line', legend_label = 'DIESEL', color = all_palettes['Set2'][3][2])
engine_castrol_trans_line = fig_trans.line('x', 'y', source = engine_castrol_trans, name = 'engine_castrol_trans_line', legend_label = 'ENGINE_CASTROL', color = all_palettes['Set2'][3][1])
engine_trans_line = fig_trans.line('x', 'y', source = engine_trans, name = 'engine_trans_line', legend_label = 'ENGINE', color = all_palettes['Set2'][3][0])
machine_trans_line = fig_trans.line('x', 'y', source = machine_trans, name = 'machine_trans_line', legend_label = 'MACHINE', color = all_palettes['Set2'][4][3])
gear_trans_line = fig_trans.line('x', 'y', source = gear_trans, name = 'gear_trans_line', legend_label = 'GEAR', color = all_palettes['Set3'][12][3])
olive_trans_line = fig_trans.line('x', 'y', source = olive_trans, name = 'olive_trans_line', legend_label = 'OLIVE', color = all_palettes['Set3'][12][4])
rapeseed_trans_line = fig_trans.line('x', 'y', source = rapeseed_trans, name = 'rapeseed_trans_line', legend_label = 'RAPESEED', color = all_palettes['Set3'][12][0])
sunflower_trans_line = fig_trans.line('x', 'y', source = sunflower_trans, name = 'sunflower_trans_line', legend_label = 'SUNFLOWER', color = all_palettes['Set3'][12][7])

fig_trans.legend.visible = False 

#tworzę wykres do matchowania
fig_match = figure(x_range = (300,1050), x_axis_label = 'Wavelength [nm]', y_axis_label = 'Light intensity [a.u.]',
             title = 'Selected spectra', width = 900, height = 580)
set_fig_properties(fig_match)

m_red_line = fig_match.line('x', 'y', source = red_spectrum, name = 'red_line', legend_label = 'RED', color = all_palettes['Spectral'][11][10])
m_orange_line = fig_match.line('x', 'y', source = orange_spectrum, name = 'orange_line', legend_label = 'ORANGE', color = all_palettes['Set2'][6][1])
m_yellow_line = fig_match.line('x', 'y', source = yellow_spectrum, name = 'yellow_line', legend_label = 'YELLOW', color = all_palettes['Set2'][6][5])
m_green_line = fig_match.line('x', 'y', source = green_spectrum, name = 'green_line', legend_label = 'GREEN', color = all_palettes['PuBuGn'][5][0])
m_blue_line = fig_match.line('x', 'y', source = blue_spectrum, name = 'blue_line', legend_label = 'BLUE', color = all_palettes['Spectral'][11][1])

m_diesel_abs_line = fig_match.line('x', 'y', source = diesel_abs, name = 'diesel_abs_line', legend_label = 'DIESEL', color = all_palettes['Set2'][3][2])
m_engine_castrol_abs_line = fig_match.line('x', 'y', source = engine_castrol_abs, name = 'engine_castrol_abs_line', legend_label = 'ENGINE_CASTROL', color = all_palettes['Set2'][3][1])
m_engine_abs_line = fig_match.line('x', 'y', source = engine_abs, name = 'engine_abs_line', legend_label = 'ENGINE', color = all_palettes['Set2'][3][0])
m_machine_abs_line = fig_match.line('x', 'y', source = machine_abs, name = 'machine_abs_line', legend_label = 'MACHINE', color = all_palettes['Set2'][4][3])
m_gear_abs_line = fig_match.line('x', 'y', source = gear_abs, name = 'gear_abs_line', legend_label = 'GEAR', color = all_palettes['Set3'][12][3])
m_olive_abs_line = fig_match.line('x', 'y', source = olive_abs, name = 'olive_abs_line', legend_label = 'OLIVE', color = all_palettes['Set3'][12][4])
m_rapeseed_abs_line = fig_match.line('x', 'y', source = rapeseed_abs, name = 'rapeseed_abs_line', legend_label = 'RAPESEED', color = all_palettes['Set3'][12][0])
m_sunflower_abs_line = fig_match.line('x', 'y', source = sunflower_abs, name = 'sunflower_abs_line', legend_label = 'SUNFLOWER', color = all_palettes['Set3'][12][7])

fig_match.legend.visible = False 

#defaultowe ustawienie widoczności wykresów olejów na false
for line_name in [diesel_abs_line, engine_castrol_abs_line, engine_abs_line, machine_abs_line, gear_abs_line,
olive_abs_line, rapeseed_abs_line, sunflower_abs_line, diesel_trans_line, engine_castrol_trans_line, engine_trans_line,
machine_trans_line, gear_trans_line, olive_trans_line, rapeseed_trans_line, sunflower_trans_line, m_red_line,
m_orange_line, m_yellow_line, m_blue_line, m_green_line, m_diesel_abs_line, m_engine_castrol_abs_line,
m_engine_abs_line, m_machine_abs_line, m_gear_abs_line, m_olive_abs_line, m_rapeseed_abs_line, m_sunflower_abs_line]:
    line_name.visible = False

