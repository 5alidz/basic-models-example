import sys
from transformers import pipeline

message = sys.argv[1]

classifier = pipeline("sentiment-analysis")
sentiment = classifier(message)

print(sentiment)


