# Mohamed BEN ALI
#####################
#!/usr/bin/env python
# -*- coding: utf-8 -*-

# import dependencies
import sys
from lang_trans.arabic import buckwalter
 
with open(sys.argv[1], 'r') as f:       # input your text file 
    contents = f.readlines()
    for content in contents:
        buck_format = buckwalter.untransliterate(content)    # untransliterate ligne by ligne
        output_res = open(sys.argv[2], "a")       # output result file
        output_res.writelines(buck_format)
    output_res.close()



