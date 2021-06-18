# Heart-disease-prediction-using-ML
Aim : Machine Learning app for predicting Heart chances of Heart disease and giving Remedies according to the condition of the heart <br>
Dataset Link : https://ieee-dataport.org/open-access/heart-disease-dataset-comprehensive#files <br>
<hr>
Steps to Install Streamlit :
pip install streamlit
<br> <hr>
for running the code :
streamlit run app.py ( open CMD in the same directory as the file ) 
<hr>
No. of rows : 1190 <br>
No. of columns : 0-11 as x and 12th as output <br>
<hr>
<b>Training and testing of data</b>
<h3>Training : 952 points</h3>
<h3>Testing : 238 points</h3>
<b> It follows 80:20 Ratio</b>
<hr>
<b>Algorithms used</b>
<li>Logistic Regression : got 84% accuracy</li>
<li>KNN Classifiers     : got 66% accuracy</li>
<li>Decision Tree       : got 90% accuracy</li>
<li>Random Forest       : got 94% accuracy</li>
<hr>
<b> As using the Random forest we got the heighest accuracy ,we had used this trained model in our web app </b>
<hr>

<b>Inputs and outputs</b>
<h3>The below data is of two patients in which if the Target value is 0 then no chances of heart disease and if 1 then positive chances .</h3> <hr>

age	sex	chest-pain type	resting bps	cholesterol	fasting blood-sugar	resting ecg	max heart-rate	exercise-angina	oldpeak	ST slope	target
40	1	    2	              140	          289	            0	              0	            172	            0	          0	       1	      0 <hr>
49	0	    3	              160	          180	            0	              0	            156	            0	          1	       2	      1 <hr>

<li>For Sex ,it is 1 for male and 0 for female<li>




