
"""
This file provide some tools to manage the mardown documentation i wrote
"""

myTextFile = """-----
title: MySQL Reference
description: A little MySQL reference.
created: 28-11-2007 00:00:00
modified: 28-11-2007 00:00:00
keywords: database, mysql, website, internet
lang: en
-----

# David Van Mosselbeen Notes

This is just a bunch of personal notes i made for my specific needs. These are all in Markdown format and shouldn't be 
shared as is as some files could have some private information. (Needs to be checked !)

"""

# Convert the string to a list
myTextFileList = []
for i in myTextFile:
    myTextFileList.append(i)

print("myTextFileList is %s chars long !" % len(myTextFileList))

def checkHeader(thatText):
    "Check if the header start with 5 dashes and contains all the attributes."
    dashCount = 0
    for character in thatText:
        # print(character)
        if character =="-": # Level 1
            print ("Level 1")
            # print("*** is a DASH : %s ***" % character)
            dashCount = dashCount + 1
            print("*** Dashcount so far: %s " % dashCount)
            if character == "-": # Level 2
                print ('Level 2')
                if character == "-": # Level 3
                    print ("Level 3")
                    if character == "-": # Level 4
                        print ("Level 4")
                        if character == "-": # Level 5
                            print ("Level 5")
    print("Totals DASHES: %s " % dashCount)


print(type(myTextFile))

# Start the thing
checkHeader(myTextFile)