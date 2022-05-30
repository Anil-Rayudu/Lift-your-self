import json
import pandas as pd
names=["Anil", "Avinash", "Nithya", "G1"]
points=[5,3,6,9]
a={ "Name":names,"Points":points}
a["BoundingBox"]=[(0,1),(1,1),(2,1),(3,1)]
print (a)
with open('data.json','w') as fp:
    json.dump(a,fp)
df=pd.DataFrame(data=a)
print (df)