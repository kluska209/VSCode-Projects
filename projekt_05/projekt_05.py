from rich.console import Console
import rich.traceback
import os
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
        sources = column(div_source, checkbox_group_source)
        oils = column(div_oil, checkbox_group_oil) 
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
        if new == 'Diesel (oil)':
            figs.diesel_abs_line.visible = True
            figs.diesel_trans_line.visible = True
        else:
            figs.diesel_abs_line.visible = False
            figs.diesel_trans_line.visible = False

        if new == 'Engine Castrol (oil)':
            figs.engine_castrol_abs_line.visible = True
            figs.engine_castrol_trans_line.visible = True
        else:
            figs.engine_castrol_abs_line.visible = False
            figs.engine_castrol_trans_line.visible = False

        if new == 'Engine (oil)':
            figs.engine_abs_line.visible = True
            figs.engine_trans_line.visible = True
        else:
            figs.engine_abs_line.visible = False
            figs.engine_trans_line.visible = False

        if new == 'Machine (oil)':
            figs.machine_abs_line.visible = True
            figs.machine_trans_line.visible = True
        else:
            figs.machine_abs_line.visible = False
            figs.machine_trans_line.visible = False

        if new == 'Gear (oil)':
            figs.gear_abs_line.visible = True
            figs.gear_trans_line.visible = True
        else:
            figs.gear_abs_line.visible = False
            figs.gear_trans_line.visible = False

        if new == 'Olive (oil)':
            figs.olive_abs_line.visible = True
            figs.olive_trans_line.visible = True
        else:
            figs.olive_abs_line.visible = False
            figs.olive_trans_line.visible = False

        if new == 'Rapeseed (oil)':
            figs.rapeseed_abs_line.visible = True
            figs.rapeseed_trans_line.visible = True
        else:
            figs.rapeseed_abs_line.visible = False
            figs.rapeseed_trans_line.visible = False

        if new == 'Sunflower (oil)':
            figs.sunflower_abs_line.visible = True
            figs.sunflower_trans_line.visible = True
        else:
            figs.sunflower_abs_line.visible = False
            figs.sunflower_trans_line.visible = False

        if old == 'LED diodes (source)' or old == 'White light (source)':
            curdoc().clear()
            controls = column(radio_button_group, select)
            figures = column(figs.fig_abs, figs.fig_trans)
            out = row(controls, figures)
            curdoc().add_root(out)

select = Select(title='Select spectra:', value= 'White light (source)', options=['White light (source)', 'LED diodes (source)', 'Diesel (oil)', 'Engine Castrol (oil)', 
'Engine (oil)', 'Machine (oil)', 'Gear (oil)', 'Olive (oil)', 'Rapeseed (oil)', 'Sunflower (oil)'], width = 200)
select.on_change('value', select_handler)

def checkbox_handler_source(new):
    global figs
    if 0 in new:
        figs.m_red_line.visible = True
    else:
        figs.m_red_line.visible = False

    if 1 in new:
        figs.m_orange_line.visible = True
    else:
        figs.m_orange_line.visible = False

    if 2 in new:
        figs.m_yellow_line.visible = True
    else:
        figs.m_yellow_line.visible = False

    if 3 in new:
        figs.m_green_line.visible = True
    else:
        figs.m_green_line.visible = False

    if 4 in new:
        figs.m_blue_line.visible = True
    else:
        figs.m_blue_line.visible = False

LABELS_LEDS = ['RED', 'ORANGE', 'YELLOW', 'GREEN', 'BLUE']
checkbox_group_source = CheckboxGroup(labels = LABELS_LEDS, active = [], width = 150)
checkbox_group_source.on_click(checkbox_handler_source)

def checkbox_handler_oils(new):
    global figs
    if 0 in new:
        figs.m_diesel_abs_line.visible = True
    else:
        figs.m_diesel_abs_line.visible = False
    
    if 1 in new:
        figs.m_engine_castrol_abs_line.visible = True
    else:
        figs.m_engine_castrol_abs_line.visible = False

    if 2 in new:
        figs.m_engine_abs_line.visible = True
    else:
        figs.m_engine_abs_line.visible = False

    if 3 in new:
        figs.m_machine_abs_line.visible = True
    else:
        figs.m_machine_abs_line.visible = False

    if 4 in new:
        figs.m_gear_abs_line.visible = True
    else:
        figs.m_gear_abs_line.visible = False

    if 5 in new:
        figs.m_olive_abs_line.visible = True
    else:
        figs.m_olive_abs_line.visible = False

    if 6 in new:
        figs.m_rapeseed_abs_line.visible = True
    else:
        figs.m_rapeseed_abs_line.visible = False

    if 7 in new:
        figs.m_sunflower_abs_line.visible = True
    else:
        figs.m_sunflower_abs_line.visible = False

LABELS_OILS = ['DIESEL', 'ENGINE CASTROL', 'ENGINE', 'MACHINE', 'GEAR', 'OLIVE', 'RAPESEED', 'SUNFLOWER']
checkbox_group_oil = CheckboxGroup(labels = LABELS_OILS, active = [], width = 150)
checkbox_group_oil.on_click(checkbox_handler_oils)

div_source = Div(text = 'LED sources:')
div_oil = Div(text = 'Oils:')

controls = column(radio_button_group, select)
out = row(controls, figs.fig_white)

curdoc().add_root(out)
curdoc().title = "Oils\' spectra"

