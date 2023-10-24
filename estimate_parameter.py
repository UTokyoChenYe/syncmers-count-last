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

def containment_distance_estimation(hash_seqa, hash_seqb):
    hash_seta = set(hash_seqa)
    hash_setb = set(hash_seqb)

    inter_m = hash_seta & hash_setb

    cde_a = len(inter_m) / len(hash_seta)
    cde_b = len(inter_m) / len(hash_setb)

    return cde_a, cde_b




    
    