# django_mission_02-my970524
## ❗️ 프로젝트 소개
조건에 맞는 데이터베이스 모델링 하기

## ✅ Basic ver.
### FAQ 모델 생성하기
- 필요한 필드 : 질문, 카테고리, 답변, 생성자, 생성일시, 최종 수정자, 최종 수정일시

#### 🗒 ERD
![my_project_want_model-1](https://user-images.githubusercontent.com/76423946/164010144-187cf6ca-5f7e-45da-a9e9-2b18c1ef3dd3.png)
- User 모델은 장고의 기존 모델 사용
- Faq의 생성자(writer) 필드는 User 참조
- Faq의 최종 수정자 필드(updater)는 User와 N:N 관계 


## ✅ Challenge ver.
### Inquiry, Answer 모델 생성하기
- Inquiry 모델에서 필요한 필드 : 카테고리 글 제목, 이메일, 전화번호, 내용, 이미지 
- Answer 모델에서 필요한 필드 : 내용, 참조 문의글, 생성자, 생성일시, 최종 수정자, 최종 수정일시

#### 🗒 ERD
![my_project_want_model](https://user-images.githubusercontent.com/76423946/164011682-5242a45b-c921-409c-8929-377372d5670c.png)
- User 모델은 장고의 기존 모델 사용
- Inquiry와 Answer은 1:N 관계
- Answer의 참조 문의글inquiry) 필드는 Answer 참조
- Answer의 생성자(writer)필드는 User 참조
- Answer의 최종 수정자 필드(updater)는 User와 N:N 관계 

<hr/>

##### 📌 장고에서 모델링할 때 ManyToMany 필드를 적용하면 자동으로 중간 Mapping 테이블을 생성해줌
##### 📌 장고에서 pygraphviz 사용하여 자동으로 ERD 생성 가능
