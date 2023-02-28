import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import ttest_ind

# read CSV file into pandas DataFrame
data = pd.read_csv("D:\\PDS\\clean_people_data.csv")

# perform t-test on two groups based on Frailty status
group1 = data[data['Frailty'] == 'Y']['Age']
group2 = data[data['Frailty'] == 'N']['Age']
t_stat, p_value = ttest_ind(group1, group2)

# print t-test results
print(f'T-Statistic: {t_stat:.2f}')
print(f'P-Value: {p_value:.3f}')

# create histogram of age distribution
plt.hist(group1, alpha=0.5, label='Frail')
plt.hist(group2, alpha=0.5, label='Not Frail')
plt.legend(loc='upper right')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.title('Age Distribution by Frailty Status')
plt.show()

# save histogram to file
plt.savefig('D:\\PDS\\age_distribution.png')