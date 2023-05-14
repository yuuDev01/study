### 📝  HTML(Hypertext Markup Language)이란?

✔ 웹 페이지의 구조적 의미를 나타내기 위해 사용되는 마크업 언어.
✔ 태그를 이용해 문서나 데이터의 구조를 명기한다.
✔ 요소와 속성으로 구성

 <br/>

**1. 요소(Elements)**
- 여는 태그, 닫는 태그, 내용(content)을 모두 합쳐 요소라고 한다.


**2. 속성(Attributes)**
- 요소에 대한 추가적인 정보를 제공
- 속성 이름(name)과  속성 값(value) 쌍으로 이루어짐
>   <태그명 속성="값">
 

 

 

 ---
 
 
### 📝  html 기본 구조
```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
   
</body>
</html>
```

<br/>
<br/><br/>

>**✏ `<!DOCTYPE html>`**
- DOCTYPE :  웹 문서가 어떤 형식으로 작성되었는지 정의하기 위해 선언하는 태그
-  HTML5는  <!DOCTYPE html> 라고 쓰면 됨

 

>**✏`<html lang="en"> ~ </html>`**
- html 문서의 최상위 요소. html이 작용하는 범위를 지정하는 태그
✔ lang 속성 : 문서의 주요 언어를 표기하는 속성. 영어는 en, 한국어는 ko 등으로 입력할 수 있다.

 

>**✏ `<head> ~ </head>`**
-  화면에 표시되진 않지만 웹 페이지를 표현하기 위해 필요한 해더 정보를 담고 있는 태그

 

>**✏ meta 태그**
- 메타데이터를 정의하는데 사용하는 태그
( 메타데이터 : 웹 페이지에 대한 정보)

 

>**✏` <meta charset="UTF-8">`**
- 인코딩 방식을 명시하는 태그
- 가변 크기 인코딩 방식. 가장 많이 사용됨

 

>**✏` <meta http-equiv="X-UA-Compatible" content="IE=edge">`**
- 모든 IE 브라우저에 호환성보기를 무시하게 된다.
✔ meta http-equiv

 

>**✏` <meta name="viewport" content="width=device-width, initial-scale=1.0">`**
<p>
✔ name속성 : 메타 정보의 이름을 명시한다. 
   viewport : 사용자가 볼 수 있는 화면의 창, 보이는 영역의 크기를 나타냄
<p>
✔ content 속성 : 뷰포트의 설정 값
width  : 뷰포트 크기.  device-width로 설정할 경우 뷰포트의 크기를 장치의 화면 너비로 함
initial-scale  : 뷰포트의 초기 배율을 설정. 소수값으로 한다.

 
>**✏ `<title>~</title>`**
- html 문서의 제목을 정의하는 태그
- 브라우저 상단에 표시된다.


>**✏` <body> ~ </body>`**
- html 문서의 내용를 지정하기 위한 태그