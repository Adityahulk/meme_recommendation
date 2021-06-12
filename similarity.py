from math import*
import pickle

def euclidean_distance(x,y):
    return sqrt(sum(pow(a-b,2) for a, b in zip(x, y)))


with open('Embedding_database','rb') as f:
    Embedding_database = pickle.load(f)


def similar_k(image_id,k):

  recommended = []
  output = Embedding_database[image_id]
  dis_dict = {}
  for key in Embedding_database:
    dis_dict[key] = euclidean_distance(Embedding_database[key],output)

  sorted_dis_dict = dict(sorted(dis_dict.items(), key=lambda item: item[1]))
  i = 0

  for key in sorted_dis_dict:
    if i == k:
      break
    if key == image_id:
      continue;
    else:
        recommended.append(key)

    i = i+1

  return recommended
