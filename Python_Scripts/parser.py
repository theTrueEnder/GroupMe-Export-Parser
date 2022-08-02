'''
TODO
- Likes
- Replies
- Images
- Other Attachments
- Order of messages (time)

'''

'''PARAMETERS
{
    "user_data_folder": "", 
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
END PARAMETERS'''

import json
import msg_unit as msg_unit
import conversation as conversation
from datetime import datetime
import html_converter


REVERSED = None

# Remove bad characters created from encoding conversion
def clean_text(dirty):
    if dirty is not None:
        if "´" or "’" or "`" or "�" or "“" or "”" or '\u202c' or '\u202d' in dirty:
            clean = dirty
            clean = clean.replace("´", "'")
            clean = clean.replace("’", "'")
            clean = clean.replace("`", "'")
            clean = clean.replace("�", '<emoji>')
            clean = clean.replace("“", '"')
            clean = clean.replace("”", '"')
            clean = clean.replace('\u202c', '')
            clean = clean.replace('\u202d', '')
        return clean
    else:
        return None

def add_msg(msg_list, msg):
    if REVERSED:
        msg_list.insert(0, msg)
    else:
        msg_list.append(msg)
    return msg_list

def run(settings):
    if settings["user_data_folder"][-1] != '/':
        settings["user_data_folder"] += '/'
    REVERSED = settings["reversed"]
    settings["nicknames"]
    settings["enable_system_messages"]
    #settings["enable_images"]
    #settings["enable_files"]
    #settings["enable_replies"]
    #settings["use_local_files"]
    settings["export_type"]
    #settings["split_type"]

    #get conversation json data
    print('Opening conversation file...')
    try:
        with open(settings["user_data_folder"]  + 'conversation.json', 'r', errors='ignore') as f:
            raw_cvn = json.load(f)
    except Exception as e:
        print('Error opening conversation.json: ' + str(e))
        return 'Error opening conversation.json: ' + str(e)

    print('Parsing conversation...')
    cvn = conversation.conversation()
    cvn.parse(raw_cvn)
    cvn_export = cvn.export()
    # cvn_export = clean_text(cvn_export) #############################################################################################################################################################
    print(f'Writing conversation export to {settings["user_data_folder"] }output.txt...')
    try:
        with open(settings["user_data_folder"]  + 'output.txt', 'w', encoding='utf-8', errors='ignore') as f:
            f.write("Compiled at: " + datetime.now().strftime('%Y-%m-%d %H:%M:%S') + '\n\n')
            f.write(cvn_export+'\n')  
    except Exception as e:
        print('Error writing conversation to file: ' + str(e))
        return 'Error writing conversation to file: ' + str(e)


    #get message json data
    try:
        print('Opening message file...')
        with open(settings["user_data_folder"]  + 'message.json', 'r', encoding='utf-8', errors='ignore') as f:
            raw_msgs = json.load(f)
    except Exception as e:
        print('Error opening message.json: ' + str(e))
        return 'Error opening message.json: ' + str(e)

    #parse conversation to get conversation metadata and user list
    print('Parsing messages...')
    msgs = []
    for msg in raw_msgs:
        tmp_msg = msg_unit.msg_unit()
        tmp_msg.parse(msg)
        if settings["enable_system_messages"] or tmp_msg.type != 'system':
            msgs.append(tmp_msg)

    #format message data for export
    print('Formatting data...')
    #msg_export = '\n'.join([msg.s_simple_export() for msg in msgs])
    dict_msg = [msg.simple_export() for msg in msgs]
    s = []

    for msg in dict_msg: # get names/nicknames of users instead of ID numbers
        temp_member = cvn.get_member_by_id(msg['sender'])
        if temp_member is not None:
            if settings["nicknames"]:
                msg['sender'] = temp_member.nickname
            else:
                msg['sender'] = temp_member.name
            s.append([ #this is the message format, for customization see here
                msg["sender"], 
                f' at {msg["time"]}: ', 
                msg["message"]
            ])
     
    concat_msgs = []
    for msg in s:
        for part in msg:
            try:
                part + 'teststring'
                concat_msgs = add_msg(concat_msgs, part)
            except: # if message part won't concatenate, ignore
                continue
        concat_msgs = add_msg(concat_msgs, '\n')

    msg_export = ''.join(concat_msgs)
    #msg_export = clean_text(msg_export) ##################################################################################################################################################

    #write message list to output file
    print(f'Writing output to {settings["user_data_folder"]}output.txt...')
    try:
        with open(settings["user_data_folder"]  + 'output.txt', 'a', encoding='utf-8', errors='ignore') as f:        
            f.write(msg_export)
    except Exception as e:
        print('Error writing messages to output file: ' + str(e))
        return 'Error writing messages to output file: ' + str(e)

    print('Parser complete.')

    if settings["export_type"] == 'txt':
        print('Exporting to .txt...')
        #try:
        #    with open(settings["user_data_folder"]  + 'output.txt', 'w', encoding='utf-8', errors='ignore') as f:
        #        f.write(msg_export)
        #except:
        #    print('Error writing output file.')
        #    return
    elif settings["export_type"] == 'html':
        print('Exporting to .html...')
        try:
            html_converter.convert(msgs, settings["user_data_folder"]  + 'output.html') # this includes system messages even if they are disabled
        except Exception as e:
            print('Error writing messages to html file: ' + str(e))
            return 'Error writing messages to html file: ' + str(e)
    
    print('Messages parsed successfully')
    return 'Messages parsed successfully'


tmp_settings = {
    "user_data_folder": "~/Groupme_Honors/", 
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
run(tmp_settings)