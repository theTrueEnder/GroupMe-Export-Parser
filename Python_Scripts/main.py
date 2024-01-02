import PySimpleGUI as sg
from json import (load as jsonload, dump as jsondump)
from os import path
from helper import write_to_error_log, clear_error_log
import traceback
import gmparser
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
    "reversed": "False",
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


SETTINGS_FILE = path.join(path.dirname(__file__), r'settings_file.cfg')

DEFAULT_SETTINGS = {
    "user_data_folder": '/', # change to None later
    "reversed": "False",
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
    if values:      # if there is stuff specified by another window, fill in those values
        for key in SETTINGS_KEYS_TO_ELEMENT_KEYS:  # update window with the values read from settings file
            try:
                settings[key] = values[SETTINGS_KEYS_TO_ELEMENT_KEYS[key]]
            except Exception as e:
                emsg = f'Problem updating settings from window values for Key={key}: ' + str(e)
                print(emsg)
                write_to_error_log(emsg, traceback.format_exc())
                sg.popup(emsg, background_color='red', text_color='white')

    with open(settings_file, 'w') as f:
        jsondump(settings, f)



""" Create a settings window """
def create_settings_window(settings):
    sg.theme('DarkGrey11')

    #TODO: make this look decent
    
    
    input_layout = [
        [
            sg.Text('GroupMe Export Folder:'),
            sg.Input(key='-USER FOLDER-', size=(40,1)), 
            sg.FolderBrowse(target='-USER FOLDER-')
        ]
    ]
    
    message_layout =[
        [
            sg.Text('Newest messages at...'),
            sg.Radio('Top', "RADIO_1", key='-REVERSED-', default=True), 
            sg.Radio('Bottom', "RADIO_1", key='-NOTREVERSED-', default=True)
        ],[
            sg.Checkbox('Use nicknames?', key='-NICKNAMES-', default=False),
            sg.Checkbox('Enable Replies?' , key='-REPLIES-', default=True, disabled=True),
            
        ],
    ]
    
    output_layout = [
        [
            sg.Checkbox('Show System Messages?', key='-SYS MESSAGES-', default=True),
            sg.Text('Note: This includes polls and user joins/exits)')            
        ],[
            sg.Checkbox('Enable images?', key='-IMAGES-', default=True, disabled=True),
            sg.Checkbox('Enable file attachments?', key='-FILES-', default=True, disabled=True),
            sg.Checkbox('Use Local Files?', key='-LOCAL-',   default=True, disabled=True)
            
        ],[ 
            sg.Text('Export Type:'),
            sg.Combo(['txt', 'pdf', 'html'], key='-EXPORT-', default_value='txt', disabled=False),
            sg.Text('Split Type:'),
            sg.Combo(['none', 'num', 'size', 'length'], key='-SPLIT-', default_value='none', disabled=True)
        ]
    ]
    
    
    layout = [
        [
            sg.Text('Settings', font='Any 15', justification='center', expand_x=True)
        ],[
            sg.Frame('Input Location', input_layout)
        ],[
            sg.Frame('Message Options', message_layout) 
        ],[
            sg.Frame('Output Options', output_layout) 
        ],[ # disabled
            sg.Button('Save Current Settings'),
            sg.Button('Cancel')
        ]
    ]

    window = sg.Window('Settings', layout, finalize=True, resizable=True, size=(550,340), element_justification='l') 

    for key in SETTINGS_KEYS_TO_ELEMENT_KEYS:   # update window with the values read from settings file
        try:
            window[SETTINGS_KEYS_TO_ELEMENT_KEYS[key]].update(value=settings[key])
        except Exception as e:
            emsg = f'Problem updating settings from window values for Key={key}: ' + str(e)
            print(emsg)
            write_to_error_log(emsg, traceback.format_exc())
            sg.popup(emsg, background_color='red', text_color='white')


    return window

""" Create the main window """
def create_main_window(settings):
    sg.theme("DarkGrey11")

    button_layout = [
        [
            sg.Button('Run Parser', button_color='green'), 
            sg.Button('Edit Settings'),
            sg.Button('Exit', button_color='red')
        ]
    ]
    
    layout = [
        [
            sg.Text('GroupMe Export Parser', justification='center', font='Any 15', expand_x=True, 
                       pad=(1,5))
        ],[
            sg.Text('Change the settings below to customize the export.')
        ],[
            sg.Frame("", button_layout, element_justification='center')
        ]
    ]

    return sg.Window('GroupMe Export Parser - Main Menu', layout, element_justification='center')


""" Main program event loop """
def main():
    window, settings = None, load_settings(SETTINGS_FILE, DEFAULT_SETTINGS )
    clear_error_log()
    
    while True:
        # create the main window if it doesn't exist
        if window is None:
            window = create_main_window(settings)

        # get new event
        event, values = window.read()
        
        if event in (None, 'Exit', 'Cancel'):
            break
        
        # if the edit settings button is clicked, open edit settings window
        if event == 'Edit Settings':
            event, values = create_settings_window(settings).read(close=True)

            if event == 'Save Current Settings':
                window.close()
                window = None
                save_settings(SETTINGS_FILE, settings, values)
        
        # if the run parser button is clicked, open edit settings window
        if event == 'Run Parser':
            c, m = gmparser.run(settings)
            
            # match the completion code with the proper message/popup
            match(c):
                case 0:
                    sg.popup(f'Success: {m}')
                case 1:
                    print(f'Read Error: {m}')
                    sg.popup('Completion error: ' + m + ". See error-log.txt for more details.", 
                             background_color='red', text_color='white')
                case 2:
                    print(f'Write Error: {m}')
                    sg.popup('Completion error: ' + m + ". See error-log.txt for more details.", 
                             background_color='red', text_color='white')
                
            break
        
    window.close()


main()