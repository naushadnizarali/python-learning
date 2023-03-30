import spacy
import nltk

from pyresparser import ResumeParser
data = ResumeParser("/Volumes/MobileDev/learning/python/sample-1.pdf").get_extracted_data()

print(data)