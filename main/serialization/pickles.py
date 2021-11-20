import pickle
#https://docs.python.org/ko/3/library/pickle.html


obj = [1,2,3]
with open('main/serialization/obj.pkl', 'wb') as f:
    pickle.dump(obj, f)
#%%

obj2 = pickle.load(open("main/serialization/obj.pkl", 'rb'))
