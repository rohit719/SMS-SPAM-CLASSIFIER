# SMS-SPAM-CLASSIFIER

The aim of this project is to create an app which could classify any given message as whether its a SPAM or not.

## What is a SPAM?

Irrelevant or unsolicited messages sent over the Internet, typically to a large number of users, for the purposes of advertising, phishing, spreading malware, etc.

## Challenges of spamming 

- It consumes Internet resources.  A deluge of spam will clog mail servers, making all email slow and burdening the ISP.
- It reduces the effectiveness of legitimate advertising.
- It raises costs for everyone who uses the Internet.
- It exposes children to inappropriate material.
- It wastes people's time.  This costs the world economy billions of dollars per year in lost productivity.
- It threatens the very utility of email as a form of communication

### Using a good Spam filter can help you deal with challenges of spamming & that is the aim of this project.

## STEPS IN DEVELOPMENT OF THIS PROJECT :-

- The dataset for this project was taken from UCI ML repository. Size of dataset is 5572*2.
- Performed Data preprocessing & Data cleaning on the dataset.
- Performed Text preprocessing (**Stemming & lemmatization**).
- Applied NLP technique **Bag of words** on stemmed & lemmatized data individually.
- Applied NLP technique **TF-IDF** on stemmed & lemmatized data individually.
- Converted the labelled categorical dependent variable into dummy variable to apply ML algorithm. 
- Used NaiveBayes classifier model & trained the model using the datasets created using NLP techniques. 
  - Accuracy achieved using Bag of words technique on stemmed data is **98.56%**.
  - Accuracy achieved using Bag of words technique on lemmatized data is **98.29%**.
  - Accuracy achieved using TF-IDF technique on stemmed data is **97.93%**.
  - Accuracy achieved using TF-IDF technique on lemmatized data is **97.93%**. 
  
  (the accuracy for tfidf model for stemmed & lemmatized data is same but confusion matrix was different)

- Created a pickle file for model with highest accuracy i.e. Bag of words technique on stemmed data (98.56%).
- Build Graphically user interactive front end web pages.
- Used **Flask** web framework to generate the web app using pickle file and front end web pages.
- Deployed the web app on **Heroku** platform.

## Deployed Model link - https://spam-identifier.herokuapp.com/

### Instructions to use deployed model :-

- Enter the message in the empty box.
- Click on predict.
- Result will be displayed on your screen.
