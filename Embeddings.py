from keras.applications.resnet50 import ResNet50
import PIL
from PIL import Image
import requests
import pickle
import numpy as np
import os

model_resnet = ResNet50(weights='imagenet', include_top=False, pooling='avg')

if(os.path.exists('Embedding_database')):
    with open('Embedding_database','rb') as f:
        Embed = pickle.load(f)
else:
    Embed = {}


def gen_embed(url,image_id):

    try:
        image = Image.open(requests.get(url, stream=True).raw)
        im = np.asarray(image)
        if(im.shape[2] != 3):
            return

        img = im.reshape(1,im.shape[0],im.shape[1],im.shape[2])
        Embed[image_id] = model_resnet(img).numpy()[0]
        try:
    	    emb = open('Embedding_database', 'wb')
    	    pickle.dump(Embed, emb)
    	    emb.close()

        except:
    	    print("Something went wrong")

    except PIL.UnidentifiedImageError:
        print("False URL")

