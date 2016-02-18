# MIST-seq protocol 

## Overview

## Detailed Protocol

### Fixation

Sample (feces, GI tract etc.) was taken and immediately placed in methacarn solution (60% methanol, 30% chloroform, 10% acetic acid). The sample was fixed at room temperature for between 4 to 48 hours. After fixation, the sample is allowed to dry/evaporate in a sterile environment at room temperature.

### Embedding

Subparts of the sample no larger than 5x10mm in size were then sliced for embedding. First, acrylamide stock solutions are generated for embedding:

monomer solution (store -20C indefinitely)

name

stock concentration

amt to add

final concentration (w/w)

acrymalide

1.25g/2.5mL
(use ~1.5mL to get 2.5mL total)

2mL

10%

bisacrymalide

0.04g/2mL

1.25mL

0.25%

PBS

10x

1mL

1x

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
Beads were extracted from GE HiTrap NHS-Activated HP columns. The bottoms were cutoff and flushed with isopropanol via a syringe, and stored in isopropanol at 4C. Beads were also passed through a 100um cell strainer (Fisher) to remove any debris or doublet beads.

### Barcoded Bead QC
DNA FISH
Deep Sequencing on MiSeq 50

### Encapsulation
An in-syringe magnetic mixer was constructed with 400 RPM mini DC geared gear box electric motor (uxcell, Amazon) driven by a Unique Goods Digital Display DC Motor Speed Controller (Amazon) and a 6V 1A power adapter (Amazon). The motor rotates a small neodynium magnet (K&J magnetics B448) via a custom 3D printed adapter.

Harvard Apparatus Pump 11 Elite
60uM flow-focusing droplet generator
Droplets of around 0.86nL

Cool syringe
Cool when collecting

PCR mix:
Load in 1mL syringe, 200uL total
3x3mm magnetic mixer

32% NycoPrep Universal (60%, final density ~ 1.1g/mL)
1% Pluronic F127
Run PCR with mineral oil on top, no heated lid

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