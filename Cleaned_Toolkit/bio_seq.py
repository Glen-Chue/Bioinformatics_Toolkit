from bio_structs import *
class bio_seq:
    """DNA sequnece class. Defalt value: ATCG, DNA, No label"""
    
    def __init__(self, seq="ATCG", seq_type="DNA", label='No Label'):
        """Sequence initialization, validation."""
        self.seq = seq.upper()
        self.label = label
        self.seq_type = seq_type
        self.is_valid = self.__validate()
        assert self.is_valid, f"Provided data does not seem to be a corret {self.seq_type} sequence"    

    # Check the sequence to make sure it is a DNA String
    def validateSeq(self, seq):
        """Check the sequence to make sure it is a valid DNA string"""
        # DNA_Nucleotides is a list of ACGT
        return set(DNA_Nucleotides).issuperset(self.seq)
    