#
#
# Automattically sort loopsdrawings
#
# Author: Håvard Syslak
#
# Date: 19.07.2020


# -----[ Import stuff ]----- 

import os
import PyPDF2
import re
import shutil


# -----[ global variables ]-----

substations = ["04", "05", "06", "07", "08", "E", "W", "V", "D", "TA", "TB", "YA", "YB", "B", "J", "C", "P", "BF", "PA", "YD", "TD", "CANCELLED"]
cabinetName = ["MC", "DC", "C"]
#regexTag= "/d2-?[A-Z]-?/d3"

# -----[ regex stuff ]-----

# Substation regex
regexSubstation ="(" + "|".join(substations) + ")-(" + "|".join(cabinetName) + r")-[0-9]{2}"
regexUtestasjon = r"OUTSTATION\s(" + "|".join([s.replace('0','') for s in substations]) + ")"
cancelled = "CANCELLED"
regexTag = r"[0-9]{2}-[A-Z]{2}-[0-9]{3}[A-Z0-9]?"

print(regexSubstation)
print(regexTag)

# Make directory for each substation.
for s in substations:
    if not os.path.isdir(s):
        os.mkdir(s)


# Make a list of all PDF files in current working dir.
pdffiles = []

for filename in os.listdir("."):
    if filename.endswith(".pdf")  or filename.endswith(".PDF"):
        pdffiles.append(filename)

print(pdffiles)


# loop trough and open each file.

for filename in pdffiles:
    print()
    obj =  open(filename, "rb")
    pdfReader = PyPDF2.PdfFileReader(obj)
    pages = pdfReader.getNumPages()

    pageobj = pdfReader.getPage(0)

    text = (pageobj.extractText()) 
#    print("text: " + str(text))

# If drawing is cannceld move to cancelled dir.
    match = re.search(cancelled, text)
    if match == None:
        
        # look for substation with this format: "06-C-08"
        match = re.search(regexSubstation, text)
        print("match: " + str(match))
        if match == None:

            # Look for substation with this format: "OUTSTATION 6"
            match = re.search(regexUtestasjon, text)
            if match == None:
                
                # If no match is found we skip the file.
                continue

    print(match)

    # If multiple substations are found we take the first one. 
    matchSubstation = match.group(0)
    
    matchTag = re.findall(regexTag, text)
    
   # print(text)
   
    print("length tagNr "+ str(len(matchTag)))    

    
    print("\nOLD FILENAME: " + str(filename) + "\n")
    
    # prevent error from having list with no elements
    if len(matchTag) > 0:
        tagNr = matchTag[0]
        newFilename = str(tagNr) + ".pdf"
        print("new filename: "+ str(newFilename))
    

    else:
        tagNr = filename + ".pdf"
        newFilename = None    
    
    # Convert match to string.
    substation = str(matchSubstation)
    print("match substatuion: " +  str(substation))
    print("matchtag: " + str(matchTag))
    print("new filename: " + str(newFilename))

  
    # Close file so we can rename and move it. 
    obj.close()

    # Adds a 0 to format "OUTSTATION 6"
    if " " in substation:
        substation = substation.split(' ')[1]
        if substation.isdigit():
            substation = "0" + substation
            
    # Splits the substation at first "-"     
    substation = substation.split('-')[0]
    print("Substation: " + substation)

    try:
        # if no tag is found we keep the existing name and move it.
        if newFilename == None: 
            shutil.move(filename, './' + substation)
        else:
            # Rename and move file.
            os.rename(filename, newFilename)
            shutil.move(newFilename, './' + substation)
    except:
        # If moving or renaming fails, print failed, continue.
        print("Failed to move file " + str(filename))
        continue
