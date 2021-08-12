# Mitochondrial Haplogroup Association with Non-Small Cell Lung Cancer Patients
## Background Information
### Mitochondrial DNA Overview

![mtDNA](https://upload.wikimedia.org/wikipedia/commons/thumb/1/15/Map_of_the_human_mitochondrial_genome.svg/504px-Map_of_the_human_mitochondrial_genome.svg.png "This picture is a work by Emmanuel Douzery.")

*This picture is a work by Emmanuel Douzery*

* Small circular DNA made up of 16,569 base pairs
* Multiple copies within the mitochondrion organelles of the cell
* Contains 37 genes
	* 2 rRNAs
	* 22 tRNAs
	* 13 Proteins
		* Encoded proteins are involved in **oxidative phosphorylation** process, generating energy through ATP production
* Economically packed with overlapping genes and a very minimal non-coding region
* Maternally inherited

### Mitochondrial Haplogroup Overview

![mtDNAhaplogroup](https://blog.23andme.com/wp-content/uploads/2017/05/ttam_major_haplogroup_migrations-e1496416263453.png)

*This image is of mtDNA Haplogroup Migration Map from 23andMeBlog*

* Mitochondrial Eve lived around 200,000 years ago and is considered to be living humans' most recent matralinial common ancestor
	* Originating in Southeast Africa
*  The accumulation of mutations in our mtDNA allow for the traceback of our lineage
	* Single Nucleotide Polymorphisms (SNPs) can be detected ar specific locations in the mitochondrial genome which can be grouped and assigned to global populations
	* The highly polymorphic, non-coding control region in the D-loop of the mtDNA is also known as the hypervariable region and is best for determining mtDNA lineage
* Haplogroup nomenclature began in North America with A, B, C, and D and branched out through all the letters of the alphabet
	* The native North American haplogroups are branched out from Asia due to early migration

### Non-Small Cell Lung Cancer (NSCLC)

* NSCLC accounts for 80%-85% of lung cancers
	* Lung Adenocarcinoma (LUAD) is the most common malignancy
* Heavily related to tobacco smoking but also the most frequent lung cancer found in “never-smokers”
* Tobacco carcinogenesis is believed to play a role in the vulnerable mtDNA through alterations by way of somatic mutations

# Project Goals

* Assign mitochondrial DNA to haplogroups
* Perform and compare global differential gene expression analysis across haplogroups
* Examine overall impact haplogroups may have on NSCLC LUAD outcome, stage, and metabolism

# Project Workflow

* Obtain controlled access data from the GDC Data Portal
* Load data into cluster environment for read depth analysis
* Generate file formats: MPG, VCF, FASTA, and HSD
* Call probable haplogroups
* Integrate haplogroups with participant clinical data
* Perform RNA-seq analysis with high dimensional data visualization

# Data Fetching

* Obtained whole exome, aligned, paired-end sequenced reads from GDC Data Portal
	* TCGA - The Cancer Genome Atlas
	* CPTAC - Clinical Proteomic Tumor Analysis Consortium
* Loaded data to HPC with GDC data trasnfer command
```linux
gdc-client download -t <token> -m <manifest>
```

