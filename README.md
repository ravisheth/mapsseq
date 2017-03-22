# MIST-seq protocol

This document contains MIST-seq v3 protocol and implementation.

### Barcoded Hydrogel Construction
Barcoded Hydrogel construction consists of three extension steps to create over 880,000 barcoded hydrogel beads. Construction largely follows Zilionis, Nature Protocols 2016 with minor modifications.

#### Required buffers
- Acry/Bis stock 4X (24%T, 3%C): 3.8mL water, 1.2g Acrylamide, 0.036g Bisacrylamide
- TBSET buffer: 10mM Tris HCl pH 8.0, 137mM NaCl, 2.7mM KCl, 10mM EDTA, 0.1% Triton-X 100  
- WB: 10mM Tris HCl pH 8.0, 0.1mM EDTA, 0.1% Tween 20
- TET: 10mM Tris HCl pH 8.0, 1mM EDTA, 0.1% Tween 20
- STOP25: 10mM Tris HCl pH 8.0, 25mM EDTA, 0.1% Tween 20, 100mM KCl
- STOP10: 10mM Tris HCl pH 8.0, 10mM EDTA, 0.1% Tween 20, 100mM KCl
- DENATURE: 0.5% Brij35, 150mM NaOH (must be made fresh and with non-expired NaOH)
- NEUTRALIZE: 100mM Tris HCl pH 8.0, 10mM EDTA, 0.1% Tween 20, 100mM NaCl
- HYBRIDIZE: 10mM Tris HCl pH 8.0, 0.1mM EDTA, 0.1% Tween-20, 330mM KCl
- PROBE: 5mM Tris HCl pH 8.0, 5mM EDTA, 0.05% Tween, 1M KCl

#### Synthesis of hydrogel beads
- Microfluidic generation of beads:
	- Prepare 3mL of HFE7500, 1% surfactant, 12uL of TEMED. Place in 3mL syringe and prime (25 gauge needle, standard tubing) on syringe pump.
	- Prepare 300uL of an acrylamide master mix:
		- 162uL nuclease free water
		- 30uL TBSET buffer
		- 75uL Acry/Bis stock 4X
		- 24uL acry-pc-pe1 primer (250uM stock; 20uM final)
		- 9uL 10% APS (wt/vol)
	- Vortex, microfuge and place in 1mL tube pre-filled with 300uL HFE7500 and prime as above, with syringe tip facing up due to HFE7500 priming. Protect tubing from light with black sheath.
	- Connect tubing to droplet formation device and flow at 5uL for acrylamide master mix and 50uL for carrier. Allow flow to stabilize and watch on microscope with red filter.
	- Once flow is stabilized (~1 minute) collect droplets with tubing in 2mL tube pre-filled with 300uL mineral oil. Ensure that droplets are 20um in diameter, which is desired for 25um input channel width in the encapsulation chip.
	- Replace with new tube after 30 minutes.
	- When finished (i.e. either acrylamide or carrier runs out) remove output tube and drain, and stop flow.
	- Clean chip quickly with water to prevent in-chip polymerization which could clog the chip.
	- Place two tubes in 65C incubator overnight, protected from light.
- Cleanup of beads:
	- The next day, ensure that beads are polymerized by pipetting on microscope field.
	- Remove mineral oil and carrier oil phases from the tubes, and pool both tubes. Add 500uL TBSET on top.
	- Add 1mL of 20% PFO in HFE7500, vortex, and centrifuge at 5000g for 30s. Remove bottom 20% part of PFO phase and centrifuge again.
	- Remove The bottom 20% of PFO phase and add 1mL of 1% Span-80 in hexane. Vortex and centrifuge at 5000g for 30s, and remove hexane layer.
	- Repeat hexane wash again.
	- Add 1mL TBSET and vortex. Centrifuge at 10,000g for 1m, and remove hexane layer by keeping tip at air-water interface to remove trace hexane.
	- Repeat TBSET wash three times.
	- Pass beads through 40um cell strainer using TBSET to pass through beads.
	- Recover beads and save in amber tube at 4C for up to 6 months. Measure diameter which should be 25-30um (due to swelling) and ensure uniformity.

#### Barcoding of hydrogel beads via primer extension (rounds 1-3)
- Barcoding reaction
	- Add 1mL WB to approximately 20,000,000 beads, vortex, and spin down at 10,000g for 1 min. Repeat wash for a total of three times.
	- Remove supernatant, and adjust volume to exactly 730uL with WB.
	- Add 140uL of isothermal amplification buffer (10X) for final 1.5X, 60uL 10mM dNTPs for final 0.645uM (final volume: 930uL)
	- Pipette 115uL into first column of 8 wells of a 96 V-well plate (Costar 3894). Protect from light.
	- Thaw primer plate for the round (pe1, pe2 or pe3). Centrifuge for 1 min to collect condensate.
	- Place on incubator at 70C for 2min and place in block at 4C (or ice for V-well plate) with lid 105C for 20s. Pull of seal and discard.
	- Place primer plate, bead plate (tap down to ensure mix is at bottom) and destination plate (96 well Eppendorf Twin-tec) on Beckman liquid handler with 2X P50 barrier tips. For bead tips, specify to the liquid handler the remaining tips.
	- Using liquid handler, mix the beads and distribute 9.3uL to the destination plate. Then distribute 4.8uL of primer to each well.
	- Re-seal primer plate with new seal and mark use on side of plate. Seal destination plate and spin down plate.
	- Incubate in PCR machine: 85C 2min, 60C 120min. Start timer for 22min.
	- Prepare reaction mix: 595uL water, 70uL 10X isothermal amplification buffer, 35uL Bst 2.0 Polymerase. Place 80uL in each well of the second column of the 96 V-well plate from before.
	- After 20 min of incubation, take plate out and remove seals via the 70C/4C step described previously.
	- Place reaction mix plate (tap down to ensure mix is at bottom), destination plate, P50 barrier tips on liquid handler. Transfer 5.4uL of the reaction mix to each well.
	- Seal destination plate and spin down plate.
	- Incubate back on PCR machine for 60m. Cool plates on ice and remove seal.
	- Remove from PCR machine, and place destination plate, 10mL STOP25 buffer in 20mL reservoir, and P50 barrier tips on liquid handler. Add 15uL STOP25, mix and place in recovery reservoir for each well. Wash each well with 20uL of STOP25 and place in recovery reservoir.
	- Discard 2 left columns of tips which are dirty.
	- Recover beads from recovery reservoir in 15mL tube with serological pipette. Wash recovery reservoir with more STOP25 and place in 15mL tube.
	- Incubate at RT for at least 30min.
- Postbarcoding washes
	- Centrifuge 15mL tube down (5000g, 5min) and transfer beads to 1.5mL tube
	- Wash beads 3 times with 1mL STOP10 buffer (vortex, incubate 1m, 10,000g 1min)
	- Incubate beads with DENATURE for 10m at room temperature
	- Wash beads 3 times with **fresh** DENATURE (vortex, incubate 1m, 10,000g 1min)
	- Wash beads 2 times with NEUTRALIZE buffer (vortex, incubate 1m, 10,000g 1min)
	- Either wash 3 times in TET buffer if storing overnight, or proceed back to barcoding reaction with 3 washes in WB for next extension rounds

#### Enzymatic cleanup of barcoded hydrogel beads
- Wash beads in WB 3 times (if not already done) as above. Save small aliquot as "before ExoI treatment" for QC
- Wash beads in HYBRIDIZE three times and remove supernatant (300uL final volume)
- Add 30uL of 250uM 16S_505f_RC primer (~20uM final concentration) and mix well
- Incubate at 85C for 2 min and 60C for 30 min.
- Mix 330uL of bead mix with 100uL 10X ExoI buffer (1X final), 555uL nuclease-free water, 15uL ExoI (0.3U/uL) in 2mL tube.
- Incubate at 37C for 1h
- Fill tube with STOP25 and invert
- Perform STOP10, DENATURE, NEUTRALIZE washes as above.
- After NEUTRALIZE washes, filter beads through 40um filter above.
- Wash recovered beads three times in TET as above.
- Pass through 40um cell strainer using TET to pass through beads.
- Spin down filtered beads, resuspend TET, and save in amber tube at 4C.

### Microfluidic device fabrication
#### Casting of devices
Water is ordered from FlowJEM and is ready to cast.
- Weigh 10:1 (50g/5g) of Sylgard 184.
- Mix for 5 minutes in sterile pipette box with P1000 tip
- Degas for 30 minutes under house vacuum
- Take large weighing boat and carefully place wafer on it.
- Pour PDMS solution on wafer, and degas again for 5-10 min or until bubbles are gone.
- Place in 80C oven for 1 hour.
- Allow to cool to room temperature.
- Carefully remove wafer and store in petri dish.
- Cut out PDMS strips, and cut holes with 1mm punch from feature side down.
- Clean off feature side with scotch tape, and clean the surface of a precleaned glass slide.
- Plasma treat PDMS device and slide
	- Turn on device
	- Turn on vacuum for 1 min with port closed
	- Switch port to low gas input for 1 minute
	- Turn on "HIGH" for 40 seconds. Strong plasma glow should be seen.
- Remove device and quickly place feature side down on precleaned glass slide.
- Place in 80C oven for 30min.

#### Aquapel treatment of microfluidic chips
Chips need to be treated when first constructed. This is best performed in parallel. Note that this protocol is adopted from Mazutis, Nat. Protocols 2013.
- Cut pad that aquapel solution is embedded within. Place ampule in 15mL conical and break the ampule within the tube.  
- Pipette solution in 1mL syringe.
- Inject solution into microfludic device. Leave solution in channels for 30s, and flush with air (pressurized air) at all three fluidic ports.
- Flush device with FC-40, and flush with air (pressurized air) at all three fluidic ports.
- Bake chip at 80C for 10 minutes.

### Fixation
Samples are fixed in methacarn to avoid damage to mucosal structures and nucleic acids that may result with other fixatives such as formaldehyde.
- Acquire sample (feces, GI tract etc.) and immediately place in methacarn solution (60% methanol, 30% chloroform, 10% acetic acid).
- Note: at this time, it will likely be of interest to save samples for 16S sequencing or clonal isolation.
	- For 16S sequencing, place sample in eppendorf tube, and save at -80C until gDNA prep
	- For clonal isolation, place sample immediately into pre-reduced (at least overnight) PBS with 0.1% cysteine (PBSc). Cycle into anaerobic chamber, and vortex until sample is homogenized (sterile glass bead can be added to enhance homogenization). Allow sample to rest for 5 minutes for particulate matter to settle, combine 500uL of supernatant with 500uL of 40% glycerol, mix and aliquot 500uL into two cryotubes. Freeze in anaerobic chamber on dry ice, and transfer to -80C for storage.
- Fix the sample at room temperature for between 24 to 48 hours.
- Replace the sample in 70% ethanol after this period for storage up to 1 month (longer periods may be possible, but have not been investigated)

### Embedding
The sample is then embedded with an degradable acrylamide matrix which preserves spatial structure and contains a reverse 16S amplification primer. Note that for inclusion of reverse primer, we target a concentration of approximately 100nM per droplet; accounting for droplet volume of 0.5nL this means that 5*10<sup>-5</sup>pmol must be loaded per particle. Assuming a median particle diameter of 20um, and assuming a spherical shape, this yields a particle volume of 4.2pL, meaning that the concentration of reverse primer should be approximately 10uM.

##### Preparation of  stock solutions
- Monomer 2X concentrate (store -20C indefinitely).

| name | amt to add | final conc in gel (w/w) |
|:----:|:----------:|:---------------:|
|Acrylamide|1g|10%|
|N,N′-Bis(acryloyl)cystamine|0.04g|0.4%|
|10X PBS filter sterilized|1.0mL|1x|
|nuclease-free water|3.0mL|n/a|

- Other stock solutions (store -20C, remake once every 2 weeks)
	- APS (10% w/w; 0.1g/1mL ddH20), final  0.2%
	- TEMED  (10% v/v stock, 0.1mL+0.9mL ddH20), final 0.2%
	- 4HT  (0.5% w/w stock, 0.005g/1mL ddH20), final 0.01%

##### Embedding of sample
```diff
- IMPORTANT: ensure that the photocleavable primer is protected from light
- IMPORTANT: once polymerized, the gel is sensitive to reducing conditions.
- Store at -20C and protect from any reagents that may contain reducing agents.
```
- Remove sample from fixative, and wash in PBS, and let sit for 5 min.
- Remove PBS, and incubate sample in permeabilization buffer (1x PBS, 0.1% Triton-X 100) for 5 min.  
- Cut sample into sub-parts no larger than 3x3mm with a sterile razor. A smaller size allows for more efficient perfusion of monomer components.
- Prepare an embedding stock solution in the following order on ice, with mixing between each step. Make sure to keep all reagents on ice.
	- 4uL reverse primer (250uM stock), 5uM final
	- 100uL monomer concentrate
	- 84uL water
	- 4uL 4HT
	- 4uL TEMED
	- 4uL APS
- Place the particle in an 1.5mL tube on ice. Place enough solution to fully embed the particle and allow to sit on ice for 5 minutes. Remove excess solution and replace; this increases concentration of embedding solution to replace any PBS from the sample. Allow to embed for 1 hour to overnight allow for full perfusion; cover the tube with foil to prevent premature cleavage of the reverse primer.
	- NB: Like any initiator, TEMED/APS may degrade over time. An alternative is VA-044, a thermally activated initiator which can be used to initiate polymerization in the same manner. This can be used, at a final concentration of 0.5% w/w in the embedding solution and 4HT, TEMED and APS can be omitted and replaced with water.
- Remove any excess liquid by pipetting out, but ensure that the sample is still fully submerged under liquid.
- Open the tube top, cycle into the anaerobic incubator (O2 impedes polymerization reaction) and allow to polymerize at 37C for 2-3 hours; cover the tube with foil to prevent premature cleavage of the reverse primer or photobleaching of the fluorophore.
- Extract the embedded sample from the tube, and trim excess polymer matrix with a sterile razor.
- Ensure that sample is fully polymerized throughout. Wash 2 times in PBS and 1 times in TET (10mM Tris HCl pH 8.0, 1mM EDTA, 0.1% Tween-20) and store in TET at 4C for short term storage (no more than 5 days) or -20C for long term storage.

### Fracturing
The embedded sample is then broken into small particles using cryofracturing.
- Place sample in stainless steel microvial (Biospec 2007). Freeze sample on LN2 ~1 min (without submerging vial) and shake vial to ensure that particle can move freely and is not adhered to wall.
- Add a single 6.35mm stainless steel bead on top (Biospec 11079635ss). Seal the tube with a silicone rubber plug cap (Biospec 2008).
- Place vial back in liquid nitrogen for at least 2 minutes.
- Quickly transfer to a bead beater (Biospec 112011) and beat for 10s. Note that beating time dictates the size distribution of particles; depending on desired particle size beating time can be adjusted to increase yield in a desired range.
- Resuspend particles in PBS, vortex, and transfer to a sterile tube. Wash 2 times in PBS. Note that during wash steps, particles should be centrifuged at greater than 10,000RPM for 10s to ensure full sedimentation. Metal residue may color the particles a grey color, but this will not affect downstream steps.

### Lysis of cells within embedded particles
Particles are then treated with lysozyme and proteinase K to lyse any remaining cells.

##### Lysozyme treatment
- Resuspend particles in 500uL lysis buffer (Tris pH 8 10mM, EDTA 1mM, NaCl 100mM)
- Add 1uL lysozyme (37.5KU/uL stock) to sample (final concentration 75U/uL)
- Incubate at 37C for 1 hour with shaking; ensure cap stopper is added.

##### Proteinase K treatment
- Resuspend particles in 500uL digestion buffer (30mM Tris HCl pH 8.0, EDTA 1mM, 0.5% Triton X-100, 800mM guanidine HCl).
- Add 1uL of proteinase K (50ug/uL stock) (final concentration 0.1ug/uL).
- Incubate at 65C for 15 min with shaking; ensure that cap stopper is added.
- Incubate at 95C for 5 min to inactivate proteinase K; ensure that cap stopper is added.
- Wash particles in 500uL TET buffer 3x times and store at 4C for short term storage (5 days maximum), or -20C for long term storage.

### Size selection
Nylon mesh filters are utilized to size-select fractured acrylamide particles. The protocol is modular to meshes of different sizes.

##### Preparation of nylon mesh filters
- Sterilize a 1/2" hole punch (Amazon) and workspace.
- Take nylon mesh filters of size 7um, 15um (Component Supply Company) and punch. Prepare multiple dots for multiple experiments in advance.
- Place in a plastic bag for long-term storage

##### Size selection of acrylamide particles
- First filter sample through a 40um cell culture filter (Falcon), and save flow-through, to remove large particles.
- Clean and sterilize Swinnex 13mm filter holders, gasket O-rings, punched nylon mesh filters via UV sterilization.
- Place each filters in a Swinnex filter holder with gasket O-ring.
- Start with the 15um filter. Place 2 filters in assembly.
	- Take sample and resuspend in 1mL of nuclease free water. Connect a 3mL syringe to the filter. Pipette the 1mL into the filter, and carefully push liquid through the filter applying minimal pressure to the syringe. Collect sample in a sterile 1.5mL tube and repeat this filtering step twice for a total of three times. Set flow-through aside; this fraction contains particles smaller than 15um.
	- Aspirate 1mL of TET, flow back and forth through the filter assembly. Pull liquid in the syringe and set aside; this contains particles greater than 15um.
- Switch filters to the 7um filter. Place 2 filters in assembly.
	- Connect a 3mL syringe to the filter. Pipette the 1mL <15um sample into the filter, and carefully push liquid through the filter applying minimal pressure to the syringe. Collect sample in a sterile 1.5mL tube and repeat this filtering step twice for a total of three times. Save flow-through; this  contains particles smaller than 7um.
	- Aspirate 1mL of nuclease-free water. In the syringe, flow back and forth through the filter assembly and discard. Repeat this wash for a total of three times.
	- Aspirate 1mL of TET; flow back and forth through the filter assembly. Pull remaining liquid in the syringe and set aside; this fraction contains particles 7-15um
- Quantify numbers and store in amber tube for short term storage at 4C (5 days maximum) or long term storage at -20C.

### Encapsulation
##### Equipment preparation
- An in-syringe magnetic mixer was constructed with 400 RPM mini DC geared gear box electric motor (uxcell, Amazon) driven by a Unique Goods Digital Display DC Motor Speed Controller (Amazon) and a 6V 1A power adapter (Amazon). The motor rotates a small neodynium magnet (K&J magnetics B448) via a custom 3D printed adapter. This spins a 3x3mm magnetic stirbar (Bel-Art Z283835) which fits within a 1mL syringe.
- We utilize three Harvard Apparatus Pump 11 Elite syringe pumps and a Zeiss Axiovert 25 inverted microscope to observe droplet formation and flow.

##### Encapsulation protocol
###### General preparation
```diff
- IMPORTANT: Particles and barcoded hydrogel beads are light sensitive.
- Minimize exposure to light, and ensure that red filter is used on microscope.
```
- UV sterilize encapsulation supplies for 30 minutes: microfluidic chip, magnetic stir-bars
- Prepare a low dead volume syringe with 300uL of 5%EA surfactant in HFE7500.
- Flow water through all channels of encapsulation chip to ensure proper flow and no debris.

###### Preparation of beads
- Centrifuge down bead stock and remove 30uL of packed beads from bottom of tube
- Wash beads twice with WB
- Wash beads twice with Bead Buffer (10mM Tris HCl pH 8.0, 0.1% Tween 20, 50mM KCl, 10mM DTT)
- Repeat centrifugation and remove last remains of supernatant with fine-tip gel tip.
- Using empty 1mL syringe connected to tubing, aspirate approximately 5uL of packed beads (approximately the length of a razor blade) and then approximately 10cm of air.
- Remaining beads can be washed twice in TET and returned to stock tube.
- Cut tubing right where beads start. Backfill a syringe with 500uL HFE7500, remove bubbles and prime with 25 gauge needle.
- Connect syringe to tubing, prime syringe such that beads are near the entry port, and cover tubing with black covering.
- Mount syringe vertically with needle facing upwards.

###### Preparation of cell-clusters
- Vortex cell-clusters for 1 min and sonicate for 1 min to ensure avoidance of any aggregates.
- Quantify cell-clusters via hemacytometer, immediately before encapsulation.
- Remove approximately 12,500 cell-clusters and wash three times in WB (~250 clusters/uL). NOTE: centrifugation steps must be done for at least 1 minute to ensure full sedimentation of cell-clusters.
- Centrifuge down cell-clusters and remove all supernatant. Repeat centrifugation and remove last remains of supernatant with fine-tip gel tip. NOTE: centrifugation steps must be done for at least 1 minute to ensure full sedimentation of cell-clusters.
- Prepare encapsulation master mix (45uL), and resuspend cell-clusters in the master mix:
	- 25uL NEB Next Q5 2x Master Mix
	- 8uL NycoPrep (60% w/v Nycodenz)
	- 5uL 10%w/v Pluronic 127
	- 1.25uL BSA (20mg/mL, NEB)
	- 5.75uL nuclease free water
- Vortex for 10s, and sonicate in water bath for 30s.
- Backfill a syringe with 500uL HFE7500, add cell cluster solution, and prime with 25 gauge needle.
- Connect syringe to tubing, prime syringe such that cell-clusters are near the entry port, and cover tubing with black covering.
- Mount syringe vertically with needle facing upwards.

###### Encapsulation
- Prime bead syringe by priming with pump and then cutting tubing where beads are at.
- Attach oil and cell-cluster mix pumps, prime via syringe, and prime into device to displace any water.
- Attach bead syringe to device
- Prime beads, flowing at 1uL/min, encapsulation mix at 0.3uL/min and oil at 0.3uL/min
- Close pack beads, flowing beads at 0.3uL/min, encapsulation mix at 0.3uL/min and oil at 2uL/min until close packing is observed.
- Start encapsulation by adjusting encapsulation mix to 2.7uL/min.
- Once proper and stable droplet formation (faint flickers at droplet junction) is observed, with bead deposition in ~90% of droplets, add capture tubing and collect droplets into a Axygen Maxymum recovery tube filled with 50uL mineral oil and 10uL of 30% EA surfactant.
- Once reagents are finished, remove capture tubing and drain into capture tube. Then turn of syringes. Extra beads may be washed with TET twice and returned to stock vial.
- Wash microfluidic chip with water.

### PCR amplification and library prep
##### First round PCR amplification
```diff
- IMPORTANT: Emulsion compatible plastics must be utilized:
- Rainin low retention/wide orifice tips MUST be used when handling emulsion;
```
- Remove oil underneath droplets and add 30uL of 30%EA in HFE7500 to a Axygen Maximum Recovery PCR tube
- Place tubes under UV light with top open on ice and treat for 10 min

```diff
- IMPORTANT: A 96 deep well cycler must be utilized for the emulsion PCR amplification.
- Ensure that proper volume is set corresponding to actual emulsion volume.
```

- Run with the following PCR program with heated lid off and 100uL volume.
	- 1 10 2h
	- 2 98 30s
	- 3 98 10s
	- 4 55 20s
	- 5 65 30s
	- 6 step 3, 29x
	- 7 65 2m
	- 8 10 infinity

##### First round clean up
- Ensure that droplets are intact after cycling. It is recommended to remove 1uL of droplets from 1 tube per sample type and observe co-encapsulation statistics.
- Remove as much of EA/oil underneath tube and mineral oil above tube.
- Add 20uL of PFO in HFE75000 to the droplet phase. Vortex for 5s, and centrifuge down on a microfuge.
- Extract as much of the aqueous phase as possible (40uL should be achievable) and pass through spin column (Costar 0.45um) in Lo Bind tube. Save spin column.
- Make ExoI master mix: 5uL 10X ExoI buffer, 2.5uL ExoI, 42.5uL water. Pass through the spin column.
- Incubate at 37C for 30min.
- Perform a 1X AmpureXP clean up by adding 90uL of AmpureXP, and follow regular protocol with 80% EtOH washes. Resuspend in 22uL of 10mM Tris-HCl pH 8.0, and save 20uL.

##### Indexing PCR
- Setup up following reaction: 10uL first round PCR product, 2.5uL forward index primer (10uM), 2.5uL reverse index primer (10um), 10uL water, 25uL NEB Next Q5 2x Master Mix and SYBR green (0.1x final concentration).
- Run with the following PCR program on qPCR cycler. Stop early if it appears samples stop exponential amplification. Ensure to run water only control to ensure that samples with non-specific amplification can be readily identified on a gel.

```diff
- IMPORTANT: for all indexes, there must be a G/T and A/C base at EACH position.
- In practice, generally the i7 barcode will be diverse
- For the i5 barcode, Nextera indices are used, so follow Nextera low-plex pooling guidelines.
```

- Run with the following PCR program:
	- 1 98 30s
	- 2 98 10s
	- 3 68 20s
	- 4 65 30s
	- 5 step 2, 29x
	- 6 65 120s
	- 7 10 infinity

##### Library QC, pooling and prep
- Assess all products on a 2% agarose E-gel to confirm library product at 489-491bp.
- Gel extract the product on a 1.5% LMP agarose gel using the Promega Wizard SV Gel and PCR Cleanup kit.
- Quantify concentration using the Qubit HS DNA kit (2uL sample).
- Sequence using a MiSeq v2 500 cycle kit, loading at 12pM (based on Qubit quant) with a 10% 12pM PhiX spike in.

### MIST-seq quality control
##### Construction of synthetic community particles
To test the ability of MIST-seq to provide data on single particles, we generated synthetic bacterial communities, and co-encapsulated these communities.
- Prepare cells for two synthetic communities:
	- One synthetic community is E. coli BL21, grown overnight; normalize to size of pellet fecal cells visually (see below)
	- Second synthetic community is homogenized fecal pellets. Vortex two pellets in PBS with 3mm glass beads for 2 min to homogenize, and pass through 40um filter (Falcon). Vortex again with 0.1mm beads for 2min, microfuge down for 5s and pass through another 40um filter. Save the pass-through and pellet.
- Samples are processed as above with minor modification. Fix for 1 hr in methacarn with shaking to prevent aggregation of cell clumps. Spin down (ensuring no liquid remains) and embed pellet as above in 50uL of gel solution (by resuspending pellet within gel solution). Polymerize at 37C with shaking to ensure cells are in suspension. Fracture and prep as above.

### Barcoded Bead Quality Control
##### Quantification of extension efficiency via FISH
To assess the efficiency of primer extension, as well ExoI cleanup, we utilize fluorescence in situ hybridization with Cy5 labeled probes targeted to the Illumina adapter (i.e. unextended ssDNA product) and the 505f primer (fully extended ssDNA product). The ratio of intensity observed with the 505f probe to the Illumina probe reflects the extension efficiency of the construction protocol.
- Perform all steps for beads before ExoI cleanup and after ExoI cleanup, as well as for PE1 and 505f probe (4 total)
- Resuspend 1uL packed beads in 18.2uL PROBE buffer. Add 0.8uL of 250uM probe (either PE1 or 505f) such that the final concentration is 10uM.
- Allow to hybridize at RT on a rotisserie for 30 min.
- Wash beads 3 times with 500uL of PROBE buffer. Resuspend in 20uL PROBE and place on slide with coverslip.
- Record average intensity per bead using an epifluorescence microscope.

##### Validation of photorelease of primers from bead and particles - Bioanalzyer
To assess UV exposure-dependent release of primers from barcoded beads and particles, we utilize the Agilent Bioanlyzer HS DNA assay kit to detect low concentrations of ssDNA product.
- Resuspend ~5,000 beads in 10uL nuclease-free water. Make two aliquots.
- Expose one aliquot to UV light (BlackRay Xenon 365nm UV) for 15 minutes on ice. Place the other aliquot on ice and protect from ambient light.
- Spin down aliquots and remove ~5uL of supernatant.
- Load 1uL of supernatant and follow manufacturer instructions for the Agilent Bioanylyzer HS DNA kit.

##### Sequencing of individual bead primers and total pool primers
To assess the composition of primers on a single bead as well as the composition of the entire pool of beads, we utilize deep sequencing of the ssDNA primers. The experiment is performed on 12 individual beads as well as a pool of ~10,000 beads.
- Perform PE1 probe staining as above. Pick individual beads on microscope field and add to PCR tube with 5uL 10mM Tris HCl pH 8.0, for 15 beads. Resuspend the remaining 10,000 beads in a PCR tube with 5uL 10mM Tris HCl pH 8.0
- Expose tubes to UV light for 15 minutes on ice.
- Add 1.1uL mix containing 0.25uL 10uM pe2-umi-505f primer, 0.6uL 10X isothermal amplification buffer, 0.25uL 10mM dNTPs to each well.
- Incubate tubes at 85C for 2 min and 60C for 5 min
- Add 3.9uL mix containing 0.4uL 10X isothermal amplification buffer, 0.25uL Bst2.0 and 3.25uL water to each well.
- Incubate tubes at 60C for 15 min and 95C for 5 min and 10C infinite.
- Add PCR mix containing 12.5uL NEB Next Q5 HiFi Hot Start Master Mix, 1uL 10uM forward primer (p5), 1uL 10uM reverse primer (p7, unique barcode for each well), 0.25uL 10X SYBR Green I, 0.25uL nuclease-free water.
- Perform qPCR amplification with the following PCR protocol. Remove tubes from amplification before they pass exponential amplification:
	- 1 98 30s
	- 2 98 10s
	- 3 68 20s
	- 4 65 30s
	- 5 step 2, 29x
	- 6 65 120s
	- 7 10 infinity
- QC products via gel, pool based on Qubit HS DNA, and gel extract the 214-216bp product. Sequence on MiSeq 150v3 R1:94 R2:73 i1:8

## 16S FISH studies
To confirm findings from the MIST-seq technique, we also perform 16S FISH protocols. We base our FISH protocol largely on commonly used FISH protocols, and previously validated probes. 3 probes are chosen with different fluorophores. They target a particular percentage of all known species within particular families listed below:

`alexa488_erec482 /5Alex488N/GCTTCTTAGTCAGGTACCG`
Lachnospiraceae 76%

`cy5_bac303 /5Cy5/CCAATGTGGGGGACCTT`
Bacteroidaceae 96%, Porphyromonadaceae 20%, Prevotellae 78%

`cy3_lab158 /5Cy3/GGTATTAGCAYCTGTTTCCA`
Enterococcaceae 96%, Lactobacillaceae 94%, Leuconostocaceae 60

Family targeting from: http://www.pnas.org/content/suppl/2013/02/28/1219247110.DCSupplemental/pnas.201219247SI.pdf

### FISH protocol
- Deparaffinize samples by placing in xylene for 10m
- Rehydrate through an ethanol gradient (95% Et0H 10m, 90% EtOH 10min; wash under running DI water)
    - Do not let dry out during this processs
- Incubate with 3x FISH probes diluted to 10ng/uL in hybridization buffer (0.9M NaCl, 20mM Tris-HCl pH 7.5, 0.01% SDS, 10% formadide) at 47C for 3-18hr in closed humid environment.
    - resuspend probes to 500ng/uL in 10mM Tris pH7.5
    - ~5uL needed per reaction, for 50uL master mix:
        - 1uL 1M TrisHCl 7.5
        - 9uL 5M NaCl
        - 5uL formadide
        - 0.1uL 10% SDS
        - 32uL water
        - 1uL each probe
	  - Add 5uL of probe mix, cover with coverslip and put in 50mL conical with cotton ball.
- Make wash buffer (0.9M NaCl, 20mM TrisHCl pH7.5) and prewarm at 47C. Wash off hybridization with pipette/wash buffer and incubate with wash buffer  at 47C for 10m
- Wash 3x in PBS
- Incubate with 10ug/mL DAPI (1:100 stock) in PBS for 5min at 4C
- Wash 3x in PBS
- Dry
- Mount with vectashield (~20uL)

### Imaging
Image at the cancer center confocal. In general here are settings: pixel size 2.4, size 1024, 2x average, pinhole 1AU. Laser 2% for 405, everything 5%. Hv gain around 100. Setting gain above 130 will generally not be a great idea. In general Z-stacks and XY we want to sample at 2-3x resolution (i.e. nyquist sampling). For scanning use 512 pixel size (reasonable). Can likely couple FR and green during scanning.

Most images we get are 1024x1024 with 3x Z-stacks separated by 0.5um (so 1uM Z axis total).
