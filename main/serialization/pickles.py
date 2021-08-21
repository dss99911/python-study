import pickle
#https://docs.python.org/ko/3/library/pickle.html


obj = [1,2,3]
f = open('main/serialization/obj.pkl', 'wb')
pickle.dump(obj, f)
#%%

obj2 = pickle.load(open("main/serialization/obj.pkl", 'rb'))
