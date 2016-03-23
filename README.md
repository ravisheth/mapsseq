# MIST-seq protocol 

## Overview

## Detailed Protocol

### Fixation
Samples are fixed in methacarn to avoid damage to mucosal structures and nucleic acids that may result with other fixatives such as formaldehyde. 
- Acquire sample (feces, GI tract etc.) and immediately placed in methacarn solution (60% methanol, 30% chloroform, 10% acetic acid). 
- Fix the sample at room temperature for between 12 to 48 hours. 

### Embedding
The sample is then embedded with an acrylamide matrix which preserves spatial structure and contains a reverse 16S amplification primer. Note that for inclusion of reverse primer, we target a concentration of approximately 100nM per droplet; accounting for droplet volume of 0.5nL this means that 5*10<sup>-5</sup>pmol must be loaded per particle. Assuming a median particle diameter of 20um, and assuming a spherical shape, this yields a particle volume of 4.2pL, meaning that the concentration of reverse primer should be approximately 10uM. 

##### Preparation of  stock solutions
- Monomer solution concentrate (store -20C indefinitely)

| name | stock concentration | amt to add | final conc (w/w) |
|:----:|:-------------------:|:----------:|:---------------:|
|acrymalide|1.25g/2.5mL (1.5mL water sufficient)|2mL|10%|
|bisacrymalide|0.04g/wmL|1.25mL|0.25%|
|PBS|10x|1mL|1x|

- Other stock solutions (store -20C,remake once every 2 weeks)
	- APS (10% w/w; 0.1g/1mL ddH20), final  0.2%
	- TEMED  (10% w/w stock, 0.1g/1mL ddH20), final 0.2%
	- 4HT  (0.5% w/w stock, 0.005g/1mL ddH20), final 0.01%

##### Embedding of sample
- Remove sample from fixative and cut into sub-parts no larger than 3x3mm. A smaller size allows for more effecient perfusion of acrymalide solution.
- Wash in 1mL of PBS, and let sit for 10 minutes. Repeat for a total of 3 times.  
- Prepare an embedding stock solution in the following order on ice, with mixing between each step. Make sure to keep all reagents on ice. 
	- 8uL reverse primer (250uM stock), 10uM final
	- 8uL Cy5 primer (250uM stock), 10uM final
	- 105uL monomer concenrate
	- 67uL water
	- 4uL 4HT
	- 4uL TEMED
	- 4uL APS
- Place the particle in an 1.5mL  eppendorf tube, on ice. Place enough solution to fully embed the particle and allow to sit on ice for approximately 4 hours to allow for full perfusion; cover the tube with foil to prevent premature cleavage of the reverse primer or photobleaching of the fluorophore. You may check for this by seeing if the sample “sinks” in the solution indicating it has equilibrated and any residual air has left.  
- Open the tube, cycle into the anaerobic incubator (O2 impedes polymerization reaction) and allow to polymerize at 37C for 4-6 hours or overnight; cover the tube with foil to prevent premature cleavage of the reverse primer or photobleaching of the fluorophore. 
- Extract the embeded sample from the tube, and trim excess acrlyamide with a sterile razor. 
- Wash 3x in PBS and store in an amber tube at 4C indefinitely. As a QC the first time this is performed, it may be helpful to do a sham sample and cut open to visually ensure that the sample has been fully embedded and polymerized.

### Fracturing
The embedded sample is then broken into small particles using cryofracturing. 
- Place sample in stainless steel microvial (Biospec 2007) and add a single 6.35mm stainless steel bead on top (Biospec 11079635ss). Seal the tube with a silicone rubber plug cap (Biospec 2008). 
- Place (but do not submerge) vial in liquid nitrogen for at least 2 minutes. 
- Quickly transfer to a bead beater (Biospec 112011) and beat for 30s. Inspect tube; if sample has not been completely fractionated repeat the liquid nitrogen freezing and bead beating for an additional step. 
- Resuspend particles in PBS, vortex, and transfer to a sterile tube. Wash 3 times in PBS. Metal residue may color the particles a grey color, but this will not affect downstream steps. 

### Lysis of cells within embedded particles
Particles are then treated with lysozyme and proteinase K to lyse any remaining cells. 
##### Lysozyme treatment
- Wash particles in 500uL TE buffer (Tris pH 8 10mM, EDTA 1mM) 3x times. 
- Resuspend particle in lysis buffer (Tris pH 8 10mM, EDTA 1mM, NaCl 100mM) 
- Add 50U/uL of lysozyme (0.66uL of 1:10 37.5U/uL stock for 50uL of sample)
- Incubate at 37C for 15 min

##### Proteinase K treatment
- Wash particles in 500uL digestion buffer (30mM Tris HCl pH 8.0, EDTA 1mM, 0.5% Triton X-100, 800mM guanidine HCl) 3x times. 
- Add 1ug/uL of proteinase K (1uL of 50ug/uL stock for 50uL of sample)
- Incubate at 65C for 15 min
- Incubate at 95C for 10 min to inactivate proteinase K.
- Wash particles in 500uL TlowE buffer 3x times and store at 4C

### Size selection
We utilize nylon mesh filters to size-select fractured acrylamide particles. 
##### Preparation of nylon mesh filters
- Sterilize a 1/2" hole punch (Amazon) and workspace. 
- Take nylon mesh filters of size 7um, 15um, 31um, 52um (Component Supply Company) and punch. Prepare multiple dots for multiple experiments in advance. 
- Place in a plastic bag for long-term storage

##### Size selection of acrylamide particles
- Clean and sterilize 4 Swinnex 13mm filter holders, 4 gasket O-rings, 1 punched nylon mesh filter of each size, and 4 3mL BD syringes via UV steriliation. 
- Place each filter in a Swinnex filter holder with gasket O-ring. 
- Perform the following steps for the 52um, 31um, 15um, 7um filters in order to yield >52um, 31-52um, 15-31um, 7-15um and <7um size filtered particles. 
	- Take sample and resuspend in 1mL of nuclease-free water. Connect a 3mL syringe to the filter. Pipette the 1mL into the filter, and carefully push liquid through the filter applying minimal pressure to the syringe. Collect sample in a sterile 1.5mL tube and repeat this filtering step twice for a total of three times. Set flow-through aside; this fraction contains particles smaller than the filter size.
	- Perform a wash by attaching a blunt syringe to the filter assembly, and aspirating 3mL of nuclease-free water. completely flow through the 3mL through and discard, repeat this wash twice for a total of three times. 
	- Aspirate 1mL of nuclease-free water. In the syringe, flow back and forth through the filter assembly for a total of three times. Pull remaining liquid in the syringe and set aside; this fraction contains particles greater than the filter size. 
- Each fraction can be pelleted via centrifugation and resuspended in storage buffer for long term storage. 

### Barcoded Bead Construction
Note: this protocol yields 3 to 4 million beads containing one of approximately 9,200 barcodes. We target at least 100nM primer concentration per droplet. Assuming a droplet volume of approximately 0.5nL, and accounting for a worst-case extension efficiency of 10%, each bead must be initially loaded with 5*10<sup>-4</sup> pmol of primer. 

##### Conjugation of streptavidin to beads
- Extract sepharose beads with a mean diameter of approximately 30μm from 1mL GE HiTrap NHS-Activated HP columns (GE Healthcare 17071601). The bottom of the column can be cut off directly above the filter assembly with a razor blade, and beads can be flushed out with a syringe filled with isopropanol coupled to the provide syringe adapter. Filter beads through a 100um cell strainer (Fisher 22-363-549) to remove any debris or aggregrated beads, and store in isopropanol at 4C. 
- Measure the concentration of bead stock with a hemacytomter, and prepare an aliquot of 10 million beads in a 1.5mL tube. Wash with 1mL of nuclease-free water, and gently pellet by centrifugation in a microcentrifuge. Repeat this wash twice for a total of three washes. Carefully remove all water from the aliquot.  
- Prepare a 250uL solution of 100mM borate, 0.75mg/mL streptavidin and 5% Streptavidin-Cy3 by mixing: 50uL 0.5M sodium borate, 187.5uL 1mg/mL streptavidin (NEB N7021S) and 12.5uL Streptavidin-Cy3 (Life Technologies 43-4315). To covalently attach the streptavidin and Cy3 label to the beads, resuspend the prepared beads in the full 250uL of the solution. Incubate at room temperature on a rotisserie for 1 hour. 
    - **Note:** from this point forward, all materials should be shielded from ambient light with amber tubes or foil to the greatest extent possible, to prevent premature cleavage of the photocleavable linker and bleaching of the Cy3 fluorophore. 
- Wash the beads with 1mL of wash buffer (10mM Tris-HCl pH 8.0, 0.1% Tween 20, 100mM NaCl) and gently pellet by centrifugation in a microcentrifuge. Repeat this wash four times for a total of five washes. Incubate the beads in approximately 1mL of wash buffer at room temperature on a rotisserie for 30 minutes to fully quench any remaining reactive groups on the beads. 

##### First round primer extension 
- In each well of a 96-well PCR plate, prepare a 10uL solution of 2.5uM 2bio-PC-pe1 primer and 10uM pe1 primer for each well. 
    - Specifically, prepare 900uL containing 10uL of 250uM 2bio-PC-pe1 and 890uL nuclease free water. Pipette 9uL of the master mix into each well of a 96 well plate. Add 1uL of 100uM e1 primer to each well. 
- Perform a stepwise cooling from 85C to 25C over 30 minutes (ramp -2C/min)
- Add a Klenow (NEB M0210L) master mix such that each well has a final volume of 20uL containing 1x NEBuffer 2, 0.5mM dNTPs, and 2U Klenow. 
    - Specifically, prepare a 1000uL master mix containing 200uL NEBuffer 2 10x, 100uL 10mM dNTPs, 40uL Klenow (5,000 units/mL) and 660uL nuclease free water. Add 10uL to each well and mix well. 
- Incubate at 25C for 30 minutes. 
- Add 1uL of 0.5M EDTA pH8.0 to each well and mix well. 
- Incubate at 75C for 20 minutes

##### Conjugation of extended oligonucleotide to beads
- Beads should be resuspended in approximately 1mL of wash buffer per protocol above. Measure concentration of beads with a hemacytometer and add 50,000 beads to each well. Mix well by pipetting. 
- Incubate on a rotisserie at room temperature overnight. 
- Quench the reaction with 70uL of 125mM NaOH, 2mM biotin and mix well. 
- Pool the reactions and wash 5 times with 10mL of 125mM NaOH, 0.1mM biotin. 
- Wash 3 times with wash buffer supplemented with 0.1mM biotin. 
- Resuspend in hybridization buffer (10mM Tris-HCl pH 8.0, 0.1% Tween 20, 1M NaCl) with 0.1mM biotin such that the final volume of the entire mixture is 900uL. 

##### Second round primer extension
- Aliquot 9uL of beads in hybridization buffer (ensure beads are in suspension throughout process) into each well of a 96-well PCR plate. 
- Add 1uL of 100uM e2 primer to each well such that the concentration is 10uM. Mix well. 
- Incubate on a rotisserie at room temperature overnight. 
- Wash the beads 3 times with wash buffer suppemented with 0.1mM biotin. The plate must be centrifuged during this step and care must be taken to not accidentally aspirate any beads. 
- Remove as much of the of wash buffer as possible, taking care not to aspirate any of the beads.  
- On ice, add a Klenow (NEB M0210L) master mix such that each well has a final volume of 20uL containing 1x NEBuffer 2, 0.5mM dNTPs. 
    - Specifically, prepare a 2000uL master mix containing 200uL NEBuffer 2 10x, 100uL 10uM dNTPs, 40uL Klenow (5,000 units/mL) and 1660uL nuclease free water, and chill on ice. Add 20uL to each well and mix well. 
- Transfer plate to a PCR block at 16C and incubate for 1hr. Vortex plate every 15 minutes to keep beads in solution. 
- Add 2uL of 0.5M EDTA pH8.0 to each well and mix well. Incubate on ice for 30 minutes to allow full chelation of magnesium ions and inactivation of Klenow.
- Quench the reaction with 70uL of 125mM NaOH, 2mM biotin and 10mM EDTA and mix well. 
- Pool the reactions and wash 5 times with 10mL of 125mM NaOH, 0.1mM biotin, 10mM EDTA.  
- Wash 3 times with wash buffer supplemented with 0.1mM biotin and 0.1mM EDTA. 
- Resuspend beads in approximately 1mL of the wash buffer, 0.1mM biotin, 0.1mM EDTA solution, and store at 4C in an amber tube.  

### Barcoded Bead Quality Control
##### Quantification of extension efficiency via FISH
To assess the efficiency of primer extension, we utilize fluorescence in situ hybridization with FAM labeled probes targeted to the Illumina adapter (i.e. unextended ssDNA product) and the 505f primer (fully extended ssDNA product). The ratio of intensity observed with the 505f probe to the Illumina probe reflects the extension efficiency of the construction protocol. 
- Resuspend ~5,000 beads in 19.2uL hybridization buffer. Add 0.8uL of 250uM probe (either Illumina or 505f) such that the final concentration is 10uM. Include a negative control (beads with streptavidin, streptavidin-Cy3, but no primer) and positive control (beads with full primer product conjugated).
- Allow to hybridize at RT on a rotisserie for 30 min. 
- Wash beads 3 times with 500uL of hybridization buffer. Resuspend in 2uL of nuclease-free water, spot onto a slide, and allow to dry. 
- Record average intensity per bead using an epifluorescence microscope. 

##### Validation of photorelease of primers from bead
To assess UV exposure-dependent release of primers from barcoded beads, we utilize the Agilent Bioanlyzer HS DNA assay kit to detect low concentrations of ssDNA product. 
- Resuspend ~5,000 beads in 10uL nuclease-free water. Make two aliquots. 
- Expose one aliquot to UV light (BlackRay Xenon 365nm UV) for 15 minutes on ice. Place the other aliquot on ice and protect from ambient light. 
- Spin down aliquots and remove ~5uL of supernatant. 
- Load 1uL of supernatant and follow manufacturer instructions for the Agilent Bioanylyzer HS DNA kit. 

##### Sequencing of individual bead primers and total pool primers
To assess the composition of primers on a single bead as well as the composition of the entire pool of beads, we utilize deep sequencing of the ssDNA primers on the Illumina MiSeq platform. 
- Suspend 100,000 beads (approximately 10x the size of the library) in 48uL of hybridization buffer with 0.1mM biotin. Add 2uL of 250uM stock pe2-umi-505f primer such that the final concentraiton is 10uM. Allow primers to anneal for 1 hr on a rotisserie at room temperature. 
- Wash beads 3 times with wash buffer supplemented with 0.1mM biotin. Remove as much of the wash buffer as possible without aspirating any of the beads. 
- Add 50uL of a Klenow master mix such that the tube has a final volume of 50uL containing 1x NEBuffer 2, 0.5mM dNTPs and and 5U Klenow. 
	- Specifically, mix 5uL NEBuffer 2 10x, 2.5uL 10uM dNTPs, 1uL Klenow (5,000 units/mL) and 41.5uL nuclease-free water. 
- Incubate at 25C for 30 minutes. Vortex every 10 minutes to keep beads in solution.
- Add 5uL of 0.5M EDTA pH8.0 and mix well. Incubate on ice for 30 minutes to allow full chelation of magnesium ions and inactivation of Klenow. 
- Quench the reaction with 100uL of 125mM NaOH, 2mM biotin and 10mM EDTA. 
- Transfer to a 1.5mL tube and wash 5 times with 500uL of 125mM NaOH, 2mM biotin and 10mM EDTA. 
- Wash 3 times with wash buffer supplemented with 0.1mM biotin and 0.1mM EDTA. 
- Dilute an aliquot of beads and isolate single beads on a microscope field by pipetting carefully with a 2uL pipette. Place 16 beads in PCR tubes with 10uL of nuclease-free water. 
- Resuspend the remaining ~100,000 beads in 10uL of nuclease free water. 
- Expose all tubes to UV light (BlackRay Xenon 365nm UV) for 15 minutes on ice. 
- Add 20uL of Kapa HiFi PCR Master Mix, forward primer, and uniquely indexed reverse primer to each tube such that the final volume is 30uL
	- Specifically, prepare a master mix of 255uL Kapa HiFi PCR Master Mix 2x, 25.5uL pe1 forward primer 10uM, 5.1uL SYBR 100x, 28.9uL nuclease-free water. Aliquot 18.5uL of this master mix into each tube, and add 1.5uL of pe2 indexed reverse primer 10uM (ie containing appropriate barcode). Mix well. 
- Amplify via a PCR reaction, with 20 cycles for the individual beads and 10 cycles for the pooled beads: 95C 5m, 98C 20s, 60C 15s, 72C 30s, 72C 5m. 
- Quantitate products using the Qubit HS DNA platform and pool together at an equimolar ratio. Clean up using a Qiagen PCR clean up kit, quantitate, and sequence on the MiSeq platform (2x25 read length, index 1 8bp). 

### Encapsulation
##### Equipment required
- An in-syringe magnetic mixer was constructed with 400 RPM mini DC geared gear box electric motor (uxcell, Amazon) driven by a Unique Goods Digital Display DC Motor Speed Controller (Amazon) and a 6V 1A power adapter (Amazon). The motor rotates a small neodynium magnet (K&J magnetics B448) via a custom 3D printed adapter. This spins a 3x3mm magnetic stirbar (Bel-Art Z283835) which fits within a 1mL syringe.
- We utilize two Harvard Apparatus Pump 11 Elite syringe pumps and a Zeiss Axiovert 25 inverted microscope to observe droplet formation and flow. 
- To generate droplets, we use a flow-focusing (T-junction) droplet generator cast in PDMS. The diameter of the droplet forming junction is 60um in width. This yields droplets of approximately 90um in diameter or 0.5nL in volume. 

##### Encapsulation protocol
A microfluidic device is used to encapsulate barcoded beads and particles. Approximately 1 in 10 droplets will receive a bead, while approximately 1 in 10 droplets will receive a particle; this implies that approximately 1 in 100 droplets will receive a bead and particles. The distribution of droplet occupancy follows the Poisson distribution as expected, leading to a low doublet rate.  
- UV sterilize encapsulation supplies for 30 minutes: microfluidic chip, magnetic stir-bar, 1mL syringe, 1.5mL  collection tube, Hamilton luer to tubing connector, tubing exit connector. 
- Clean appropriate amount of beads and acrylamide particles (~20K beads, ~10K particles) with 100uL nuclease-free water. Resuspend in 4uL of water each. 
- Mix 200uL encapsulation master mix as follows: 100uL Kapa HiFi PCR MasterMix, 20uL 10%w/v Pluronic 127, 32uL NycoPrep (60% w/v Nycodenz), 5uL BSA (20mg/mL, NEB), 4uL acrylamide particles, 4uL barcoded beads and water to 200uL. Note that the final density of a 16% NycoPrep solution should be approximately 1.05g/mL.
- Mix mixture well without introducing bubbles and pipette into 1mL syringe. Carefully load syringe with magnetic mixer. 
- Prepare a second syringe with 1mL of 2%EA surfactant in HFE7500. 
- Connect tubing to chip, and prime syringes. Turn on the syringe mixer to 400rpm. 
- Flow syringes as 15uL/min for the PCR and 30uL/min for the oil. 
- Observe proper and stable droplet formation (faint flickers at droplet junction)
- Collect droplets into a LoBind tube cooled on ice


### PCR amplification and library prep
##### First round PCR amplification
- Pipette out 10uL of just droplets into PCR tubes. Each 10uL contains approximately 100 particles. 
- Add 10uL of 10%EA in HFE7500 to each tube
- Place tubes under UV light with top open on ice and treat for 15 min
- Cover with 30uL of mineral oil
- Run with the following PCR program:
	- 1 95 30s
	- 2 95 10s
	- 3 55 15s 
	- 4 72 30s
	- 5 step 2, 9x
	- 6 72 30s
	- 7 10 infinity

##### Ampure clean up
- Ensure that droplets are intact after cycling. One tube can be taken and droplet encapsulation distributions can be observed for QC purposes if desired. 
- Add 10uL of perfluorooctonal to the droplet phase. Vertically flick 3-4 times hard and centrifuge down.
- Extract 6uL of the aqueous phase and add 14uL nuclease free water.
- Clean up with AmpureXP 0.8x and resuspend in 5uL of nuclease free water.

##### Indexing PCR
- Setup up following reaction: 5uL first round PCR product, 0.4uL forward index primer (10uM), 0.4uL reverse index primer (10um), 4.2uL water, 10uL 2x Kapa Hifi MasterMix. 
- Run with the following PCR program:
	- 1 95 2m
	- 2 98 20s
	- 3 72 60s
	- 4 step 2, 29x
	- 5 72 2m
	- 6 10 infinity