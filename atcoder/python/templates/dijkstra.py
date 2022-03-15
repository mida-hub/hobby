#!/usr/bin/env python3
# abc012d
import heapq

def main():
    def dijkstra(i):
        # print('-'*100)
        hq = [(i, 0)]

        time_list = [float('inf')] * N
        # 引っ越し候補地のバス停のコストは0
        time_list[i] = 0

        heapq.heapify(hq)
        # print(f'time_list: {time_list}')
        while hq:
            bus_stop, total_time = heapq.heappop(hq)

            # print(f'bus_stop, total_time: {bus_stop}, {total_time}')

            for a2b, a2b_time in rosen[bus_stop]:
                # print(f'a2b, a2b_time: {a2b}, {a2b_time}')

                if total_time + a2b_time < time_list[a2b]:
                    time_list[a2b] = total_time + a2b_time
                    heapq.heappush(hq, (a2b, time_list[a2b]))
            # print(f'time_list: {time_list}')

        return time_list

    N, M = map(int, input().split())
    rosen = [[] for _ in range(N)]

    for _ in range(M):
        a, b, t = map(int, input().split())
        a -= 1
        b -= 1
        rosen[a].append((b, t))
        rosen[b].append((a, t))
    # print(rosen)

    ans = float('inf')
    for i in range(N):
        d = dijkstra(i)
        ans = min(ans, max(d))
    print(ans)

if __name__ == '__main__':
    main()
