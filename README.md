[README.md](https://github.com/el-kh/Online-Payments-Fraud-Detection-mini-project/files/12329687/README.md)


# Online Payments Fraud Detection

This project uses machine learning to predict and detect internet fraud.



How to Run and Test the Project

    Visualizing Data: As you run the code, you'll observe a pie chart displaying the distribution of transaction types in the dataset. This visualization offers an initial insight into the data's composition.

    Preprocessing Data: The code takes care of data preprocessing by removing irrelevant columns and applying one-hot encoding to categorical variables.

    Training the Model: A Decision Tree classifier model is trained using the preprocessed dataset.

    Example Testing: The trained model is then put to the test with a provided example transaction. The model predicts whether the transaction is fraudulent or legitimate.

    Model Evaluation: The code calculates and prints the model's accuracy on the test dataset, showcasing its performance.

Libraries and Functions Used

    Pandas: Used for data manipulation and analysis.
    Plotly Express: Applied for data visualization, particularly in generating a pie chart. Used function: pie()
    Scikit-learn: Employed for various machine learning tasks, such as model training and predicting. Used: train_test_split(), DecisionTreeClassifier, model.score(), model.predict()

Output Examples

    Data Visualization:
        The pie chart visually represents the distribution of transaction types, offering insights into the data's nature.

    Example Testing:
        The provided example transaction is subjected to the trained model, resulting in a prediction of whether the transaction is fraudulent or not.

    Model Evaluation:
        The code prints the model's accuracy on the test dataset, helping gauge its effectiveness.

Model Results

    Accuracy: The Decision Tree classifier model's accuracy is calculated and printed in the output. Result is 0.9997210268725777

    Prediction: The provided example transaction's predicted status (fraudulent or not) is revealed in the output. Result is 'Fraudulent'
