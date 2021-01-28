#!/usr/bin/env python
# coding: utf-8

# ### Note
# * Instructions have been included for each segment. You do not have to follow them exactly, but they are included to help you think through the steps.

# In[9]:


# Dependencies and Setup
import pandas as pd
import numpy as np

# File to Load (Remember to Change These)
school_data_to_load = "Resources/schools_complete.csv"
student_data_to_load = "Resources/students_complete.csv"

# Read School and Student Data File and store into Pandas DataFrames
school_data = pd.read_csv(school_data_to_load)
student_data = pd.read_csv(student_data_to_load)

# Combine the data into a single dataset.  
school_data_complete = pd.merge(student_data, school_data, how="left", on=["school_name", "school_name"])


# ## District Summary
# 
# * Calculate the total number of schools
# 
# * Calculate the total number of students
# 
# * Calculate the total budget
# 
# * Calculate the average math score 
# 
# * Calculate the average reading score
# 
# * Calculate the percentage of students with a passing math score (70 or greater)
# 
# * Calculate the percentage of students with a passing reading score (70 or greater)
# 
# * Calculate the percentage of students who passed math **and** reading (% Overall Passing)
# 
# * Create a dataframe to hold the above results
# 
# * Optional: give the displayed data cleaner formatting

# In[14]:


total_schools = school_data_complete["school_name"].nunique()
total_schools


# In[25]:


total_students=school_data_complete["Student ID"].nunique()
total_students


# In[30]:


total_budget = school_data_complete['budget'].sum()

total_budget


# In[31]:


average_math_score = school_data_complete['math_score'].mean()
average_math_score


# In[33]:


average_reading_score = school_data_complete['reading_score'].mean()
average_reading_score


# In[36]:


passing_math = len(school_data_complete[school_data_complete['math_score'] >= 70])
passing_math


# In[38]:


percent_passing_math = passing_math/total_students * 100
percent_passing_math


# In[39]:


passing_reading = len(school_data_complete[school_data_complete['reading_score'] >= 70])
passing_reading


# In[40]:


percent_passing_reading = passing_reading/total_students * 100
percent_passing_reading


# In[43]:


percent_overall_passing = (average_math_score + average_reading_score)/2
percent_overall_passing


# In[60]:


district_summary_df = pd.DataFrame({"Total Schools": [total_schools], 
    "Total Students": [total_students], 
    "Total Budget": [total_budget], 
    "Average Math Score": [average_math_score], 
    "Average Reading Score": [average_reading_score],    
    "Passing Math": [percent_passing_math], 
    "Passing Reading": [percent_passing_reading],
    "Overall Passing Rate": [percent_overall_passing]
})
district_summary_df


# ## School Summary

# In[ ]:





# * Create an overview table that summarizes key metrics about each school, including:
#   * School Name
#   * School Type
#   * Total Students
#   * Total School Budget
#   * Per Student Budget
#   * Average Math Score
#   * Average Reading Score
#   * % Passing Math
#   * % Passing Reading
#   * % Overall Passing (The percentage of students that passed math **and** reading.)
#   
# * Create a dataframe to hold the above results

# In[64]:


grouped_school_df = school_data_complete.groupby(["school_name"])
schoolType = grouped_school_df["type"].first()
schoolType


# In[66]:


totalStudents = grouped_school_df["Student ID"].count()
totalStudents


# In[69]:


totalSchoolBudget = grouped_school_df["budget"].first()
totalSchoolBudget


# In[71]:


perStudentBudget = totalSchoolBudget / totalStudents
perStudentBudget


# In[80]:


averageMathScore = grouped_school_df["math_score"].mean()
averageMathScore


# In[78]:


averageReadingScore = grouped_school_df["reading_score"].mean()
averageReadingScore


# In[83]:


passingMath = school_data_complete[school_data_complete["math_score"]
                                   >= 70].groupby(["school_name"])["math_score"].count()
passingMath
percentPassingMath = passingMath / totalStudents * 100
percentPassingMath


# In[85]:


passingRead = school_data_complete[school_data_complete["reading_score"] >= 70].groupby(["school_name"])["reading_score"].count()
percentPassingReading = passingRead / totalStudents * 100
percentPassingReading


# In[87]:


percentOverallPassingRate = (percentPassingMath + percentPassingReading) / 2
percentOverallPassingRate


# In[89]:


school_summary_df = pd.DataFrame({"School Type": schoolType,
      "Total Students": totalStudents,
      "Total School Budget": totalSchoolBudget,
      "Per Student Budget": perStudentBudget,
      "Average Math Score": averageMathScore,
      "Average Reading Score": averageReadingScore,
      "Passing Math": percentPassingMath,
      "Passing Reading": percentPassingReading,
      "Overall Passing Rate": percentOverallPassingRate})
school_summary_df


# In[91]:


school_summary_df = school_summary_df.sort_values(["Overall Passing Rate"], ascending=False)
school_summary_df


# In[93]:


# top 5 schools

school_summary_df.head()


# In[ ]:





# In[ ]:





# In[ ]:





# ## Top Performing Schools (By % Overall Passing)

# * Sort and display the top five performing schools by % overall passing.

# In[ ]:





# ## Bottom Performing Schools (By % Overall Passing)

# * Sort and display the five worst-performing schools by % overall passing.

# In[98]:


school_summary_df = school_summary_df.sort_values(["Overall Passing Rate"], ascending=True)

school_summary_df[["School Type", "Total Students", "Total School Budget",
                   "Per Student Budget","Average Math Score",
                   "Average Reading Score", "Passing Math",
                   "Passing Reading","Overall Passing Rate"]].head()
school_summary_df


# ## Math Scores by Grade

# * Create a table that lists the average Reading Score for students of each grade level (9th, 10th, 11th, 12th) at each school.
# 
#   * Create a pandas series for each grade. Hint: use a conditional statement.
#   
#   * Group each series by school
#   
#   * Combine the series into a dataframe
#   
#   * Optional: give the displayed data cleaner formatting

# In[110]:


grade9th_ds = school_data_complete.loc[school_data_complete["grade"] == "9th"].groupby(["school_name"])["math_score"].mean()
grade10th_ds = school_data_complete.loc[school_data_complete["grade"] == "10th"].groupby(["school_name"])["math_score"].mean()
grade11th_ds = school_data_complete.loc[school_data_complete["grade"] == "11th"].groupby(["school_name"])["math_score"].mean()
grade12th_ds = school_data_complete.loc[school_data_complete["grade"] == "12th"].groupby(["school_name"])["math_score"].mean()

grade_summary_df = pd.DataFrame({"9th": grade9th_ds,
      "10th": grade10th_ds,
      "11th": grade11th_ds,
      "12th": grade12th_ds})

grade_summary_df[["9th", "10th", "11th", "12th"]]


# In[104]:


grade9th_ds.head()
grade10th_ds.head()


# ## Reading Score by Grade 

# * Perform the same operations as above for reading scores

# In[111]:


grade9th_ds = school_data_complete.loc[school_data_complete["grade"] == "9th"].groupby(["school_name"])["reading_score"].mean()
grade10th_ds = school_data_complete.loc[school_data_complete["grade"] == "10th"].groupby(["school_name"])["reading_score"].mean()
grade11th_ds = school_data_complete.loc[school_data_complete["grade"] == "11th"].groupby(["school_name"])["reading_score"].mean()
grade12th_ds = school_data_complete.loc[school_data_complete["grade"] == "12th"].groupby(["school_name"])["reading_score"].mean()

grade_summary_df = pd.DataFrame({"9th": grade9th_ds,
      "10th": grade10th_ds,
      "11th": grade11th_ds,
      "12th": grade12th_ds})

grade_summary_df[["9th", "10th", "11th", "12th"]]


# ## Scores by School Spending

# * Create a table that breaks down school performances based on average Spending Ranges (Per Student). Use 4 reasonable bins to group school spending. Include in the table each of the following:
#   * Average Math Score
#   * Average Reading Score
#   * % Passing Math
#   * % Passing Reading
#   * Overall Passing Rate (Average of the above two)

# In[118]:


spending_bins = [0, 585, 615, 645, 675]
group_names = ["<$585", "$585-615", "$615-645", "$645-675"]
group_names
spending_bins


# In[132]:


school_summary_df["Per Student Budget"] = school_summary_df["Per Student Budget"].apply
(lambda x:x.replace('$', '').replace(',', '')).astype("float")


school_summary_df = school_summary_df.reset_index() 

school_summary_df["Spending_Ranges (Per Student)"] = pd.cut(school_summary_df["Per Student Budget"], spending_bins, labels=group_names)


grouped_spend_df = school_summary_df.groupby(["Spending Ranges (Per Student)"])              

spending_summary_df = grouped_spend_df.mean()

# Display Summary
spending_summary_df[["Average Math Score",
                    "Average Reading Score",
                    "Passing Math",
                    "Passing Reading",
                    "Overall Passing Rate"]]
Spending_summary_df



# ## Scores by School Size

# * Perform the same operations as above, based on school size.

# In[130]:


school_summary_df = school_summary_df.reset_index()
school_summary_df["School Size"] = pd.cut(school_summary_df["Total Students"], labels=group_names)
grouped_size_df = school_summary_df.groupby(["School Size"])   

size_summary_df = grouped_size_df.mean()

size_summary_df[["Average Math Score",
                "Average Reading Score",
                "Passing Math",
                "Passing Reading",
                "Overall Passing Rate"]]


# ## Scores by School Type

# * Perform the same operations as above, based on school type

# In[24]:





# In[134]:


school_summary_df = school_summary_df.reset_index()

grouped_type_df = school_summary_df.groupby(["School Type"])              

type_summary_df = grouped_type_df.mean()

type_summary_df[["Average Math Score",
                "Average Reading Score",
                "Passing Math",
                "Passing Reading",
                "Overall Passing Rate"]]


# In[ ]:




