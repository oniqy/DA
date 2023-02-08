import numpy as np
import pandas as pd
# lab = ['a','b','c']
# maydaa=[10,40,30]
# arr= np.array(maydaa)
# d = {'a':10,'b':20,'c':30}
# num = lambda x,y:x*y

# arr2 = np.arange(25)
# print(arr2.reshape(5,5))

#Data Frame
 
from numpy.random import randn
np.random.seed(0) 
# print(np.random.randint(1,100,2))
# df = pd.DataFrame(randn(5,4),index='A B C D E'.split(),columns='W X Y Z'.split())
# rand = np.random.randint(1,100,10)
# print(rand.min())##gia tri
# print(rand.argmin())##vi tri

# df['T']=df['X']+df['Y']
# df.drop('T',axis=1)##inplace=True##)
# print(df.shape)
# print(df.loc['C'])##Dung cho row
# print(df.loc[['A','B'],['H','G']])

# boolen = df >0
# ref = df[boolen]
# col = ['X','Y']
# df.reset_index()
# alo = 'NY Vo Thi Thu Thao'.split()
# df['Columnmoi'] = alo
# print(df.set_index('Columnmoi'))
# print(ref[col])
# print(df[df>0][['X','Y']])
# print(df['X']>0)
# print(df[df['X']> 0])##'Dùng cho column'
# print(boolen)
# print(df[boolen])

# outside = ['G1','G1','G1','G2','G2','G2']
# inside =[1,2,3,1,2,3]
# hier_index = list(zip(outside,inside))
# hier_index = pd.MultiIndex.from_tuples(hier_index)
# df = pd.DataFrame(randn(6,2),hier_index,['A','B'])
# df.index.names = ['Cac','Num']
# dt = df.loc['G2'].loc[3]['A']
# dc = df.xs(2,level='Num')
# print(dc)
# print(df)

#Missing data

# d = {'A':[1,np.nan,np.nan],'B':[3,1,np.nan],'C':[1,2,3],'D':[4,6,1]}
# df = pd.DataFrame(d)
# print(df)
# print(df.dropna())##goi ra cac hang k co gia tri null , them axis=1 de goi cac cot
# print(df.dropna(thresh=3))## goi cac cot co it nhat 1 gia tri ,=2 goi cac cot co it nhat 2 gia tri
# print('Avg:',df['B'].mean()) ##Tinh trung binh
# df.fillna(value=2)##chen gia tri vao o trong
# print(df['A'].fillna(value=df['A'].mean()))

#group by

# data = {'Company':['GOOG','GOOG','MSFT','MSFT','FB','FB'],
#        'Person':['Sam','Charlie','Amy','Vanessa','Carl','Sarah'],
#        'Sales':[200,120,340,124,243,350]}
# df = pd.DataFrame(data)
# print(df)
# bycomp =df.groupby('Company')
# print(bycomp.mean())
# print(bycomp.sum())
# print(bycomp.std())
# print(bycomp.sum().loc['FB'])
# print(bycomp.count())
# print(bycomp.min())
# print(bycomp.describe())##.transpose([']))

#Merging ,join,Concate

# df1 = pd.DataFrame({'A': ['A0', 'A1', 'A2', 'A3'],
#                         'B': ['B0', 'B1', 'B2', 'B3'],
#                         'C': ['C0', 'C1', 'C2', 'C3'],
#                         'D': ['D0', 'D1', 'D2', 'D3']},
#                         index=[0, 1, 2, 3])
# df2 = pd.DataFrame({'A': ['A4', 'A5', 'A6', 'A7'],
#                         'B': ['B4', 'B5', 'B6', 'B7'],
#                         'C': ['C4', 'C5', 'C6', 'C7'],
#                         'D': ['D4', 'D5', 'D6', 'D7']},
#                          index=[4, 5, 6, 7]) 
# df3 = pd.DataFrame({'A': ['A8', 'A9', 'A10', 'A11'],
#                         'B': ['B8', 'B9', 'B10', 'B11'],
#                         'C': ['C8', 'C9', 'C10', 'C11'],
#                         'D': ['D8', 'D9', 'D10', 'D11']},
#                         index=[8, 9, 10, 11])
# print(pd.concat([df1,df2,df3]))#,axis=1)
# left = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3'],
#                      'A': ['A0', 'A1', 'A2', 'A3'],
#                      'B': ['B0', 'B1', 'B2', 'B3']})
   
# right = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3'],
#                           'C': ['C0', 'C1', 'C2', 'C3'],
#                           'D': ['D0', 'D1', 'D2', 'D3']})  

# print(pd.merge(left,right,how='inner',on='key'))

# left = pd.DataFrame({'key1': ['K0', 'K0', 'K1', 'K2'],
#                      'key2': ['K0', 'K1', 'K0', 'K1'],
#                         'A': ['A0', 'A1', 'A2', 'A3'],
#                         'B': ['B0', 'B1', 'B2', 'B3']})
# right = pd.DataFrame({'key1': ['K0', 'K1', 'K1', 'K2'],
#                                'key2': ['K0', 'K0', 'K0', 'K0'],
#                                   'C': ['C0', 'C1', 'C2', 'C3'],
#                                   'D': ['D0', 'D1', 'D2', 'D3']})

# print(pd.merge(left, right, on=['key1', 'key2']))
# print(pd.merge(left,right,how='outer',on=['key1','key2']))

#toan Tu

# df = pd.DataFrame({'col1':[1,2,3,4],'col2':[444,555,666,444],'col3':['abc','def','ghi','xyz']})
# print(df.head())
# print(df['col1'].unique())
# print(df['col1'].nunique())#same len(df['col1].unique())
# print(df['col2'].value_counts())#đêms số lần xuất hiện của từng giá trị
# print(df[(df['col2']>500)&(df['col1']>2)])#thêm df đằng trước để trả về kiểu static nếu không biểu thức sẽ trả về kiểu boolen    

# def nhan2(x):
#    return x *2
# print(df['col1'].apply(nhan2))
# #hoặc
# print(df['col2'].apply(lambda x:x*2))

# print(df['col3'].apply(len))# đếm độ dài chuỗi\
# print(df.drop('col1',axis=1))
# print(df.sort_values('col2'))

# data = pd.DataFrame({'A':['foo','foo','foo','bar','bar','bar'],
#      'B':['one','one','two','two','one','one'],
#        'C':['x','y','x','y','x','y'],
#        'D':[1,3,2,5,4,1]})
# print(data)
# print(data.pivot_table(values='D',index=['A','B'],columns='C'))#chỉnh sửa lại bảng , hãy tìm hiểu thêm 

#doc file

df = pd.read_csv('example')
print(df)
print(df.to_csv('example',index=False))
print(pd.read_excel('Excel_Sample.xlsx',sheet_name='Sheet1'))
print(df.to_excel('Excel_Sample.xlsx',sheet_name='Sheet1'))
# df = pd.read_html('http://www.fdic.gov/bank/individual/failed/banklist.html')
from sqlalchemy import create_engine
engine = create_engine('sqlite:///:memory:')
df.to_sql('my_table',engine)
sql_df = pd.read_sql('data',con=engine)
print(sql_df)