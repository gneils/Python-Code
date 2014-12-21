import csv, sys, re, msvcrt, time
import datetime as DT
import os
import shutil

wpJunk = ( '50x150', '-90x90', '00x200', '00x300', '19x212', '19x319', '70x600')

startTime = DT.datetime.now()

print ( "Program start : %s" % startTime )

selectedFolder = 'C:/Users/Greg/Desktop/delete/upper/'

outputFolder   = 'C:/Users/Greg/Desktop/delete/lower/'

allFiles = os.listdir( selectedFolder )

for eachFileName in allFiles:
	originalFileName = selectedFolder + eachFileName

	newName = eachFileName

	print (originalFileName)

	modifiedFile = 0

# change to lower case
	if ( eachFileName.lower() != selectedFolder + eachFileName) :
		newName =  newName.lower() 
		modifiedFile = 1

	if ( '-img' in newName )	: 
		newName =  newName.replace( "-img", "")
		modifiedFile = 1

	if ( '_' in newName )	: 
		newName =  newName.replace( "_", "-")
		modifiedFile = 1
# look for spaces
	if ( ' ' in newName )	: 
		newName =  newName.replace( " ", "-")
		modifiedFile = 1

	fileNameEndsIn = eachFileName[ -10: -4] 
	if ( fileNameEndsIn in  wpJunk ) :
		print ('WordPress extra files: ' + originalFileName )
	

# Prepend a prefix to the file name, must modify code below to work
	customPrefix = 'snowplow-'
	if ( 'addPrefix' == 'NOaddPrefix' ):
		newName = customPrefix  + eachFileName
		modifiedFile = 1
	
# if the name was changed copy the file to the new foler	
	if ( modifiedFile == 1 ):
		print ('Modified Name: ' + newName )
		newName = outputFolder + newName
		shutil.copy2( originalFileName, newName )

input( "press any key to exit" )
exit()
