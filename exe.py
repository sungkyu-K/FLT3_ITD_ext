import os
import sys
import yaml
import argparse
from reference import *

__version__ = '1.1.1'

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="FLT3_ITD_ext caller")
    parser.add_argument('-b', '--bam', type=str, help='Input bamfile (either this or fastq1+2 required)')
    parser.add_argument('-t', '--typeb', type=str, default="targeted", choices=["targeted", "loose", "all"],
        help='Reads to extract from input bam (defaults to "targeted" [FLT3-aligned]; or can be "loose" or "all")')
    parser.add_argument('-f1', '--fastq1', type=str, help='Input fastq1 (either fastq1+2 or bam required)')
    parser.add_argument('-f2', '--fastq2', type=str, help='Input fastq1 (either fastq1+2 or bam required)')
    parser.add_argument('-o', '--output', type=str, required=True, help='Output path (required)')
    parser.add_argument('-n', '--ngstype', type=str, default="HC", choices=["HC", "amplicon", "NEB", "Archer"], help='NGS platform type (defaults to "HC" [hybrid capture]; or can be "amplicon", "NEB", or "Archer")')
    parser.add_argument('-a', '--adapter', help='Trim adapters (defaults to true; assumes illumina)')
    parser.add_argument('-w', '--web', help='Create html webpages for each ITD call (defaults to false)')
    parser.add_argument('-u', '--umitag', help='BAM tag holding UMIs in the input bamfile for fgbio (defaults to ""; standard is "RX")')
    parser.add_argument('-s', '--strat', help='Strategy for UMI assignment used in fgbio GroupReadsByUmi (defaults to "adjacency" )')
    parser.add_argument('-p', '--probes', type=str, default="", help='Probes/baits file basename (defaults to ""); assumes fasta file, bwa indexfiles')
    parser.add_argument('-mr', '--minreads', type=int, default=0, help='Minimum number of supporting reads to be included in VCF (umi-based if umitag set)')
    parser.add_argument('-d', '--debug', action='store_true', help='Save all intermediate files (defaults to false)')
    parser.add_argument('-v', '--version', action='store_true', help='Print version')

    args = parser.parse_args()

    if args.version:
        print(__version__)
        sys.exit()

    if args.bam is None:
        if not all([args.fastq1, args.fastq2]):
            sys.exit(help_message = parser.parse_args(['-h']))

    print(reference_fasta)
