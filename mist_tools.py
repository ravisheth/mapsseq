#mist_tools v0.1
#author: ravi sheth, wang lab, columbia university
#last updated 4/5/2016

import numpy as np
import os
from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from Bio.Alphabet import generic_dna
from Bio.SeqIO import FastaIO
import click

USEARCH = '/Users/ravi/Dropbox/wang_lab/mist_seq/mist_seq/usearch8.1.1861_i86osx32'
FILE_DIR = os.path.dirname(__file__)

bc1_7=np.loadtxt(FILE_DIR+'/bc1_7.txt',dtype=str)
bc1_8=np.loadtxt(FILE_DIR+'/bc1_8.txt',dtype=str)
bc1_9=np.loadtxt(FILE_DIR+'/bc1_9.txt',dtype=str)
bc2_8=np.loadtxt(FILE_DIR+'/bc2.txt',dtype=str)
anchor='GACCTGCG'

@click.group()
def cli():
	pass

@cli.command()
@click.argument('input', type=click.Path(exists=True))
def process(input):
	seq=[]
	fasta_id=[]
	with click.progressbar(SeqIO.parse(open(input),'fasta'), label='reading sequences') as bar:
		for record in bar:
			seq.append(str(record.seq))
			fasta_id.append(str(record.id).split('.')[0])

	extract=[]
	extract_anchor=[]
	with click.progressbar(seq, label='mapping barcodes ') as bar:
		for s in bar:
			f_barcode, f_anchor = extract_barcodes(s)
			extract.append(f_barcode)
			extract_anchor.append(f_anchor)

	extract_cnt=0
	for i in extract:
		if np.sum(i) > 0 and np.product(i) > 0:
			extract_cnt+=1

	index_map=list(set(fasta_id))
	bc_map=[]
	bc_count=[]
	for n in index_map:
		temp=[]
		for i in np.arange(1,97):
			for i2 in np.arange(1,97):
				temp.append([i,i2])
		bc_map.append(temp)
		count=np.zeros(shape=9216)
		bc_count.append(count)

	label = input.split('.')[0]
	handle = open(label+'_out.fasta', "w")
	fasta_out = FastaIO.FastaWriter(handle, wrap=None)
	fasta_out.write_header()

	write_cnt=0
	with click.progressbar(range(len(extract)),label='writing output   ') as bar:
		for i in bar:
			if np.product(extract[i]) != 0:
				s = filtered_seq(seq[i],extract_anchor[i])
				if len(s) > 100 and len(s) < 400:
					source_id=fasta_id[i]
					index_n=index_map.index(source_id)
					bcn=bc_map[index_n].index(extract[i])
					ind=bc_count[index_n][bcn]
					fasta_out.write_record(SeqRecord(Seq(s,generic_dna), id=(source_id+str(bcn)+'.'+str(int(ind))),description=""))
					bc_count[index_n][bcn]+=1
					write_cnt+=1

	fasta_out.write_footer()
	click.echo('read '+str(len(seq))+'; ',nl=False)
	click.echo('mapped '+str(extract_cnt)+'; ',nl=False)
	click.echo('wrote '+str(write_cnt)+' sequences')

def extract_barcodes(seq):
	bc1_id=0
	bc2_id=0

	found_anchor=None
	#attempt to make inexact match of anchor with single snp
	bc_length=[7,8,9]
	for i in bc_length:
		possible_anchor=seq[i:(i+8)]
		if hamming(possible_anchor,anchor) < 2:
			found_anchor=possible_anchor
	if found_anchor == None:
		return [0,0], found_anchor
	else:
		bc1_s=seq.split(found_anchor)[0]
		bc2_s=seq.split(found_anchor)[1][:8]

	#assign bc1
	if len(bc1_s) == 7:
		d,i=min_hamming(bc1_7,bc1_s)
		if d < 2: bc1_id=i
	elif len(bc1_s) == 8:
		d,i=min_hamming(bc1_8,bc1_s)
		if d < 2: bc1_id=i+32
	elif len(bc1_s) == 9:
		d,i=min_hamming(bc1_9,bc1_s)
		if d < 2: bc1_id=i+64

	#assign bc2
	d,i=min_hamming(bc2_8,bc2_s)
	if d < 2: bc2_id=i
	return [bc1_id, bc2_id], found_anchor

def hamming(a, b):
	dist = 0
	for i, j in zip(a, b):
		if i != j:
			dist += 1
	return dist

def min_hamming(array, s):
	if array.size == 1:
		return hamming(array,s)
	if array.size > 1:
		minimum=len(s)
		match=0
		i=1
		for bc in array:
			d=hamming(bc,s)
			if d < minimum:
				minimum = d
				match = i
			i=i+1
		return minimum, match

def filtered_seq(seq, f_anchor):
	return seq.split(f_anchor)[1][27:][:-20]
