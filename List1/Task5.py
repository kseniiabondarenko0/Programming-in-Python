pairs = {"A": "T", "T": "A", "C": "G", "G": "C"}

def dna_complement(orig_strand):

    if type(orig_strand) != str:
        raise TypeError("Input must be a string")

    result = ""
    for base in orig_strand:
        if base not in pairs:
            raise ValueError("Input must be a valid DNA strand")
        result += pairs[base]

    return result[::-1]