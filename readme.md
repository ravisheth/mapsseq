# MaPS-seq: Metagenomic Plot-sampling by sequencing

Code, protocols and additional information from the paper "Spatial metagenomic characterization of microbial biogeography in the gut" Sheth RU, Li M, Jiang W, Sims PA, Leong KW, Wang HH. Nature Biotechnology, 2019

The full paper and supplemental information can be accessed [here](https://doi.org/10.1038/s41587-019-0183-2)

### Step-by-step protocol

A comprehensive step-by-step protocol to performing a MaPS-seq experiment can be found [here](./protocol.md).


### Microfluidic chip design

The microfluidic device design can be found [here](./microfluidic/). We ordered the wafer from FlowJEM with a feature height of ~40 μm. 

### MaPS-seq processing code

We developed a [script](./processing/) to demultiplex and process MaPS-seq barcodes after sequencing for input into a typical OTU generation pipeline (e.g. usearch, but your favorite software could also be utilized). 

The sequence analysis workflow as implemented in the manuscript was as follows: 
- Reads for individual samples were merged (usearch -fastq_mergepairs) 
- Merged reads were quality filtered (usearch -fastq_filter)
- The MaPS-seq processing code was utilized to demultiplex and rename individual reads by their barcode, and strip barcode and 16S primer sequences
- Resulting processed reads were subjected to a standard OTU generation pipeline; reads were dereplicated (usearch -derep_fullength), clustered (usearch -cluster_otus), and reads were searched against the generated OTUs (usearch -usearch_global) resulting in a final OTU table for analysis

The MaPS-seq processing script is called from the command line and takes the following arguments. In addition, a file named `param` must be included in the same directory which includes the structure of the barcode utilized (anchor sequences and barcode sequences). The script calls barcodes, renames individual reads with a unique name for each barcode, and strips the barcode and primer sequences from the reads, so the resulting read file can be analyzed in standard OTU generation pipelines. In addition, it is advisable to call the function in parallel (e.g. using [gnuparallel](https://www.gnu.org/software/parallel/)) using a simple shell for loop if you have more than a few samples. 

```
python maps_process.py file_name primer_fwd_length primer_rev_length min_length max_length norm_length write_bc_count
``` 

The requirements for these parameters are explained here: 
- file_name: fastq file input
- primer_fwd_length: length of the forward primer to strip from the 5' of the read
- primer_rev_length: length of the reverse primer to strip from the 3' of the read
- min_length: minimum length of the stripped read (both barcode and primers) to retain in the output
- max_length: maximum length of the stripped read (both barcode and primers) to retain in the output
- norm_length: basepairs from 5' of the stripped read (both barcode and primers) to normalize the read length to; 0 for no read length normalization
- write_bc_count: True or False; should the program write an output file of reads per barcode? 

In the manuscript, we utilized the following parameters with the script, but can be altered if you make a different barcode design or use different sequencing read lengths. 

```
python maps_process.py <filename.fq> 21 20 240 260 0 True
```

### OTU tables

OTU tables containing filtered clusters as analyzed in the manuscript (those that meet the minimum read criteria, and filtered for clusters representing technical artifacts, all as detailed in the methods) are avaliable for re-analysis [here](./otu_tables). TableS5 in the text provides for details around samples names and metadata. We note that there are three different clustered OTU tables (e.g. for Fig2, Fig3, and Fig4 respectively as detailed in TableS5) and the OTU sequences (tableX_otus.fa) correspond to those tables. 

### Generating figures from the manuscript

We developed a [utility script](./utilities/) to easily process data from a MaPS-seq experiment and plot common analyses. A walk-through jupyter notebook can be found [here](./utilities/MaPSseqDemo.ipynb). 

### Data accessibility 

Raw data from the study can be found at NCBI SRA under PRJNA541181

