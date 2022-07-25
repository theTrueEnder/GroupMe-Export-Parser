def detect(file):
    import chardet    
    rawdata = open(file, "r").read()
    result = chardet.detect(rawdata)
    charenc = result['encoding']
    return charenc

'''
TODO
- Likes
- Replies
- Images
- Other Attachments
- Order of messages (time)

'''

from ast import SetComp
import json
import msgUnit as msgUnit
import conversation as conversation
import os

CHAR_ENCOD = 'cp1252'
CHAR_DECOD = 'utf-8'
REVERSED = True

def clean(unsanitized):
    original = unsanitized
    if unsanitized is not None:
        if "´" or "’" or "`" or "�" or "“" or "”" or '\u202c' or '\u202d' in unsanitized:
            sanitized = unsanitized
            sanitized = sanitized.replace("´", "'")
            sanitized = sanitized.replace("’", "'")
            sanitized = sanitized.replace("`", "'")
            sanitized = sanitized.replace("�", '<emoji>')
            sanitized = sanitized.replace("“", '"')
            sanitized = sanitized.replace("”", '"')
            sanitized = sanitized.replace('\u202c', '')
            sanitized = sanitized.replace('\u202d', '')
            print("Warning: Input Sanitized ")
    return sanitized

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
    os.chdir('GroupMe Parser\\Groupme_Honors')

    print('Opening conversation file...')
    with open('conversation.json', 'r') as f:
        raw_cvn = json.load(f)
    
    cvn = conversation.conversation()

    #get message json data
    print('Opening message file...')
    with open('message.json', 'r', encoding=CHAR_DECOD, errors='ignore') as f:
        raw_msgs = json.load(f)

    os.chdir('...')
    #print(os.getcwd())
    
    #parse conversation to get conversation metadata and user list
    print('Parsing files...')
    cvn.parse(raw_cvn)
    msgs = []
    for msg in raw_msgs:
        tmp_msg = msgUnit.msgUnit()
        tmp_msg.parse(msg)
        msgs.append(tmp_msg)

    #write conversation metadata to output file
    print('Exporting data...')
    cvn_export = cvn.export()
    msg_export = '\n'.join([msg.s_simple_export() for msg in msgs])

    #delete conversation and message list
    print('Deleting data...')
    #del cvn
    #del msgs

    #write message list to output file
    print('Writing output to text file...')

    dict_msg = [msg.simple_export() for msg in msgs]
    s = []
    for msg in dict_msg:
        temp_member = cvn.get_member_by_id(msg['sender'])
        if temp_member is not None:
            #msg['sender'] = temp_member.nickname
            msg['sender'] = temp_member.name
        s.append([
            msg["sender"], 
            f' at {msg["time"]}: ', 
            msg["message"]
        ])

    col_width1 = max(len(word) for word in s[0]) + 2  # padding
    col_width2 = max(len(word) for word in s[1]) + 2  # padding
    col_width3 = max(len(word) for word in s[2]) + 2  # padding
    #msg_export = ''.join(f'{word[0]:<{col_width1}}{word[1]:<{col_width2}}{word[2]:<{col_width3}}' for word in s)
    #msg_export = ''.join([s[i][0].ljust(col_width1) + s[i][1].ljust(col_width2) + s[i][2].ljust(col_width3) for i in range(len(s))])
    #t = s[0][i].ljust(col_width1) + s[1][i].ljust(col_width2) + s[2][i].ljust(col_width3)
    #t = [(s[i][0]).rjust(col_width1) for i in range(len(s))]
    t = []
    for i in range(len(s)):
        r = ''
        if s[i][0] is not None:
            r += s[i][0]#.ljust(col_width1)
        if s[i][1] is not None:
            r += s[i][1]#.ljust(col_width2)
        if s[i][2] is not None:
            r += s[i][2]#.rjust(col_width3)
        if REVERSED:
            t.insert(0, r)
        else:
            t.append(r)

    msg_export = '\n'.join(t)


    # {
    #     'message': self.text,
    #     'sender': self.senderID,
    #     'time': self.time
    # }
    
    cvn_export = clean(cvn_export)
    msg_export = clean(msg_export)

    with open('parser_output.txt', 'w', encoding=CHAR_DECOD, errors='ignore') as f:
        f.write(cvn_export+'\n')        
        f.write(msg_export)
        
    print('Program complete.')


run()
with open('output.txt', 'r', encoding=CHAR_DECOD, errors='ignore') as f:
    raw = f.read()

'''
encoded_raw = raw.encode('utf-8')
#raw.decode('cp1252').encode('utf-8')
with open('output_utf8.txt', 'w', encoding='utf-8') as f:
    f.write(encoded_raw)
    # f.write(encoded_raw.decode('utf-8')) 
'''