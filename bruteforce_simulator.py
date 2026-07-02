def estimate_bruteforce(length):
    charset=94
    combinations=charset**length
    attempts_per_second=1000000000
    years=(combinations/attempts_per_second)/(60*60*24*365)
    print(f"Combinations: {combinations:,}")
    print(f"Estimated Time: {years:.2f} years")
