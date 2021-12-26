import MeCab
import sys
from matplotlib import pyplot as plt
from wordcloud import WordCloud

args = sys.argv
input_data = args[1]
remove_word = args[2]

with open(input_data, mode='rt', encoding='utf-8') as inpFILE:
    source_text = inpFILE.read()

tagger = MeCab.Tagger()
tagger.parse('')
node = tagger.parseToNode(source_text)

word_list = []
while node:
    word_type = node.feature.split(',')[0]
    if word_type == '名詞':
        word_list.append(node.surface)
    node = node.next

remove_word_list = []
remFILE = open(remove_word)
for i in remFILE:
    remove_word_list.append(i.rstrip())

word_chain = ' '.join(word_list)

W = WordCloud(width=640,height=480,background_color='white',font_path="./ipag.ttf",stopwords = remove_word_list).generate(word_chain)

plt.imshow(W)
plt.axis('off')
plt.show()