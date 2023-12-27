import emoji
import json
import traceback

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
        if line in (b"", b"\r", b"\n", b"\r\n"): continue
        
        # debug.focusWindowOnBreak: false
        try:
            line = clean_text(line.decode("UTF8", errors="ignore"))
            line = line.replace("\r", "")
            line = line.replace("\n", "")
            strlines.append(line)
            
        except UnicodeEncodeError:
            emsg = traceback.format_exc()
            pos_loc = emsg.index("in position ") + 12  #TODO check that this is the right index
            colon_loc = emsg.index(":", pos_loc)
            position = emsg[pos_loc:colon_loc]
            print(f'Error: undefined character at Line {ctr}, Position {position} of file {path}\n')
            import sys
            sys.exit(1)

    jstring = '\n'.join(strlines)
    return json.loads(jstring)