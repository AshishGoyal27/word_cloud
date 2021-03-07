from wordcloud import WordCloud, STOPWORDS 
import matplotlib.pyplot as plt 
import pandas as pd 

df1 = pd.read_csv('five_star_reviews.csv')
df1.head()
df2 = pd.read_csv('one_star_reviews.csv')
df2.head()

stopwords = set(STOPWORDS) 
words = ''
for review in df1.Review:
    tokens = str(review).split()
    tokens = [i.lower() for i in tokens]
    
    words += ' '.join(tokens) + ' '
    
wordcloud = WordCloud(width = 800, height = 800, background_color ='white', 
                stopwords = stopwords, min_font_size = 10).generate(words) 
  
# plot the WordCloud image                        
plt.figure(figsize = (8, 8), facecolor = None) 
plt.imshow(wordcloud) 
plt.axis("off") 
plt.tight_layout(pad = 0)
plt.savefig('word_cloud.png')
plt.show()
print("Successfully saved")
