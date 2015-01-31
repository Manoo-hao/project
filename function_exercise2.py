from __future__ import division
def get_percentage(sequence, amino_acids=['A','I','L','M','F','W','Y','V']):
    length = len(sequence)
    #DMAM 30/1 amino_acis is a list. You have to count each element in the list separately
    amino_acid_count = sequence.count(amino_acids)
    #set amino_acid count to 0
    #loop through amino_acids, adding th ecount for each amino acid to amino_acid_count
    percentage = amino_acid_count / length
    return round(percentage, 2)
