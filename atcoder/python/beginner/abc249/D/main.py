from collections import Counter

def make_divisors(n: int) -> list:
    return_list = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            return_list.append(i)
            if i != n // i:
                return_list.append(n//i)

    return return_list

def main():
    n = int(input())
    an = list(map(int, input().split()))
    an_set = set(an)
    counter_an = Counter(an)

    answer = 0
    for ai in an_set:
        for aj in make_divisors(ai):
            answer += counter_an[ai] * counter_an[aj] * counter_an[ai/aj]
    print(answer)
    return

main()
