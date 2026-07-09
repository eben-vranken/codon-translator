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
    "UAA": "Stop",
    "UAG": "Stop",

    "UGU": "Cysteine",
    "UGC": "Cysteine",
    "UGA": "Stop",
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

    # First base A
    "AUU": "Isoleucine",
    "AUC": "Isoleucine",
    "AUA": "Isoleucine",
    "AUG": "Methionine",

    "ACU": "Threonine",
    "ACC": "Threonine",
    "ACA": "Threonine",
    "ACG": "Threonine",

    "AAU": "Asparagine",
    "AAC": "Asparagine",
    "AAA": "Lysine",
    "AAG": "Lysine",

    "AGU": "Serine",
    "AGC": "Serine",
    "AGA": "Arginine",
    "AGG": "Arginine",

    # First base G
    "GUU": "Valine",
    "GUC": "Valine",
    "GUA": "Valine",
    "GUG": "Valine",

    "GCU": "Alanine",
    "GCC": "Alanine",
    "GCA": "Alanine",
    "GCG": "Alanine",

    "GAU": "Aspartic Acid",
    "GAC": "Aspartic Acid",
    "GAA": "Glutamic Acid",
    "GAG": "Glutamic Acid",

    "GGU": "Glycine",
    "GGC": "Glycine",
    "GGA": "Glycine",
    "GGG": "Glycine"
}

amino_to_short = {
    "Phenylalanine": "Phe",
    "Leucine": "Leu",
    "Serine": "Ser",
    "Tyrosine": "Tyr",
    "Cysteine": "Cys",
    "Tryptophan": "Trp",
    "Proline": "Pro",
    "Histidine": "His",
    "Glutamine": "Gln",
    "Arginine": "Arg",
    "Isoleucine": "Ile",
    "Methionine": "Met",
    "Threonine": "Thr",
    "Asparagine": "Asn",
    "Lysine": "Lys",
    "Valine": "Val",
    "Alanine": "Ala",
    "Aspartic Acid": "Asp",
    "Glutamic Acid": "Glu",
    "Glycine": "Gly",
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

def shorten_to_three(amino_list):
    shortened_list = []
    for amino in amino_list:
        if amino in amino_to_short:
            abbrev = amino_to_short[amino]
            amino_list.append(abbrev)
        else:
            shortened_list.append(amino)
    
    return shortened_list