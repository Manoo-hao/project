from __future__ import division
def hello(name):
    print("Hello "+name)

me='David'
hello(me)

def get_at_content(dna):
        length = len(dna)
        a_count = dna.count('A')
        t_count = dna.count('T')
        at_content = (a_count + t_count) / length
        return at_content
