#!/usr/bin/env python
# coding: utf-8

# In[7]:


get_ipython().system('pip install openai')
import fitz
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


# In[8]:


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

def find_most_common_keyword(text):
    """
    텍스트에서 가장 많이 사용되는 키워드 추출 (TF-IDF 기반)
    :param text: 추출된 텍스트
    :return: 가장 많이 사용되는 키워드
    """
    # 텍스트에서 알파벳과 한글 문자만 추출
    cleaned_text = re.sub(r'[^a-zA-Z가-힣]', ' ', text)
    
    # TfidfVectorizer를 이용하여 텍스트를 벡터화
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform([cleaned_text])
    
    # 각 단어의 TF-IDF 값 계산
    word_tfidf = dict(zip(vectorizer.get_feature_names(), tfidf_matrix.toarray()[0]))
    
    # 프로그래밍 코드나 숫자를 제외한 단어 추출
    keywords = [word for word in word_tfidf.keys() if not word.isdigit() and not re.match(r'^\W+$', word)]
    
    # TF-IDF 값이 가장 큰 단어 추출
    most_common_keyword = max(keywords, key=word_tfidf.get)
    
    return most_common_keyword

# PDF 파일 경로 지정
pdf_file_path = "C:\Processes.pdf"

# 텍스트 추출 함수 호출
text_list = extract_text_from_pdf(pdf_file_path)

# 각 페이지마다 텍스트와 가장 많이 사용되는 키워드 출력
for page_number, text in text_list:
    print("페이지 번호: ", page_number)
    print("텍스트: ", text)
    most_common_keyword = find_most_common_keyword(text)
    print("키워드: ", most_common_keyword)
    print("="*30)


# In[ ]:




