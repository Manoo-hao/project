from __future__ import division
def get_percentage(sequence, amino_acid_list=['A','I','L','M','F','W','Y','V']): #sets a default for amino_acid_list
    length = len(sequence)
    amino_acid_count = 0 #sequence.count(amino_acid)
    for aa in amino_acid_list: # go through the list one at a time, each time putting it in aa
        amino_acid_count = amino_acid_count + sequence.count(aa) # add teh count for aa to the running total
    
    for amino_acid in sequence: # get rid of this block
        if amino_acid == 'A' or amino_acid == 'I' or amino_acid == 'L' or amino_acid == 'M' or amino_acid == 'F' or amino_acid == 'W' or amino_acid == 'Y' or amino_acid == 'V' or amino_acid == 'G' or amino_acid == 'P' or amino_acid == 'C' or amino_acid == 'H' or amino_acid == 'K' or amino_acid == 'R' or amino_acid == 'Q' or amino_acid == 'N' or amino_acid == 'E' or amino_acid == 'D' or amino_acid == 'S' or amino_acid == 'T':
            amino_acid_count = amino_acid_count +1
        else:
            amino_acid_count = sequence.count(['A','I','L','M','F','W','Y','V'])
    percentage = amino_acid_count / length
    return round(percentage, 2)
