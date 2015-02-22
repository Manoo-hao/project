fastafile=open("fasta.txt","w")
#Open the file fasta.txt in write mode and store its contents in the variable fastafile
fastafile.write(">ABC123"+"\n"+"ATCGTACGATCGATCGATCGCTAGACGTATCG"+"\n")
#Write into fastafile (which is the content of the newly created file fasta.txt) the header, a new line, the specified sequence, and another new line.
fastafile.write(">DEF456"+"\n"+"actgatcgacgacgatcgatcgatcacgact".upper()+"\n")
#Write into fastafile the header, a new line, the specified sequence in upper case, and another new line.
fastafile.write(">HIJ789"+"\n"+"ACTGAC-ACTGT--ACTGTA----CATGTG".replace("-","")+"\n")
#Write into fastafile the header, a new line, the specified sequence where every gap (-) is replaced by nothing, i.e. removed, and another new line.
fastafile.close()
#Close the open file.
print("Done")
#Print 'Done' in order to confirm that the script was executed successfully.