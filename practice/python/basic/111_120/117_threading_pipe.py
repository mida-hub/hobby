from multiprocessing import Process, Pipe

def sender(conn, msgs):
    for msg in msgs:
        conn.send(msg)
        print(f'Sent message: {msg}')

def receiver(conn):
    while 1:
        msg = conn.recv()
        if msg == 'END':
            break
        print(f'received message: {msg}')

if __name__ == '__main__':
    msgs = ['hello', 'hey', 'goodbye', 'END']
    parent_conn, child_conn = Pipe()

    p1 = Process(target=sender, args=(parent_conn, msgs))
    p2 = Process(target=receiver, args=(child_conn,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()
