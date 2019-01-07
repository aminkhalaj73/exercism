

def to_rna(dna_strand):
    dna = dna_strand.maketrans("GCTA" , "CGAU")
    return dna_strand.translate(dna)
