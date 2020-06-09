def has_negatives(a):

    cache = {}
    
    result = []
    
    for e in a: 
        if e not in cache:
            cache[e] = e
        
    for e in cache: 
        if e > 0 and e * (-1) in cache:
            result.append(e)
    
    return result


if __name__ == "__main__":
    print(has_negatives([-1,-2,1,2,3,4,-4]))