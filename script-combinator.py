### MODULES
import os
import random
import string



### CONSTANTS
QUARTERS = ["0", "1", "2", "3"]



### VARIABLES

# Number of starting combination
cmb_str = 10

# Number of combinations to generate
cmb_num = 10

# Glyph left and right margin
gly_mrg = 50



### SYSTEM VARIABLES
separator = "|"



### INSTRUCTIONS
fnt = CurrentFont()



"""
Listing and sorting all the quarters (-> qrt_data)
-
Data structure

d = {'0': ['0A',
           '0B',
           '0C',
           ...
          ],
     '1': ['1A',
           '1B',
           ...
          ],
     ...
    } 
"""
qrt_data = {}
for Q in QUARTERS:
    qrt_data[Q] = []
    for gly in fnt:
        if Q in gly.name:
            qrt_data[Q].append(gly.name)
    qrt_data[Q].sort()



"""
Calculating combinations (-> cmb_data)
-
Combinations will be expressed as concatenation of glyph names:
0A|1B|2A|3D
-
Data structure

d = [
     0A|1B|2A|3D,
     0A|1A|2C|3A,
     ...
    ]
"""
cmb_data = []

# Creating temporary lists that will store combinations
# First iteration, we have one quarter with all its variations
# Second iteration, for each initial quarter we have all its combinations with the variations of the second quarter
t0 = qrt_data["0"]
t1 = []

# Iterating over the other lists of quarters
for Q in QUARTERS[1:]:
    # Iterating over each quarter variation
    for qrt_var in qrt_data[Q]:
        # Each quarter variation has to combine with each element in t0  
        for item in t0:
            t1.append(item + separator + qrt_var)
    # Updating lists
    t0 = t1
    t1 = []

# "Uploading" combinations
t0.sort()
cmb_data = t0



"""
Generating combinations
"""
assert cmb_num<len(cmb_data), "The number of available combinations is %d. You choose too many to generate!" % len(cmb_data)

# "Iterating over a list of %d randomly selected combinations" % cmb_num
for cmb in cmb_data[cmb_str:cmb_str+cmb_num]:

    # Getting quarters/glyphs names
    qrt_lst = cmb.split(separator)
    
    # Creating new glyph
    #cmb_name = "G-" + "".join(qrt_lst)
    cmb_name = "cmb" + str(cmb_data.index(cmb)).zfill(len(str(len(cmb_data))))
    cmb_gly = fnt.newGlyph(cmb_name, clear=True)
    
    # Getting glyph pen
    pen = cmb_gly.getPen()
    
    # Iterating over quarters
    for qrt in qrt_lst:
        # Iterating over each contour of each quarter
        for cnt in fnt[qrt]:
            # Drawing all the contours in the main glyph
            cnt.draw(pen)
    
    # Fixing the glyph
    cmb_gly.width = abs(cmb_gly.box[0]-cmb_gly.box[2])
    cmb_gly.leftMargin = gly_mrg
    cmb_gly.rightMargin = gly_mrg