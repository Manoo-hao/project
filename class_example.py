class Protein():
    protein_id=''
    protein_sequence=''
    def __init__ (self, id, sequence):
        self.protein_id = id
        self.protein_sequence = sequence
    def aminocount (self, aminoacid):
'''method returns the total count of that amino acid in the sequence'''
        aacount=0
        for a in self.protein_sequence:
            inf a ==aminoacid:
                aacount=aacount+1
            return aacount
#query with myprot=Protein('A1','AGSHGRTHDRT')
#myprot.aminocount('A')