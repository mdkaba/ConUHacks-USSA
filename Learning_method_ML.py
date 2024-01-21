import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

dataset = pd.read_csv('dataset.csv')
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, -1].values
df_main = dataset[["Sentence", "Type"]].copy()

new_column = []

for i in range(len(dataset)):
    extracted_strings = dataset["Sentence"].tolist()[i].lower().strip().split()
    extracted_strings_cleaned = ""
    # print(extracted_strings)
    for word in extracted_strings:
        word_cleaned = word.replace(".", "").replace(",", "").replace("?", "").replace("!", "").replace("(", "").replace(")","").replace(
            "<", "").replace(">", "").replace("*", "").replace("_", "").replace("[", "").replace("]", "")
        if word_cleaned != "":
            extracted_strings_cleaned = extracted_strings_cleaned + " " + word_cleaned
            # print(extracted_strings_cleaned)

    new_column.append(extracted_strings_cleaned)

df_main["parsed_words"] = new_column
df_main.drop(["Sentence"], axis=1)
# print(df_main)

from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(df_main["parsed_words"], df_main["Type"], test_size=0.20,
                                                    random_state=0)

v = CountVectorizer()

X_train_count = v.fit_transform(X_train)

model = MultinomialNB()
model.fit(X_train_count, Y_train)

X_test_count = v.transform(X_test)

# print(model.score(X_test_count, Y_test))

def user_input(sentence):
    new_x = [sentence]
    new_x_vectorized = v.transform(new_x)
    predict = model.predict(new_x_vectorized)
    return predict

# print(user_input(""))
