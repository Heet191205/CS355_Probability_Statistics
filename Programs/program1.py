import numpy as np

#Calculates r
def calc_r(d, og, n, sumi, sumsq, sqsum): #d - deck and og - original
    sum_iyi = sum(i * d[i-1] for i in og)
    r = (n * sum_iyi - sqsum) / (n * sumsq - sqsum)
    return r

# shuffle method 1 : halves in 2
def d_1run(d):
    h1 = d[:len(d)//2] # half 1 of deck
    h2 = d[len(d)//2:] # half 2 of deck
    shuffled = []
    for i in range(len(h1)): # using index
        shuffled.append(h1[i])
        shuffled.append(h2[i])
    return shuffled

# shuffle method 2 : swaps order of halved
def d_2run(d):
    h1 = d[:len(d)//2]
    h2 = d[len(d)//2:]
    shuffled = []
    for i in range(len(h1)):  # using index
        shuffled.append(h2[i])
        shuffled.append(h1[i])
    return shuffled

# for running the program and to print output
def run_prog(shuffle_m, d_size):
    og = list(range(1, d_size + 1))
    d = og[:]
    r = []
    n = len(d)

    sumi = sum(og) # 1 to n sum 
    sumsq = sum(i**2 for i in og) # 1 to n (sum of squares)
    sqsum = sumi * sumi # square of sum 

    for _ in range(15):
        d = shuffle_m(d)
        r.append(calc_r(d, og, n , sumi, sumsq, sqsum))
    
    print("Shuffle | r-val")
    print("---")
    for i, r in enumerate(r, 1):
        print(f"{i:>6}  | {r:.5f}")
    return r

# bonus: full deck and random shuffle 
def bonus(d):
    np.random.shuffle(d)
    return d

if __name__ == "__main__":
    print("First Run (52 cards)")
    run_prog(d_1run, 52)
    
    print("\nSecond Run (52 cards)")
    run_prog(d_2run, 52)
    
    print("\nThird Run (104 cards)")
    run_prog(d_1run, 104)
    
    print("\nFourth Run (104 cards)")
    run_prog(d_2run, 104)
    
    print("\nBonus Shuffle (52 cards)")
    run_prog(bonus, 52)
