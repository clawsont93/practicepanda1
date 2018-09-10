
# coding: utf-8

# In[2]:


git init


# In[5]:


from pandas import DataFrame, read_csv


# In[6]:


import matplotlib.pyplot as plt
import pandas as pd #this is how I usually import pandas
import sys #only needed to determine Python version number
import matplotlib #only needed to determine Matplotlib version number

# Enable inline plotting


# In[7]:


get_ipython().run_line_magic('matplotlib', 'inline')


# In[8]:


print('Python version ' + sys.version)
print('Pandas version ' + pd.__version__)
print('Matplotlib version ' + matplotlib.__version__)


# In[9]:


# The inital set of baby names and bith rates
names = ['Bob','Jessica','Mary','John','Mel']
births = [968, 155, 77, 578, 973]


# In[10]:


get_ipython().run_line_magic('pinfo', 'zip')


# In[11]:


BabyDataSet = list(zip(names,births))
BabyDataSet


# In[12]:


df = pd.DataFrame(data = BabyDataSet, columns=['Names', 'Births'])
df


# In[13]:


get_ipython().run_line_magic('pinfo', 'df.to_csv')


# In[14]:


df.to_csv('births1880.csv',index=False,header=False)


# In[15]:


get_ipython().run_line_magic('pinfo', 'readcsv')


# In[16]:


get_ipython().run_line_magic('pinfo', 'read_csv')


# In[17]:


echo "# practice" >> README.md
git init
git add README.md
git commit -m "first commit"
git remote add origin https://github.com/clawsont93/practice.git
git push -u origin master

