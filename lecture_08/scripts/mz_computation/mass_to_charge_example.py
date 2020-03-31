import masses
from pprint import pprint


list_of_protein_dicts = [{'seq': 'ACACIMED', 'ch': 2},
                         {'seq': 'ELEMYRATNE', 'ch': 1},
                         {'seq': 'wapwop', 'ch': 3},
                         {'seq': 'zeittsieg', 'ch': 2},
                         {'seq': 'DESFBIRC', 'ch': 1},
                         {'seq': 'altaatsiv', 'ch': 3},
                         {'seq': 'MEINWOHC', 'ch': 2}]
# 1. loop over list
# 2. check for validity
# 3. if valid compute m/z

def is_valid(seq):
    valid = True
    for char in seq.upper():
        if char not in masses.mass_dict:
            valid = False
    return valid

def compute_mz(seq, ch):
    mz = 0
    for char in seq.upper():
        mass = masses.mass_dict[char]
        mz += mass
    mz += masses.mass_h2o
    mz = (mz+ch)/ch
    return mz

def main():
    for item in list_of_protein_dicts:
        seq = item['seq']
        ch = item['ch']
        if not is_valid(seq):
            print('seq: {} is invalid'.format(seq))
            continue
        mz = compute_mz(seq, ch)
        print('seq: {}, mz: {}'.format(seq, mz))


if __name__ == '__main__':
    main()
