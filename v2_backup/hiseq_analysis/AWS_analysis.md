# MIST-seq data analysis on AWS
Start c4.4xlarge AWS instance, 250GB HDD, Amazon linux, and SSH in
```bash
ssh -i [keypair] ec2-user@[location]
```

Configure AWS CLI with keypair and secret key
```bash
sudo pip install awscli
aws configure
```

Copy usearch executable
```bash
aws s3 cp s3://ravi_sheth/bin/usearch9.1.13_i86linux32 ./bin/usearch
sudo chmod +x ~/bin/usearch
```

Sync data and unzip
```bash
aws s3 sync s3://ravi_sheth/seq_files/20161208_MIST_hiseq/fastq/ ./fastq/
cd fastq
gzip -d *.gz
```

For each file, merge lanes together
```bash
find ./fastq/*_L001_R1_001.fastq -type f | while read LANE1 ; do
    LANE2="$(echo ${LANE1} | sed 's/L001/L002/')";
    NEWFILE="$(echo ${LANE1} | sed 's/_.*$//')_L12.fastq";
    cat "${LANE1}" "${LANE2}" > "${NEWFILE}";
done
```

usearch filtering of each lane
```bash
find ./fastq/*_L12.fastq -type f | while read FILENAME ; do
    OUTFILE="$(echo ${FILENAME} | sed 's/_.*$//')_L12_f.fastq";
    ./bin/usearch -fastq_filter "${FILENAME}" -relabel @ -fastq_maxee 1.0 -fastq_trunclen 205 -fastqout "${OUTFILE}";
done
```

Parallel MIST processing
```bash
aws s3 sync s3://ravi_sheth/bin/mist_extract_hiseq/ ./bin/mist_extract_hiseq
cd /etc/yum.repos.d/
sudo wget http://download.opensuse.org/repositories/home:tange/CentOS_CentOS-5/home:tange.repo
sudo yum install parallel
cd ~
ls fastq/*_f.fastq | parallel -j8 "python ./bin/mist_extract_hiseq/mist_tools.py {}"
 ```

Save intermediate files
```bash
aws s3 sync fastq/ s3://ravi_sheth/working/20161213_mist_hiseq_processing/
 ```

Change instance to r4.4 for greater memory, and perform vsearch dereplication
```bash
aws s3 sync s3://ravi_sheth/bin/vsearch-2.3.4-linux-x86_64/ ./bin/vsearch
chmod +x ./bin/vsearch/bin/vsearch
rm fastq/*.fastq
cat fastq/*.fq > fastq/all.fq
./bin/vsearch/bin/vsearch -derep_fulllength fastq/all.fq -relabel Uniq -sizeout -output uniques.fa
 ```

Change instance back to c4.8xlarge and perform clustering
```bash
./bin/usearch -cluster_otus uniques.fa -minsize 2 -otus otus.fa -relabel Otu
#note, could be parallelized...
find ./fastq/*_out.fq -type f | while read FILENAME ; do
    OUTFILE="$(echo ${FILENAME} | sed 's/_.*$//')_97.txt";
    ./bin/usearch -usearch_global "${FILENAME}" -db otus.fa -strand plus -id 0.97 -otutabout "${OUTFILE}";
done
mkdir output
mkdir output/table_out
mv uniques.fa output/
mv otus.fa output/
mv out.txt output/
mv fastq/*.txt output/table_out/
 ```

Backup output data
```bash
aws s3 sync output/ s3://ravi_sheth/working/20161213_mist_hiseq_processing/output/
```

Remove #OTUID string from tables
```bash
find output/table_out/*.txt -type f | while read FILENAME ; do sed -i.bak -r '1s/^.{8}//' "${FILENAME}"; done
rm output/table_out/*.bak
aws s3 sync output/ s3://ravi_sheth/working/20161213_mist_hiseq_processing/output/
```

Then perform processing of tables locally

Note: we could try UNOISE two when it is fixed. Skeleton code below:
```bash
aws s3 cp s3://ravi_sheth/bin/usearch9.0.2132_i86linux32 ./bin/usearch90
sudo chmod +x ~/bin/usearch90
./bin/usearch90 -unoise uniques.fa -tabbedout out.txt -fastaout denoised.fa
usearch -usearch_global reads.fq -db denoised.fa -strand plus -id 0.97 -otutabout otu_table.txt
```
