# MaP-seq: Metagenomic Plot-sampling by sequencing

Code, protocols and additional information from the paper "Spatial metagenomic characterization of microbial biogeography in the gut" Sheth RU, Li M, Jiang W, Sims PA, Leong KW, Wang HH. Nature Biotechnology, 2019

The full paper and supplemental information can be accessed here [TO BE ADDED]

### Step-by-step protocol

A comprehensive step-by-step protocol to performing a MaP-seq experiment can be found [here](./protocol.md).

### MaP-seq processing code

We developed a [script](./processing/) to demultiplex and process MaP-seq barcodes after sequencing for input into a typical OTU generation pipeline (e.g. usearch, but your favorite software could also be utilized). 

The sequence analysis workflow as implemented in the manuscript was as follows: 
- Reads for individual samples were merged (usearch -fastq_mergepairs) 
- Merged reads were quality filtered (usearch -fastq-filter)
- The MaP-seq processing code was utilized to demultiplex and rename individual reads by their barcode, and strip barcode and primer sequences
- Resulting processed reads were subjected to a standard OTU generation pipeline; reads were dereplicated (usearch -derep_fullength), clustered (usearch -cluster_otus), and reads were searched against the generated OTUs (usearch -usearch global) resulting in a final OTU table for analysis

The MaP-seq processing script is called from the command line and takes the following arguments. In addition, a file named `param` must be included in the same directory which includes the structure of the barcode utilized (anchor sequences and barcode sequences). The script calls barcodes, renames individual reads with a unique name for each barcode, and strips the barcode and primer sequences from the reads, so the resulting read file can be analyzed in standard OTU generation pipelines. 

```
python map_process.py file_name primer_fwd_length primer_rev_length min_length max_length norm_length write_bc_count
``` 

The requirements for these parameters are explained here: 
- file_name: fastq file input
- primer_fwd_length: length of the forward primer to strip from the 5' of the read
- primer_rev_length: length of the reverse primer to strip from the 3' of the read
- min_length: minimum length of the stripped read (both barcode and primers) to retain in the output
- max_length: maximum length of the stripped read (both barcode and primers) to retain in the output
- norm_length: basepairs from 5' of the stripped read (both barcode and primers) to normalize the read length to; 0 for no read length normalization
- write_bc_count: True or False; should the program write an output file of reads per barcode? 

In the manuscript, we utilized the following parameters with the script. 

```
python map_process.py <filename.fq> 21 20 240 260 0 True
```

In addition, it is advisable to call the function in parallel (e.g. using [gnuparallel](https://www.gnu.org/software/parallel/)) using a simple shell script if you have a few samples. 

### Microfluidic chip design

The microfluidic device design can be found [here](./microfluidic/). We ordered the wafer from FlowJEM with a feature height of ~40 μm. 

### OTU tables

[TODO]

### Generating figures from the manuscript

[TODO]

