import spacy
from   spacy.training.example import Example
import random
import pandas as pd

# Load a blank English spaCy model
nlp = spacy.blank("en")

# Define the NER component and add it to the pipeline
ner = nlp.create_pipe("ner")
nlp.add_pipe("ner")

# Load your labeled dataset
data = pd.read_csv("dataset.csv")

# Convert the dataset into spaCy's training format
TRAIN_DATA = []

for index, row in data.iterrows():
    text = row["Text"]
    label = row["Label"]
    annotations = {"entities": [(0, len(text), label)]}
    TRAIN_DATA.append((text, annotations))

# Training loop
nlp.begin_training()

for _ in range(20):  # You can adjust the number of iterations
    random.shuffle(TRAIN_DATA)
    losses = {}

    for text, annotations in TRAIN_DATA:
        example = Example.from_dict(nlp.make_doc(text), annotations)
        nlp.update([example], losses=losses)

# Save the trained model
nlp.to_disk("/Users/madhuupadhyay/Documents/Natural_Language_Processing/Information_Extraction/nlp_address")

# Example usage
loaded_nlp = spacy.load("/Users/madhuupadhyay/Documents/Natural_Language_Processing/Information_Extraction/nlp_address")
text = "Please deliver the package to 123 Main Street, Cityville."
doc = loaded_nlp(text)

for ent in doc.ents:
    print(f"Entity: {ent.text}, Label: {ent.label_}")



#/Users/madhuupadhyay/Documents/Natural_Language_Processing/Information_Extraction/nlp_address