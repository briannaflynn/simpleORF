#!/usr/bin/python
import sys
from Bio import SeqIO
from Bio.Seq import Seq
import warnings
from Bio import BiopythonWarning
warnings.simplefilter('ignore', BiopythonWarning)

# input a DNA sequence as a string, output a list of all possible ORFs
def orf_tracker(dna:str):
	
	dna = Seq(dna)
	rev_dna = dna.reverse_complement()
	rna = dna.transcribe()
	rev_rna = rev_dna.transcribe()
	
	readingframes_plus = [Seq.translate(rna[i:], table='Standard', stop_symbol='*') for i in range(3)]
	readingframes_minus = [Seq.translate(rev_rna[i:], table='Standard', stop_symbol='*') for i in range(3)]

	rf_plus = [str(y) for y in readingframes_plus]
	rf_minus = [str(y) for y in readingframes_minus]

	
	
	def rf2orf(rf):
		orfs = []
		for seq in rf:
			list = []
			for i in range(len(seq)):
				j = seq[i:]
				n = j.count("M")
				if n > 0:
					M_id = j.index("M")
					w = j[M_id:]
					list.append(w)
			for i in list:
				if i.count("*") > 0:
					stop_id = i.index("*")
					t = i[:stop_id]
					orfs.append(t)
		myset = set(orfs)
		orf_list = [s for s in myset]
		return orfs


	orf_plus = rf2orf(rf_plus)

	orf_minus = rf2orf(rf_minus)
	
	orfs = orf_plus + orf_minus
	
	orfset = set(orfs)
	orf_list = [s for s in orfset]
			
	return orf_list

# input your fasta file here, or manually input a DNA string

record = SeqIO.read(sys.argv[1], "fasta")
dna = record.seq
dna = str(dna)

orfs = orf_tracker(dna)

