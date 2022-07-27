'''
TODO
- Likes
- Replies
- Images
- Other Attachments
- Order of messages (time)

'''

'''PARAMETERS'''
GROUPME_FILE_PATH = 'GroupMe Parser\\Groupme_Honors\\'
REVERSED = True
USE_NICKNAMES = False
ENABLE_SYSTEM_MESSAGES = True
'''END PARAMETERS'''

import json
import msg_unit as msg_unit
import conversation as conversation
import os




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

def run():
    '''
    get conversation json data
    parse conversation to get conversation metadata and user list
    write conversation metadata to output file
    delete conversation

    get message json data
    parse message to get message list
    write message list to output file
        #get images and add into output file
    delete message list
    
    
    '''
    #get conversation json data
    print('Opening conversation file...')
    with open(GROUPME_FILE_PATH + 'conversation.json', 'r') as f:
        raw_cvn = json.load(f)
    

    #get message json data
    print('Opening message file...')
    with open(GROUPME_FILE_PATH + 'message.json', 'r', encoding='utf-8', errors='ignore') as f:
        raw_msgs = json.load(f)
    

    #parse conversation to get conversation metadata and user list
    print('Parsing files...')
    cvn = conversation.conversation()
    cvn.parse(raw_cvn)
    msgs = []
    for msg in raw_msgs:
        tmp_msg = msg_unit.msg_unit()
        tmp_msg.parse(msg)
        msgs.append(tmp_msg)


    #format the conversation and message data for export
    print('Formatting data...')
    cvn_export = cvn.export()
    msg_export = '\n'.join([msg.s_simple_export() for msg in msgs])
    dict_msg = [msg.simple_export() for msg in msgs]
    s = []

    for msg in dict_msg: # get names/nicknames of users instead of ID numbers
        temp_member = cvn.get_member_by_id(msg['sender'])
        if temp_member is not None:
            if settings["nicknames"]:
                msg['sender'] = temp_member.nickname
            else:
                msg['sender'] = temp_member.name
        if settings["enable_system_messages"]:
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
    
    cvn_export = clean_text(cvn_export)
    msg_export = clean_text(msg_export)

    #write message list to output file
    print(f'Writing output to {settings["user_data_folder"] }output.txt...')
    with open(settings["user_data_folder"]  + 'output.txt', 'w', encoding='utf-8', errors='ignore') as f:
        f.write("Compiled at: " + datetime.now().strftime('%Y-%m-%d %H:%M:%S') + '\n\n')
        f.write(cvn_export+'\n')        
        f.write(msg_export)
        
    print('Program complete.')


tmp_settings = {
    "user_data_folder": "GroupMe Parser/Groupme_Honors/", 
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