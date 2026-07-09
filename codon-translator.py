from argparse import ArgumentParser

from src import translator

def parse_args():
    parser = ArgumentParser()

    parser.add_argument("sequence", help="The nucleotide sequenced to be translated")
    
    parser.add_argument("-s", "--short", action="store_true", help="Shorten the amino acids to their three letter abbreviations")

    return parser.parse_args()

if __name__ == "__main__":
    args = parse_args()

    codon_list = translator.parse(args.sequence)
    amino_list = translator.translate(codon_list)
    if args.short:
        print(translator.shorten_to_three(amino_list))
    else:
        print(amino_list)