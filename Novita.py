import pandas as pd
import numpy as np
import sys  

spam_data = pd.read_csv('/resources/data/UAS/datalagunovita.csv')
spam_data['label'] = np.where(spam_data['label']=='positif',1,0)
print(spam_data.shape)
spam_data.head(10)
import pandas as pd
import numpy as np
import sys  

spam_data = pd.read_csv('/resources/data/UAS/datalagunovita.csv')
spam_data['label'] = np.where(spam_data['label']=='positif',1,0)
print(spam_data.shape)
spam_data.head(10)
print(preds)
X_train
X_test
