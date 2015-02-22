fastafile=open("fasta.txt","w")
#open the file fasta.txt in write mode and store its contents in the variable fastafile
fastafile.write(">ABC123"+"\n"+"ATCGTACGATCGATCGATCGCTAGACGTATCG"+"\n")
#write into fastafile (which is the content of the newly created file fasta.txt) the header, new line, and sequence
fastafile.write(">DEF456"+"\n"+"actgatcgacgacgatcgatcgatcacgact".upper()+"\n")
#write into fastafile the header, new line, and sequence in upper case
fastafile.write(">HIJ789"+"\n"+"ACTGAC-ACTGT--ACTGTA----CATGTG".replace("-","")+"\n")
#write into fastafile the header, new line, and sequence, replacing every - with nothing
fastafile.close()
#close the file
print("Done")