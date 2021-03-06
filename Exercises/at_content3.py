from __future__ import division
def get_at_content(dna, significant_figures):
'''takes the content of a file that was stored in a variable called 'dna'.
Counts the length of the string of characters of 'dna'.
Counts the occurrence of the letter A in dna, ignoring the case, and storing it in the variable 'a_count'.
Counts the occurrence of T and stores it in a variable in the same fashion.
Divides the sum of a_count and t_count by the length, and hence returns the at-count.
The 'return round()' will return the result with the amount of decimal points specified.

e.g. the following code will return the at-content with 1 decimal place:
test_dna = "ATGCATGCAACTGTAGC"
print(get_at_content(test_dna, 1))'''
    length = len(dna)
    a_count = dna.upper().count('A')
    t_count = dna.lower().count('T')
    at_content = (a_count + t_count) / length
    return round(at_content, significant_figures)