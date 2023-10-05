def seed_count(sequence_a, sequence_b):

    seed_count = 0

    for seed_a in sequence_a:
        for seed_b in sequence_b:
            if seed_a == seed_b:
                seed_count = seed_count + 1
    
    return seed_count
                

