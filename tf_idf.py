import nltk.tokenize as tk
import sklearn.feature_extraction.text as ft
import numpy as np

doc = 'The brown dog is running. ' \
      'The black dog is in the black room. ' \
      'Running in the room is forbidden.'

sents = tk.sent_tokenize(doc)

cv = ft.CountVectorizer()
bow = cv.fit_transform(sents)

tt = ft.TfidfTransformer()          # 获取TF-IDF模型训练器
tfidf = tt.fit_transform(bow)       # 训练
print(np.round(tfidf.toarray(), 2))       # 精确到小数点后两位
