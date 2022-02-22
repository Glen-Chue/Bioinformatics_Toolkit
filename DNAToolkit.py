# DNA Toolkit file
import collections
from structures import *

# Check the sequence to make sure it is a DNA String
def validateSeq(dna_seq):
    """Check the sequence to make sure it is a valid DNA string"""
    tmpseq = dna_seq.upper() #as lower and upper case are different
    for nuc in tmpseq:
        if nuc not in Nucleotides:
            return False
    return tmpseq

def nucleotide_frequency(seq):
    """Count nucleotides in a given sequence. Return a dictionary"""
    tmpFreqDict = {"A": 0, "C": 0, "G": 0, "T": 0} #Hashmap
    for nuc in seq:
        tmpFreqDict[nuc] += 1
    return tmpFreqDict
    #return dict(collections.Counter(seq))

def transcription(seq):
    """DNA -> RNA Transcription. Replacing Thymine with Uracil"""
    return seq.replace("T","U")

def reverse_complement(seq):
    """
    Swapping adenine with thymine and guanine with cytosine.
    Reversing newly generated string
    """
    # mapping = str.maketrans('ATCG', 'TAGC') #make translation function
    # return seq.translate(mapping)[::-1]

    return ''.join([DNA_ReverseComplement[nuc] for nuc in seq])[::-1]

def gc_content(seq):
    """GC Content in a DNA/RNA sequence"""
    return round((seq.count('C') + seq.count('G')) / len(seq) * 100)

def gc_content_subsec(seq, k=20):
    """GC Content in a DNA/RNA sub-sequence length k. k=20 by default"""
    res = []
    for i in range(0, len(seq) - k + 1, k):
        subseq = seq[i:i + k]
        res.append(gc_content(subseq))
    return res

#hi