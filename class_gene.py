class Gene()
    sequence = ''
    accession = ''

    def __init__ (self, accession, sequence):
        self.sequence = sequence.upper().replace('\n','')
        self.accession = accession.upper()

    def setsequence(self, seq):
        self.sequences = seq.upper().replace('\n','')

    def getAT(self)
        at_count = self.sequence.count("A")+self.sequence.count("T")
        return at_count

    def length(self)
        return len(self.sequence)