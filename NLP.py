#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install openai')
import fitz
import math
import re
from collections import Counter
from sklearn.feature_extraction.text import TfidfVectorizer
import openai

openai.api_key = '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'

Lecture = input("강의명을 입력하세요: ")
Keyword = input("키워드: ")

prompt_text = "{}와 관련된 {}문제를 객관식으로 사용자가 선택할 수 있게 문제를 4지선다로 만들어주고 답도 알려줘.".format(Lecture, Keyword)

max_tokens = 3000

response = openai.Completion.create(
  engine="text-davinci-003",
  prompt=prompt_text,
  max_tokens=max_tokens,
)

generated_text = response.choices[0].text.strip()

if len(generated_text) < max_tokens:
    print(generated_text)
else:
    print(generated_text[:max_tokens])



# In[2]:


get_ipython().system('pip install rake-nltk')


# In[2]:


get_ipython().system('pip install PyMuPDF')


# In[3]:


def extract_text_from_pdf(file_path):
    """
    PDF 파일에서 각 페이지의 텍스트 추출
    :param file_path: PDF 파일 경로
    :return: 추출된 텍스트의 리스트, 각 원소는 (페이지 번호, 텍스트) 형태의 튜플
    """
    # PDF 파일 열기
    pdf_file = fitz.open(file_path)
    
    # 텍스트 추출
    extracted_text = []
    for page_number in range(pdf_file.page_count):
        page = pdf_file.load_page(page_number)
        text = page.get_text("text")
        extracted_text.append((page_number + 1, text))  # 페이지 번호는 0-based이므로 1을 더해줌
    
    # PDF 파일 닫기
    pdf_file.close()
    
    return extracted_text


# PDF 파일 경로 지정
pdf_file_path = "C:\네트워크.pdf"

# 텍스트 추출 함수 호출
text_list = extract_text_from_pdf(pdf_file_path)

# 각 페이지마다 텍스트 출력
for page_number, text in text_list:
    print("페이지 번호: ", page_number)
    print("텍스트: ", text)
    print("="*30)


# In[4]:


import fitz
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np
import re

def extract_text_from_pdf(file_path):
    # PDF 파일 열기
    pdf_file = fitz.open(file_path)
    
    # 텍스트 추출
    extracted_text = []
    for page_number in range(pdf_file.page_count):
        page = pdf_file.load_page(page_number)
        text = page.get_text("text")
        extracted_text.append((page_number + 1, text))  # 페이지 번호는 0-based이므로 1을 더해줌
    
    # PDF 파일 닫기
    pdf_file.close()
    
    return extracted_text

def find_previous_word(text, keyword):
    # 키워드 앞의 단어를 찾습니다.
    pattern = r'\b(\w+)\b\s+' + re.escape(keyword) + r'\b'
    match = re.search(pattern, text)
    return match.group(1) if match else keyword

# PDF 파일 경로 지정
pdf_file_path = "C:\\네트워크.pdf"

# 텍스트 추출 함수 호출
text_list = extract_text_from_pdf(pdf_file_path)

# 페이지별 텍스트를 리스트로 만듭니다.
documents = [text for page_number, text in text_list]

# 숫자와 단어의 조합이 아닌 숫자만 있는 텍스트는 배제하고, 길이가 3 이상인 단어만 포함하는 패턴
vectorizer = TfidfVectorizer(stop_words='english', token_pattern=r'\b[a-zA-Z_]\w{2,}\b')
tfidf_matrix = vectorizer.fit_transform(documents)

# 피처 이름들을 따로 저장합니다.
feature_names = vectorizer.get_feature_names_out()

# 각 문서에서 가장 높은 TF-IDF 점수를 가진 단어를 찾습니다.
keywords = []
for row in range(tfidf_matrix.shape[0]):
    col = np.argmax(tfidf_matrix[row, :].toarray())
    keyword = feature_names[col]
    # 동일한 키워드가 이미 등장한 경우 해당 키워드 바로 앞의 단어를 찾아 합칩니다.
    if keyword in keywords:
        page_text = documents[row]
        previous_word = find_previous_word(page_text, keyword)
        combined_keyword = previous_word + ' ' + keyword
        keywords.append(combined_keyword)
    else:
        keywords.append(keyword)

# 각 페이지에서 키워드를 출력합니다.
for page_number, keyword in enumerate(keywords, 1):
    print("페이지 번호: ", page_number)
    print("키워드: ", keyword)
    print("="*30)

