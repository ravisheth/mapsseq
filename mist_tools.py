#mist_tools v0.1
#author: ravi sheth, wang lab, columbia university
#last updated 4/5/2016
import numpy as np
import os
from tqdm import tqdm 
from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from Bio.Alphabet import generic_dna
from Bio.SeqIO import FastaIO
import subprocess
import click

USEARCH = '/Users/ravi/Dropbox/wang_lab/mist_seq/mist_seq/usearch8.1.1861_i86osx32'
FILE_DIR = os.path.dirname(__file__)

bc1_7=np.loadtxt(FILE_DIR+'/bc1_7.txt',dtype=str)
bc1_8=np.loadtxt(FILE_DIR+'/bc1_8.txt',dtype=str)
bc1_9=np.loadtxt(FILE_DIR+'/bc1_9.txt',dtype=str)
bc2_8=np.loadtxt(FILE_DIR+'/bc2.txt',dtype=str)
anchor='GACCTGCG'

#TODO: error catching & user notifications
#TODO: multiple index processing
#TODO: auto configure usearch binary location (merging, quality filtering, clustering pipeline)
#TODO: better loading of barcode sequences (standard format)
#TODO: better loading of anchor sequence (probably in barcode sequence file)
#TODO: better annotation of script
#subprocess.call(USEARCH, shell=True)

@click.group()
def cli():
	pass

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('-l','--label',default='output',type=str)
def process(input,label):
	#takes merged, quality filtered FASTA as input
	#load data 
	seq=[]
	for record in SeqIO.parse(open(input),'fasta'):
		seq.append(str(record.seq))
	click.echo('read '+str(len(seq))+' sequences')
	
	extract=[]
	for s in tqdm(seq, ncols=80, desc='mapping barcodes', \
		bar_format='{l_bar}{bar}|[{elapsed}<{remaining}s]'):
		extract.append(extract_barcodes(s))
	
	extract_cnt=0
	for i in extract:
		if np.sum(i) > 0 and np.product(i) > 0:
			extract_cnt+=1
	click.echo('mapped '+str(extract_cnt)+' sequences')

	bc_map=[]
	for i in np.arange(1,97):
		for i2 in np.arange(1,97):
			bc_map.append([i,i2])

	bc_count=np.zeros(shape=9216)
	write_cnt=0
	output=[]
	for i in tqdm(range(len(extract)), ncols=80, desc='writing output',\
		bar_format='{l_bar}{bar}|[{elapsed}<{remaining}s]'):
		if np.product(extract[i]) != 0:
			if len(filtered_seq(seq[i])) > 225 \
				and len(filtered_seq(seq[i])) < 275:
				bcn=bc_map.index(extract[i])
				ind=bc_count[bcn]
				output.append(SeqRecord(Seq(filtered_seq(seq[i]),generic_dna),\
					id=(label+'-'+str(bcn)+'.'+str(int(ind))),description=""))
				bc_count[bcn]+=1
				write_cnt+=1

	handle = open(label+'.fna', "w")
	fasta_out = FastaIO.FastaWriter(handle, wrap=None)
	fasta_out.write_file(output)
	click.echo('wrote '+str(write_cnt)+' sequences')

def extract_barcodes(seq):
	bc1_id=0
	bc2_id=0
	#IMPROVEMENT: allow mismatch of 1 (likely yield 2% improvement)
	if len(seq.split(anchor))==1: #no exact match to anchor
		return [0, 0]
	
	#extract bcs
	bc1_s=seq.split(anchor)[0]
	bc2_s=seq.split(anchor)[1][:8]
	
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
	return [bc1_id, bc2_id]

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

def filtered_seq(seq):
	return seq.split(anchor)[1][27:][:-20]