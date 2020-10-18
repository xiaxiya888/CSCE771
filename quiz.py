# Do imports
import spacy
nlp = spacy.load('en_core_web_sm')

f=open("dataset-nyt-nobel2020.txt")
data=f.readlines()
