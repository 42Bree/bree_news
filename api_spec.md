# 검색  뉴스

 뉴스 검색 시스템을 keyword랑 writer을 사용해 검색할 수 있게끔 만들었습니다.
  옵션에는 정확도와 최신순으로 결과 값을 정렬할 수 있게끔 설정해 뒀고 
  그 외에 사용자가 원하면 뉴스 검색 기간 설정도 할 수 있습니다. 

## 1. API 기본 정보

   메써드          인증      요청 URL   출력 포맷    
 ------------  -----------  --------------  ------------------------------------ 
   GET    &nbsp;    -  http127.0.0.15000keyword_resultkeyword={keyword}&operator={operator}&start={start}&end={end}  HTML      
   GET    &nbsp; &nbsp;    -  http127.0.0.15000writer_resultwriter={writer}&operator={operator}&start={start}&end={end}  HTML    


## 2. 요청 변수 (request parameter) - 기사검색

 요청변수   타입   필수 여부   기본값  설명 
 ----------  ---------  --------------  --------  --------- 
 keyword  string  Y    검색하고자 하는 키워드를 받습니다. 제목  본문 순으로 검색 결과를 도출합니다 
 operator  string  N  정확도순  정확도순과 최신순으로 결과 값들을 정렬합니다. 
 start  string  N  2015-01-01  검색하고자 하는 날짜의 start date 값입니다 (Optional) 
 end  string  N  now  검색하고자 하는 날짜의 end date 값입니다 (Optional) 


## 2. 요청 변수 (request parameter) - 기자검색

 요청변수   타입   필수 여부   기본값  설명 
 ----------  ---------  --------------  --------  --------- 
 keyword  string  Y    검색하고자 하는 키워드를 받습니다. 제목  본문 순으로 검색 결과를 도출합니다 
 operator  string  N  정확도순  정확도순과 최신순으로 결과 값들을 정렬합니다. 
 start  datetime  N  2015-01-01  검색하고자 하는 날짜의 start date 값입니다 (Optional) 
 end  datetime  N  now  검색하고자 하는 날짜의 end date 값입니다 (Optional) 

## 3. 출력 결과

 필드   타입     설명   
--------------------  --------------  
 title    string  기사의 제목을 return한다 
 body   string  기사의 본문기사를 return한다 
 regdate  datetime  기사가 쓰여진 기간을 return한다 
 moddate  datetime  기사 최정 수정일자를 return한다  
 cpname    string  기사를 쓴 출판사명을 return한다 
 writer   string  기사를 쓴 기자의 이름을 return한다 
 images     string  기사에 쓰였던 이미지들의 링크를 return한다 
 html        string  가지고 있는 기사의 위치를 return한다  
 category     string  기사의 카테고리를 return한다 
 url        string  기사의 url 주소를 리턴한다  

## 4. 요청 예시

   메써드          요청 예시      
 ------------  -----------  
   GET    &nbsp;    http127.0.0.15000keyword_resultkeyword=%EC%98%81%ED%99%94%EA%B0%90%EB%8F%85&operator=%EC%A0%95%ED%99%95%EB%8F%84%EC%88%9C&start=20160729&end=20200729  
   GET    &nbsp; &nbsp;    http127.0.0.15000writer_resultwriter=%EB%B0%95%EB%8C%80%EA%B8%B0+%EA%B8%B0%EC%9E%90&operator=%EC%A0%95%ED%99%95%EB%8F%84%EC%88%9C&start=&end=  
