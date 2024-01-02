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
import msg_unit
from conversation import Conversation
from datetime import datetime
import html_converter
from helper import clean_text, get_clean_json, write_to_error_log
import emoji
import traceback

# REVERSED = None

#TODO find static url for the default GM pic
# is the id static to the system? idk
# took a guess on the roles as well
SYSTEM_USER = json.loads('''
    {
        "user_id": "system",
        "nickname": "system",
        "image_url": "https://imgs.search.brave.com/4vMvrshEmayMwfpUjotgeYpsv9FuSInGyMZWQUR8Uhs/rs:fit:150:172:1/g:ce/aHR0cHM6Ly92aWdu/ZXR0ZTIud2lraWEu/bm9jb29raWUubmV0/L2xvZ29wZWRpYS9p/bWFnZXMvNS81Yi9H/cm91cE1lMjAxMi5w/bmcvcmV2aXNpb24v/bGF0ZXN0L3NjYWxl/LXRvLXdpZHRoLWRv/d24vMTUwP2NiPTIw/MTUwNjE0MjAwMTMx",
        "id": "60768421",
        "muted": false,
        "autokicked": false,
        "roles": [
            
            "admin",
            "system"
        ],
        "name": "system"
    }''')



def throw_error(code, message, traceback_msg):
    print(message)
    write_to_error_log(traceback_msg)
    return (code, message)

""" Add a message to the message list (accounts for reversal option) """
def add_msg(msg_list, msg, reversed):
    if reversed:
        msg_list.append(msg)
    else:
        msg_list.insert(0, msg)
    return msg_list

def run(settings):
    # if the user data folder doesn't end in a slash, add one
    if settings["user_data_folder"] is None or settings["user_data_folder"] == "":
        print("Error: User Data Folder blank")
        return "Error: User Data Folder blank"
    
    if settings["user_data_folder"][-1] != '/':
        settings["user_data_folder"] += '/'

    #TODO clean up
    # get settings
    reversed = settings["reversed"]
    settings["nicknames"]
    settings["enable_system_messages"]
    #settings["enable_images"]
    #settings["enable_files"]
    #settings["enable_replies"]
    #settings["use_local_files"]
    settings["export_type"]
    #settings["split_type"]


    '''
    Get data from conversation.json, which is mostly metadata-related, and is the source of the
    header lines in output.txt.
    '''

    # get conversation json data from file
    print('Opening and cleaning conversation file...')
    try:
        raw_cvn = get_clean_json(settings["user_data_folder"] + 'conversation.json')
    except Exception as e:
        emsg = 'Failed to open conversation.json: ' + str(e)
        return throw_error(1, emsg, traceback.format_exc())
    
    raw_cvn['members'].append(SYSTEM_USER)

    # parse conversation json data
    print('Parsing conversation...')
    cvn = Conversation()
    cvn.parse(raw_cvn)
    cvn_export = cvn.export()
    
    
    # write conversation data to the output file
    print('Writing conversation export...')
    try:
        with open(settings["user_data_folder"]  + 'output.txt', 'w', encoding='utf-8', errors='ignore') as f:
            f.write("Compiled at: " + datetime.now().strftime('%Y-%m-%d %H:%M:%S') + '\n\n')
            f.write(cvn_export+'\n')  
    except Exception as e:
        emsg = 'Failed writing conversation to file: ' + str(e)
        return throw_error(2, emsg, traceback.format_exc())
    


    ''' Get data from message.json, which is the actual content of the exported chat. '''

    # get message json data from file
    print('Opening and cleaning message file... (this may take a moment)')
    try:
        raw_msgs = get_clean_json(settings["user_data_folder"]  + 'message.json')
    except Exception as e:
        emsg = 'Failed to read message.json: ' + str(e)
        return throw_error(1, emsg, traceback.format_exc())


    # parse conversation to get conversation metadata and user list
    print('Parsing messages...')
    msgs = []
    for msg in raw_msgs:
        tmp_msg = msg_unit.msg_unit()
        tmp_msg.parse(msg, cvn)

        # if message is sent by a user or if a system message and system messages are enabled, append to message list
        if tmp_msg.senderType != 'system' or settings["enable_system_messages"]:
            msgs.append(tmp_msg)


    # format message data for export
    print('Formatting data...')
    dict_msg = [msg.simple_export() for msg in msgs]
    s = []


    # replace ID numbers with names/nicknames of users
    for msg in dict_msg: 
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
     
     
    # put all messages into one list
    concat_msgs = []
    msg_export = ''
    for msg in s:
        full_message = ''
        for part in msg:
            # if message part won't concatenate, ignore
            try:
                part + 'teststring'
                full_message += part
                # concat_msgs = add_msg(concat_msgs, part, True)
            except: 
                continue
        full_message += '\n'
        concat_msgs = add_msg(concat_msgs, full_message, reversed)

    msg_export = ''.join(concat_msgs)
    msg_export = emoji.emojize(msg_export)  # turn the emoji placeholders back into Unicode characters


    # write message list to output file
    print(f'Writing output to {settings["user_data_folder"]}output.txt...')
    try:
        with open(settings["user_data_folder"]  + 'output.txt', 'a', encoding='utf-8') as f:        
            f.write(msg_export)
    except Exception as e:
        emsg = 'Messages failed to write to output file' + str(e)
        return throw_error(2, emsg, traceback.format_exc())

    print('Parser complete.')

    if settings["export_type"] == 'txt':
        # The following is empty until the selector for export type is enabled.
        # When it is, the section above would be moved here.
        pass

    elif settings["export_type"] == 'html':
        print('Exporting to HTML... (this may take a moment)')
        try:
            html_converter.convert(msgs, settings, settings["user_data_folder"]) # this includes system messages even if they are disabled
        except Exception as e:
            emsg = 'Messages failed to write to html file: ' + str(e)
            return throw_error(2, emsg, traceback.format_exc())
    
    print('Messages parsed successfully.')
    return (0, 'Messages parsed and exported')