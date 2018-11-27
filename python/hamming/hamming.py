def distance(strand_a, strand_b):
    if len(strand_a) == len(strand_b):
            i = 0
            dist = 0
            for i in range(len(strand_a)):
                if strand_a[i] != strand_b[i]:
                    dist += 1
            return dist
    else:
        raise ValueError("strands are different lengths")