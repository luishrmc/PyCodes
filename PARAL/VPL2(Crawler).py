import threading
import requests
import ssl


class Worker(threading.Thread):
    def __init__(self, id_, **kwargs):
        super(Worker, self).__init__(**kwargs)
        self._id = id_
        self._counter = 0
    
    def run(self):
        ssl._create_default_https_context = ssl._create_unverified_context
        arq = requests.get('http://www.gutenberg.org/files/{}/{}-0.txt'.format(self._id, self._id))
        for words in arq.text:
            if words == '\n':
                self._counter += 1
    
    def get_result(self):
        return self._counter


def crawler(id):
    #Lista contendo os id_ dos links
    ids = list()
    with open('dados/ids.txt', 'r') as file:
        for line in file:
            ids.append(int(line.strip()))
    
    #Lista contendo o resultado das threads
    threads = list()

    #Execução das threads, em que cada elemento da lista é objeto do tipo Worker
    for i in range(16): threads.append(Worker(ids[i]))
    for i in range(16): threads[i].start()
    for i in range(16): threads[i].join()
    
    #Soma dos resultados
    sum = 0
    for i in range(16):
        sum += threads[i].get_result()
    
    return sum
