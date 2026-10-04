from textblob import TextBlob
text= input("Enter the sentence:    ")
analysis= TextBlob(text)
polarity = analysis.sentiment.polarity

if polarity > 0:
  sentiment= "positive"
elif polarity < 0:
  sentiment= "negative"
else :
  sentiment= "neutral"

print("text:", text)
print("polarity:", polarity)
print("sentiment:", sentiment)
