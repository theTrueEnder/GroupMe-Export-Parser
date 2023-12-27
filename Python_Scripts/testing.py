import json
from helper import clean_text, get_clean_json
import emoji
lines = []
raw_cvn = None


get_clean_json("C:/Users/manic/Documents/GitHub/GroupMe-Export-Parser/Groupme_Honors/"  + 'edited-conversation.json')

'''
with open("C:/Users/manic/Documents/GitHub/GroupMe-Export-Parser/Groupme_Honors/"  + 'message.json', 'rb') as f:
    lines = f.readlines()
    ctr = 1
    for line in lines:
        a = line.decode("UTF8", errors="ignore")
        b = emoji.demojize(line.decode("UTF8", errors="ignore"))
        line = b
        line = line.replace("…", "...")
        line = line.replace("￼", "<?>")
        if a != b:
            try:
                print(line)
            except Exception:
                print('Line', ctr)
                import traceback
                traceback.print_exc()
                import sys
                sys.exit(1)
                
        ctr += 1
'''