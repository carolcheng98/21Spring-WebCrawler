<Center><h3>Topic Modeling and Sentimental Analysis of Alzheimer's Caregivers on Online Forums</h3>
  <strong>Progress Report</strong>
<br>CS 3891 <br>Carol (Kerou) Cheng</Center>

### Progress

- **Dataset**: the data was scraped from alzconnected.org and reddit. Up until now, we have only explore the initial posts on the forums. The documents were the <u>content</u> of the posts, and the metadata was the <u>source</u> (reddit/alzconnected) of the posts, and the <u>date</u> of the posts.

  - Reddit data: contains initial posts in the dementia and Alzheimer's subreddits
    - size: 9,069 observations
  - Alzconnected data: contains initial posts in the caregiver forum on Alizconnected.org
    - size: 33,132 observations

- **Models**: we explored the data primarily using the `stm` package with R, which is a tool to perform structural topic modeling. 

  - After cleaning the data, we first did a search on the number of topics K with the `searchK()` function.
    - The function runs `selectModel()` for different topic numbers and computes the exclusivity, remantic coherence, heldout likelihood, bound, lower bound, and residual dispersion for the returned model.
  - We chose the most appropriate K and fit the model for topic modeling. We used the `selectModel()` function and the `stm()` function.
    - The `selectModel()` function discards models with the low likelihood values based on a small number of EM iterations, and calculates semantic coherence, exclusivity, and sparsity of models given a specific K. We were able to choose the best model based on the coherence-exclusivity measure.
    - The `stm()` function performs the variational EM for structural topic model
  - We explored topic-metadata relationship using the `estimateEffect()` function on a learned model.

- **Results**: 

  - <u>Number of topics (K)</u>: we did a search on K with values = c(6,8,10,11,12,14,16,18,20,30), the diagonostic statistics is as followed:

    <img src="/Users/carolcheng/Library/Application Support/typora-user-images/image-20210401025401697.png" alt="image-20210401025401697" style="zoom:30%;" />

    The larger K is, the lower semantic coherence and the higher the exclusivity a model has. We trained one model for K = 20 and one for K = 30.

  - <u>Overall topics</u>:

    - K = 20

      - Candidate models diagnostic statistics after `selectModel()`: we selected model 3 for higher exclusivity for further exploration

        <Center><img src="/Users/carolcheng/Library/Application Support/typora-user-images/image-20210401030849949.png" alt="image-20210401030849949" style="zoom:30%;" /></Center>	

      - Expected topic proportions for model 3:

        <Center><img src="/Users/carolcheng/Library/Application Support/typora-user-images/image-20210331233025512.png" alt="image-20210331233025512" style="zoom:30%;" /></Center>

      - Expected topic proportions for model with `stm()`:

    <Center><img src="/Users/carolcheng/Library/Application Support/typora-user-images/image-20210331233127365.png" alt="image-20210331233127365" style="zoom:30%;" /></Center>

    - K = 30
      - Candidate models diagnostic statistics after `selectModel()`: we selected model 2 for higher exclusivity for further exploration

    <Center><img src="/Users/carolcheng/Library/Application Support/typora-user-images/image-20210401024104398.png" alt="image-20210401024104398" style="zoom:30%;" /></Center>

    - Expected topic proportions for model 2:

    <Center><img src="/Users/carolcheng/Library/Application Support/typora-user-images/image-20210401120102748.png" alt="image-20210401120102748" style="zoom:30%;" /></Center>

    - Expected topic proportions for model with `stm()`:

      <Center><img src="/Users/carolcheng/Library/Application Support/typora-user-images/image-20210401135435629.png" alt="image-20210401135435629" style="zoom:65%;" /></Center>

  - <u>Topic-metadata correlation</u>

    - k = 20

      - visualization of some topic words by source:

        <img src="/Users/carolcheng/Library/Application Support/typora-user-images/image-20210401144833358.png" alt="image-20210401144833358" style="zoom: 40%;" /><img src="/Users/carolcheng/Library/Application Support/typora-user-images/image-20210401144948693.png" alt="image-20210401144948693" style="zoom:40%;" />    

        <img src="/Users/carolcheng/Library/Application Support/typora-user-images/image-20210401145112237.png" alt="image-20210401145112237" style="zoom: 37%;" /><img src="/Users/carolcheng/Library/Application Support/typora-user-images/image-20210401145212868.png" alt="image-20210401145212868" style="zoom:37%;" /> 

      - Effect of covariates on topics

      <img src="/Users/carolcheng/Library/Application Support/typora-user-images/image-20210401140431697.png" alt="image-20210401140431697" style="zoom:60%;" />

    - k = 30

      - Visualization of some topic words by source:

        <img src="/Users/carolcheng/Library/Application Support/typora-user-images/image-20210401145710527.png" alt="image-20210401145710527" style="zoom:35%;" /><img src="/Users/carolcheng/Library/Application Support/typora-user-images/image-20210401144249342.png" alt="image-20210401144249342" style="zoom:35%;" /><img src="/Users/carolcheng/Library/Application Support/typora-user-images/image-20210401144507110.png" alt="image-20210401144507110" style="zoom: 35%;" /><img src="/Users/carolcheng/Library/Application Support/typora-user-images/image-20210401144557935.png" alt="image-20210401144557935" style="zoom:35%;" />

        

      - Effect of covariates on topics:

  <img src="/Users/carolcheng/Library/Application Support/typora-user-images/image-20210401141705518.png" alt="image-20210401141705518" style="zoom:100%;" />

  

### Problems

- model selection:
  - the output topics vary a lot even when K is consistent by the functions used. Which one produces a better model?

- model interpretation: 
  - how to interpret the topics after getting the topic keywords? Do we summarize them using our intuition?
- unbalanced data:
  - Would the imbalanced data size affect model performance? Right now we only have around 9000 reddit posts, but if we use all of the forums data on alzconnected.org, there will be more than 40,000 posts in the end. (Right now we are only using the data from one caregiver forum)

### Backup Plan

- Gensim package

### Timeline

[x] 2/21 - 3/6: Finish the web crawler to acquire necessary data

[x] 3/7 - 4/1: Data preprocessing; topic modeling; identifiy questions to explore

[ ] 4/1 - 4/8: finish up topic modeling

[ ] 4/8 - 4/18: explore user interaction, etc.

[ ] 4/18 - 4/29: final report, presentation

