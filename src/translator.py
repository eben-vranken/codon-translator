codon_table = {
    # First base U
    "UUU": "Phenylalanine",
    "UUC": "Phenylalanine",
    "UUA": "Leucine",
    "UUG": "Leucine",
    
    "UCU": "Serine",
    "UCC": "Serine",
    "UCA": "Serine",
    "UCG": "Serine",

    "UAU": "Tyrosine",
    "UAC": "Tyrosine",
    "UAA": "Stop (Ochre)",
    "UAG": "Stop (Amber)",

    "UGU": "Cysteine",
    "UGC": "Cysteine",
    "UGA": "Stop (Opal)",
    "UGG": "Tryptophan",

    # First base C
    "CUU": "Leucine",
    "CUC": "Leucine",
    "CUA": "Leucine",
    "CUG": "Leucine",

    "CCU": "Proline",
    "CCC": "Proline",
    "CCA": "Proline",
    "CCG": "Proline",

    "CAU": "Histidine",
    "CAC": "Histidine",
    "CAA": "Glutamine",
    "CAG": "Glutamine",
    
    "CGU": "Arginine",
    "CGC": "Arginine",
    "CGA": "Arginine",
    "CGG": "Arginine",


}

def parse(sequence):
    return [sequence[i:i+3] for i in range(0, len(sequence), 3)]

def translate(codon_list):
    amino_list = []
    for codon in codon_list:
        if codon in codon_table:
            amino = codon_table[codon]
            amino_list.append(amino)

    return amino_list