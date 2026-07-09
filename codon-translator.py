from argparse import ArgumentParser

from src import translator

def parse_args():
    parser = ArgumentParser()

    parser.add_argument("sequence", help="The nucleotide sequenced to be translated")
    
    return parser.parse_args()

if __name__ == "__main__":
    args = parse_args()

    codon_list = translator.parse(args.sequence)
    print(translator.translate(codon_list))