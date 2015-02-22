from __future__ import division
def get_at_content(dna):
        length = len(dna)
        a_count = dna.upper().count('A')
        t_count = dna.upper().count('T')
        at_content = (a_count + t_count) / length
        return round (at_content, 2)