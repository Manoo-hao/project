from __future__ import division
def get_percentage(sequence, amino_acid):
'''This function takes 2 arguments:
sequence: a sequence of amino acids in one-letter notation
amino_acid: the name of an amino acid writtin in one-letter notation (can be entered in lower case)
It returns the percentage of the specified amino acid with respect to the length of the sequence
Example for using this function that will return the percentage of methionines:
get_percentage("MSRSLLLRFLLFLLLLPPLP", "M")'''
    length = len(sequence) #calculates length of sequence
    amino_acid_count = sequence.count(amino_acid.upper()) # counts the occurrence of the specified amino_acid in the sequence-string and ignores the case. Stores it in the variable 'amino_acid_count'
    percentage = amino_acid_count / length #calculates percentage by dividing amino_acid_count by the length of 'sequence'.
    return round(percentage, 2) # returns percentage with 2 decimal points
