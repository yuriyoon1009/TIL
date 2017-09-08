
# coding: utf-8

# In[137]:

# 2의 이승, index 방
# index**2 for index in range(1,11)
#apple = [2 for index in range(0,3)]

target = 49

datas = [index**2 for index in range(1,11)]

datas


# In[138]:

start = 0
end = len(datas) - 1
mid = (start + end)//2

left = [0,1,2,3,4]
right = [5,6,7,8,9]


if datas[mid] == target:
    getDatas = [datas[mid]]
elif datas[mid] > target:
    getDatas = [datas[l] for l in left]
elif datas[mid] < target and target <= datas[end]:
    getDatas = [datas[r] for r in right]
else:
    print("try again")
    
getDatas  


# In[139]:

for data in getDatas:
    #print(idx, data)
    while data == target:
        print("data값은 {}이다.".format(data))
        break


# In[127]:

#for idx, data in enumerate(getDatas):
#    #print(idx, data)
#    while data == target:
#        print(idx, data)
#        break

    
            
            
      


# In[ ]:




# In[ ]:


    


# In[ ]:



  


# In[ ]:




# In[ ]:




# In[ ]:



