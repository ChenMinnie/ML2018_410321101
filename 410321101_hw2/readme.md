# Assignment 2 report
## Handwritten Character Recognition
### Downloading Dataset
![downloading dataset](https://user-images.githubusercontent.com/32957934/42211793-f9c8bcd6-7ee6-11e8-9e26-b57ef4db6bca.jpg)
### Preprocessing Character Images
#### The size normalization
![normalization](https://user-images.githubusercontent.com/32957934/42211831-15883906-7ee7-11e8-9db6-c004b2a091d5.JPG)
### Reducing Dimension 
#### Principal Component Analysis (PCA)
![pca](https://user-images.githubusercontent.com/32957934/42212117-cfb22346-7ee7-11e8-9e3c-2da236280065.JPG)
#### Fisher Linear Discriminant Analysis (LDA)
![lda](https://user-images.githubusercontent.com/32957934/42212364-7620afd6-7ee8-11e8-9492-97a4c552404a.JPG)
#### TruncatedSVD
![svd](https://user-images.githubusercontent.com/32957934/42212281-3aa42b4a-7ee8-11e8-956b-785f450c531b.JPG)
### Chosssing a Classifier and Training It
#### Logistic Classifier
![log](https://user-images.githubusercontent.com/32957934/42255448-680dd66c-7f7e-11e8-9c13-7c6077fa54d7.JPG)
#### Decision Tree Classifier
![tree](https://user-images.githubusercontent.com/32957934/42255457-7255c044-7f7e-11e8-8477-bf3b3f9ff692.JPG)
#### Support Vector Classification (SVC)
![svc](https://user-images.githubusercontent.com/32957934/42255464-7874506c-7f7e-11e8-9bb2-29119e43ee7b.JPG)
#### Multi-layer Perceptron Classifier (MLP)
![mlp](https://user-images.githubusercontent.com/32957934/42255472-83a3b2b6-7f7e-11e8-961e-fc66ff0cd5c2.JPG)

### Demonstrate The Results

#### PCA
##### Logistic Classifier
>![log](https://user-images.githubusercontent.com/32957934/42255740-d76a520a-7f7f-11e8-868e-540b36f926dc.JPG)
##### Decision Tree Classifier
>![tree](https://user-images.githubusercontent.com/32957934/42255741-d7a649ae-7f7f-11e8-83cd-40729d81db4b.JPG)
##### SVC
>![svc](https://user-images.githubusercontent.com/32957934/42255896-b59ead3c-7f80-11e8-89b0-f183577d883c.JPG)
##### MLP
>![mlp](https://user-images.githubusercontent.com/32957934/42255743-d7ff7ae2-7f7f-11e8-846c-e77d09c33209.JPG)

#### PCA + LDA
##### Logistic Classifier
>![log](https://user-images.githubusercontent.com/32957934/42255597-14069f9e-7f7f-11e8-89c9-41b6f780c623.JPG)
##### Decision Tree Classifier
>![tree](https://user-images.githubusercontent.com/32957934/42255598-14304bd2-7f7f-11e8-907f-3870d3857b11.JPG)
##### SVC
>![svc](https://user-images.githubusercontent.com/32957934/42255599-14598826-7f7f-11e8-8212-0ab6b6322926.JPG)
##### MLP
>![mlp](https://user-images.githubusercontent.com/32957934/42255600-14804308-7f7f-11e8-9a0f-1948d1ac84cb.JPG)

#### TruncatedSVD
##### Logistic Classifier
>![log](https://user-images.githubusercontent.com/32957934/42256011-49027fd6-7f81-11e8-8973-32c0d6f89ee6.JPG)
##### Decision Tree Classifier
>![tree](https://user-images.githubusercontent.com/32957934/42256012-492e460c-7f81-11e8-8a57-7bb7f4488c45.JPG)
##### SVC
>![svc](https://user-images.githubusercontent.com/32957934/42256013-4970c644-7f81-11e8-94ec-eb0774ff05db.JPG)
##### MLP
>![mlp](https://user-images.githubusercontent.com/32957934/42256014-49980c5e-7f81-11e8-9078-121c835ebb92.JPG)



### Discussions

#### Accuracy Of Classifier
|Classifier \ Reducing Dimension| PCA |  PCA + LDA | TruncatedSVD |
|:-----------------------------:|:---------:|:--------:|:--------:|
|           Logistic            | 0.8766457 | 0.876743 | 0.876971 |
|         Decision Tree         | 0.8480000 | 0.847943 | 0.845886 |
|             SVC               | 0.9836000 | 0.983657 | 0.983200 |
|             MLP (取20筆)      | 0.976343  | 0.976229 | 0.975486 |
>##### 1. Reducing Dimension 三種方法整體效果 : PCA + LDA > PCA > TruncatedSVD
>##### 2. Classifier 四種方法整體效果 : SVC > MLP > Logistic > Decision Tree

### What I Have Learned
>#### 1. Preprocessing Character Images :
>##### 一開始要下載圖片時，無法讀取圖片檔的情形。遇到 HTTP Error 500,後來直接下載檔案，將檔案放入資料夾解決問題。
>#### 2. Reducing Dimension
>##### 一直遇到Memory Error 。查資料發現TruncatedSVD方法不會造成Memory Error。至於PCA，PCA(n_components= 30,copy = False)，n_components不能太小，且 copy = False 可解決。n_components 愈小 Accuracy Of Classifier 愈不佳。

