from bs4 import BeautifulSoup
from functools import reduce
from collections import Counter
import multiprocessing as mp
import tarfile

def extract_and_process(member):

    #extract
    tar = tarfile.open("dados.tar.gz", "r:gz")
    f = tar.extractfile(member)
    soup = BeautifulSoup(f, 'html.parser')

    #process
    result = Counter()
    for aux in soup.find_all(class_='trackInfo'):

        name = aux.find(class_='trackName').string.strip().split('-')[-1]
        popularity = int(aux.find(class_='counts').string.split()[-2])

        if name in result:
            result[name] += popularity
        else:
            result[name] = popularity
    return result
    
def merge_function(dict_1, dict_2):
    return Counter(dict_1) + Counter(dict_2)


def mapreduce(num_cpus=2):
    tar = tarfile.open('dados.tar.gz', 'r:gz')
    if num_cpus > 1:
        with mp.Pool(num_cpus) as pool:
            intermed = pool.imap_unordered(extract_and_process,
                                           tar.getmembers())
    else:
        intermed = map(extract_and_process, tar.getmembers())
    final = reduce(merge_function, intermed)
    return final


