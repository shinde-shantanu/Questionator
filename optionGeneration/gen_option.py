import pickle

from gensim.models.keyedvectors import KeyedVectors
glove_model = KeyedVectors.load_word2vec_format("gensim_glove_vectors.txt", binary=False)

def mk_option(ip):
	try:
		op=glove_model.most_similar([ip])
		op_list = [o[0] for o in op]
		return(op_list)
	except:
        	return("Word not in corpora")

#print(mk_option("messi"))

