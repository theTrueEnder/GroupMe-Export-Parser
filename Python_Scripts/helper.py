import emoji
import json
import traceback

''' Append a given error message to error-log.txt '''
def write_to_error_log(error_msg, traceback_msg=''):
    with open('error-log.txt', 'a') as f:
        f.write(error_msg + '\n' + traceback_msg)

''' Clear the contents of error-log.txt '''
def clear_error_log():
    open('error-log.txt', 'w').close()

# Remove bad characters created from encoding conversion
def clean_text(dirty):
    if dirty is not None:
        #if "´" or "’" or "`" or "�" or "“" or "”" or '\u202c' or '\u202d' in dirty:
        clean = dirty
        # clean = emoji.demojize(clean.decode("UTF-8", errors="ignore"))
        clean = emoji.demojize(clean)
        clean = clean.replace("…", "...")
        clean = clean.replace("￼", "<?>")
        clean = clean.replace("´", "'")
        clean = clean.replace("’", "'")
        clean = clean.replace("`", "'")
        clean = clean.replace("�", '<?>')
        clean = clean.replace("“", '\\"')
        clean = clean.replace("”", '\\"')
        clean = clean.replace("—", '-')
        
        clean = clean.replace('\u202c', '')
        clean = clean.replace('\u202d', '')
        return clean
    else:
        return None
    
    
def get_clean_json(path):
    strlines = []
    lines = []
    with open(path, 'rb') as f:
        lines = f.readlines()

    ctr = 0
    for line in lines:
        ctr += 1
        
        # skip line if it's empty or whitespace
        if line in (b"", b"\r", b"\n", b"\r\n"): continue
        
        try:
            # call clean_text on the decoded line (decode converts from the raw bytes to a string. It ignores any
            # conversion errors, because clean_text should fix all of them), then get rid of any \r or \n bytes
            line = clean_text(line.decode("UTF8", errors="ignore"))
            line = line.replace("\r", "")
            line = line.replace("\n", "")
            strlines.append(line)
            
        except UnicodeEncodeError as e:
            tbmsg = traceback.format_exc()
            pos_loc = tbmsg.index("in position ") + 12  #TODO check that this is the right index
            colon_loc = tbmsg.index(":", pos_loc)
            position = tbmsg[pos_loc:colon_loc]            
            
            emsg = f'Error: undefined character at Line {ctr}, Position {position} of file {path}'
            print(emsg)
            write_to_error_log(emsg, tbmsg)
            import sys
            sys.exit(1)

    jstring = '\n'.join(strlines)
    return json.loads(jstring)