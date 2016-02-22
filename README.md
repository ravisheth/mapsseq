# MIST-seq protocol 

## Overview

## Detailed Protocol

### Fixation

Sample (feces, GI tract etc.) was taken and immediately placed in methacarn solution (60% methanol, 30% chloroform, 10% acetic acid). The sample was fixed at room temperature for between 4 to 48 hours. After fixation, the sample is allowed to dry/evaporate in a sterile environment at room temperature.

### Embedding

Subparts of the sample no larger than 5x10mm in size were then sliced for embedding. First, acrylamide stock solutions are generated for embedding:

monomer solution (store -20C indefinitely)

| name | stock concentration | amt to add | final conc (w/w) |
|:----:|:-------------------:|:----------:|:---------------:|
|acrymalide|1.25g/2.5mL (1.5mL water sufficient)|2mL|10%|
|bisacrymalide|0.04g/wmL|1.25mL|0.25%|
|PBS|10x|1mL|1x|

Other chemicals (store -20C,remake once every 2 weeks)

- APS (10% w/w; 0.1g/1mL ddH20), final  0.2%
- TEMED  (10% w/w stock, 0.1g/1mL ddH20), final 0.2%
- 4HT  (0.5% w/w stock, 0.005g/1mL ddH20), final 0.01%

A stock solution was then mixed in the following order, on ice, with mixing in between each step. All reagents are kept on ice.

- 8uL reverse primer (250uM stock), 10uM final
- 4uL Cy5 primer (250uM stock), 5uM final
- 105uL monomer concenrate
- 71uL water
- 4uL 4HT
- 4uL TEMED
- 4uL APS

The particle is placed in an 1.5mL amber eppendorf tube, on ice. 100uL of the solution is added and allowed to sit for 5 minutes. Then the solution is carefully pipetted out and replaced with the next 100uL of the solution. This is allowed to embed for approximately 1 hour, or until the sample is embedded. You may check for this by seeing if the sample “sinks” in the solution indicating it has equilibrated and any residual air has left.

The tube is then opened, cycled into the anaerobic incubator (O2 impedes polymerization reaction) and allowed to polymerize at 37C for 4-6 hours. You can use a small aliquot of previously removed solution polymerized in identical conditions as a “sham” to detect if polymerization has occured.

The pellet is then extracted from the tube, excess acrlyamide trimmed with a sterile razor, washed 3x in PBS and stored in an amber tube at 4C indefinitely. As a QC the first time this is performed, it may be helpful to do a sham sample and cut open to visually ensure that the sample has been fully embedded and polymerized with your protocol.

### Fractionation

### Size Selection
Nylon mesh filters of size XX, XX, XX (Component Supply Company) were punched using a 1/2” hole punch (Amazon) and placed in a Swinnex 13mm filter holder (ThermoFisher).

### Lysis
Wash

- Wash particle T<sub>10</sub>E<sub>1</sub> (Tris pH 8 10mM, EDTA 1mM) buffer 500uL 2x

Lysozyme:

- resuspend particle in T<sub>10</sub>E<sub>1</sub>S<sub>100</sub> buffer (Tris pH 8 10mM, EDTA 1mM, NaCl 100mM) 
- use 50U/uL or 2.5K units, or 0.066uL of 37.5K stock
- Incubate RT 15 min
- Wash 2x 500uL TK Buffer

Proteinase K:

- digestion buffer: 30mM Tris HCl 30mM EDTA< 5% Tween 20 0.5% Triton X 100 800mM GuHCl 
- use 1:50 of 50ug/uL stock (0.5uL)
- Incubate at 65C, 15 min vortex every 5min
- Incubate at 95C, 10 min (inactivate PK to make sure we are OK for PCR)
- Wash 2x T<sub>10</sub>E<sub>1</sub>  buffer and store at 4C

### Barcoded Bead Construction
Note: this protocol yields 3 to 4 million beads containing one of approximately 9,200 barcodes. We target at least 100nM primer concentration per droplet. Assuming a droplet volume of approximately 0.5nL, and accounting for a worst-case extension efficiency of 10%, each bead must be initially loaded with 5*10<sup>-4</sup> pmol of primer. 

##### Conjugation of streptavidin to beads
- Extract sepharose beads with a mean diameter of approximately 30μm from 1mL GE HiTrap NHS-Activated HP columns (GE Healthcare 17071601). The bottom of the column can be cut off directly above the filter assembly with a razor blade, and beads can be flushed out with a syringe filled with isopropanol coupled to the provide syringe adapter. Filter beads through a 100um cell strainer (Fisher 22-363-549) to remove any debris or aggregrated beads, and store in isopropanol at 4C. 
- Measure the concentration of bead stock with a hemacytomter, and prepare an aliquot of 10 million beads in a 1.5mL tube. Wash with 1mL of nuclease-free water, and gently pellet by centrifugation in a microcentrifuge. Repeat this wash twice for a total of three washes. Carefully remove all water from the aliquot.  
- Prepare a 250uL solution of 100mM borate, 0.75mg/mL streptavidin and 5% Streptavidin-Cy3 by mixing: 50uL 0.5M sodium borate, 187.5uL 1mg/mL streptavidin (NEB N7021S) and 12.5uL Streptavidin-Cy3 (Life Technologies 43-4315). To covalently attach the streptavidin and Cy3 label to the beads, resuspend the prepared beads in the full 250uL of the solution. Incubate at room temperature on a rotisserie for 1 hour. 
    - Note: from this point forward, all materials should be shielded from ambient light with amber tubes or foil to the greatest extent possible, to prevent premature cleavage of the photocleavable linker and bleaching of the Cy3 fluorophore. 
- Wash the beads with 1mL of wash buffer (10mM Tris-HCl pH 8.0, 0.1% Tween 20, 100mM NaCl) and gently pellet by centrifugation in a microcentrifuge. Repeat this wash four times for a total of five washes. Incubate the beads in approximately 1mL of wash buffer at room temperature on a rotisserie for 30 minutes to fully quench any remaining reactive groups on the beads. 

##### First round primer extension 
- In each well of a 96-well PCR plate, prepare a 10uL solution of 2.5uM 2bio-PC-pe1 primer and 10uM pe1 primer for each well. 
    - Specifically, prepare 900uL containing 10uL of 250uM 2bio-PC-pe1 and 890uL nuclease free water. Pipette 9uL of the master mix into each well of a 96 well plate. Add 1uL of 100uM pe1 primer. 
- Perform a stepwise cooling from 85C to 25C over 30 minutes (ramp -2C/min)
- Add a Klenow (NEB M0210L) master mix such that each well has a final volume of 20uL containing 1x NEBuffer 2, 0.5mM dNTPs, and 2U Klenow. 
    - Specifically, prepare a 1000uL master mix containing 200uL NEBuffer 2 10x, 100uL 10mM dNTPs, 40uL Klenow (5,000 units/mL) and 660uL nuclease free water. Add 10uL to each well and mix well. 
- Incubate at 25C for 30 minutes. 
- Add 1uL of 0.5M EDTA pH8.0 to each well and mix well. 
- Incubate at 75C for 20 minutes

##### Conjugation of extended oligonucleotide to beads
- Beads should be resuspended in approximately 1mL of wash buffer per protocol above. Measure concentration of beads with a hemacytometer and add 50,000 beads to each well and mix well by pipetting. 
- Incubate on a rotisserie at room temperature overnight. 
- Quench the reaction with 70uL of 125mM NaOH, 2mM biotin and mix well. 
- Pool the reactions and wash 5 times with 10mL of 125mM NaOH, 0.1mM biotin. 
- Wash 3 times with wash buffer supplemented with 0.1mM biotin. 
- Resuspend in hybridization buffer (10mM Tris-HCl pH 8.0, 0.1% Tween 20, 1M NaCl) with 0.1mM biotin such that the final volume of the entire mixture is 900uL. 

##### Second round primer extension
- Aliquot 9uL of beads in hybridization buffer (ensure beads are in suspension throughout) into each well of a 96-well PCR plate. 
- Add 1uL of 100uM pe2 primer to each well such that the concentration is 10uM. Mix well. 
- Incubate on a rotisserie at room temperature overnight. 
- Wash the beads 3 times with wash buffer suppemented with 0.1mM biotin. The plate must be centrifuged during this step and care must be taken to not accidentally aspirate any beads. 
- Remove 8uL of wash buffer such that the remaining beads are resuspended in in 2uL. Replace with 8uL of nuclease free water. 
- Add a Klenow (NEB M0210L) master mix such that each well has a final volume of 20uL containing 1x NEBuffer 2, 0.5mM dNTPs. Note that Klenow will be added in a subsequent step. Cool the mixture to 16C. 
    - Specifically, prepare a 960uL master mix containing 200uL NEBuffer 2 10x, 100uL 10uM dNTPs, 40uL Klenow (5,000 units/mL) and 860uL nuclease free water. Add 9.6uL to each well and mix well. 
- Once mixture is cooled to 16C, add 0.4uL of Klenow (5,000 units/mL).
- Incubate at 16C for 1hr. 
- Add 2uL of 0.5M EDTA pH8.0 to each well and mix well. 
- Incubate on ice for 30 minutes to allow full chelation of magnesium ions and inactivation of Klenow.
- Quench the reaction with 70uL of 125mM NaOH, 2mM biotin, 10mM EDTA and mix well. 
- Pool the reactions and wash 5 times with 10mL of 125mM NaOH, 0.1mM biotin, 10mM EDTA.  
- Wash 3 times with wash buffer supplemented with 0.1mM biotin. 
- Resuspend beads in approximately 1mL  storage buffer (10mM Tris-HCl pH 8.0, 0.1mM EDTA, 0.1% Tween-20) supplemented with 0.1mM biotin. 

### Barcoded Bead QC
DNA FISH
Deep Sequencing on MiSeq 50

### Encapsulation
##### Equipment required
- An in-syringe magnetic mixer was constructed with 400 RPM mini DC geared gear box electric motor (uxcell, Amazon) driven by a Unique Goods Digital Display DC Motor Speed Controller (Amazon) and a 6V 1A power adapter (Amazon). The motor rotates a small neodynium magnet (K&J magnetics B448) via a custom 3D printed adapter. This spins a 3x3mm magnetic stirbar (Bel-Art Z283835) which fits within a 1mL syringe.
- We utilize two Harvard Apparatus Pump 11 Elite syringe pumps and a Zeiss Axiovert 25 inverted microscope to observe droplet formation and flow. 
- To generate droplets, we use a flow-focusing (T-junction) droplet generator cast in PDMS. The diameter of the droplet forming junction is 60um in width. This yields droplets of approximately 90um in diameter or 0.5nL in volume. 

##### Encapsulation protocol
- UV treatment of all required equipment. 
- Mix 200uL encapsulation master mix as follows: 100uL Kapa Hifi PCR MasterMix, 32uL NycoPrep (60% w/v Nycodenz), 20uL 10%w/v Pluronic 127, 5uL BSA (20mg/mL, NEB), XXuL acrylamide particles, XXuL barcoded beads (approximately 200 particles/uL). Note that the final density of a 16% NycoPrep solution should be approximately 1.05g/mL.
- Pipette into 1mL syringe (BD) and carefully load syringe

tubing
        
Cool syringe
Cool when collecting


### Droplet PCR
PCR program:
1 98 30s
2 98 10s
3 55 30s (Tm on NEB website is calculated to be 67C)
4 72 60s
5 step 2, 20x
6 72 2:00

### Droplet breakage
Perfluorooctaonal

### Second round PCR
PCR program:
1 98 30s
2 98 10s
3 65 30s
4 72 30s
5 step 2, 9 or 19x
6 72 2:00

