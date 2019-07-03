# MaP-seq data processing script
# Modified 1/19/16 for new MaP-seq setup
import ConfigParser
import sys
import os

#open configuration file
dir_path = os.path.dirname(os.path.realpath(__file__))
config = ConfigParser.ConfigParser()
config.read(dir_path+'/param') #read config file
anchor1 = config.get('default','anchor1')
anchor2 = config.get('default','anchor2')
bc1_7 = config.get('default','bc1_7').split(',')
bc1_8 = config.get('default','bc1_8').split(',')
bc1_9 = config.get('default','bc1_9').split(',')
bc2_8= config.get('default','bc2_8').split(',')
bc3_8= config.get('default','bc3_8').split(',')

def process(file_name, primer_fwd_length, primer_rev_length, min_length, max_length, norm_length, write_bc_count):
    #read input sequences
    line=0
    header=[]
    seq=[]
    qual=[]
    for l in open(file_name):
        line += 1
        if line%4 == 1: header.append(l.split('@')[1].split('.')[0])
        if line%4 == 2: seq.append(l.rstrip())
        if line%4 == 0: qual.append(l.rstrip())
    print 'read ' + str(len(seq)) + ' from ' + str(file_name)

    #extract barcodes
    extract=[] #barcode id for each read
    extract_anchor1=[] #anchor identity for each read
    extract_anchor2=[] #anchor identity for each read
    for s in seq: #iterate through sequences and extract barcode/anchor
        f_barcode,anchor1,anchor2 = extract_barcodes(s)
        extract.append(f_barcode)
        extract_anchor1.append(anchor1)
        extract_anchor2.append(anchor2)

    #count number of sequences which we can identify a barcode in
    extract_cnt=0
    for i in extract:
        if i[0] > 0 and i[1] > 0 and i[2] > 0: #0 denotes unidentifiable barcode
            extract_cnt+=1
    print 'mapped '+str(extract_cnt)+' barcodes'+', '+str(round(100*extract_cnt/float(len(seq)),2))+'%'

    #set up barcode mapping/counting for rewriting output file
    index_map=list(set(header)) #all unique sample IDs
    bc_count=[] #count of reads mapping to each barcode ID
    for n in index_map: #for each sample add entry to bc_count
        bc_count.append([0]*(96**3))

    fq_out = open(file_name.split('.')[0]+'_out.fq', "w") #open output file
    write_cnt=0 #track number of files written
    for i in range(len(extract)): #iterate through all extracted barcodes
        if extract[i][0] > 0 and extract[i][1] > 0 and extract[i][2] > 0: #if both barcodes can be mapped
            s,q = filter_seq_qual(seq[i],qual[i],extract_anchor1[i],primer_fwd_length, primer_rev_length) # filter the sequence (remove primers)
            if len(s) >= min_length and len(s) <= max_length:
                if norm_length != 0:
                    s = s[:norm_length]
                    q = q[:norm_length]
                source_id = header[i] #what sample did this come from
                index_n = index_map.index(source_id) #map this back to a index number
                bcn = (extract[i][0]-1)*9216+(extract[i][1]-1)*96+(extract[i][2]-1)
                ind = bc_count[index_n][bcn] #read# we are at for particular barcode for particular sample
                fq_out.write('@'+source_id+str(bcn)+'.'+str(int(ind))+'\n') #write header (source,barcode_id.read#)
                fq_out.write(s+'\n') #write sequence
                fq_out.write('+\n')
                fq_out.write(q+'\n')
                bc_count[index_n][bcn] += 1 #add count to count tracker
                write_cnt += 1
    fq_out.close() #close output file
    print 'wrote '+str(write_cnt)+' sequences'+', '+str(round(100*write_cnt/float(len(seq)),2))+'%'

    #writing barcode count list
    if write_bc_count == True:
        bc_out = open(file_name.split('.')[0]+'_bc.txt', "w")
        for n in range(len(index_map)):
            bc_out.write("%s\n" % index_map[n])
            bc_count[n].sort()
            for i in bc_count[n][::-1]:
                if i > 0: bc_out.write("%s\n" % i)
    bc_out.close()

def extract_barcodes(seq): #wrapper function for barcode extraction from sequence
    bc1_id=0
    bc2_id=0
    bc3_id=0
    found_anchor1=None
    found_anchor2=None
    bc1_length=[7,8,9]
    possible_anchor1=[seq[i:(i+len(anchor1))] for i in bc1_length]
    d,i = min_hamming(possible_anchor1, anchor1)
    if d < 4: found_anchor1 = possible_anchor1[i-1]
    if found_anchor1 == None: #if no anchor can be found return no match
        return [0,0,0], found_anchor1, found_anchor2
    else: #if anchor is found, extract barcode sequences
        bc1_s = seq.split(found_anchor1)[0]
        bc2_s = seq.split(found_anchor1)[1][:8]
        found_anchor2 = seq.split(found_anchor1)[1][8:8+len(anchor2)]
        bc3_s = seq.split(found_anchor1)[1][8+len(anchor2):8+8+len(anchor2)]
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
    #assign bc3, hamming=1 error correction
    d,i = min_hamming(bc3_8,bc3_s)
    if d < 2: bc3_id=i
    return [bc1_id, bc2_id, bc3_id], found_anchor1, found_anchor2

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
                #to speed up searching, return match within 1 hamming when found
                if minimum < 2: return minimum, match
            i=i+1
        return minimum, match

#return a filtered sequence with barcode/primers trimmed
def filter_seq_qual(seq, qual, extract_anchor1, primer_fwd_length, primer_rev_length):
    strip_length_l = len(seq.split(extract_anchor1)[0])+len(anchor1)+8+len(anchor2)+8+primer_fwd_length
    seq_return = seq[strip_length_l:]
    qual_return = qual[strip_length_l:]
    if primer_rev_length > 0:
        seq_return = seq_return[:-primer_rev_length]
        qual_return = qual_return[:-primer_rev_length]
    return seq_return, qual_return

if __name__ == '__main__':
    if len(sys.argv) == 8:
        file_name = sys.argv[1]
        primer_fwd_length = int(sys.argv[2])
        primer_rev_length = int(sys.argv[3])
        min_length = int(sys.argv[4])
        max_length = int(sys.argv[5])
        norm_length = int(sys.argv[6])
        write_bc_count = bool(sys.argv[7])
        process(file_name, primer_fwd_length, primer_rev_length, min_length, max_length, norm_length, write_bc_count)
    else:
        print "error: inputs not fully defined"
        print "syntax: FILE_NAME FWD_PRIMER_LENGTH REV_PRIMER_LENGTH MIN_SEQ_LENGTH MAX_SEQ_LENGTH NORM_LENGTH WRITE_BC_COUNT"
