
# coding: utf-8

# In[1]:

def print_result(result_df,packages_num=5):
    from prettytable import PrettyTable
    x= PrettyTable(["Pkg#", "Price","Out Flight", "Return Flight","Hotel Name","Rating","Review#"])
    for index in range(packages_num):
        pos=result_df.iloc[index]
        x.add_row([index,'%.2f'%pos['total package price'],            '%s(%s)->%s(%s)'% (pos['depart airport1'],pos['depart flight depart time'],pos['depart airport2'],pos['depart flight arrival time']),            '%s(%s)->%s(%s)'% (pos['arrival airport1'],pos['arrival flight depart time'],pos['arrival airport2'],pos['arrival flight arrival time']),            pos['hotel name'][:20],            pos['rating'],            pos['comments']])
    print(x)


# In[ ]:



