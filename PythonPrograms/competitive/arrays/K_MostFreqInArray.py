def print_N_mostFrequentNumber(arr, N, K):
    count = {}

    # Array to store the elements according
    # to their frequency
    freq = [[] for i in range(len(arr) + 1)]
    for n in arr:
        count[n] = 1 + count.get(n, 0)
    for n, c in count.items():
        freq.append(n)

    res = []
    # if K elements have been printed
    for i in range(len(freq) - 1, 0, -1):
        for n in freq[i]:
            res.append(n)
            if len(res) == K:
                return res[-1::-1]


arr = [3, 1, 4, 4, 5, 2, 6, 1]
K = 2
print(print_N_mostFrequentNumber(arr, len(arr), K))
