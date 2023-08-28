import pickle


def save(filename:str, obj:object):
    with open(filename, 'wb') as handle:
        pickle.dump(obj, handle, protocol=pickle.HIGHEST_PROTOCOL)

def load(filename:str) -> object:
    with open(filename, 'rb') as handle:
        b = pickle.load(handle)
    return b