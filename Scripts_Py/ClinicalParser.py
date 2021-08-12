#! /bin/python3.9.5

import sys
import json
import numpy as np

## Script parses a clinical data JSON and returns tab delimited array

## Checks use and opens files
if len(sys.argv) < 3 :
	print('Usage: ClincalParser.py Clincal.JSON outfile.tsv')
	sys.exit()
else :
	data = json.load(open(sys.argv[1], 'r'))
	clinout = open(sys.argv[2], 'w')

## Make numpy array starting with header
clinical=np.array(['CaseID','Race','Ethnicity','Vital_Status','Smoker_Status']) #blank np array

## Parser is easliy added to if you have any specific variables to extract

## Parse through JSON
for i in data:
	caseID = i['exposures'][0]['submitter_id']
	caseID = caseID[:-4] #Discard key end of caseID
	race = i['demographic']['race']
	ethnicity = i['demographic']['ethnicity']
	vitals = i['demographic']['vital_status']
	smoker = i['exposures'][0]['tobacco_smoking_status']
	clinical=np.vstack((clinical,[caseID,race,ethnicity,vitals,smoker])) #stack values in row

## Write numpy array to tab delimited file
np.savetxt(clinout, clinical, fmt='%s', delimiter='\t')

## Close file
clinout.close()


