import re
import os

def set_outname(*args, **kwargs):
    outname = args[0].split("/")[-1]
    if kwargs["type"].upper() == "BAM":
        outname = re.sub(r".bam$", "", outname)
    else:
        outname = re.sub(r".gz$", "", outname)
        outname = re.sub(r".fastq$", "", outname)
        outname = re.sub(r".R1$", "", outname)
        outname = re.sub(r"_R1$", "", outname)
    outname = "{}_FLT3".format(outname)
    return outname