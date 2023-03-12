# MedEn-Medical-Search-Engine
 
![image](https://user-images.githubusercontent.com/30213777/224561752-8d38d1a5-4a45-4c01-91de-2bf366b146cb.png)

We've all probably wondered why when we search for a specific term on Google, it doesn't simply return results that also contain that word, but also results that are 
really closely linked to it. For instance, searching Google for the term "medicine" returns results that include the word "medicine" as well as terms such as "health," 
"pharmacy," and "WHO." Google therefore recognizes that these phrases are connected in some way. Word embeddings have a role in this situation. Word 
embeddings are numerical representations of the words in a phrase that vary based on context. In this project, we have utilized word embeddings to develop a clever 
search engine, specifically for medical science. The project is executed or deployed using multiple services on Azure. We have also created a Docker image for our 
application.

## Technology Stack
• Language: Python\
• Packages: NLTK, Scikit-Learn, Pandas, Numpy, Streamlit\
• Cloud: Azure App Services, Azure Data Factory, Azure Blob Storage, Azure Databricks, Azure Web Apps\
• Code Management: Git, Github, Docker

## Project Flowchart
This project consist of 3 important layers which is explained in the diagram below:
### Data Layer
The data layer is the primary layer where we performed all the basic data preprocessing steps on the data that we obtain from the Azure Blob storage 
and again store the cleaned data to Azure Blob storage as a different file.

### Training Layer
The training layer is the intermediary layer which involves the crucial step of model building. The model was trained using Azure Databricks and the generated 
model object was stored back to Azure Blob Storage. A trigger was set to the model training process, to train the model periodically when new data was
obtained.

### Application Layer
This layer involved building a user interface using Streamlit to the model built, so that the users can interact with our model object. The user application was then 
deployed to the cloud using Azure App Services.

![image](https://user-images.githubusercontent.com/30213777/224562353-00dd77bd-339d-4481-a6a9-00c44f5a007b.png)

## Cloud Service Architecture
![image](https://user-images.githubusercontent.com/30213777/224563164-77dbfbbf-842a-4328-ba8e-4521638ea720.png)

Firstly, we created “IST615Project” as a resource group in Azure. In that resource group, we invoked “Azure Blob Storage” service that stores our data.\
• “Azure Databricks” service is used as a resource where all the Python scripts are mounted and run.\
• One of the python scripts, “authenticate.py” contains the code that connects and integrates the Azure Blob Storage and Azure Databricks service.\
• “Azure Data Factory” resources is leveraged to generate a “training” pipeline that trains the model.\
• The trained model is then stored in Azure Blob Storage.\
• We have integrated all our python scripts (stored in Databricks) with our Git Repository.\
• This integration with Git helps in verison controlling of our code.\
• Then, we created a “Docker Image” of the entire application which is then published into “Docker Hub”.\
• Lastly, “Web App” service is created that runs the docker file and displays the User Interface (UI) of our project.

## References

1. https://learn.microsoft.com/en-us/azure/data-factory/
2. https://learn.microsoft.com/en-us/azure/storage/blobs/
3. https://learn.microsoft.com/en-us/azure/databricks/
4. https://www.analyticsvidhya.com/blog/2021/06/text-preprocessing-in-nlp-with-python-codes/
5. https://stackoverflow.com/questions/21979970/how-to-use-word2vec-to-calculate-the-similarity-distance-by-giving-2-word




