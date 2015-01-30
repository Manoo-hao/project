fastafile1=open("ABC123.txt","w")
fastafile2=open("DEF456.txt","w")
fastafile3=open("HIJ789.txt","w")
#open the files ABC123.txt, DEF456.txt, and HIJ789.txt in write-mode and store their contents in the variables fastafile1, fastafile2, and fastafile3 respectively
fastafile1.write(">ABC123"+"\n"+"ATCGTACGATCGATCGATCGCTAGACGTATCG"+"\n")
#write into fastafile1 (which is the content of the newly created file ABC123.txt) the header, new line, and sequence
fastafile2.write(">DEF456"+"\n"+"actgatcgacgacgatcgatcgatcacgact".upper()+"\n")
#write into fastafile2 (which is the content of the newly created file DEF456.txt) the header, new line, and sequence in upper case
fastafile3.write(">HIJ789"+"\n"+"ACTGAC-ACTGT--ACTGTA----CATGTG".replace("-","")+"\n")
#write into fastafile3 (which is the content of the newly created file HIJ789.txt) the header, new line, and sequence, replacing every - with nothing
fastafile1.close()
fastafile2.close()
fastafile3.close()
print("Done")

