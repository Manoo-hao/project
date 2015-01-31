from __future__ import division
def get_percentage(sequence, amino_acids=['A','I','L','M','F','W','Y','V']):
    length = len(sequence)
    amino_acid_count = sequence.count(amino_acids)
    percentage = amino_acid_count / length
    return round(percentage, 2)