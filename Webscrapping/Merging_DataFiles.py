import pandas as pd

df=pd.read_csv('data_NYC.csv')
df_tempo=pd.read_csv('data_Chicago.csv');
df=df.append(df_tempo,ignore_index=True)
df_tempo=pd.read_csv('data_Boston.csv');
df=df.append(df_tempo,ignore_index=True)
df_tempo=pd.read_csv('data_washigton-dc.csv');
df=df.append(df_tempo,ignore_index=True)
df_tempo=pd.read_csv('data_San-Francisco.csv');
df=df.append(df_tempo,ignore_index=True)
df_tempo=pd.read_csv('data_Los-Angeles.csv');
df=df.append(df_tempo,ignore_index=True)
df.to_csv('MergedData.csv')
