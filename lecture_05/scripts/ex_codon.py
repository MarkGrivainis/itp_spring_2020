import pprint
gen_code = {'uuu': 'Phe', 'uuc': 'Phe', 'uua': 'Leu', 'uug': 'Leu',
          'ucu': 'Ser', 'ucc': 'Ser', 'uca': 'Ser', 'ucg': 'Ser',
          'uau': 'Tyr', 'uac': 'Tyr', 'uaa': 'Stop', 'uag': 'Stop',
          'ugu': 'Cys', 'ugc': 'Cys', 'uga': 'Stop', 'ugg': 'Trp',
          'cuu': 'Leu', 'cuc': 'Leu', 'cua': 'Leu', 'cug': 'Leu',
          'ccu': 'Pro', 'ccc': 'Pro', 'cca': 'Pro', 'ccg': 'Pro',
          'cau': 'His', 'cac': 'His', 'caa': 'Gln', 'cag': 'Gln',
          'cgu': 'Arg', 'cgc': 'Arg', 'cga': 'Arg', 'cgg': 'Arg'}


# pprint.pprint(gen_code)

## solution 1
# aa_codon_map = {}
# for key, value in gen_code.items():
#     if value in aa_codon_map:
#         aa_codon_map[value].append(key)
#     else:
#         aa_codon_map[value] = [key]

## solution 2
# aa_codon_map = {}
# for key, value in gen_code.items():
#     # Note: dict.get(value, []).append() will not work here since .append is an in-place operation
#     aa_codon_map.setdefault(value, []).append(key)

## solution 3
# from collections import defaultdict
# aa_codon_map = defaultdict(list)
# for key, value in gen_code.items():
#     aa_codon_map[value].append(key)

pprint.pprint(aa_codon_map)
