import pickle


with open('knn_model_iris.pkl', 'rb') as f:
    data = pickle.load(f)