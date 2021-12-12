#Import the library
from textblob import TextBlob
x = input("Enter the String:")

#using the TextBlob function and check the Polarity score
edu = TextBlob(x)
y = edu.sentiment.polarity

# Check for the condition to determine sentiment
if y < 0 :
    print(x)
    print("The sentence is Negative")
    
elif y <=1 and y>0:
    print(x)
    print("The sentence is Positive")
    
else:
    print(x)
    print("The sentence is Neutral")
    
