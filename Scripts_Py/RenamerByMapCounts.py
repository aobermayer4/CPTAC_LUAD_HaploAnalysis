#! /bin/python3.9.5

import sys
import os
import pandas as pd

## This scrip is for renaming CPTAC study HTseq count files AFTER UNZIPPING

if len(sys.argv) < 3 :
	print('Usage: RenamerByMapCounts.py /path/to/Sample/Folders/ SampleSheet.tsv')
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
		#remaing sub-directories and files within (e.g. log folders)
		for file in os.listdir(os.path.join(filepath, folder)) : #loop through folders for files/sub-dir
			if os.path.isdir(os.path.join(filepath, folder, file)) == True : #if sub-dir exists
				for file2 in os.listdir(os.path.join(filepath,folder, file)) : #loop through sub-dir for files
					ext=file2.split('.')[1:] #extract file extensions
					ext='.'.join(ext) #join extensions
					newID=namemap.at[folder,'Case ID'] #extract CaseID from namemap
					if ',' in newID : #looks for names with 2 possible IDs and only keeps the first one
						newID=newID.split(',')[0]
					src=os.path.join(filepath, folder, file, file2) #old path to file
					dst=os.path.join(filepath, folder, file, #new path to file
						newID+'_'+namemap.at[folder,'Sample Type'][0]+'.'+str(ext))
					if os.path.exists(dst) == True : #if duplicate file a 2 is added (special case, not typically used)
						dst=os.path.join(filepath, folder, file, #new path to file
						newID+'_'+namemap.at[folder,'Sample Type'][0]+str(2)+'.'+str(ext))
					os.rename(src,dst) #rename function
			else :
				#renaming files in main sample directory
				if 'annotation' in file : #dont change annotation file name
					continue
				else :
					ext=file.split('.') #makes sure to keep file extension
					if 'htseq_counts' in ext : #removed htseq_counts from sample name
						ext=ext[2:]
						ext='.'.join(ext)
					else : #for files without htseq_counts in name
						ext=ext[1:]
						ext='.'.join(ext)
					newID=namemap.at[folder,'Case ID'] #get caseID from namemap
					if ',' in newID : #checks if comma in name
						newID=newID.split(',')[0]
					src=os.path.join(filepath, folder, file)
					dst=os.path.join(filepath, folder,
						newID+'_'+namemap.at[folder,'Sample Type'][0]+'.'+str(ext))
					if os.path.exists(dst) == True : #checks if file already exists
						dst=os.path.join(filepath, folder,
						newID+'_'+namemap.at[folder,'Sample Type'][0]+str(2)+'.'+str(ext))
					os.rename(src,dst)
		#renaming folder
		newID=namemap.at[folder,'Case ID']
		if ',' in newID : #checks if comma in name
			newID=newID.split(',')[0]
		src=os.path.join(filepath, folder)
		dst=os.path.join(filepath, newID+'_'+namemap.at[folder,'Sample Type'][0])
		if os.path.exists(dst) == True : #checks if file already exists
			dst=os.path.join(filepath, newID+'_'+namemap.at[folder,'Sample Type'][0]+str(2))
		foldernew=os.rename(src, dst)
