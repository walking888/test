import pandas as pd

df = pd.read_excel('tmp2.xlsx', sheet_name="Sheet")
print df.columns
df = df[(True^df['firstiframets'].isin([0]))]
df = df[(True^df['sdkboundts'].isin([0]))]
mod1 = df['model']
lll = df['sdkboundts'].tolist()
mod2 =list(set(mod1))
#print mod2
dic = {}
for i in mod2:
    dic[i] = 0

dic1 = {}
for i in mod2:
    dic1[i] = 0

count = 0
for i,x in enumerate(mod1):
    dic[x] = dic[x]+1
    dic1[x] = dic1[x] + lll[i]
    count = count + 1


asd =sorted(dic.items(),key=lambda x:x[1])
print count
print asd
for x,value in asd:
    print x, dic1[x]/dic[x]
