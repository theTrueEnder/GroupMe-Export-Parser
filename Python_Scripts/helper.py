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