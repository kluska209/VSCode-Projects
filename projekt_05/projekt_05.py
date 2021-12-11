from rich.console import Console
import rich.traceback
from bokeh.plotting import row, column
from bokeh.io import curdoc
from bokeh.models import Select, RadioButtonGroup, CheckboxGroup, Div

import figs

console = Console()
console.clear()
rich.traceback.install()

#widgets handlery
def radio_button_handler(new):
    global figs
    if new == 0:
        curdoc().clear()
        select.value = 'White light (source)'
        controls = column(radio_button_group, select)
        out = row(controls, figs.fig_white)
        curdoc().add_root(out)
    elif new == 1:
        curdoc().clear()
        sources = column(div_sources, checkbox_group_source)
        oils = column(div_oils, checkbox_group_oil) 
        controls = column(radio_button_group, row(sources, oils))
        out = row(controls, figs.fig_match)
        curdoc().add_root(out)

radio_button_group = RadioButtonGroup(labels = ['Show measured spectra','Match oil with light source'], active = 0, width = 320)
radio_button_group.on_click(radio_button_handler)

def select_handler(attr, old, new):
    global figs
    if new == 'White light (source)':
        curdoc().clear()
        controls = column(radio_button_group, select)
        out = row(controls, figs.fig_white)
        curdoc().add_root(out)
    elif new =='LED diodes (source)':
        curdoc().clear()
        controls = column(radio_button_group, select)
        out = row(controls, figs.fig_LED)
        curdoc().add_root(out)
    else:
        for n in [['Diesel (fuel)', 'diesel_abs_line', 'diesel_trans_line'], ['Castrol EDGE 0W-20 (engine oil)', 'castrol_edge_0w20_abs_line', 'castrol_edge_0w20_trans_line'],
        ['Castrol EDGE 0W-30 (engine oil)', 'castrol_edge_0w30_abs_line', 'castrol_edge_0w30_trans_line'], ['Castrol MAGNATEC (engine oil)', 'castrol_magnatec_abs_line', 'castrol_magnatec_trans_line'],
        ['COMMA Pro-NRG (engine oil)', 'comma_pro-nrg_abs_line', 'comma_pro-nrg_trans_line'], ['COMMA Xtech (engine oil)', 'comma_xtech_abs_line', 'comma_xtech_trans_line'],
        ['elf EVOLUTION (engine oil)', 'elf_evolution_abs_line', 'elf_evolution_trans_line'], ['MILLERS OILS (engine oil)', 'millers_oils_abs_line', 'millers_oils_trans_line'],
        ['Mobil Super 2000 (engine oil)', 'mobil_super_2000_abs_line', 'mobil_super_2000_trans_line'], ['MOTUL Specific (engine oil)', 'motul_specific_abs_line', 'motul_specific_trans_line'],
        ['COMMA ASW (gear oil)', 'comma_asw_abs_line', 'comma_asw_trans_line'], ['febi bilstein axle drive (gear oil)', 'febi_bilstein_axle_drive_abs_line', 'febi_bilstein_axle_drive_trans_line'],
        ['febi bilstein gear oil (gear oil)', 'febi_bilstein_gear_oil_abs_line', 'febi_bilstein_gear_oil_trans_line'], ['Olive (cooking oil)', 'olive_abs_line', 'olive_trans_line'],
        ['Rapeseed (cooking oil)', 'rapeseed_abs_line', 'rapeseed_trans_line'], ['Sunflower (cooking oil)', 'sunflower_abs_line', 'sunflower_trans_line']]:
            if new == n[0]:
                figs.abs_lines[n[1]].visible = True
                figs.trans_lines[n[2]].visible = True
            else:
                figs.abs_lines[n[1]].visible = False
                figs.trans_lines[n[2]].visible = False

        if old == 'LED diodes (source)' or old == 'White light (source)':
            curdoc().clear()
            controls = column(radio_button_group, select)
            figures = column(figs.fig_abs, figs.fig_trans)
            out = row(controls, figures)
            curdoc().add_root(out)

select = Select(title = 'Select spectra:', value = 'White light (source)', options = ['White light (source)', 'LED diodes (source)', 'Diesel (fuel)', 'Castrol EDGE 0W-20 (engine oil)', 
'Castrol EDGE 0W-30 (engine oil)', 'Castrol MAGNATEC (engine oil)', 'COMMA Pro-NRG (engine oil)', 'COMMA Xtech (engine oil)', 'elf EVOLUTION (engine oil)', 'MILLERS OILS (engine oil)',
'Mobil Super 2000 (engine oil)', 'MOTUL Specific (engine oil)', 'COMMA ASW (gear oil)', 'febi bilstein axle drive (gear oil)', 'febi bilstein gear oil (gear oil)', 'Olive (cooking oil)', 
'Rapeseed (cooking oil)', 'Sunflower (cooking oil)'], width = 300)
select.on_change('value', select_handler)

def checkbox_handler_source(new):
    global figs

    for n in [[0, 'm_red_line'], [1, 'm_orange_line'], [2, 'm_yellow_line'], [3, 'm_green_line'], [4, 'm_blue_line'], [5, 'm_uv_line']]:
        if n[0] in new:
            figs.m_leds_lines[n[1]].visible = True
        else:
            figs.m_leds_lines[n[1]].visible = False

LABELS_LEDS = ['RED', 'ORANGE', 'YELLOW', 'GREEN', 'BLUE', 'UV']
checkbox_group_source = CheckboxGroup(labels = LABELS_LEDS, active = [], width = 150)
checkbox_group_source.on_click(checkbox_handler_source)

def checkbox_handler_oils(new):
    global figs
    for n in [[0, 'm_diesel_abs_line'], [1, 'm_castrol_edge_0w20_abs_line'], [2, 'm_castrol_edge_0w30_abs_line'], [3, 'm_castrol_magnatec_abs_line'],
     [4, 'm_comma_pro-nrg_abs_line'], [5, 'm_comma_xtech_abs_line'], [6, 'm_elf_evolution_abs_line'], [7, 'm_millers_oils_abs_line'], [8, 'm_mobil_super_2000_abs_line'],
     [9, 'm_motul_specific_abs_line'], [10, 'm_comma_asw_abs_line'], [11, 'm_febi_bilstein_axle_drive_abs_line'], [12, 'm_febi_bilstein_gear_oil_abs_line'],
     [13, 'm_olive_abs_line'], [14, 'm_rapeseed_abs_line'], [15, 'm_sunflower_abs_line']]:  
        if n[0] in new:
            figs.m_abs_lines[n[1]].visible = True
        else:
            figs.m_abs_lines[n[1]].visible = False

LABELS_OILS = ['DIESEL', 'CASTROL EDGE 0W-20', 'CASTROL EDGE 0w-30', 'CASTROL MAGNATEC', 'COMMA PRO-NRG', 'COMMA XTECH', 'ELF EVOLUTION',
'MILLERS OILS', 'MOBIL SUPER 2000', 'MOTUL SPECIFIC', 'COMMA ASW', 'FEBI BILSTEIN AXLE DRIVE', 'FEBI BILSTEIN GEAR OIL', 'OLIVE', 'RAPESEED', 'SUNFLOWER']
checkbox_group_oil = CheckboxGroup(labels = LABELS_OILS, active = [], width = 150)
checkbox_group_oil.on_click(checkbox_handler_oils)

div_sources = Div(text = 'LED sources:')
div_oils = Div(text = 'Oils:')

controls = column(radio_button_group, select)
out = row(controls, figs.fig_white)

curdoc().add_root(out)
curdoc().title = "Oils\' spectra"

