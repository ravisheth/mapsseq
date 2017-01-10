# MIST-seq data processing script
# Modified 12/13/16 for hiseq SE data and handling fastq
import ConfigParser
import sys
import os 

#open default configuration file
dir_path = os.path.dirname(os.path.realpath(__file__))
config = ConfigParser.ConfigParser()
config.read(dir_path+'/param') #read config file
anchor = config.get('default','anchor')
bc1_7 = config.get('default','bc1_7').split(',')
bc1_8 = config.get('default','bc1_8').split(',')
bc1_9 = config.get('default','bc1_9').split(',')
bc2_8= config.get('default','bc2_8').split(',')

def process(input):
	#read input sequences
	line=0
	header=[]
	seq=[]
	qual=[]
	for l in open(input):
		line += 1
		if line%4 == 1: header.append(l.split('@')[1].split('.')[0])
		if line%4 == 2: seq.append(l.rstrip())
		if line%4 == 0: qual.append(l.rstrip())
	print 'read '+str(len(seq))+' from ' + str(input)
	#extract barcodes
	extract=[] #barcode id for each read
	extract_anchor=[] #anchor identity for each read
	for s in seq: #iterate through sequences and extract barcode/anchor
		f_barcode, f_anchor = extract_barcodes(s)
		extract.append(f_barcode)
		extract_anchor.append(f_anchor)
	#count number of sequences which we can identify a barcode in
	extract_cnt=0
	for i in extract:
		if i[0] > 0 and i[1] > 0: #0 denotes unidentifiable barcode
			extract_cnt+=1
	print 'mapped '+str(extract_cnt)+' barcodes'+', '+str(round(100*extract_cnt/float(len(seq)),2))+'%'
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
	fq_out = open(input.split('.')[0]+'_out.fq', "w") #open output file
	write_cnt=0 #track number of files written
	for i in range(len(extract)): #iterate through all extracted barcodes
		if extract[i][0] > 0 and extract[i][1] > 0: #if both barcodes can be mapped
			s,q = filter_seq_qual(seq[i],qual[i],extract_anchor[i]) # filter the sequence (remove primers)
			if len(s) > 160 and len(s) < 164: #given 205bp input, the seq should be 161,162,163bp
				s = s[:161]
				q = q[:161]            
				source_id = header[i] #what sample did this come from
				index_n = index_map.index(source_id) #map this back to a index number
				bcn = bc_map[index_n].index(extract[i]) #barcode ID number
				ind = bc_count[index_n][bcn] #read# we are at for particular barcode for particular sample
				fq_out.write('@'+source_id+str(bcn)+'.'+str(int(ind))+'\n') #write header (source,barcode_id.read#)
				fq_out.write(s+'\n') #write sequence
				fq_out.write('+\n')
				fq_out.write(q+'\n')                
				bc_count[index_n][bcn] += 1 #add count to count tracker
				write_cnt += 1
	fq_out.close() #close output file
	print 'wrote '+str(write_cnt)+' sequences'+', '+str(round(100*write_cnt/float(len(seq)),2))+'%'
	
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

def filter_seq_qual(seq, qual, f_anchor): #return a filtered sequence with barcode/primers trimmed
	strip_length=len(seq.split(f_anchor)[0])+len(f_anchor)+27
	return seq[strip_length:], qual[strip_length:]

if __name__ == '__main__':
	file_name = sys.argv[1]
	process(file_name)
