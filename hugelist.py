from pyw3x import archive
from collections import OrderedDict
from pyw3x import fileutils
from tkinter.filedialog import askopenfilename
import sys
import io
import os
# all files that comma is an important character
#commachecker = ['war3map.j', 'war3map.w3i', 'war3mapMisc.txt', 'war3mapSkin.txt']
mode = 'r' #Mode Used for pyw3x, pretty useless
hugelist = [] #list with all matches before putting them into a dictionary
import re #Script uses regex to find matches
filename = askopenfilename() #Prompts the user to choose a map file and makes a path.
filenamebase = os.path.basename(os.path.normpath(filename)) #The exact map name with no path
listfile = 'grape2.txt'
print(filename) #prints the map opened

#Listfile for extracting strings from the map
with open('grape2.txt', 'r', encoding='utf-8', errors='ignore') as f:
        files = f.read().splitlines()
#3rd party module for opening maps and extracting files from the listfile.
with archive.open_archive(filename, mode) as a:
    outdir = filenamebase
    a.extract_all_files(outdir, listfile)

dir = os.path.dirname(__file__)
outlocation = os.path.join(dir,filenamebase)

os.chdir(outlocation) #Changes director to outlocation
for x in files: #iterates through listfile
    print(x) #print every file it iterates through
    try:
        temp = open(x, encoding='utf-8', errors='ignore').read().splitlines()
    except Exception:
        print('Could not find that file')
        continue
    #opens everyfile in the list file
    ##hugelist.append(x+'***!') #Appends the filename and a delimiter for our list
    for y in temp:
        if x == 'war3map.j':
            for abe in re.findall(r'[\u4e00-\u9fff\002C\uFF0C]+[\u4e00-\u9fffu\002C\uFF0C\+\%\s\d]+[\u4e00-\u9fff\002C\uFF0C\s\d]+|[\u4e00-\u9fff]+', y):
                if '.mdl' in y: #Checks for mdl and mdx are on the line and skips them
                    
                    continue
                elif '.mdx' in y: #Checks for mdl and mdx are on the line and skips them
                        continue
                elif 'call DisplayTimedTextToForce' in y:
                    hugelist.append(abe)
                    
            
                    
                
                    
        else:
            for abe in re.findall(r'[\u4e00-\u9fff\002C\uFF0C]+[\u4e00-\u9fffu\002C\uFF0C\+\%\s\d+\!\@\#\$\%\^\&\*Xx\[\{\]\}\;\:\'\"\<\>\-]+[\u4e00-\u9fff\002C\uFF0C\s\d]+|[\u4e00-\u9fff]+', y): #morepowerfulsearch for object files
            
                if '.mdl' in y: #Checks for mdl and mdx are on the line and skips them
                    continue
                elif '.mdx' in y: #Checks for mdl and mdx are on the line and skips them
                        continue
                else:
                    hugelist.append(abe)
count = 0
        
hugelist = list(dict.fromkeys(hugelist))
#removes duplicates in a one liner

hugelist = sorted(hugelist, key=len, reverse=True)

#writes text to outfile
with open('your_file.txt', 'w', encoding='utf-8') as f:
    for item in hugelist:

        f.write("%s\n" % item)


    



