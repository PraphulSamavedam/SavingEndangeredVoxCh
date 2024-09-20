# Saving Endangered Species Using Satellite Images and Vegetation Patterns
This project focuses on collecting information about endangered species from 
IUCN Red List and leveraging satellite images of their habitats to analyze 
vegetation changes over time. The project uses advanced machine learning 
techniques, including Convolutional Neural Networks (CNNs) and Long 
Short-Term Memory (LSTM) models, to calculate the Normalized 
Difference Vegetation Index (NDVI) and predict potential risks of species 
becoming endangered based on vegetation patterns.
 
### Procedure:
- Collect data on endangered species from the IUCN Red List.
- Obtain satellite images of the habitats of these species using geographic 
  coordinates.
- Analyze vegetation changes over time by calculating the NDVI from 
  satellite images.
- Use CNN and LSTM models to predict trends in vegetation health and 
  identify potential risks for species becoming endangered based on the patterns found.
- Provide actionable insights for conservation efforts.
 
### Data Sources
- IUCN Red List: Information on endangered species (https://www.iucnredlist.
  org)
- Satellite Images: Acquired from sources like NASA's Earth Observing System 
  Data and Information System (EOSDIS) or Google Earth Engine.
- NDVI Calculation: NDVI is computed from satellite images using spectral 
  bands in the red and near-infrared regions.
 
### Technologies:
- Python: The primary language used for data processing, model building, and 
visualization.
- TensorFlow / Keras: For building and training CNN and LSTM models.
- OpenCV: For image processing and NDVI calculation.
- NumPy and Pandas: For data manipulation.
- Geopandas: For handling geographic data.
- Google Earth Engine API: For satellite image retrieval and processing.
- Matplotlib / Seaborn: For data visualization.
 
### Usage:
- Collect IUCN Red List Data: Use the IUCN API to gather information about 
  endangered species, including their geographic location.
- Satellite Image Retrieval: Input the species’ location coordinates to 
  fetch satellite images of the region.
- NDVI Calculation: Using the satellite images, calculate NDVI to measure 
  vegetation health over time.

### Model Training:
 
Train the CNN model to process satellite image data and detect patterns in vegetation changes.
Use LSTM for time-series analysis to predict future changes in the environment.
Prediction:
 
Run predictions on the model to assess the risk of species becoming endangered based on the environmental changes observed.
Visualization:
 
Visualize the results, including NDVI trends and species risk analysis.

### Model Description
CNN: A Convolutional Neural Network is used for image processing and feature extraction from the satellite images. It helps detect patterns in vegetation changes (e.g., deforestation or degradation of habitats).

LSTM: The LSTM network processes the time-series data related to vegetation health and NDVI to predict future environmental conditions. This is critical for identifying trends that might lead to a species' habitat becoming less suitable for survival.
 
NDVI Calculation:

NDVI = NDVI=(NIR+Red)/(NIR−Red)​ 
Where:
NIR represents the near-infrared light reflected by the vegetation.
Red represents the red light absorbed by the vegetation.


Results
The key outcomes of this project include:
 
Historical NDVI data trends for the species’ habitats.
Predictions about future vegetation changes and potential threats to the species' environment.
Insights into which species might be at risk of becoming endangered based on habitat degradation.
 

### Contributors:
- Sanjay Prabhakar
- Venkatesh Shivandi
- Manikhanta Praphul Samavedam
- Gowreesh Gunupati

# Hackathon Prompt: Design Visual AI for addressing Nature imbalance.
Ideas showcased:
- Endangered species

Judging critera:
- Clear Vision: Idea is well informed, edge cases have been considered and 
  its benefits are clear, the project is well communicated to judges.
- Createive
- Code: Code must be well maintained.

Teams will have to present
- Present their projects to the judges (5 mins)
- Create slides that explains the inspiration or importance of the project 
  (4-6 slides)
- 
