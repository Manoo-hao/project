fh=open('samples.txt','a')
samples="GSM567686,GSM567687,GSM567676,GSM567677,GSM567666,GSM567667".split(",")
experiment="in vitro planktonic (control)"
for s in samples:
   fh.write("%s\t%s\n"%(s,experiment))




