# engageclients

This repository includes the answers to the two tasks of the data scientist challenge.  
It is designed in a way that one can classify if a user would be loyal or not. There are two models to suggest new pages and products to users.

The new Tensorflew Recommendation API has been utilized to develop the recommender system.

# A. Exercise #1

#### Based on the information provided, What are some of the biggest drivers of retention and engagement? Why?

1. Desktop applications have much better retention rates
2. Linux OS has similar users compared to IOS and Android, but with higher retention
Therefore I conclude that users with personal computers have better interaction with the product.
3. Most of the users use Firefox browser to benefit from the product however, still many will not engage enough and will not return
4. IOS and Mac OS users are a few in comparison to the other OS users with relatively low retention
5. word, compress, and merge are the most used products by users
6. and more

### Based on the analyses (descriptive statistics) I did, the primary users come from Firefox, under the Windows operating system, and use the word, compress, and merge pages.


## First Run of Visualization


#### Retention of all instances based on the page feature
![Retention of all instances based on the page feature](Assets/all_instances_page_freq.png)


#### Retention of all instances based on the os feature
![Retention of all instances based on the os feature](Assets/all_instances_os_freq.png)


#### Retention of all instances based on the browser featur
![Retention of all instances based on the browser feature](Assets/all_instances_browser_freq.png)


#### Retention of all instances based on the browser feature
![Retention of all instances based on the browser feature](Assets/all_instances_all_in_one_freq.png)




## Second Run of Visualization

#### Retention of Unique Clients based on the chrome browser feature
![Retention of Unique Clients based on the chrome browser feature](Assets/Unique_id_brows_chrome_freq.png)


#### Retention of Unique Clients based on the chrome browser feature
![Retention of Unique Clients based on the chrome browser feature](Assets/Unique_id_brows_edge_freq.png)


#### Retention of Unique Clients based on the Firefox browser feature
![Retention of Unique Clients based on the Firefox browser feature](Assets/Unique_id_brows_firefox_freq.png)


#### Retention of Unique Clients based on the chrome IE feature
![Retention of Unique Clients based on the chrome IE feature](Assets/Unique_id_brows_ie_freq.png)


#### Retention of Unique Clients based on the Opera browser feature
![Retention of Unique Clients based on the Opera browser feature](Assets/Unique_id_brows_opera_freq.png)


#### Retention of Unique Clients based on the Safari browser feature
![Retention of Unique Clients based on the Safari browser feature](Assets/Unique_id_brows_safari_freq.png)


#### Retention of Unique Clients based on the Android OS feature
![Retention of Unique Clients based on the Android OS feature](Assets/Unique_id_os_android_freq.png)


#### Retention of Unique Clients based on the IOS OS feature
![Retention of Unique Clients based on the IOS OS feature](Assets/Unique_id_os_ios_freq.png)


#### Retention of Unique Clients based on the Linux OS feature
![Retention of Unique Clients based on the Linux OS feature](Assets/Unique_id_os_linux_freq.png)


#### Retention of Unique Clients based on the Mac OS feature
![Retention of Unique Clients based on the Mac OS feature](Assets/Unique_id_os_macos_freq.png)


#### Retention of Unique Clients based on the Windows OS feature
![Retention of Unique Clients based on the Windows OS feature](Assets/Unique_id_os_windows_freq.png)


#### Retention of Unique Clients based on the Monthly Plan feature
![Retention of Unique Clients based on the Monthly Plan feature](Assets/Unique_id_plan_monthly_freq.png)


#### Retention of Unique Clients based on the Yearly Plan feature
![Retention of Unique Clients based on the Yearly Plan feature](Assets/Unique_id_plan_yearly_freq.png)


#### Retention of Unique Clients based on the pages feature
##### These are promising results showing the engagement of unique users based on the product they use
![Retention of Unique Clients based on the pages feature](Assets/Unique_id_page_all_freq.png)



## Assessments for exercise 1 - ML
It could be assumed that the features are independent, or we can not recognize the relationship between them based on the exploratory analyses. 
That's exactly where the machine learning models can help us to find either a user will be loyal or not?
To decide if a customer is loyal or not? And to see if the user will return to the platform and use other pages, we need to benefit from ML first to classify the users and second to recommend the new products and pages. 

As it is a supervised machine learning problem, we first need to lablelize the data.
In this task, I calculated the averages and the percentile 50% of the frequency of instances and found the Q50 is 3. So I used Q50.

So a user is loyal and will return and use pages if the total frequency of the user is equal or greater than 3. 

Labels : 
Yes or 1 for total usage >= 3
No or 0 for total usage < 3


### The folwing steps are the ones I performed on the data to setup the ML models: 
#### 1. Data cleaning and handling missing data (I used the mode of feature to fill the nan)
#### 2. ML on the entire instances
#### 3. ML on the unique users
#### 4. ML on uniques users by adding a new feature (frequency of usage per user)
#### 5. ML on uniques users by adding a new feature (frequency of usage per user) and limiting the maximum usage (mainly to improve SVM)



### Finally, we have trained a group of models that perform well on the taring set and are verified accurately on the test set. 
The next step would be to use a voting system for the ensemble of models 

# B. Exercise #2
## For this exercise I did not only draw the skeleton but rather built a recommender system using Tensorflow recommenders and scikit learn library separately

#### 1. Create models to recommend products based on the pages
#### 2. Use modeles in a REST API, developed in Python



## C. Discussion

### C.1. Web App
#### The machine learning model will serve as a service, and the web and mobile applications are connected to that using REST API

![the schematic framework of the web app (Oreilly 2019, hands-on machine learning](Assets/web_app.PNG)

![the schematic framework of the web app Oreilly 2019, hands-on machine learning](Assets/flow.png)


### C.2. Release flow

#### The release cycle of our products in case we needed to develop a package. For instance, other colleagues and data scientists might benefit from our product.

![The package development flow](Assets/release_flow.PNG)



## Contributing

To contribute follow these steps:

1. Fork the project on GitHub.
2. Create a local clone of the develop branch (`git clone https://github.com/YOUR-USERNAME/engageclients.git -b develop`)
3. Install the packages in `engageclients/requirements/env_engageclients.yml` and `engageclients/requirements/env_developer.yml`.
4. Make well commented and clean commits to your repository.
5. Make unit and integration tests on your code, preferably during development.
6. Perform a static code analysis of your code with ENGAGECLIENTS's configuration `.pylintrc`.
7. Add your name to the AUTHORS file.
8. Push the changes to GitHub (`git push origin develop`).
9. On GitHub, create a new pull request onto the develop branch of CLIENTS-project/engageclients.

See our [contribution guidelines](http://www.saeidashraf.com/) for more information.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [releases on this repository](https://github.com/saeedashraf/engageclients).

## License

Copyright (C) 2021 saeidashraf, engageclients contributors listed in AUTHORS.

engageclients is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License Version 3, 29 June 2007 as published by the Free Software Foundation, https://www.gnu.org/licenses/gpl-3.0.html

engageclients is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details: https://www.gnu.org/licenses/gpl-3.0.html
