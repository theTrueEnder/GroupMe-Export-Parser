import PySimpleGUI as sg
from json import (load as jsonload, dump as jsondump)
from os import path

"""
    A simple "settings" implementation.  Load/Edit/Save settings for your programs
    Uses json file format which makes it trivial to integrate into a Python program.  If you can
    put your data into a dictionary, you can save it as a settings file.
    
    Note that it attempts to use a lookup dictionary to convert from the settings file to keys used in 
    your settings window.  Some element's "update" methods may not work correctly for some elements.
    
    Copyright 2020 PySimpleGUI.com
    Licensed under LGPL-3
"""

'''PARAMETERS'''
#GROUPME_FILE_PATH = 'GroupMe Parser\\Groupme_Honors\\'
#REVERSED = True
#USE_NICKNAMES = False
#ENABLE_SYSTEM_MESSAGES = True
#Single user setting
#Enable images
#Enable replies
#Date range
#Local/server files
#Text-only or PDF or HTML
#Split by num, size, or length
'''END PARAMETERS'''

'''
{
    "user_data_folder": None, 
    "reversed": "True",
    "nicknames": "False",
    "enable_system_messages": "True",
    "enable_images": "True",
    "enable_files": "True",
    "enable_replies": "True",
    "use_local_files": "True",
    "export_type": "txt",
    "split_type": "none"
}
'''

#import Python_Scripts.gmparser as gmparser
import gmparser

SETTINGS_FILE = path.join(path.dirname(__file__), r'settings_file.cfg')

DEFAULT_SETTINGS = {
    "user_data_folder": '/', # change to None later
    "reversed": "True",
    "nicknames": "False",
    "enable_system_messages": "True",
    "enable_images": "True",
    "enable_files": "True",
    "enable_replies": "True",
    "use_local_files": "True",
    "export_type": "txt",
    "split_type": "none"
}

# "Map" from the settings dictionary keys to the window's element keys
SETTINGS_KEYS_TO_ELEMENT_KEYS = {
    'user_data_folder': '-USER FOLDER-' ,
    'reversed': '-REVERSED-',
    'nicknames' : '-NICKNAMES-',
    'enable_system_messages' : '-SYS MESSAGES-',
    'enable_images' : '-IMAGES-',
    'enable_files' : '-FILES-',
    'enable_replies' : '-REPLIES-',
    'use_local_files' : '-LOCAL-',
    'export_type' : '-EXPORT-',
    'split_type' : '-SPLIT-'
}


def run_parser(settings):
    gmparser.run(settings)

    
""" Load the given settings file, if it fails, return the default settings instead. """
def load_settings(settings_file, default_settings):
    try:
        with open(settings_file, 'r') as f:
            settings = jsonload(f)
    except Exception as e:
        sg.popup_quick_message(f'exception {e}', 'No settings file found... will create one for you', keep_on_top=True)
        settings = default_settings
        save_settings(settings_file, settings, None)
    return settings

""" Save the given settings to the settings file """
def save_settings(settings_file, settings, values):
    if values:      # if there are stuff specified by another window, fill in those values
        for key in SETTINGS_KEYS_TO_ELEMENT_KEYS:  # update window with the values read from settings file
            try:
                settings[key] = values[SETTINGS_KEYS_TO_ELEMENT_KEYS[key]]
            except Exception as e:
                print(f'Problem updating settings from window values. Key = {key}')
                sg.popup(f'Problem updating settings from window values. Key = {key}', background_color='red', text_color='white')

    with open(settings_file, 'w') as f:
        jsondump(settings, f)

    sg.popup('Settings saved')


""" Create a settings window """
def create_settings_window(settings):
    sg.theme('DarkGrey7')

    def TextLabel(text): return sg.Text(text+' ', justification='r', size=(len(text),1))

    layout = [  [sg.Text('Settings', font='Any 15')],
                [TextLabel('GroupMe Export Folder:'),sg.Input(key='-USER FOLDER-', size=(10,1)), sg.FolderBrowse(target='-USER FOLDER-')],
                [TextLabel('Newest messages at...'),sg.Radio('Top', "RADIO_1", key='-REVERSED-', default=True), sg.Radio('Bottom', "RADIO_1", default=False)],
                [TextLabel(''),sg.Checkbox('Use nicknames?', key='-NICKNAMES-', default=False)],
                [TextLabel(''),sg.Checkbox('Show System Messages?', key='-SYS MESSAGES-', default=True)],
                [TextLabel('Note: System messages include polls and user joins/exits)')],
                [TextLabel('- - - - - - - -')],
                [TextLabel('FOLLWING SETTINGS ARE DISABLED')],
                [TextLabel(''),sg.Checkbox('Enable Images?',   key='-IMAGES-',  default=True, disabled=True)], # disabled
                [TextLabel(''),sg.Checkbox('Enable Files?',    key='-FILES-',   default=True, disabled=True)], # disabled
                [TextLabel(''),sg.Checkbox('Enable Replies?' , key='-REPLIES-', default=True, disabled=True)], # disabled
                [TextLabel(''),sg.Checkbox('Use Local Files?', key='-LOCAL-',   default=True, disabled=True)], # disabled
                [TextLabel('Export Type:'),sg.Combo(['txt', 'pdf', 'html'], key='-EXPORT-', default_value='txt', disabled=True)], # disabled
                [TextLabel('Split Type:'),sg.Combo(['none', 'num', 'size', 'length'], key='-SPLIT-', default_value='none', disabled=True)], # disabled
                [sg.Button('Save Current Settings'), sg.Button('Cancel')]  ]

    window = sg.Window('Settings', layout, finalize=True, resizable=True, size=(550,550), element_justification='r') 

    for key in SETTINGS_KEYS_TO_ELEMENT_KEYS:   # update window with the values read from settings file
        try:
            window[SETTINGS_KEYS_TO_ELEMENT_KEYS[key]].update(value=settings[key])
        except Exception as e:
            print(f'Problem updating PySimpleGUI window from settings. Key = {key}')
            sg.popup(f'Problem updating PySimpleGUI window from settings. Key = {key}', background_color='red', text_color='white')

    return window

""" Create the main window """
def create_main_window(settings):
    sg.theme("DarkGrey11")

    layout = [[sg.T('GroupMe Export Parser')],
              [sg.T('Change the settings below to customize the export.')],
              [sg.B('Edit Settings')],
              [sg.B('Run Parser'), sg.B('Exit')]]

    return sg.Window('Main Application', layout)

""" Main program event loop """
def main():
    window, settings = None, load_settings(SETTINGS_FILE, DEFAULT_SETTINGS )

    while True:
        if window is None:
            window = create_main_window(settings)

        event, values = window.read()
        if event in (None, 'Exit', 'Cancel'):
            break
        if event == 'Edit Settings':
            event, values = create_settings_window(settings).read(close=True)

            if event == 'Save Current Settings':
                window.close()
                window = None
                save_settings(SETTINGS_FILE, settings, values)
                
        if event == 'Run Parser':
            m = run_parser(settings)
            if m == 'Messages parsed successfully':
                sg.popup('Messages parsed successfully')
            else:
                #sg.popup('Completion error: ' + m, background_color='red', text_color='white')
                pass
            break
    window.close()


main()