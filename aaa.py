#!/usr/bin/env python
# coding: utf-8

# In[1]:


text = '한 가지 생각을 선택하라. 그 생각을 당신의 삶으로 만들어라. 그걸 생각하고, 꿈꾸고, 그에 기반해서 살아가라. 당신의 몸의 모든 부분, 뇌, 근육, 신경을 그 생각으로 가득 채우고 다른 생각은 다 내버려둬라. 이것이 성공하는 방법이다.'


# In[4]:


from nltk.tokenize import sent_tokenize
from kiwipiepy import Kiwi
kiwi = Kiwi()


# In[5]:


sentence = []

sent_kr = kiwi.split_into_sents(text)

for s in sent_kr:
    sentence.append(s.text)

print(sentence)


# In[ ]:




