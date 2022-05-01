#!/usr/bin/env python3

def add(target_dict, target_value):
    if target_value in target_dict:
        target_dict[target_value] += 1
    else:
        target_dict[target_value] = 1
    
    return target_dict

def search(target_dict):
    for i in target_dict:
        if target_dict[i] == 1:
            return i

def main():
    X = {}
    Y = {}

    for _ in range(3):
        x, y = map(int, input().split())

        X = add(X, x)
        Y = add(Y, y)

    x, y = search(X), search(Y)
    print(x, y)

if __name__ == '__main__':
    main()
