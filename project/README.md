# Depression Severity and Factor Analysis Using Reported Health Data with Machine Learning Models

## Description
This project covers a report which analyses the correlations between depression metric by using various machine learning models and reported health data (PHQ-9 survey, fitbit, socio-demographic information).<br><br>

## Abstract
Depression is a significant global health concern, as it impacts individuals’ daily lives and productivity. Challenges remain unexplored and unresolved, with a concerning factor that certain types of depression have little to no treatment [5], and it sometimes even remains undetected [8]. However, recent studies have demonstrated the potential of leveraging wearable device data, patient-generated health metrics and socio-demographic information into this complex health disorder [2] [3] [4].<br>
Specifically, current research highlighted various factors, for example, a study done in Sweden found that socio-economic conditions, such as unemployment, economic hardships, as well as lifestyle factors (physical activity, alcohol consumption) contribute to mental health issues, and that young people more commonly have them. [2].  Digital engagement has also become a crucial aspect of mental health, with individuals suffering from mental health issues often turning to social media for support and information, particularly younger, lower-income women with chronic health challenges [3].<br>
This study aims to address the gap in knowledge and investigate hypotheses by employing machine learning models to predict depression severity while exploring key contributing factors.  Particularly, Support Vector Machines have shown promise in handling depression related predictions [4], and thus have been used in this project, with various kernel methods and optimization techniques, utilizing feature selection by PCA.<br>
The question of this research is, what factors influence depression, and how accurately can the severity of the mood disorder be predicted using machine learning models?<br>
Preliminary findings reveal correlations between depression severity and factors such as physical activity, sleep hygiene and comorbid health conditions. The optimized model used for the prediction achieved a high R² score of 0.94, and a low Mean Squared Error of 2.1. These results are consistent with existing literature, demonstrating the potential of integrating wearable technology and machine learning research.<br>


<br>
Download the dataset form [Zenodo](https://zenodo.org/records/5085146) and place it in the same directory as the main ipynb file. <br>
Keep in mind that this has packages installed by Jupyter Notebook in standard, and the requirements are related to Jupyter Notebook itself.<br>

## Project Structure
The project consists of the following files:

```depressionanalysis.ipynb: Jupyter notebook containing the code for analysis.
requirements.txt: List of Python libraries required for the project.
Depression Severity and Factor Analysis Using Reported Health Data with Machine Learning Models.pdf: Complete study report.
```

## How to Run
### 1. Clone this repository or download the project files.
### 2. Install the required Python libraries by downloading the following requirements:

Python version 3.0 and above<br>
Libraries such as NumPy, Pandas, Matplotlib, Seaborn, Scikit-Learn<br>
To install these directories use this command:<br>
``` 
pip install -r requirements.txt 
```


### 3. Download the dataset from Zenodo and place it in the same folder as the notebook file.
### 4. Open the Jupyter notebook (notebook.ipynb) and run each cell in order to perform the analysis.
