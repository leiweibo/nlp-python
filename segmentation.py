import nltk.tokenize as tk

doc = "Are you curious about tokenization? " \
      "Let's see how it works! " \
      "We need to analyze a couple of sentences " \
      "with punctuations to see it in action."
print(doc)
tokens = tk.sent_tokenize(doc)  # 句子分词
for i, token in enumerate(tokens):
    print("%2d" % (i + 1), token)
# 1 Are you curious about tokenization?
# 2 Let's see how it works!
# 3 We need to analyze a couple of sentences with punctuations to see it in action.

tokens = tk.word_tokenize(doc)  # 单词分词
for i, token in enumerate(tokens):
    print("%2d" % (i + 1), token)