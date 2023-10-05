import sys
# Add sequence data path here to sys.path
sys.path.append('/home/chenye/result/John')
sys.path.append('/home/chenye/data/mitochondrion')
from load_file import read_noverlap_results
from seed_count import seed_count
from plot_dic import plot_dic

#Get the name of species fro a file and add to a list

if __name__ == '__main__':
    with open('species.txt', 'r') as f:
        species_list = []
        for line in f:
            species_list.append(line.strip()+'.txt')

    # Get the results from the file, pack as list
    sequence_human = read_noverlap_results('Homo sapiens neanderthalensis mitochondrion.txt')

    species_human_jaccard_index_dic = {}

    for species_name in species_list:
        sequence_none_human = read_noverlap_results(species_name) 
        seed_same_count = seed_count(sequence_human, sequence_none_human)
        
        jaccard_index = seed_same_count / ( len(sequence_human) + len(sequence_none_human ) )

        species_human_jaccard_index_dic[species_name] = jaccard_index
    
    plot_dic(species_human_jaccard_index_dic, species_human_blast_dic)



    

