from Task5 import pairs, dna_complement


def find_genes(dna):
    genes = []
    stops = ["TAG", "TAA", "TGA"]

    if type(dna) != str:
        raise TypeError("Input must be a string")
    for base in dna:
        if base not in pairs:
            raise ValueError("Input must be a valid DNA strand")


    for start in range(len(dna) - 2):       #we won't find gen in last 2 letters so we cut them off
        if dna[start:start+3] == "ATG":     #looking for start codon
            for pos in range(start + 3, len(dna) - 2, 3):   #looking for stop codon by passing 3 letters in a time
                codon = dna[pos:pos + 3]
                if codon in stops:          #if the stop codon is found it goes from the start till the stop codon and finito
                    genes.append(dna[start:pos + 3])
                    break
    return genes


if __name__ == "__main__":
    dna = input("Enter a DNA sequence (A, T, C, G): ")
    dna = dna.strip().upper()

    for base in dna:
        if base not in pairs:
            print("Error: only A, T, C, G are allowed.")
            exit()

    print("Genes in your sequence:")
    genes = find_genes(dna)
    if len(genes) == 0:
        print("  No genes found.")
    for gene in genes:
        print("  " + gene)

    print("Genes in the complementary sequence:")
    genes = find_genes(dna_complement(dna))
    if len(genes) == 0:
        print("  No genes found.")
    for gene in genes:
        print("  " + gene)