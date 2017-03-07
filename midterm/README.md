# python_spring17_midterm

##Question 1 
###Analysis 1:
Aim of this analysis was to find the no of emails sent during each hour of the day and also for each day of the month, this was done using the sent emails from the enron email data.

- Step1 Created a dictionary with keys in the range of 0 to 24, for each hr of the day.
- Step2 Traversed through the sent emails of each employee.
- Step3 For each email the hour and minute at which the email was sent was extracted from its time stamp.
- Step4 Incremented the values of the corresponding hour the mail was sent.
- Step5 Plot the values using matplotlib.
<img width="783" alt="screen shot 2017-03-06 at 9 58 32 pm" src="https://cloud.githubusercontent.com/assets/22924110/23639952/72f9bada-02b8-11e7-8bdb-e73f03c964db.png">

From this we can conclude that major percentage of the mails are being sent during the early hours of the day.

- Step6 Created a dictionary with keys in the range of 0 to 31, for each day of the month.
- Step7 Traversed through the sent emails of each employee.
- Step8 For each email the the day on which the email was sent was extracted from its time stamp.
- Step9 Incremented the values of the corresponding day the mail was sent.
- Step10 Plot the values using matplotlib.
<img width="802" alt="screen shot 2017-03-06 at 9 58 56 pm" src="https://cloud.githubusercontent.com/assets/22924110/23639984/98f38766-02b8-11e7-92de-900392043bcb.png">


###Analysis 2:
Aim of this analysis was to find the top100 email threads and also the top50 employees who started the most no of email threads.

- Step1 Created 2 empty dictionaries for counting the mail thread and the thread starter.
- Step2 From each email the subject was extracted.
- Step3 If 're:' or 'fw:' is not part of the subject and it is added and incremented to the library.
- Step4 If 're:' or 'fw:' is a part of the subject it is striped of these prefix and it is added and incremented to the library.
- Step5 The dictionary containing the thread count is sorted according to its values and the top 100 is displayed.
<img width="236" alt="screen shot 2017-03-06 at 10 27 11 pm" src="https://cloud.githubusercontent.com/assets/22924110/23640702/51016310-02bd-11e7-9778-98b423ce7f17.png">

- Step6 Values from the employee dictionary is ploted using the matplotlib.
<img width="803" alt="screen shot 2017-03-06 at 10 22 21 pm" src="https://cloud.githubusercontent.com/assets/22924110/23640739/81c77c3c-02bd-11e7-9952-66c8b9e6142a.png">


###Analysis 3:
Aim of this analysis was to find the top email sender and reciever among the  employees.

- Step1 Created a dictionary for counting the mail send by each employee.
- Step2 From each email the from address was extracted.
- Step3 Count of each mail was added to the corresponding employee. 
- Step4 Plot the values using matplotlib.
<img width="814" alt="screen shot 2017-03-06 at 10 39 16 pm" src="https://cloud.githubusercontent.com/assets/22924110/23640947/ab32ca44-02be-11e7-99cc-311d138573c3.png">

- Step5 Created a dictionary for counting the mail recieved by each employee.
- Step6 From each email the to address was extracted and split to get individual ids.
- Step7 Count of each mail was added to the corresponding employee. 
- Step8 Plot the values using matplotlib.
<img width="823" alt="screen shot 2017-03-06 at 10 39 34 pm" src="https://cloud.githubusercontent.com/assets/22924110/23640948/ada51f98-02be-11e7-8399-3ff5f513f5b2.png">


##Question 2 
From NYT Archive API articles from 2012-2016 were extracted and individual article was separated and stored in a month-year hierarchy folder structure.The parent folder is named 'Archive'
From NYT Article Search API the latest articles were extracted and individual article was separated and stored in a folder named 'Article Search'

###Analysis 1:
Aim of this analysis was to find the article about President Barack Obama in relataion to topics which were the major positives of his term in office.

- Step1 Created multiple dictionaries for different topics with keys in the range of 2012 to 2016.
- Step2 Traversed through Archive directory.
- Step3 The date was extracted from each article about President Barack Obama in relataion to certain topics .
- Step4 Count for each topic was added to the corresponding dictionary according to the specific year. 
- Step5 Plot the values using matplotlib.
<img width="764" alt="screen shot 2017-03-06 at 10 55 17 pm" src="https://cloud.githubusercontent.com/assets/22924110/23641314/c3f7430a-02c0-11e7-88ad-3f39950af689.png">

###Analysis 2:
Aim of this analysis was to find the no of articles which was published per year with regard to certain topics.

- Step1 Created multiple dictionaries for different topics with keys in the range of 2012 to 2016.
- Step2 Traversed through Archive directory.
- Step3 The date was extracted from each article.
- Step4 Count for each topic was added to the corresponding dictionary according to the specific year. 
- Step5 Plot the values using matplotlib.
<img width="757" alt="screen shot 2017-03-06 at 11 02 52 pm" src="https://cloud.githubusercontent.com/assets/22924110/23641351/1acaa01e-02c1-11e7-8209-dbbf3db811c4.png">
<img width="775" alt="screen shot 2017-03-06 at 11 02 40 pm" src="https://cloud.githubusercontent.com/assets/22924110/23641350/1ac9cf36-02c1-11e7-9ed2-0edb70b77772.png">

###Analysis 3:
Aim of this analysis was to find the no of different article topics and their count for the month of march 2017.

- Step1 Created a dictionary for counting the no articles for each topic.
- Step2 Traversed through Article search directory.
- Step3 Count for each topic was added to the corresponding key. 
- Step4 Plot the values using matplotlib.
<img width="183" alt="screen shot 2017-03-06 at 11 00 29 pm" src="https://cloud.githubusercontent.com/assets/22924110/23641313/c3f6db2c-02c0-11e7-8005-8850f9a783b7.png">
<img width="768" alt="screen shot 2017-03-06 at 11 00 15 pm" src="https://cloud.githubusercontent.com/assets/22924110/23641312/c3f63276-02c0-11e7-81e4-05e37a87dabf.png">




















