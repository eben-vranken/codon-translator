from argparse import ArgumentParser

from src import translator

def parse_args():
    parser = ArgumentParser()

    parser.add_argument("sequence", nargs="?", help="The nucleotide sequenced to be translated")
    
    parser.add_argument("-s", "--short", action="store_true", help="Shorten the amino acids to their three letter abbreviations")
    parser.add_argument("-f", "--fasta", action="store_true", help="Shorten the amino acids to their standard FASTA format")
    parser.add_argument("-i", "--input", help="The file from which to read the amino acids")
    
    args = parser.parse_args()

    if not args.sequence and not args.input or (args.sequence and args.input):
        parser.error("You must provide either a 'sequence' positional argument or an '--input' file.")
    return args

if __name__ == "__main__":
    args = parse_args()


    sequence = ""
    if args.sequence:
        sequence = args.sequence
    else:
        with open(args.input) as fp:
            for line in fp:
                sequence += line.strip()

    codon_list = translator.parse(sequence)
    amino_list = translator.translate(codon_list)
    if args.short:
        print(translator.shorten_to_three(amino_list))
    elif args.fasta:
        print(translator.shorten_to_fasta(amino_list))
    else:
        print(amino_list)