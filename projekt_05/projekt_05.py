from rich.console import Console
import rich.traceback
from bokeh.plotting import row, column
from bokeh.io import curdoc
from bokeh.models import Select, RadioButtonGroup, CheckboxGroup, Div

import figs
import transmittance

console = Console()
console.clear()
rich.traceback.install()

#widgets handlery
def radio_button_handler(new):
    global figs
    if new == 0:
        curdoc().clear()
        select.value = 'White light (source)'
        out = column(radio_button_group, row(select, figs.fig_white))
        curdoc().add_root(out)
    elif new == 1:
        curdoc().clear()
        sources = column(div_sources, checkbox_group_source)
        oils = column(div_oils, checkbox_group_oil) 
        out = column(radio_button_group, row(sources, oils, figs.fig_match))
        curdoc().add_root(out)
    elif new == 2:
        curdoc().clear() 
        figs_rep = row(transmittance.fig_rep['castrol'], transmittance.fig_rep['jasol'], transmittance.fig_rep['olive'])
        figs_trans = row(transmittance.fig_trans['castrol'], transmittance.fig_trans['jasol'], transmittance.fig_trans['olive'])
        figs_ratio = row(transmittance.fig_ratio['castrol'], transmittance.fig_ratio['jasol'], transmittance.fig_ratio['olive'])
        out = out = column(radio_button_group, transmittance.div_reps, figs_rep, transmittance.div_trans, figs_trans, transmittance.div_ratio, figs_ratio)
        curdoc().add_root(out)   

radio_button_group = RadioButtonGroup(labels = ['Show measured spectra','Match oil with light source', 'Show transmittance values'], active = 0, width = 450)
radio_button_group.on_click(radio_button_handler)

def select_handler(attr, old, new):
    global figs
    if new == 'White light (source)':
        curdoc().clear()
        out = column(radio_button_group, row(select, figs.fig_white))
        curdoc().add_root(out)
    elif new =='LED diodes (source)':
        curdoc().clear()
        out = column(radio_button_group, row(select, figs.fig_LED))
        curdoc().add_root(out)
    else:
        for n in [['Diesel (fuel)', 'diesel_abs_line', 'diesel_trans_line', 'light yellow', 'mineral'], ['Castrol EDGE 0W-20 (engine oil)', 'castrol_edge_0w20_abs_line', 'castrol_edge_0w20_trans_line', 'green', 'synthetic'],
        ['Castrol EDGE 0W-30 (engine oil)', 'castrol_edge_0w30_abs_line', 'castrol_edge_0w30_trans_line', 'light brown', 'synthetic'], ['Castrol MAGNATEC (engine oil)', 'castrol_magnatec_abs_line', 'castrol_magnatec_trans_line', 'light brown', 'synthetic'],
        ['COMMA Pro-NRG (engine oil)', 'comma_pro-nrg_abs_line', 'comma_pro-nrg_trans_line', 'green', 'synthetic'], ['COMMA Xtech (engine oil)', 'comma_xtech_abs_line', 'comma_xtech_trans_line', 'light brown', 'synthetic'],
        ['elf EVOLUTION (engine oil)', 'elf_evolution_abs_line', 'elf_evolution_trans_line', 'light brown', 'semi-synthetic'], ['LOTOS (engine oil)', 'lotos_abs_line', 'lotos_trans_line', 'light brown', 'mineral'],
        ['MILLERS OILS (engine oil)', 'millers_oils_abs_line', 'millers_oils_trans_line', 'light brown', 'synthetic'], ['Mobil Super 2000 (engine oil)', 'mobil_super_2000_abs_line', 'mobil_super_2000_trans_line', 'light brown', 'semi-synthetic'], 
        ['MOTUL Specific (engine oil)', 'motul_specific_abs_line', 'motul_specific_trans_line', 'light brown', 'synthetic'], ['COMMA ASW (gear oil)', 'comma_asw_abs_line', 'comma_asw_trans_line', 'red', 'semi-synthetic, for automatics'],
        ['febi bilstein axle drive (gear oil)', 'febi_bilstein_axle_drive_abs_line', 'febi_bilstein_axle_drive_trans_line', 'yellow', 'for manuals'], ['febi bilstein gear oil (gear oil)', 'febi_bilstein_gear_oil_abs_line', 'febi_bilstein_gear_oil_trans_line', 'yellow', 'unknown'], 
        ['jasol AFT (gear oil)', 'jasol_aft_abs_line', 'jasol_aft_trans_line', 'red', 'mineral, for automatics'], ['ORLEN HIPOL (gear oil)', 'orlen_hipol_abs_line', 'orlen_hipol_trans_line', 'light brown', 'semi-synthetic, for spiral bevel gears'], 
        ['jasol L-DAA 100 (compressor oil)', 'jasol_l-daa_100_abs_line', 'jasol_l-daa_100_trans_line', 'yellow', 'mineral'], ['ORLEN BOXOL 26 (hydroil)', 'orlen_boxol_26_abs_line', 'orlen_boxol_26_trans_line', 'yellow', 'mineral'], ['TermoPasty (machine oil)', 'termo_pasty_abs_line', 'termo_pasty_trans_line', 'transparent', 'unknown'], 
        ['Olive (cooking oil)', 'olive_abs_line', 'olive_trans_line', 'yellow', '-'], ['Rapeseed (cooking oil)', 'rapeseed_abs_line', 'rapeseed_trans_line', 'yellow', '-'], ['Sunflower (cooking oil)', 'sunflower_abs_line', 'sunflower_trans_line', 'yellow', '-']]:
            if new == n[0]:
                figs.abs_lines[n[1]].visible = True
                figs.trans_lines[n[2]].visible = True
                div_color.text = f'Color: {n[3]}'
                div_type.text = f'Type: {n[4]}'
            else:
                figs.abs_lines[n[1]].visible = False
                figs.trans_lines[n[2]].visible = False

        if old == 'LED diodes (source)' or old == 'White light (source)':
            curdoc().clear()
            figures = column(figs.fig_abs, figs.fig_trans)
            out = column(radio_button_group, row(column(select, div_color, div_type), figures))
            curdoc().add_root(out)

select = Select(title = 'Select spectra:', value = 'White light (source)', options = ['White light (source)', 'LED diodes (source)', 'Diesel (fuel)', 'Castrol EDGE 0W-20 (engine oil)', 
'Castrol EDGE 0W-30 (engine oil)', 'Castrol MAGNATEC (engine oil)', 'COMMA Pro-NRG (engine oil)', 'COMMA Xtech (engine oil)', 'elf EVOLUTION (engine oil)', 'LOTOS (engine oil)', 'MILLERS OILS (engine oil)',
'Mobil Super 2000 (engine oil)', 'MOTUL Specific (engine oil)', 'COMMA ASW (gear oil)', 'febi bilstein axle drive (gear oil)', 'febi bilstein gear oil (gear oil)', 'jasol AFT (gear oil)',
'ORLEN HIPOL (gear oil)', 'jasol L-DAA 100 (compressor oil)', 'ORLEN BOXOL 26 (hydroil)', 'TermoPasty (machine oil)',
'Olive (cooking oil)', 'Rapeseed (cooking oil)', 'Sunflower (cooking oil)'], width = 300)
select.on_change('value', select_handler)

def checkbox_handler_source(new):
    global figs

    for n in [[0, 'm_red_line', 'm_red_patch'], [1, 'm_orange_line', 'm_orange_patch'], [2, 'm_yellow_line', 'm_yellow_patch'], [3, 'm_green_line', 'm_green_patch'], [4, 'm_blue_line', 'm_blue_patch'], [5, 'm_uv_line', 'm_uv_patch']]:
        if n[0] in new:
            figs.m_leds_lines[n[1]].visible = True
            figs.m_leds_lines[n[2]].visible = True
        else:
            figs.m_leds_lines[n[1]].visible = False
            figs.m_leds_lines[n[2]].visible = False

LABELS_LEDS = ['RED', 'ORANGE', 'YELLOW', 'GREEN', 'BLUE', 'UV']
checkbox_group_source = CheckboxGroup(labels = LABELS_LEDS, active = [], width = 150)
checkbox_group_source.on_click(checkbox_handler_source)

def checkbox_handler_oils(new):
    global figs
    for n in [[0, 'm_diesel_abs_line'], [1, 'm_castrol_edge_0w20_abs_line'], [2, 'm_castrol_edge_0w30_abs_line'], [3, 'm_castrol_magnatec_abs_line'],
     [4, 'm_comma_pro-nrg_abs_line'], [5, 'm_comma_xtech_abs_line'], [6, 'm_elf_evolution_abs_line'], [7, 'm_lotos_abs_line'], [8, 'm_millers_oils_abs_line'], 
     [9, 'm_mobil_super_2000_abs_line'], [10, 'm_motul_specific_abs_line'], [11, 'm_comma_asw_abs_line'], [12, 'm_febi_bilstein_axle_drive_abs_line'],
     [13, 'm_febi_bilstein_gear_oil_abs_line'], [14, 'm_jasol_aft_abs_line'], [15, 'm_orlen_hipol_abs_line'], [16, 'm_jasol_l-daa_100_abs_line'], [17, 'm_orlen_boxol_26_abs_line'], 
     [18, 'm_termo_pasty_abs_line'], [19, 'm_olive_abs_line'], [20, 'm_rapeseed_abs_line'], [21, 'm_sunflower_abs_line']]:  
        if n[0] in new:
            figs.m_abs_lines[n[1]].visible = True
        else:
            figs.m_abs_lines[n[1]].visible = False

LABELS_OILS = ['DIESEL', 'CASTROL EDGE 0W-20', 'CASTROL EDGE 0w-30', 'CASTROL MAGNATEC', 'COMMA PRO-NRG', 'COMMA XTECH', 'ELF EVOLUTION', 'LOTOS',
'MILLERS OILS', 'MOBIL SUPER 2000', 'MOTUL SPECIFIC', 'COMMA ASW', 'FEBI BILSTEIN AXLE DRIVE', 'FEBI BILSTEIN GEAR OIL', 'JASOL AFT', 'ORLEN HIPOL',
'JASOL L-DAA 100', 'ORLEN BOXOL 26', 'TERMO PASTY', 'OLIVE', 'RAPESEED', 'SUNFLOWER']
checkbox_group_oil = CheckboxGroup(labels = LABELS_OILS, active = [], width = 190)
checkbox_group_oil.on_click(checkbox_handler_oils)

div_color = Div(text ='')
div_type = Div(text ='')

div_sources = Div(text = 'LED sources:')
div_oils = Div(text = 'Oils:')

out = column(radio_button_group, row(select, figs.fig_white))

curdoc().add_root(out)
curdoc().title = "Oils\' spectra"

