fh=open('samples.txt','w')
samples="GSM567668,GSM567669,GSM567670,GSM567671,GSM567666,GSM567667,GSM567674,GSM567675,GSM567672,GSM567673".split(",")
experiment="PBCLOp10"
for s in samples:
   fh.write("%s\t%s\n"%(s,experiment))

