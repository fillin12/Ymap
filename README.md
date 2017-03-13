# Ymap_mean_ploidy.py

### [Ymap](http://lovelace.cs.umn.edu/Ymap/) is a software that enables the user to visualize DDRadseq data acquired from the commensal fungus C. albicans strain SC5314 in a succinct and compact format. The software allows visualization of genomic traits like ploidy, copy number variation (CNV) and can also be used to find recombination events that result from pseudomeiosis that occurs during mating. 

### This program will calculate the average CNV or ploidy across every chromosome in a dataset acquired from Ymap data, or it can calculate the CNV and ploidy in a specific location. 

### Problems and Solutions: 

1. Some CNV bins from Ymap list "0.0" this may be the absence of real data or problem with alignment. 
 Fix: The user can choose to include or exclude the CNV data with 0.0
 
2. Skips the remaining part of the file when an issue with formatting arises
 

### Use: 
There are two seperate options for obtaining average CNV/ploidies: 

Specific average: this requires the file name, chromosome name, and base pair start and end position the average is to be calculated from:
 `$ python3 ymap_mean_cnv.py input_file.gff3.txt chrR 867 5309`
           
General average: requires that the ymap_mean_cnv.py file is placed in the same directory as all files that data is to be taken from:
`$ python3 ymap_mean_cnv.py`
