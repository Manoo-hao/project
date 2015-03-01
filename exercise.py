dna_file=open('genomic_dna.txt')
#open the file genomic_dna.txt in the current directory and store its contents in the variable dna_file
dna_seq=dna_file.read()replace('\n','')
#read the content of dna_file, replacing all newline character with nothing, and store the result in dna_seq.
intronfile=open('introns.txt','w') # open the file introns.txt for writing and store its contents in the variable intronfile.
exonfile=open('exons.txt','w') # open the file exons.txt for writing and store its contents in the variable exonfile.
exonfile.write(dna_seq[0:63]=dna_seq[90:]) #write into exonfile: contents of dna_seq up to but not including the 63rd character, and then from the 90th character until the end.
intronfile.write(dna_seq[63:90]) # write into intronfile: content of dna_seq from including the 63rd character up to but not including the 90th character
#close all used files
dna_file.close()
exonfile.close()
intronfile.close()
