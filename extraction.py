import nltk.tokenize as tk
import sklearn.feature_extraction.text as ft

doc = 'The brown dog is running. ' \
      'The black dog is in the black room. ' \
      'Running in the room is forbidden.'

sents = tk.sent_tokenize(doc)

cv = ft.CountVectorizer()           # 构建词袋模型
bow = cv.fit_transform(sents)       # 训练词袋模型
print(cv.get_feature_names())       # 获取所有特征名
# ['black', 'brown', 'dog', 'forbidden', 'in', 'is', 'room', 'running', 'the']
print(bow.toarray())