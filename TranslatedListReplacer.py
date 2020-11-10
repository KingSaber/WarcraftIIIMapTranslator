#TranslatedListReplacer requires you to run hugelist.py and to create a translated text document called your_file.txt. I use google translated documents to translate at the moment.
from pyw3x import archive
from itertools import zip_longest
import errno
from collections import OrderedDict
from pyw3x import fileutils
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import askdirectory
import io
import os
import os.path
mode = 'r'
hugelist = []
mylist = []
import re
translist=[]
filename = askopenfilename()
filenamebase = os.path.basename(os.path.normpath(filename)) #The exact map name with no path


listfile = 'grape2.txt'


with open('grape2.txt', 'r', encoding='utf-8', errors='ignore') as f:
        files = f.read().splitlines()

os.chdir(filenamebase)


Translated = open('Translated.txt', 'rb').read().splitlines()
Untranslated = open('your_file.txt', 'rb').read().splitlines()
changecomma = 0 #change commas count
#Files that need full utf-8 comma
CommaFullFiles = ['Units\CampaignAbilityStrings.txt', 'Units\CampaignUnitStrings.txt', 'Units\ItemStrings.txt']



filenamebase = os.path.basename(os.path.normpath(filename))
print(filenamebase)

for y in files:
    try:
        file = open(y, 'rb').read()
    except Exception:
        continue
    count = 0
    Translated = open('Translated.txt', 'rb').read().splitlines()
    if y in CommaFullFiles:
        
    
        Translated = open('Translated.txt', 'rb').read()
        Translated = re.sub(','.encode(), '，'.encode(), Translated)
        Translated = Translated.splitlines()
        
        print('yes')
    
    for X in Untranslated:

        file = re.sub(re.escape(Untranslated[count]), Translated[count], file)
        count = count + 1
        if count == len(Untranslated):
            if not os.path.exists(os.path.dirname(os.path.basename(os.path.normpath(filename)))):
                try:
                    os.makedirs(filenamebase)
                except OSError as exc: # Guard against race condition
                    if exc.errno != errno.EEXIST:
                        raise
                thefile = os.path.basename(os.path.normpath(y))
                MyFile=open(thefile,'wb')
                print(thefile)
                MyFile.write(file)    
                MyFile.close()
                
         




        
            
  
        

