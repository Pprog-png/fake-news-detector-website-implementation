from flask import Flask, render_template,request
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import re
import string
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

import search
import webbrowser

print("Training the model...")

def cleaning(text):
    text = text.lower()
    text = re.sub(r'\[.*?\]', '', text)
    text = re.sub(r"\\W"," ",text) 
    text = re.sub(r'https?://\S+|www\.\S+', '', text)
    text = re.sub(r'<.*?>+', '', text)
    text = re.sub(r'[%s]' % re.escape(string.punctuation), '', text)
    text = re.sub(r'\n', '', text)
    text = re.sub(r'\w*\d\w*', '', text)    
    return text

df=pd.read_csv("FakeNewsTrainingSetUpdated.csv")
print("Training the model...")


df["text"] = df["text"].apply(cleaning)
x = df["text"]
y = df["class"]
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.25)
print("Training the model...")

vectorization = TfidfVectorizer()
xt_train = vectorization.fit_transform(x_train)
xt_test = vectorization.transform(x_test)
print("Training the model...")

classifier = LogisticRegression()
classifier.fit(xt_train,y_train)
print("Training the model...")

def testing(data):
    testing_news = {"text":[data]}
    new_def_test = pd.DataFrame(testing_news)
    new_def_test["text"] = new_def_test["text"].apply(cleaning) 
    new_x_test = new_def_test["text"]
    new_xv_test = vectorization.transform(new_x_test)
    pred = classifier.predict(new_xv_test)
    return pred

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return render_template('index.html')

@app.route('/credits')
def credits():
    return render_template("credits.html")


@app.route("/api",methods=["GET"])
def get_delay():
    data=request.args['data']
    query = testing(data)

    stop = stopwords.words('english')
    words = word_tokenize(data)
    words = [w for w in words if w not in stop]
    q = ''
    for i in words:
        q +=i+" "
    s = search.searchnet(q)
    #s = [{'title': "India's Modi starts Washington visit to build Biden, US ties | Reuters", 'snippet': 'Jun 21, 2023 ... U.S. President Joe Biden and Indian Prime Minister Narendra Modi are expected to deepen defense and technology cooperation between their\xa0...', 'link': 'https://www.reuters.com/world/biden-will-not-lecture-modi-human-rights-white-house-says-2023-06-21/'}, {'title': 'Department Press Briefing – April 8, 2024', 'snippet': 'Apr 3, 2024 ... ... Prime Minister Netanyahu to open Rafah to allow humanitarian assistance to get ... QUESTION: So recently Prime Minister Modi has visited the\xa0...', 'link': 'https://www.state.gov/?post_type=state_briefing&%3Bp=92333'}, {'title': "Biden defends calling China's Xi a 'dictator' | PBS NewsHour", 'snippet': "Jun 22, 2023 ... U.S. President Joe Biden and India's Prime Minister Narendra Modi hold joint press conference at the. By —. Ellen Knickmeyer, Associated Press\xa0...", 'link': 'https://www.pbs.org/newshour/world/biden-defends-calling-chinas-xi-a-dictator'}, {'title': 'This Alien Legacy: The Origins of "Sodomy" Laws in British ...', 'snippet': 'Dec 17, 2008 ... [178] Human Rights Watch, "Letter to Indian Prime Minister Singh on the Arrest of Four Men on Charges of Homosexual Conduct in Lucknow," January\xa0...', 'link': 'https://www.hrw.org/report/2008/12/17/alien-legacy/origins-sodomy-laws-british-colonialism'}, {'title': "Japan's new first lady was abducted by aliens, knew Tom Cruise in ...", 'snippet': "Sep 3, 2009 ... ... Prime Minister-elect, Yukio Hatoyama, is a lifestyle ... ... “I believe he'd get ... Is India Really the Next China? 3. Modi's Messenger to the\xa0...", 'link': 'https://foreignpolicy.com/2009/09/03/japans-new-first-lady-was-abducted-by-aliens-knew-tom-cruise-in-former-life/'}, {'title': 'U.S. Citizen Services - U.S. Embassy & Consulates in India', 'snippet': "International Parental Child Abduction ... Biden, Jr.'s Meeting with Prime Minister Narendra Modi and President Joko Widodo ... Ministry of Home Affairs - Indian\xa0...", 'link': 'https://in.usembassy.gov/u-s-citizen-services/'}, {'title': 'A Brief History of UFOs in Japan – The Diplomat', 'snippet': 'Jul 3, 2021 ... ... UFOs, to the administration of then Prime Minister Fukuda Yasuo. ... abducted by a triangular-shaped UFO.', 'link': 'https://thediplomat.com/2021/07/a-brief-history-of-ufos-in-japan/'}, {'title': 'Anand Ranganathan (@ARanganathan72) / X', 'snippet': 'Tamil Nadu is the new Bengal where, while in 2014 the BJP got 2 seats, 5 years later it got 18. Modi has sensed this like a cat. Predictably there is a flutter\xa0...', 'link': 'https://twitter.com/ARanganathan72'}, {'title': 'China Says Giant Telescope May Have Detected Signals From Alien ...', 'snippet': "Jun 14, 2022 ... The Pro Golf Drama Is Back. by Alan Shipnuck. India Prime Minister Narendra Modi Campaign Event. Why India's South Rejects Modi — And Why It\xa0...", 'link': 'https://www.bloomberg.com/news/articles/2022-06-15/china-says-it-may-have-detected-signals-from-alien-civilizations'}, {'title': 'Narendra Modi, a man with a massacre on his hands, is not the ...', 'snippet': "Apr 7, 2014 ... Aditya Chakrabortty: It looks likely that Modi will be India's next prime minister. But his apologists can't dismiss the facts about his\xa0...", 'link': 'https://www.theguardian.com/commentisfree/2014/apr/07/narendra-modi-massacre-next-prime-minister-india'}]

    return {"data":str(query),"search":{"s":s}}



if __name__ == '__main__':
    webbrowser.open('http://127.0.0.1:8080/home', new = 0, autoraise = True)
    app.run(port=8080, debug=False)
