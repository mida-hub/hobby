def main():
    n = int(input())

    r_n_1 = int(n ** 0.5) + 1
    divider = []
    divided = []

    for i in range(1, r_n_1 + 1):
        if n % i == 0:
            divider.append(i)
    
    for i in divider:
        divided.append(n // i)

    # print(divider)
    # print(divided)
    
    output = set(divider + divided)
    
    # print(sorted(output))

    for i in sorted(output):
        print(i)
    

main()
