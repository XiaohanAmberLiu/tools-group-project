
# coding: utf-8

# In[1]:

#standardize hotel rating
def change_airbnb_rating(rat):
    import re
    if re.match(r'Rating',str(rat)):
        return (int(re.findall(r'\d',rat)[0])/int(re.findall(r'\d',rat)[1]))
    else:
        try:
            return (int(rat))
        except:
            return rat


# In[2]:

#price normalization (max-x)/(max-min)
def normalization(df,m=1): #m=1=>(x-min)/(max-min); m=0 =>(max-x)/(max-min)
    mx=df.max()
    mn=df.min()
    if m==1:
        return df.apply(lambda x: (x-mn)/(mx-mn))
    else:
        return df.apply(lambda x: (mx-x)/(mx-mn))


# In[ ]:

def recommended_packages(df_packages,sort=0):  #0:sorted by total price; 1:sorted by hotel's rating; 2:sorted by recommendation
##data processing
    import pandas as pd
    import re
    df_packages['comments']=pd.to_numeric(df_packages['comments']) 
    #normalizae rating
    df_packages['rating']=df_packages['rating'].apply(lambda x: change_airbnb_rating(x))
    
    if sort==0:
        #sort by package price, hotel rating 
        result=df_packages.sort_values(by=['total package price','rating'],ascending=[True,False])
    
    elif sort==1:
        #sort by hotel rating, price 
        result=df_packages.sort_values(by=['rating','total package price'],ascending=[False,True])

    elif sort==2:
        #recommendation score weight: price 50%, Rating 30%, comments 20%
        df_packages['std_pkg_price']= normalization(df_packages['total package price'],m=0)
        df_packages['std_comments']= normalization(df_packages['comments'],m=1)
        df_packages['recommend_score']=df_packages['std_pkg_price']*0.5 + df_packages['rating']*0.3 + df_packages['std_comments']*0.2
        result=df_packages.sort_values(by=['recommend_score'],ascending=False)
    
    else:
        print('Sorry, we can not recognize the sorting condition. Please try again.')
    
    return result

