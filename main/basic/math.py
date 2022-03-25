#%%
print(round(3.1415))
print(round(3.1415, 2))

print(3 / 2)  # 1.5
print(3 // 2)  # 1
#%%

def get_median_v2(data):
    # recommended to use numpy
    data = sorted(data)
 
    centerIndex = len(data)//2
    return (data[centerIndex ] + data[-centerIndex - 1])/2