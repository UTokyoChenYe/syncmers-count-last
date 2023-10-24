import mmh3
#使用mmh3包，可以生成32bit的哈希值

def hash(seqa, seqb):
    #已经完成去重排序
    hash_seqa = []
    hash_seqb = []
    for a_mer in seqa:
        hash_seqa.append(mmh3.hash(a_mer))
    for b_mer in seqb:
        hash_seqb.append(mmh3.hash(b_mer))
    hash_seta = set(hash_seqa)
    hash_setb = set(hash_seqb)
    hash_lista = list(hash_seta)
    hash_listb = list(hash_setb)
    hash_lista.sort()
    hash_listb.sort()
    return hash_lista, hash_listb

def jaccard_distance_estimation(hash_seqa, hash_seqb, s):
    hash_seqa_s = hash_seqa[:s]
    hash_seqb_s = hash_seqb[:s]

    hash_seta_s = set(hash_seqa_s)
    hash_setb_s = set(hash_seqb_s)

    inter_s = hash_seta_s & hash_setb_s
    same_count = len(inter_s)
    
    return same_count / s

def containment_distance_estimation(hash_seqa, hash_seqb, m):
    hash_seta = set(hash_seqa)
    hash_setb = set(hash_seqb)

    hash_seqa_m = hash_seqa[:m]
    hash_seqb_m = hash_seqb[:m]

    hash_seta_m = set(hash_seqa_m)
    hash_setb_m = set(hash_seqb_m) 

    inter_a_m = hash_seta_m & hash_setb
    inter_b_m = hash_setb_m & hash_seta

    cde_a = len(inter_a_m) / len(hash_seta_m)
    cde_b = len(inter_b_m) / len(hash_setb_m)

    return cde_a, cde_b




    
    