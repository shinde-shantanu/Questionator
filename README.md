# QuestionatorMvision

This is the main repository for the questionator. In this you will come across a number of folders. So lets look at each folder modularly.
Every folder has it's own readme to install the respective API. In order to install all the below mentioned four api do the following steps:-

1. Install virtualenv.
2. Create a separate python environment for all the api so that there is no dependencies later on.
3. Run each api in different screen on the AWS Instance. 

## 1. ImagesAnalysisInTheEntertainmentDomain

This is the face recognition api code base. This module is responsible for the caption generation. 

## 2. ImageAnalysisInTheSportsDomain

This is the face recognition api section. This module does the task of recognising the face of the sportsperson and return the classification from set of trained people. As usual the module contains All the steps to run the module.
## 3. TextAnalysisInSportsDomain

This is the question Generation module. This module is responsible for generating question from text. The steps will be provided in the readme.

## 4. optionGeneration

This is the option generation module. As usual you just need to check the readme file.

## Website
After running all the above four api on the respective AWS instance, we can now move onto the Front-End.
The entire frontend is contained in the website folder. There is no specific installation required for this, only XAMP server needs to started, after this you just need to put this folder in the htdocs of the xamp folder
In place of 4430, please input the port number of your XAMP server. Default value - 8000

For example, 
### http://localhost:4430/myra/HTML/home.php


All the remaining folder have a particular task and work which was deemed superflous for website and questionator in General. Those modules are :-

## 1. DataAnalyticsUsingMachineLearning

This module uses tf-idf to cluster the news article. As of now, it is not necessary for the utilization.

## 2. GamingPlatformWithRealTimePlayerCapacity

This was a telegram chatbot, but because we never could truly grasp on how to use it, we switched to the web platform.

## 3.TextAnalysisInTheEntertainmentDomain

This utilizes a completely different platfom from the current api. Can be utilised as an alternative if the current question Generation feels insufficient.
