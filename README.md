## 🎬 Movie Reviews Sentiment Analysis

### 📌 Aim
The goal of this project is to leverage **Word2Vec** for sentiment analysis on movie reviews. By transforming words into meaningful vector representations, we aim to build a model that can accurately classify sentiments as **positive** or **negative**. 

This project explores:
- 🧠 **Natural Language Processing (NLP)** techniques
- 🔍 **Deep learning-based word embeddings (Word2Vec)**
- 📊 **Sentiment classification using machine learning models**

---

### 📝 Introduction
Sentiment analysis, also known as **opinion mining**, is a key task in **NLP** that involves determining the sentiment expressed in textual data. One major challenge is capturing the contextual meaning of words, especially when dealing with **sarcasm, ambiguity, and complex sentence structures**.

🔹 **Word2Vec**, developed by Google, represents words as dense vectors in a high-dimensional space. These embeddings capture **semantic relationships** between words, helping machine learning models understand text more effectively.

🔹 Unlike traditional **bag-of-words** models, **Word2Vec preserves word meaning and context**, improving sentiment classification performance.

🔹 This project uses the **IMDB movie reviews dataset**, containing both positive and negative reviews. We preprocess the text, train a Word2Vec model, and apply various sentiment classification techniques to analyze the effectiveness of this approach.

📌 **Dataset Link:** [IMDB Movie Reviews](https://www.kaggle.com/competitions/word2vec-nlp-tutorial/data)

---

### 📊 Dataset Columns Explanation
The dataset consists of the following columns:

| Column | Description |
|--------|-------------|
| **id** | Unique identifier for each review |
| **sentiment** | Sentiment label (1 = Positive, 0 = Negative) |
| **review** | Text of the movie review, varying in length and complexity |

This dataset serves as the foundation for training and evaluating our **sentiment analysis model using Word2Vec embeddings**.

---

### ⚡ Models & Accuracy Scores
| Model | Accuracy |
|------------------------------|-----------|
| **Logistic Regression** | **88.70%** ✅ |
| **Bernoulli Naïve Bayes** | 86.10% |
| **Multinomial Naïve Bayes** | 86.10% |
| **Random Forest Classifier** | 85.14% |
| **Gradient Boosting Classifier** | 81.38% |
| **Ada Boost Classifier** | 80.48% |
| **Decision Tree Classifier** | 71.46% ❌ |

✅ **Logistic Regression** achieved the highest accuracy, making it the most suitable model for this task.

---

### 🔎 Conclusion
📌 Based on our sentiment analysis results:
- **Logistic Regression** performed the best, achieving **88.70% accuracy**.
- **Naïve Bayes models** (Bernoulli & Multinomial) followed closely with **86.10% accuracy**.
- **Tree-based models** like **Decision Tree Classifier** performed the worst (**71.46% accuracy**), indicating that they may require further **hyperparameter tuning**.

✨ **Traditional machine learning algorithms such as Logistic Regression and Naïve Bayes, combined with effective text preprocessing and feature extraction techniques (Word2Vec), are well-suited for sentiment classification tasks.**

---

### 🔗 Important Links
📌 **Kaggle Notebook:** [Movie Review Sentiment Analysis](https://www.kaggle.com/code/senasudemir/movie-review-sentiment-analysis?scriptVersionId=222152424)  
📌 **Hugging Face Demo:** [Sentiment Analysis Web App](https://huggingface.co/spaces/Senasu/Movie_Review_Sentiment_Analysis)  
📌 **Dataset:** [IMDB Movie Reviews](https://www.kaggle.com/competitions/word2vec-nlp-tutorial/data)  
