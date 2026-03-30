# f1-race-winner-prediction
#  F1 Finish Position Prediction using Machine Learning

##  Overview

This project focuses on predicting the finishing position of Formula 1 drivers using Machine Learning techniques. By analyzing race-related features such as qualifying position, grid penalties, driver identity, constructor team, and circuit performance, the model attempts to estimate how a driver will perform in a race.

The project demonstrates the application of classification algorithms in a real-world sports analytics scenario and highlights how data-driven decision-making can be used in motorsports.

---

##  Problem Statement

Predicting race outcomes in Formula 1 is challenging due to multiple influencing factors such as driver skill, car performance, and race conditions. This project aims to build a predictive model that can estimate a driver's finishing position based on key pre-race inputs.

---

##  Solution Approach

* Data is collected and structured into a dataset
* Categorical variables (driver, constructor) are converted using one-hot encoding
* The dataset is split into training and testing sets
* A **Random Forest Classifier** is used to train the model
* The model is evaluated using accuracy score
* Predictions are made for new race scenarios


---

##  Example Output

```id="q1mx9p"
Accuracy: 0.83
Predicted Finish Position: 1
```

* **Accuracy** indicates how well the model performs
* **Predicted Finish Position** shows expected race outcome

---

## 🧠 Features Used

* Qualifying Position
* Grid Penalty
* Circuit Performance
* Driver (encoded)
* Constructor Team (encoded)

---

## 📁 Project Structure

```id="gk0t9m"
f1-finish-position-prediction/
│── main.py
│── README.md
│── requirements.txt
│── data/
```

---

##  Future Improvements

* Use larger real-world datasets (multiple seasons)
* Include weather conditions and tire strategies
* Apply advanced models like XGBoost
* Improve evaluation metrics beyond accuracy
* Build a web interface using Streamlit or Flask

---

##  Limitations

* Small dataset reduces model reliability
* Does not account for dynamic race conditions
* Predictions are simplified and not fully realistic

---

##  Technologies Used

* Python
* Pandas
* Scikit-learn
* Matplotlib

---

##  Learning Outcomes

* Understanding of classification models
* Hands-on experience with Random Forest
* Data preprocessing and feature engineering
* Model evaluation techniques

---

##  Author

Shreya Srivastava

This project was developed as part of an academic assignment to explore the application of Machine Learning in real-world problem-solving.
