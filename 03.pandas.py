import pandas as pd

data= {
    "name":["nader","Ahmet","Mehmet","nader","Sami","shadi","bagi",],
    "surname":["dal","alfa","beta","dal","theta","sigma",None,]
    }

df = pd.DataFrame(data , index =['a', 'b', 'c', 'd', 'e', 'f', 'g'])

print(df)
# print(dir(pd.DataFrame))

