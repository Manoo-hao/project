dna=open ('genomic_dna.txt') #Open the file genomic_dna.txt present in the folder and store it in the variable dna
sequence=dna.read() #create the variable sequence and store the content of the file dna in it
intronfile=open("introns.txt", "w") #create the file introns.txt in write mode and store its content in the variable intronfile
exonfile=open("exons.txt", "w") #create the file exons.txt in write mode and store its content in the variable exonfile
intronfile.write(sequence[64:91]+" ") #write into intronfile (which is a variable storing the content of introns.txt) the content of sequence from the first character up to but not including the 64th character, etc
exonfile.write(sequence[:64]+" "+sequence[91:]) #write into the variable exonfile (which is a variable storing the content of exons.txt) the content of sequence with the given character-numbers
dna.close() #close opened file
intronfile.close() #close opened file
exonfile.close() #close opened file
print("Done") #print the word Done to be able to see when the script has been successfully executed