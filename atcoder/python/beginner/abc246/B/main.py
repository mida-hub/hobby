#!/usr/bin/env python3
def main():
    A, B = map(int, input().split())
    C = (A * A + B * B) ** 0.5
    
    print(A / C, B / C)

if __name__ == '__main__':
    main()
