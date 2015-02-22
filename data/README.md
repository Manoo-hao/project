#DATA

##Datasets

GDS4479_full.soft is the dataset that was used for the purposes of the 
BS32011 project. The dataset is about pseudomonas aeruginosa infection 
of different hosts. The folder gds2449 contains another dataset that was 
previously used but not carried forward for the project. It was kept for 
personal practice and educational purposes.

##Parser

Contains all files related to building a relational database. 
Functional_parser.py is the script of the parser used in order to 
retrieve and categorise data from the GEO dataset GDS4479_full.soft. All 
other filenames that contain 'parser' are non-functional or partially 
functional versions of the parser that were kept for personal 
educational purposes.

##.txt files

genes.txt, expression.txt, and probes.txt are files that are created by 
running the functional parser on GDS4479_full.soft. They contain 
tab-delimited data in a way suitable to read it into MySQL tables. 
isolates.txt and strains.txt are also tab-delimited files for the same 
purpose as the above files, but were created manually. samples.txt is a 
combined table of isolates.txt, and strains.txt and was also created 
manually. samples.txt is not used for building a relational database.

##Other files

msscript and testfile are files that were created by Dr Martin and 
remain for educational purposes.
