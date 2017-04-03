# Ymap_mean_ploidy.py

### [Ymap](http://lovelace.cs.umn.edu/Ymap/) is a software that enables the user to visualize DDRadseq data acquired from the commensal fungus C. albicans strain SC5314 in a succinct and compact format. The software allows visualization of genomic traits like ploidy, copy number variation (CNV) and can also be used to find recombination events that result from pseudomeiosis that occurs during mating. 

### This program will calculate the average CNV or ploidy across every chromosome in a dataset acquired from Ymap data, or it can calculate the CNV and ploidy in a specific location. 

### Problems and Solutions: 

1. Some CNV bins from Ymap list "0.0" this may be the absence of real data or problem with alignment. 
 Fix: The user can choose to include or exclude the CNV data with 0.0 by changing the "1" to a "0" in the Grand_File_Parser and Parse_File initiation lines. I would like to add this so it can be changed through command options and include some measure of its effect. 
 
2. Skips the remaining part of the file when an issue with formatting arises
 

### Use: 

There are two seperate options for obtaining average CNV/ploidies: 

Specific average: this requires the file name, chromosome name, and base pair start and end position the average is to be calculated from:
 `$ python3 ymap_mean_cnv.py input_file.gff3.txt chrR 867 5309`
           
General average: requires that the ymap_mean_cnv.py file is placed in the same directory as all files that data is to be taken from:
`$ python3 ymap_mean_cnv.py` or `$python3 ymap_mean_cnv.py output_file_name.csv`. The first will use the day's date as a default name for the file and the second will use the given name for the file. 


### Input format:

The input required is a variation of GFF3:

 `##gff-version 3

 [CNV]
 glyph = xyplot
 graph_type = histogram
 fgcolor = black
 bgcolor = black
 height = 50
 min_score = 0
 max_score = 4
 label = 1
 bump = 0
 scale = none
 balloon hover = Estimated CNV is $description
 key = 7069_C12_vs_spo11marked CNVs

 Ca21chr1_C_albicans_SC5314	Ymap	CNV	1	4555	0.0	.	.	Note=0.0
 Ca21chr1_C_albicans_SC5314	Ymap	CNV	4556	9110	0.0	.	.	Note=0.0
 Ca21chr1_C_albicans_SC5314	Ymap	CNV	9111	13665	0.0	.	.	Note=0.0
 Ca21chr1_C_albicans_SC5314	Ymap	CNV	13666	18220	3.1	.	.	Note=3.1
 Ca21chr1_C_albicans_SC5314	Ymap	CNV	18221	22775	2.4	.	.	Note=2.4
 Ca21chr1_C_albicans_SC5314	Ymap	CNV	22776	27330	2.6	.	.	Note=2.6
 Ca21chr1_C_albicans_SC5314	Ymap	CNV	27331	31885	0.0	.	.	Note=0.0
 Ca21chr1_C_albicans_SC5314	Ymap	CNV	31886	36440	2.3	.	.	Note=2.3
 Ca21chr1_C_albicans_SC5314	Ymap	CNV	36441	40995	2.9	.	.	Note=2.9
 Ca21chr1_C_albicans_SC5314	Ymap	CNV	40996	45550	0.0	.	.	Note=0.0
 Ca21chr1_C_albicans_SC5314	Ymap	CNV	45551	50105	0.0	.	.	Note=0.0
 Ca21chr1_C_albicans_SC5314	Ymap	CNV	50106	54660	2.5	.	.	Note=2.5
 Ca21chr1_C_albicans_SC5314	Ymap	CNV	54661	59215	2.9	.	.	Note=2.9
 Ca21chr1_C_albicans_SC5314	Ymap	CNV	59216	63770	0.0	.	.	Note=0.0
 Ca21chr1_C_albicans_SC5314	Ymap	CNV	63771	68325	3.2	.	.	Note=3.2
 Ca21chr1_C_albicans_SC5314	Ymap	CNV	68326	72880	2.9	.	.	Note=2.9
 Ca21chr1_C_albicans_SC5314	Ymap	CNV	72881	77435	2.5	.	.	Note=2.5
 Ca21chr1_C_albicans_SC5314	Ymap	CNV	77436	81990	2.5	.	.	Note=2.5`
