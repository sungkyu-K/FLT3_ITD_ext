import os

pwd = os.path.dirname(os.path.abspath(__file__))

_index_fasta_name = "FLT3_dna_e14e15"
_fasta_name = "{}.fa".format(_index_fasta_name)

refindex = os.path.join(pwd, _index_fasta_name)
reffasta = os.path.join(pwd, _fasta_name)
refstart = 28607438
refend = 28608937
with open(reffasta) as f:
    refseq = "".join([i.strip() for i in f if not i.startswith(">")])