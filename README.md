# Snake-Classification-Recognizer
Welcome to Snake Classification & Recognizer

Can classify 13 different types of Snakes around the world
The types are following:

1. Python
2. Rattle
3. Cobra
4. Anaconda
5. Black Mamba
6. King Cobra
7. Coral Snake
8. Water Snake
9. Sea Snake
10. Bushmaster
11. Rat Snake
12. Parot Snake
13. Lora

# Data Preperation

Data collection: downloaded images with each category name using the search_image_ddg() function from the DuckDuckGo search engine.

Data Augmentation: fastai provides default data augmentation which operates in GPU. Details can be found in
'Notebook/Snake_Data_Preperation'

# Data Training & Cleaning
Training: Fine-tuned a resnet34 model for 5 epochs (5 times) respectively and got upto ~80% accuracy.

![Screenshot_5](https://github.com/Somoresh/snake-classification-recognizer/assets/45269154/18979211-a75d-4153-adcf-bb410f56752e)

Data Cleaning: Cleaning snake image data typically involves pre-processing and refining the dataset to ensure that it is suitable for use in machine learning or computer vision applications. 
 Using fastai ImageClassifierCleaner, I updated and cleaned the data. Gather a diverse set of snake images from various sources, ensuring representation of different species, angles, lighting conditions, and backgrounds.

 # Model Deployment
 I utilized the Gradio App to deploy the model. I can not deployment in Huggingface Yet.
 The implementation can be found in Future.
 HuggingFace Spaces [Here](https://huggingface.co/spaces/Somoresh/snake-classification)
 
 ![Screenshot_2](https://github.com/Somoresh/snake-classification-recognizer/assets/45269154/ca95537a-c876-47ef-83a4-cb6153564d07)

 # API embedding with GitHub Pages
 
 I am sorry to say that i could not deploy Gradio App model in HuggingFace
 as a result i failed to API embading with Github Pages.But basic Page is [Here](https://somoresh.github.io/snake-classification-recognizer/)
