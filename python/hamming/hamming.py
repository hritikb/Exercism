def distance(strand_a, strand_b):
    strand_a = strand_a.lower()
    strand_b = strand_b.lower()

    if len(strand_a) != len(strand_b):
        raise ValueError('Both the sequences must be of same length')
    
    mapping = zip(strand_a, strand_b)
    lst = [True for i in mapping if i[0] != i[1]]
    return len(lst)

