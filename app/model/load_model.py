import pickle


def load_model(path: str):
    model = pickle.load(open(path, 'rb'))
    return model
