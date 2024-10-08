import random
import time

def generate_prices(n):
    prices = sorted([random.randint(1, n) for _ in range(1, n+1)])
    print(f"Preços gerados para n={n}: {prices[:10]}...")
    return prices

def dynamic_programming(prices, n):
    dp = [0] * (n + 1)
    for i in range(1, n + 1):
        max_val = 0
        for j in range(1, i + 1):
            max_val = max(max_val, prices[j - 1] + dp[i - j])
        dp[i] = max_val
    print(f"Resultado DP para n={n}: {dp[n]}")
    return dp[n]

def greedy(prices, n):
    density = [(prices[i] / (i + 1), i + 1) for i in range(n)]
    density.sort(reverse=True, key=lambda x: x[0])
    total_value = 0
    remaining_length = n
    while remaining_length > 0:
        for d, length in density:
            if length <= remaining_length:
                total_value += prices[length - 1]
                remaining_length -= length
                break
    print(f"Resultado guloso para n={n}: {total_value}")
    return total_value

def main():
    inc, fim, stp = 1000, 20000, 1000
    results = []

    for n in range(inc, fim + 1, stp):
        prices = generate_prices(n)

        start = time.time()
        vDP = dynamic_programming(prices, n)
        tDP = time.time() - start

        start = time.time()
        vGreedy = greedy(prices, n)
        tGreedy = time.time() - start

        if vDP != 0:
            accuracy = (vGreedy / vDP) * 100
        else:
            accuracy = 0
        
        results.append((n, vDP, tDP, vGreedy, tGreedy, accuracy))

    print("n vDP tDP vGreedy tGreedy %")
    print("----------------------------------------------------")
    for result in results:
        print(f"{result[0]} {result[1]} {result[2]:.6f} {result[3]} {result[4]:.6f} {result[5]:.2f}")

if __name__ == "__main__":
    main()