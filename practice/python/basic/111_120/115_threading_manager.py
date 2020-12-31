import multiprocessing
import concurrent.futures

def list_append(shared_list, name):
    shared_list.append(name)

def update_dict(shared_list, key, value):
    shared_list[key] = value

if __name__ == '__main__':
    manager = multiprocessing.Manager()
    shared_list = manager.list([1, 2, 3])
    shared_dict = manager.dict({'Name': 'Saburo', 'Age': 12, 'Sex': 'Man'})
    with concurrent.futures.ProcessPoolExecutor(max_workers=4) as executor:
        executor.submit(list_append, shared_list, 'A')
        executor.submit(list_append, shared_list, 'B')
        executor.submit(update_dict, shared_dict, 'Name', 'Taro')
        executor.submit(update_dict, shared_dict, 'Age', 21)
    print(shared_list)
    print(shared_dict)
