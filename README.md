<h1>Data Analyses of Patient Appointment No-Shows in Brazil 🇧🇷</h1>

<h2>Introduction 📝</h2>

<p>This repository contains an analysis of a dataset containing information on medical appointments in Brazil. The focus of the analysis is on predicting whether or not patients will show up for their scheduled appointments.</p>

<p> This analysis was carried out as part of the project requirements for the Udacity Data Analyst Nanodegree programme which required demonstrating the ability to conduct independent data analysis and to communicate observed findings.</p>


<h2>Dataset 📊</h2>

<p> The data used in this dataset is sourced from the Kaggle Dataset: <a href=https://www.kaggle.com/datasets/joniarroba/noshowappointments?select=KaggleV2-May-2016.csv> Medical Appointment No Shows</a> and provided by Udacity in <a href=https://d17h27t6h515a5.cloudfront.net/topher/2017/October/59dd2e9a_noshowappointments-kagglev2-may-2016/noshowappointments-kagglev2-may-2016.csv> this location</a>.

<p>The dataset, containing about 100k rows, includes the following features for each patient-appointment event (as defined by the source reference for the data, and the Udacity project rubric):</p>

<ul>
  <li><code>PatientId</code>: the patient's unique identification</li>
  <li><code>AppointmentId</code>: the unique identification for each appointment</li>
  <li><code>Gender</code>: whether the patient is Male or Female</li>
  <li><code>AppointmentDay</code>: the day on which the patient or their proxy called to set up their appointment</li>
  <li><code>ScheduledDay</code>: the day on which the patient has the actual appointment and has to visit the doctor</li>
  <li><code>Age</code>: the patient's age (in years)</li>
  <li><code>Neighborhood</code>: the location of the hospital</li>
  <li><code>Scholarship</code>: whether or not the patient is enrolled in the Brasilian welfare program, <a href= https://en.wikipedia.org/wiki/Bolsa_Fam%C3%ADlia> Bolsa Família</a></li>
  <li><code>Hipertension</code>: whether or not the patient has hypertension</li>
  <li><code>Diabetes</code>: whether or not the patient has diabetes</li>
  <li><code>Alcoholism</code>: whether or not the patient is addicted to alcohol</li>
  <li><code>Handcap</code>: whether or not the patient is physically handicapped</li>
  <li><code>SMS_received</code>: whether or not the patient received text messages regarding their appointment</li>
  <li><code>No-show</code>: whether or not the patient showed up for their appointment (encoded as "No" if the patient showed up and "Yes" if they did not)</li>
</ul>

<h2>Analysis 🧮</h2>

<p>The analysis aims to answer the following questions:</p>

<ul>
  <li>What factors are important for predicting whether or not a patient will show up for their scheduled appointment?</li>
  <li>Are there any trends or patterns in the data that can help us understand why some patients miss their appointments?</li>
  <li>Can we develop a model to accurately predict whether or not a patient will show up for their appointment?</li>
</ul>

<h2>Results 📈</h2>

<p>The results of the analysis will be published in a Jupyter Notebook in the <code>notebooks</code> directory.</p>

<h2>License 🔑</h2>

<p>This repository is licensed under the <a href="LICENSE">Creative Commons Attribution 4.0 International (CC BY 4.0) license</a>.</p>
