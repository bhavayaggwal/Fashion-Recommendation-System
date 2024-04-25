import pickle
import numpy as np
from tensorflow.keras.preprocessing import image

feature_list = np.array(pickle.load(open('embeddings.pkl','rb')))
filenames = pickle.load(open('filenames.pkl','rb'))

