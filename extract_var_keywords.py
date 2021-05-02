# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import pandas as pd 
pd.__version__


# %%
import yake
yake.__version__


# %%
## load the data
allData = pd.read_csv('variables.csv')
allData.head(3)


# %%
labels = allData['label'].tolist()
labels[0]


# %%
text  = ' '.join(labels)


# %%
len(text)


# %%
kw_extractor = yake.KeywordExtractor()
keywords = kw_extractor.extract_keywords(text)

for kw in keywords:
	print(kw)


# %%



