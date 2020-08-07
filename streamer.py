import nltk.stem.porter as pt
import nltk.stem.lancaster as lc
import nltk.stem.snowball as sb

words = ['table', 'probably', 'wolves', 'playing', 'is',
         'dog', 'the', 'beaches', 'grounded', 'dreamt', 'envision']

pt_stemmer = pt.PorterStemmer()         # 波特词干提取器，偏宽松
lc_stemmer = lc.LancasterStemmer()      # 朗卡斯特词干提取器，偏严格
sb_stemmer = sb.SnowballStemmer('english')  # 思诺博词干提取器，偏中庸
for word in words:
    pt_stem = pt_stemmer.stem(word)
    lc_stem = lc_stemmer.stem(word)
    sb_stem = sb_stemmer.stem(word)
    print('%8s %8s %8s %8s' % (word, pt_stem, lc_stem, sb_stem))