def distance(strand_a, strand_b):
    strand_a = strand_a.lower()
    strand_b = strand_b.lower()

    if len(strand_a) != len(strand_b):
        raise ValueError('Both the sequences must be of same length')
    
    mapping = zip(strand_a, strand_b)
    
                                                            # sum([True, False, True]) gives 2.
    return sum(i != j for i, j in mapping)             # generator comprehension is being used 
                                                            # instead of list comprehension.