import os
import yaml

pwd = os.path.dirname(os.path.abspath(__file__))

_config = "FLT3_ITD_ext.yml"
_vcfheader = "vcf_header.txt"

header_file = os.path.join(pwd, _vcfheader)
config_file = os.path.join(pwd, _config)

with open(header_file) as f:
    lines = f.readlines()

with open(config_file, encoding='UTF-8') as f:
    _cfg = yaml.load(f, Loader=yaml.FullLoader)

vcfheader = "".join(lines)