import pandas as pd

df = pd.read_excel('tmp.xlsx', sheet_name="Sheet")
print df.columns
df = df[(True-df['firstiframets'].isin([0]))]

dfselect = df[['medialogints']]
dfselect['video-voice-play'] = df['firstiframets'].copy().sub(df['firstvoiceplayts'],axis=0)
dfselect['connectrtt'] = df['vsconnectedts'].copy().sub(df['medialogints'],axis=0)
dfselect['firstpacktime'] = df['firstvideopackts'].copy().sub(df['vsconnectedts'],axis=0)
dfselect['assembletime'] = df['firstiframeassemblets'].copy().sub(df['firstvideopackts'],axis=0)
dfselect['displaytime'] = df['firstiframets'].copy().sub(df['firstiframeassemblets'],axis=0)

from sklearn.cluster import KMeans

km=KMeans(n_clusters=32, init='k-means++', max_iter=100)

km.fit(dfselect)

Z= km.predict(dfselect)

print km.cluster_centers_
#print Z
writer = pd.ExcelWriter('output1.xlsx')
df['clusterid'] = Z
lista = [0 for i in range(32)]
avg = [[0 for i in range(5)] for x in range(32)]
key = ['medialogints','vsconnectedts','firstvideopackts','firstiframeassemblets','firstiframets']
for index,i in enumerate(Z):
    lista[i] = lista[i] + 1
    for x in key:
        mod1=df[x]
        #print index, mod1
        avg[i][x] = mod1[index+1] + avg[i][x]
for i in range(32):
    for x in key:
        avg[i][x] = avg[i][x]/lista[i]
#print df.head(5)
df.to_excel(writer,'sheet1')
result=pd.DataFrame(km.cluster_centers_)
result['count'] = lista
result.append(pd.DataFrame(avg))
result.to_excel(writer,'sheet2')
writer.save()
