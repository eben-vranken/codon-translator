<h1 align="center">🧬 Codon Translator</h1>

<p align="center">
    A lightweight command-line tool to translate RNA (or DNA) sequences into their corresponding amino acid chains.
</p>

<p align="center">
    <a href="LICENSE"><img src="https://img.shields.io/badge/License-MIT-yellow.svg" alt="MIT License"></a>
</p>

A small, zero-dependency Python CLI that takes a raw nucleotide sequence, splits it into codons, and translates each one to its amino acid using the standard genetic code, with output as full names, three-letter abbreviations, or single-letter FASTA-style codes.

📝 [I wrote about the design decisions here](https://www.ebenvranken.be/blog/codon-to-amino)

## Install

Clone the repository directly:
```bash
git clone https://github.com/eben-vranken/codon-translator.git
cd codon-translator
```

## Usage

Pass an RNA sequence as a positional argument:

```bash
python codon-translator.py AUGAAAUAA
```

If your sequence is DNA rather than RNA, add `-d` to convert T→U before translating:

```bash
python codon-translator.py -d ATGAAATAA
```

### Output Formats

By default, amino acids are printed by their full name. Use `-s` for three-letter abbreviations, or `-f` for single-letter FASTA-style codes:

```bash
python codon-translator.py -s AUGAAAUAA
python codon-translator.py -f AUGAAAUAA
```

### File Input & Output

Translate directly from a FASTA file with `-i`, and write the result to a file with `-o`:

```bash
python codon-translator.py -d -f -i data/synthetic_zika.fasta -o protein.txt
```

## Configuration Matrix

| Argument | Option / Choices | Default | Description |
| --- | --- | --- | --- |
| `sequence` | *Positional sequence string* | *Required if `-i` not set* | The raw RNA (or DNA, with `-d`) sequence to translate. |
| `-i`, `--input` | *File path* | *Required if `sequence` not set* | Read the sequence from a FASTA file instead of the command line. |
| `-o`, `--output` | *File path* | `None` (prints to stdout) | Write the translated output to a file. |
| `-d`, `--dna` | *Flag* | `False` | Treat the input as DNA and convert T→U before translating. |
| `-s`, `--short` | *Flag* | `False` | Output amino acids as three-letter abbreviations (e.g. `Met`). |
| `-f`, `--fasta` | *Flag* | `False` | Output amino acids as single-letter FASTA codes (e.g. `M`). |

## Feature Set

* **Standard Genetic Code:** Full 64-codon lookup table, including all three stop codons.
* **DNA or RNA Input:** Accepts RNA natively, or DNA via the `-d` flag.
* **Multiple Output Formats:** Full amino acid names, three-letter abbreviations, or single-letter FASTA codes.
* **FASTA File Support:** Reads multi-line FASTA records directly with `-i`, skipping header lines automatically.

## License

MIT
