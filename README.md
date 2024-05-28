# LSTM Weather Prediction

This project implements a Long Short-Term Memory (LSTM) neural network model for weather prediction using historical weather data. The model is trained to predict future weather conditions based on past observations.

## Overview

The project consists of the following main components:

1. **Data Preprocessing**: The provided historical weather data is preprocessed to prepare it for training the LSTM model. This includes data cleaning, normalization, and sequence splitting.

2. **Model Training**: An LSTM model is built and trained using the preprocessed data. The model is trained to predict future weather conditions based on a sequence of past observations.

3. **Prediction and Visualization**: The trained model is used to generate predictions for future weather conditions. These predictions are visualized using GeoPandas and Plotly to create choropleth maps showing predicted and actual weather values.

## Files

- **DataPreprocessing.ipynb**: Jupyter Notebook containing code for data preprocessing.
- **ModelTraining.ipynb**: Jupyter Notebook containing code for building and training the LSTM model.
- **PlotResults.ipynb**: Jupyter Notebook containing code for visualizing predicted and actual weather values.
- **requirements.txt**: Text file listing all dependencies required to run the project.

## Usage

1. Install the required dependencies listed in `requirements.txt`.
    ```
    pip install -r requirements.txt
    ```

2. Run the `DataPreprocessing.ipynb` notebook to preprocess the data.
3. Run the `ModelTraining.ipynb` notebook to train the LSTM model.
4. Run the `PlotResults.ipynb` notebook to visualize the predicted and actual weather values.

## Dependencies

- numpy
- pandas
- geopandas
- plotly
- matplotlib
- scikit-learn
- tensorflow
- tqdm

