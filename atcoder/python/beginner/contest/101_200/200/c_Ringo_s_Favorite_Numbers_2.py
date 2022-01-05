def main():
    n = int(input())
    an = list(map(int, input().split()))
    bn = [0] * 200
    
    for i in range(n):
        bn[an[i]%200]+=1

    total = 0
    for i in range(200):
        total += (bn[i] * (bn[i]-1))//2

    print(total)

main()
