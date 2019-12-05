
import pandas as pd
import re



df = pd.read_csv('csv_comentarios/comments_AMLO.csv')
df['Comment'] = df['Comment'].str.replace('[^\w\s#@/:%.,_-]', '', flags=re.UNICODE)
df2 = pd.read_csv('csv_comentarios/comments_lusito comunica.csv')
df2['Comment'] = df2['Comment'].str.replace('[^\w\s#@/:%.,_-]', '', flags=re.UNICODE)
df3 = pd.read_csv('csv_comentarios/comments_Mexico.csv')
df3['Comment'] = df3['Comment'].str.replace('[^\w\s#@/:%.,_-]', '', flags=re.UNICODE)
df4 = pd.read_csv('csv_comentarios/comments_unotv.csv')
df4['Comment'] = df4['Comment'].str.replace('[^\w\s#@/:%.,_-]', '', flags=re.UNICODE)
df5 = pd.read_csv('csv_comentarios/comments_Karen Espíndola.csv')
df5['Comment'] = df5['Comment'].str.replace('[^\w\s#@/:%.,_-]', '', flags=re.UNICODE)
df6 = pd.read_csv('csv_comentarios/comments_werevertumorro.csv')
df6['Comment'] = df6['Comment'].str.replace('[^\w\s#@/:%.,_-]', '', flags=re.UNICODE)
df7 = pd.read_csv('csv_comentarios/comments_chapucero.csv')
df7['Comment'] = df7['Comment'].str.replace('[^\w\s#@/:%.,_-]', '', flags=re.UNICODE)




df8 = pd.concat([df,df2,df3,df4,df5,df6,df7])
df8.to_csv('excel_generado/comentarios.csv')
final_df = pd.read_csv('excel_generado/comentarios.csv')
final_df['Comment'] = final_df['Comment'].str.replace('[^\w\s#@/:%.,_-]', '', flags=re.UNICODE)
archivo = final_df.to_excel('excel_generado/dataset.xlsx')
