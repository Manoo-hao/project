from __future__ import division
def get_at_content(dna):
'''Takes the content of a file that was stored in a variable called 'dna'.
Counts the length of the string of characters od 'dna'.
Counts the occurrence of the letter A in dna, ignoring the case, and storing it in the variable 'a_count'.
Counts occurrence of T stores it in a variable in the same fashion.
Divides the sum of a_count and t_count by the length and hence returns the at-content.
The 'return round()' will return the result with 2 decimal points.'''
        length = len(dna)
        a_count = dna.upper().count('A')
        t_count = dna.upper().count('T')
        at_content = (a_count + t_count) / length
        return round (at_content, 2)