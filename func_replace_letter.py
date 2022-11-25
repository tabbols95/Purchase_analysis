#!/usr/bin/env python
# coding: utf-8

# In[1]:


def replace_letter(no_correct_data):
    correct_data = no_correct_data.lower() \
        .replace('a', 'а') \
        .replace('b', 'в') \
        .replace('c', 'с') \
        .replace('e', 'е') \
        .replace('h', 'н') \
        .replace('k', 'к') \
        .replace('m', 'м') \
        .replace('o', 'о') \
        .replace('p', 'р') \
        .replace('t', 'т') \
        .replace('x', 'х') \
        .replace('y', 'у') \
        .replace('0', 'о') \
        .replace('3', 'з')
    return correct_data

