# Assignment 1 report
## Image Decryption by a Single-Layer Neual Network
### Introduce image
#### Image Key1(K1)
![key1](https://user-images.githubusercontent.com/32957934/39427925-2c2ecd8e-4cb8-11e8-837b-832ade7d42ca.png)
#### Image Key2(K2)
![key2](https://user-images.githubusercontent.com/32957934/39427926-2c64d9c4-4cb8-11e8-9767-11a4bcc156ee.png)
#### Input Image to be encrypted(I)
![i](https://user-images.githubusercontent.com/32957934/39427924-2c002d76-4cb8-11e8-8883-ad1d9b7ea669.png)
#### The encrypted Image(E)
![e](https://user-images.githubusercontent.com/32957934/39427922-2b9e33b4-4cb8-11e8-9e1c-eb321260af9b.png)
#### Another encrypted Image(E')
![eprime](https://user-images.githubusercontent.com/32957934/39427923-2bd31fc0-4cb8-11e8-9169-3555c8881dce.png)
### Flowchart Of Program
#### Step1:
![3](https://user-images.githubusercontent.com/32957934/39430745-4461e464-4cc1-11e8-9415-a3cb37a573e1.jpg)
#### Step2:
![4](https://user-images.githubusercontent.com/32957934/39430746-448a683a-4cc1-11e8-9192-7a535cc8cc60.jpg)
### The Way To Set Up And Run Program
>#### 1.讀取Image K1,K2,E,I
>#### 2.代入下方公式
>#### ![1](https://user-images.githubusercontent.com/32957934/39430927-cc432974-4cc1-11e8-8163-6c1a96dff105.JPG)
>#### 3.解出w =[w1,w2,w3]
>#### 4.讀取 Image E'
>#### 5.代入下方公式解出 I'
>#### ![2](https://user-images.githubusercontent.com/32957934/39430928-cc6b20fa-4cc1-11e8-9ba4-2a9b6b1e172d.JPG)
### Demonstrate The Results
#### 1. w = [w1,w2,w3]
##### w =[0.24997882,0.66077444,0.08950885]
#### 2. The decrypted Image(I')
![decryption](https://user-images.githubusercontent.com/32957934/39427921-2b6d15ea-4cb8-11e8-9406-75113f77e88d.jpg)
### Discussions
>#### 1.使用opencv顯示圖片，一開始發生圖片白色處有黑點。造成此現象原因是overflow，最後經過調整解決此問題。
>#### 2.下方虛擬碼 α 值代 0.00001。
>#### 3.下方虛擬碼 MaxlterLimit 值代 2，實驗過當值為 5 和 10 其 w 值並未改變。
>![5](https://user-images.githubusercontent.com/32957934/39431683-0b9b68c8-4cc4-11e8-85a3-e0b0fd8a2da8.JPG)
### What I Have Learned
>#### 1.How to use python.
>#### 2.Image Decryption by a Single-Layer Neual Network.

