from __future__ import division
def get_percentage(sequence, amino_acid):
    length = len(sequence)
    amino_acid_count = sequence.upper().count(amino_acid)
    percentage = amino_acid_count / length
    return round(percentage, 2)