#mist processing script. author: ravi sheth, wang lab, columbia university
import click
import os
from itertools import groupby
import ConfigParser

#open default configuration file
FILE_DIR = os.path.dirname(__file__) #default param file in script install directory
config = ConfigParser.ConfigParser()
config.read(FILE_DIR+'/param') #read config file
anchor = config.get('default','anchor')
bc1_7 = config.get('default','bc1_7').split(',')
bc1_8 = config.get('default','bc1_8').split(',')
bc1_9 = config.get('default','bc1_9').split(',')
bc2_8= config.get('default','bc2_8').split(',')

@click.group()
def cli():
	pass
@cli.command()
@click.argument('input', type=click.Path(exists=True)) #input file name
def process(input):
	#read input sequences
	header=[]
	seq=[]
	fiter=fasta_iter(input) #open fasta file via iterator
	for rec in fiter: #iterate through records
		h,s = rec #extract header and sequence
		header.append(h.split('.')[0]) #extract sample ID from header
		seq.append(s) #extract sequence
	#extract barcodes
	extract=[] #barcode id for each read
	extract_anchor=[] #anchor identity for each read
	with click.progressbar(seq, label='mapping barcodes') as bar:
		for s in bar: #iterate through sequences and extract barcode/anchor
			f_barcode, f_anchor = extract_barcodes(s)
			extract.append(f_barcode)
			extract_anchor.append(f_anchor)
	#count number of sequences which we can identify a barcode in
	extract_cnt=0
	for i in extract:
		if i[0] > 0 and i[1] > 0: #0 denotes unidentifiable barcode
			extract_cnt+=1
	#set up barcode mapping/counting for rewriting output file
	index_map=list(set(header)) #all unique sample IDs
	bc_map=[] #all possible barcode ID combinations
	bc_count=[] #count of reads mapping to each barcode ID in bc_map
	for n in index_map: #for each sample add entry to bc_map and bc_count
		temp=[]
		for i in range(1,97):
			for i2 in range(1,97):
				temp.append([i,i2])
		bc_map.append(temp)
		count=[0]*9216 #9216 total possible barcodes
		bc_count.append(count)
	fasta_out = open(input.split('.')[0]+'_out.fasta', "w") #open output file
	write_cnt=0 #track number of files written
	with click.progressbar(range(len(extract)),label='writing output  ') as bar:
		for i in bar: #iterate through all extracted barcodes
			if extract[i][0] > 0 and extract[i][1] > 0: #if both barcodes can be mapped
				s = filtered_seq(seq[i],extract_anchor[i]) #filter the sequence (remove primers)
				if len(s) > 100 and len(s) < 400: #ensure that filtered sequence meets size criteria
					source_id = header[i] #what sample did this come from
					index_n = index_map.index(source_id) #map this back to a index number
					bcn = bc_map[index_n].index(extract[i]) #barcode ID number
					ind = bc_count[index_n][bcn] #read# we are at for particular barcode for particular sample
					fasta_out.write('>'+source_id+str(bcn)+'.'+str(int(ind))+'\n') #write header (source,barcode_id.read#)
					fasta_out.write(s+'\n') #write sequence
					bc_count[index_n][bcn] += 1 #add count to count tracker
					write_cnt += 1
	fasta_out.close() #close output file
	#print statistics of filtering
	click.echo('read '+str(len(seq))+'; ',nl=False)
	click.echo('mapped '+str(extract_cnt)+'; ',nl=False)
	click.echo('wrote '+str(write_cnt)+' sequences')

def fasta_iter(fasta_name): #iterator for fasta files
    fh = open(fasta_name)
    faiter = (x[1] for x in groupby(fh, lambda line: line[0] == ">"))
    for header in faiter:
        header = header.next()[1:].strip()
        seq = "".join(s.strip() for s in faiter.next())
        yield header, seq

def extract_barcodes(seq): #wrapper function for barcode extraction from sequence
	bc1_id=0
	bc2_id=0
	found_anchor=None
	bc_length=[7,8,9]
	for i in bc_length: #attempt to make inexact match of anchor with single snp
		possible_anchor=seq[i:(i+8)] #attempt to find anchor given different bc1 sizes
		if hamming(possible_anchor,anchor) < 2: #hamming=1 max distance
			found_anchor=possible_anchor
	if found_anchor == None: #if no anchor can be found return no match
		return [0,0], found_anchor
	else: #if anchor is found, extract barcode sequences
		bc1_s = seq.split(found_anchor)[0]
		bc2_s = seq.split(found_anchor)[1][:8]
	#assign bc1, hamming=1 error correction
	if len(bc1_s) == 7:
		d,i = min_hamming(bc1_7,bc1_s)
		if d < 2: bc1_id=i
	elif len(bc1_s) == 8:
		d,i = min_hamming(bc1_8,bc1_s)
		if d < 2: bc1_id=i+32 #id assumes 32x of 3 different sizes
	elif len(bc1_s) == 9:
		d,i = min_hamming(bc1_9,bc1_s)
		if d < 2: bc1_id=i+64 #id assumes 32x of 3 different sizes
	#assign bc2, hamming=1 error correction
	d,i = min_hamming(bc2_8,bc2_s)
	if d < 2: bc2_id=i
	return [bc1_id, bc2_id], found_anchor

def hamming(a, b): #hamming distance between two sequences
	dist = 0
	for i, j in zip(a, b):
		if i != j:
			dist += 1
	return dist

def min_hamming(ref_list, s): #find match in list with minimum hamming dist to string
	if len(ref_list) == 1: #if there is only one item in the input list
		return hamming(ref_list,s)
	if len(ref_list) > 1:
		minimum=len(s)
		match=0
		i=1
		for bc in ref_list: #iterate through list
			d=hamming(bc,s)
			if d < minimum: #record minimum hamming distance
				minimum = d
				match = i
			i=i+1
		return minimum, match

def filtered_seq(seq, f_anchor): #return a filtered sequence with barcode/primers trimmed
	return seq.split(f_anchor)[1][27:][:-20]
