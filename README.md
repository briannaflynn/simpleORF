# simpleORF
A simple python script to index all ORFs from a DNA sequence

Many of the examples I found on Biostars were overly complicated for this task, and so I hope this simple indexing tool helps. This tool requires that you install biopython, ```pip install biopython```, first.

Biopython is used to generate the translated amino acid sequence from the DNA sequence input from the fasta file, as well as get the translation sequence from its reverse complement strand. From the reading frames generated from these strings, pass a list of reading frames to the sub-function ```rf2orf```, which aggregates the ORFs it finds into a simple list based on whether the sequence contains a start and stop codon.

Set is used to narrow down the lists to unique ORFs only.

The function returns a list of all ORFs found. This was created for a simple programming exercise; the caveat being that most real ORFs are more than 100 amino acids in length, and this tool pulls out all possible ORFs no matter the length. Thus, if you're a researcher, it would be best to use something like NCBI ORF finder or take my code and add an additional parameter to the main ```orf_tracker``` function, one that takes the minimum length of amino acid sequences as an argument. 

# How to run

Clone the repository, and copy over the input fasta file to this directory.

Make sure your fasta file is formatted like so:

```
>contig_example
AGCCATGTAGCTAACTCAGGTTACATGGGGATGACCCCGCGACTTGGATTAGAGTCTCTTTTGGAATAAGCCTGAATGATCCGAGTAGCATCTCAG
```

While on the command line, execute the script like so:

```Bash
python orf.py my_genome.fasta
```

The input can be a text file, so long as the text file is formatted like a fasta file. 

The output will be all ORFs found within the fasta file, printed out like this:

```Bash
MLLGSFRLIPKETLIQVAGSSPCNLS
M
MGMTPRLGLESLLE
MTPRLGLESLLE
```
