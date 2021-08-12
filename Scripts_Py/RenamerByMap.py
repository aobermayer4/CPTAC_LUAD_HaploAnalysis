#! /bin/python3.9.5

import sys
import os
import pandas as pd

## Script developed for renaming CPTAC BAM files and log files within

if len(sys.argv) < 3 :
	print('Usage: RenamerByMap.py /path/to/Sample/Folders/ SampleSheet.tsv')
	sys.exit()
else :
	filepath=sys.argv[1]
	namemap=open(sys.argv[2], 'r')

## make pandas df with namemap
namemap=pd.read_csv(namemap, sep='\t', index_col=0)

## will rename from deepest file out to folders in directory
#  rename is based off of 'Case ID' and first character of 'Sample Type' found in 'namemap' + extensions

for folder in os.listdir(filepath) : #loop through given path for sub-directories
	if len(str(folder)) < 15 : #ignores names that are already adjusted
		continue
	else :
		#loop through folders and find possible subfolder to loop through
		for file in os.listdir(os.path.join(filepath, folder)) : #loop through folders for files/sub-dir
			if os.path.isdir(os.path.join(filepath, folder, file)) == True : #if sub-dir exists
				for file2 in os.listdir(os.path.join(filepath,folder, file)) : #loop through sub-dir for files
					ext=file2.split('.')[1:] #extract file extensions
					ext='.'.join(ext) #join extensions
					newID=namemap.at[folder,'Case ID'] #extracts CaseID from namemap
					if ',' in newID : #checks for comma in name and only extracts CaseID  first label
						newID=newID.split(',')[0]
					src=os.path.join(filepath, folder, file, file2) #old path to file
					dst=os.path.join(filepath, folder, file, #new path to file
						newID+'_'+namemap.at[folder,'Sample Type'][0]+'.'+str(ext))
					if os.path.exists(dst) == True :
						dst=os.path.join(filepath, folder, file, #new path to file
						newID+'_'+namemap.at[folder,'Sample Type'][0]+str(2)+'.'+str(ext))
					os.rename(src,dst) #rename function
			else :
				#rename file in main folder
				ext=file.split('.')[1:]
				ext='.'.join(ext)
				newID=namemap.at[folder,'Case ID']
				if ',' in newID :
					newID=newID.split(',')[0]
				src=os.path.join(filepath, folder, file)
				dst=os.path.join(filepath, folder,
					newID+'_'+namemap.at[folder,'Sample Type'][0]+'.'+str(ext))
				if os.path.exists(dst) == True :
					dst=os.path.join(filepath, folder,
					newID+'_'+namemap.at[folder,'Sample Type'][0]+str(2)+'.'+str(ext))
				os.rename(src,dst)
		newID=namemap.at[folder,'Case ID']
		#rename folder
		if ',' in newID :
			newID=newID.split(',')[0]
		src=os.path.join(filepath, folder)
		dst=os.path.join(filepath, newID+'_'+namemap.at[folder,'Sample Type'][0])
		if os.path.exists(dst) == True :
			dst=os.path.join(filepath, newID+'_'+namemap.at[folder,'Sample Type'][0]+str(2))
		foldernew=os.rename(src, dst)
