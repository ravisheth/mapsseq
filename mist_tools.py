#mist processing script
#author: ravi sheth, wang lab, columbia university
import click
import os
from itertools import groupby
import ConfigParser

FILE_DIR = os.path.dirname(__file__)
config = ConfigParser.ConfigParser()
config.read(FILE_DIR+'/param')
anchor = config.get('default','anchor')
bc1_7 = config.get('default','bc1_7').split(',')
bc1_8 = config.get('default','bc1_8').split(',')
bc1_9 = config.get('default','bc1_9').split(',')
bc2_8= config.get('default','bc2_8').split(',')

@click.group()
def cli():
	pass

@cli.command()
@click.argument('input', type=click.Path(exists=True))

def process(input):
	header=[]
	seq=[]
	fiter=fasta_iter(input)
	for rec in fiter:
		h,s = rec
		header.append(h.split('.')[0])
		seq.append(s)

	extract=[]
	extract_anchor=[]
	with click.progressbar(seq, label='mapping barcodes') as bar:
		for s in bar:
			f_barcode, f_anchor = extract_barcodes(s)
			extract.append(f_barcode)
			extract_anchor.append(f_anchor)

	extract_cnt=0
	for i in extract:
		if i[0] > 0 and i[1] > 0:
			extract_cnt+=1

	index_map=list(set(header))
	bc_map=[]
	bc_count=[]
	for n in index_map:
		temp=[]
		for i in range(1,97):
			for i2 in range(1,97):
				temp.append([i,i2])
		bc_map.append(temp)
		count=[0]*9216
		bc_count.append(count)

	label = input.split('.')[0]
	fasta_out = open(label+'_out.fasta', "w")
	write_cnt=0
	with click.progressbar(range(len(extract)),label='writing output  ') as bar:
		for i in bar:
			if extract[i][0] > 0 and extract[i][1] > 0:
				s = filtered_seq(seq[i],extract_anchor[i])
				if len(s) > 100 and len(s) < 400:
					source_id=header[i]
					index_n=index_map.index(source_id)
					bcn=bc_map[index_n].index(extract[i])
					ind=bc_count[index_n][bcn]
					fasta_out.write('>'+source_id+str(bcn)+'.'+str(int(ind))+'\n')
					fasta_out.write(s+'\n')
					bc_count[index_n][bcn]+=1
					write_cnt+=1
	fasta_out.close()
	click.echo('read '+str(len(seq))+'; ',nl=False)
	click.echo('mapped '+str(extract_cnt)+'; ',nl=False)
	click.echo('wrote '+str(write_cnt)+' sequences')

def fasta_iter(fasta_name):
    fh = open(fasta_name)
    faiter = (x[1] for x in groupby(fh, lambda line: line[0] == ">"))
    for header in faiter:
        header = header.next()[1:].strip()
        seq = "".join(s.strip() for s in faiter.next())
        yield header, seq

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
	if len(array) == 1:
		return hamming(array,s)
	if len(array) > 1:
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
