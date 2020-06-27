import multiprocessing
import time

class MyProcess(multiprocessing.Process):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def process_function(self):
        print(f'Process {self.name} : start')
        time.sleep(2)
        print(f'Process {self.name} : end')

    def run(self):
        print('run start')
        self.process_function()

if __name__ == '__main__':
    myProcess = MyProcess('Matsuda')
    myProcess.start()
    myProcess.join()
    print('Main end')

