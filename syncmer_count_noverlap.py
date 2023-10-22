import sys
# Add sequence data path here to sys.path
sys.path.append('/home/chenye/result/John')
sys.path.append('/home/chenye/data/mitochondrion')
from load_file import read_noverlap_results
from estimate_parameter import hash, jaccard_distance_estimation, containment_distance_estimation
from distance import mash_distance, mash_containment 

#Get the name of species fro a file and add to a list

if __name__ == '__main__':
    with open('species.txt', 'r') as f:
        species_list = []
        for line in f:
            species_list.append(line.strip()+'.txt')

    # Get the results from the file, pack as list
    sequence_human = read_noverlap_results('Homo_sapiens_neanderthalensis_mitochondrion.txt')

    species_human_jaccard_index_dic = {}

    for species_name in species_list:

        sequence_none_human = read_noverlap_results(species_name) 
        # sequence_none_human sequence_human
        hash_human, hash_none_human = hash(sequence_human, sequence_none_human)

        s = min(len(sequence_human), len(sequence_none_human))
        j = jaccard_distance_estimation(hash_human, hash_none_human, s)
        cde_a, cde_b = containment_distance_estimation(hash_human, hash_none_human, s)

        mash_distance_13 = mash_distance(13, j)
        mash_containment_13_a = mash_containment(13, cde_a)
        mash_containment_13_b = mash_containment(13, cde_b)

        print(mash_distance_13)
        print(mash_containment_13_a)
        print(mash_containment_13_b)
        break



    

