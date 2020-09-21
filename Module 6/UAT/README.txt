Note: this is readme for Telcom customer churn prediction, UAT testing

******************** Essential Environment **********************
1. Software to be installed: python 3.6 or above
2. python packages: pandas, joblib
3. Python should be added as environment variable path

******************** Data Format ********************************
The format has to be same as the file file input_data.xlsx
columns order: International plan,Number vmail messages,Total day minutes,Total eve minutes,Total night minutes,Total intl minutes,Customer service calls

    - International plan  - Yes / No
    - Number vmail messages - Count of voice mail messages in a month
    - Total day minutes - total number of day minutes in a month
    - Total eve minutes - total number of evening minutes in a month
    - Total night minutes - total number of night minutes in a month
    - Total intl minutes - total number of international minutes in a month
    - Customer service calls - total number of customer service calls in a month
    
    
- kindly rename your data file as "input_data.xlsx" and keep it in the UAT folder

******************** Test Execution ****************************
Step1 : Open command prompt from start menu
Step2 : naviagte to the UAT folder extracted, by using command cd c:/.../UAT
Step3 : run the command python test.py
Step4 : You can check the results in results.csv file in the UAT folder
Step5 : In case of error, please email us to abc@xyz.com

