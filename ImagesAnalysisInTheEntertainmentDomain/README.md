version https://git-lfs.github.com/spec/v1
oid sha256:96c673bc0a23c72f08ea4e43a03c2ba3d024fc460de5aabe0d5e324a97f01d40
size 1447

1. Author Name: Animesh
2. Version No. 1.0
3. Research Title:ImageAnalysisInEntertainmentDomain
4. Features :


EVERYTHING HAS BEEN RUN ON PYHTON 2.7
//Crawlers
1)The python script crawl.py calls an API from news.org to generate a JSON file for scraped images in the sports domain for football and the python file crawl1.py for cricket.

2)An API called post.py in the same folder is used to call both the funtions .
To get the o/p ,run the post.py file ,open postman change get to post and put the localhost address.
Then hit SEND and the JSON obj o/p is produced.

3)However,since we are using the free version of the API ,we are restricted to only 100 images and the 'content' tag for an image in the JSON file contains only 260 charecters.

4)Additional charecters will be represented as [+x ]charecters. 


//IMAGE CAPTIONING

1)The python file called sample.py will be found in questionatormvision/ImagesAnalysisInTheEntertainmentDomain/image_captioning

2)The API for captioning called api.py is also present in the same folder as sample.py which has to be run.

3)After running the API,open postman ,change GET to POST,insert the URL of an image in the body and the o/p i.e the caption for the image should be produced.


ALL PYHTON PACKAGES FOR RUNNING(ON LINUX) CAN BE INSTALLED USING : pip install packagename
GITHUB LINK FOR THE PROJECT:
https://github.com/yunjey/pytorch-tutorial/tree/master/tutorials/03-advanced/image_captionin
