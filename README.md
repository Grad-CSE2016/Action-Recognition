# Action-Recognition

##Action Recognition on KTH Dataset.

1. I used the STIP Binaries found at [here] (https://www.di.ens.fr/~laptev/download.html#stip) , to extract the STIPs with the HOG-HOF descriptors.
2. The descriptors extracted are then clustered -using k-means with N cluster- in order to form a visual codebook with N words.
3. A Bag of words is then constructed for each example (video sequence)  based on the occurrences of the codewords in the given example.
4. The examples (N+1-vector-BoW+Label) are then classified using Multi-Class non-Linear SVM.

<img src="/images/pipeline.png" width="400" height"200"><img src="/images/svm.png" width="400" height="300">

###Results :

I used RBF kernel for the SVM, SVM params: [gamma = 0.0002, C = 2]

          Settings           |    HoF with 1000 cluster     |  HoG/HoF with 3000 cluster    |   HoG/HoF with 4000 cluster   |
| ---------------------------|:----------------------------:| :----------------------------:|:-----------------------------:|
|         Accuracy           |             88.98%           |             <b>90.07%</b>     |              83.89%           |

<b>Note:</b> [Hof with 1000 clusters] was by far the fastet, it acheived 500% gain in performance in comparison with [HoG/HoF with 3000 clusters]
####Confusion Matrix of HoG/HoF with 3000 clusters
<img src="/images/confustion-Matrix.png" width="500" height="500" align="center">



##References 
* On Space-Time Interest Points. [Ivan Laptev ,2004] [[PDF](www.irisa.fr/vista/Papers/2003_iccv_laptev.pdf)]
* Evaluation of local descriptors for action recognition in videos. [Piotr Bilinski and Francois Bremond .2009] [[PDF](www.irisa.fr/vista/Papers/2009_bmvc_wang.pdf)]
* My Bachelor's thesis "Smart Airport Surveillance System" [[PDF](https://www.researchgate.net/publication/308903971_Smart_Airport_Surveillance_System_Action_Recognition_Unattended_Object_Detection_Tracking)]


