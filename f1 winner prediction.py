import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

data = {
    'driver': ['Verstappen', 'Hamilton', 'Leclerc', 'Norris', 'Perez', 'Sainz'],
    'constructor': ['Red Bull', 'Mercedes', 'Ferrari', 'McLaren', 'Red Bull', 'Ferrari'],
    'qualifying_position': [1, 2, 3, 4, 5, 6],
    'grid_penalty': [0, 0, 0, 0, 5, 0],
    'circuit_performance': [9, 8, 7, 7, 8, 7],
    'finish_position': [1, 2, 3, 4, 5, 6]   
}

df = pd.DataFrame(data)

df = pd.get_dummies(df, columns=['driver', 'constructor'])

# Features (X) and Target (y)
X = df.drop('finish_position', axis=1)
y = df['finish_position']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)


model = RandomForestClassifier(n_estimators=100)
model.fit(X_train, y_train)


y_pred = model.predict(X_test)

print("Accuracy:", accuracy_score(y_test, y_pred))

# Create a new DataFrame for prediction with all required columns, initialized to 0
new_race = pd.DataFrame(0, index=[0], columns=X_train.columns)

# Fill in the specific values for the new race scenario
new_race['qualifying_position'] = 1
new_race['grid_penalty'] = 0
new_race['circuit_performance'] = 9
new_race['driver_Verstappen'] = 1
new_race['constructor_Red Bull'] = 1

prediction = model.predict(new_race)

print("Predicted Finish Position:", prediction[0])
