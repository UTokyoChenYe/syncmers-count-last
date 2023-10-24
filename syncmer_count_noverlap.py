from load_file import read_noverlap_results
from estimate_parameter import hash, jaccard_distance_estimation, containment_distance_estimation
from distance import mash_distance, mash_containment 
import pandas as pd

#Get the name of species fro a file and add to a list

if __name__ == '__main__':
    with open('/home/chenye/data/mitochondrion/species.txt', 'r') as f:
        species_list = []
        for line in f:
            species_list.append(line.strip()+'.txt')

    # Get the results from the file, pack as list
    sequence_human = read_noverlap_results('/home/chenye/result/John/Homo_sapiens_neanderthalensis_mitochondrion.txt')

    species_human_mash_similarity_13_dic = {}
    species_human_mash_similarity_cde_human_13_dic = {}
    species_human_mash_similarity_cde_none_human_13_dic = {}

    for species_name in species_list:

        sequence_none_human = read_noverlap_results("/home/chenye/result/John/"+species_name) 
        # sequence_none_human sequence_human
        hash_human, hash_none_human = hash(sequence_human, sequence_none_human)

        s = min(len(sequence_human), len(sequence_none_human))
        j = jaccard_distance_estimation(hash_human, hash_none_human, s)
        cde_human, cde_none_human = containment_distance_estimation(hash_human, hash_none_human, s)

        mash_similarity_13 = 1.0 - mash_distance(13, j)
        mash_similarity_cde_human_13 = 1.0 - mash_containment(13, cde_human)
        mash_similarity_cde_none_human_13 = 1.0 - mash_containment(13, cde_none_human)

        species_human_mash_similarity_13_dic[species_name] = mash_similarity_13
        species_human_mash_similarity_cde_human_13_dic[species_name] = mash_similarity_cde_human_13
        species_human_mash_similarity_cde_none_human_13_dic[species_name] = mash_similarity_cde_none_human_13

    species_human_mash_similarity_13_list = [species_human_mash_similarity_13_dic]
    jaccard_distance_df = pd.DataFrame(species_human_mash_similarity_13_list).T
    jaccard_distance_df.rename(columns={0: 'jaccard_distance'}, inplace=True)
    print(jaccard_distance_df)
    print(species_human_mash_similarity_cde_human_13_dic)


    
    




    

