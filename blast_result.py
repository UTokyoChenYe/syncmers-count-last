import pandas as pd

def blast_result():
    blast_dic = {"Bos_taurus_isolate_CLH_19_mitochondrion.txt": 0.7434,
           "Bufo_gargarizans_mitochondrion.txt": 0.7044,
           "Crocodylus_porosus_mitochondrion.txt": 0.7067,
           "Echinocrepis_rostrata_mitochondrion.txt": 0.7123,
           "Equus_caballus_mitochondrion.txt": 0.7501,
           "Eudyptes_chrysolophus_mitochondrion.txt": 0.6931,
           "Giraffa_camelopardalis_camelopardalis_isolate_GF272_mitochondrion.txt": 0.7405,
           "Graptemys_ouachitensis_mitochondrion.txt": 0.7016,
           "Latimeria_menadoensis_mitochondrion.txt": 0.6893,
           "Loxodonta_cyclotis_isolate_Coco_mitochondrion.txt": 0.7277,
           "Mus_musculus_molossinus_mitochondrion.txt": 0.7222,
           "Ornithorhynchus_anatinus_mitochondrion.txt": 0.6912,
           "Pan_troglodytes_mitochondrion.txt": 0.9138,
           "Pelagia_noctiluca_mitochondrion.txt": 0.6715,
           "Trimerodytes_annularis_mitochondrion.txt": 0.6962,
           }
    blast_list = [blast_dic]
    blast_df = pd.DataFrame(blast_list).T
    blast_df.rename(columns={0: 'blast'}, inplace=True)
    return blast_df
