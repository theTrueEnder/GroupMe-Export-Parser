import glob
import os
import shutil

parent_path = r'C:\\Users\\manic\\Downloads\\gm_export_20_dec' + r'\\'

# make sure the zip files exist
if glob.glob(parent_path + "[0-9][0-9][0-9][0-9][0-9]") is None:
    print('Error: No export folders of the pattern "#####.zip" found')
    exit(1)
    
# gets all of the 2nd-level folders (the ones below 00001) and makes a set of them
# this removes duplicates and is the list of all the GM exports in the batch
subfolders = glob.glob(parent_path + "[0-9][0-9][0-9][0-9][0-9]\\*")
exports = set([f[f.rfind('\\')+1:] for f in subfolders])

# create an export folder for each export of the batch 
newpath = parent_path + r'gm-export-'
for export in exports:
    if os.path.exists(newpath + export):
        print(f'Error: export folder "gm-export-{export}" already exists')
        exit(1)
    else:
        os.makedirs(newpath + export)

# deal with folders
for folder in subfolders:
    export_dir = parent_path + f'gm-export-{folder[folder.rfind('\\')+1:]}'
    contents = [f[f.rfind('\\')+1:] for f in glob.glob(folder + '\\*')]
    
    # move the files to the respective export folder if they're found
    if 'conversation.json' in contents:
        shutil.copy(folder + '\\conversation.json', export_dir)
    if 'message.json' in contents:
        shutil.copy(folder + '\\message.json', export_dir)
    if 'poll.json' in contents:
        shutil.copy(folder + '\\poll.json', export_dir)
        
    # move entire folder if doesn't exist; otherwise just move the contents
    if 'likes' in contents:
        if os.path.exists(export_dir + '\\likes'):
            [shutil.copy(file, export_dir + '\\likes') for file in glob.glob(folder + '\\likes\\*')]
        else:
            shutil.copytree(folder + '\\likes', export_dir + '\\likes')

    if 'gallery' in contents:
        if os.path.exists(export_dir + '\\gallery'):
            [shutil.copy(file, export_dir + '\\gallery') for file in glob.glob(folder + '\\gallery\\*')]
        else:
            shutil.copytree(folder + '\\gallery', export_dir + '\\gallery')

print('Folders combined!')