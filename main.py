import pandas as pd
import volume

data1 = pd.read_csv('./example-data/smalldata1.csv')
data2 = pd.read_csv('./example-data/smalldata3.csv')

print(volume.volume_change(data1, data2))

