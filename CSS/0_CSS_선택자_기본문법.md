

  
  # **📝 CSS (Cascading Style Sheets) 란?**

✔ 웹페이지의 디자인과 레이아웃을 제어하는 스타일 시트 언어  
 
 </br>
 </br> </br>
 

---

 
## **👀 선택자(Selector) 란?**
: 스타일을 적용하고 싶은 html 요소를 선택하는 요소

> **선택자 { 스타일 속성1, : 스타일 값1; **스타일 속성2, : 스타일 값2;**  ...  }**   
>   
> ex)   
> body { background-color : black; }


<br/>

**👉  전체 선택자 \*** 
: 모든 요소를 선택
``` 
* { margin: 10px; } //모든 요소에 마진 10px를 줌 
```
<br/>

**👉 id 선택자 #**
: 특정 아이디 요소를 선택
```　
<div id="my\_id"> 

#my\_id{ 속성:값 }

```
<br/>

**👉 클래스 선택자  .**

해당 클래스 요소 선택

``` 
<div class="my\_class">

  #my\_class{ 속성:값 } 
``` 

> **✔ id 선택자와 클래스 선택자 차이?**  
> id 선택자는 유일한 값으로 한 번만 사용 가능하지만 클래스 선택자는 여러 요소에 중복으로 값을 넣을 수 있다.   
> 아이디와 클래스 선택자가 중복 정의할 경우 우선순위 : 아이디 선택자 > 클래스 선택자

**👉 태그 선택자**

: html 태그를 선택
```
p { 속성: 값 }  // p태그에 속성 값을 줌 
```
✔ 여러 선택자를 선택할 경우 ,를 사용한다. ex ) h1, h2, h3 { }
<br/>
**👉속성 선택자 : 특정 속성을 갖는 HTML의 요소를 선택**

| 사용 방법|  |
| --- | --- |
|  태그명\[속성\] | 특정 속성을 가진 태그를 선택.  img\[src\]{ 속성:값 }  |
| 태그명\[속성 = 값\]  | 특정한 속성 값을 가진 태그를 선택 |
  
<br/>

  
  
** 👉자손 선택자 : 선택자A > 선택자B **
선택자A 바로 밑의 자식 중 선택자B를 선택
<br/>
  
**👉후손 선택자 : 선택자A 선택자B**
선택자A의 **모든 하위요소** 중 선택자B를 선택
<br/>

  
> ex)   
```
<div id="p1">
        <p>1번</p>
        <div>
            <p>2번</p>
        </div>
        <p>3번</p>
</div> 
``` 
✏ 자손 선택자
```
#p1 > p{
            background-color: yellow;
        }
```
![](https://velog.velcdn.com/images/dev____123/post/81add300-762f-43a0-b0f5-c2c7fd780ced/image.png)
✏ 후손 선택자
```
#p1 p{
            background-color: yellow;
        }
```
![](https://velog.velcdn.com/images/dev____123/post/2f7f67ee-e152-419d-a029-79ad25a4f61e/image.png)


**👉동위 선택자 선택자A + 선택자 B**
선택자A와 인접한 선택자B를 선택

<br/><br/>


----



## **✍ CSS 기본 속성 정리**

(단축 속성 :서로 다른 여러 가지 CSS 속성의 값을 지정할 수 있는 CSS 속성)

</br>

**👉박스 관련 속성**
<table>
	<tr>
    	<th>박스 관련 속성</th>
    </tr>
    <tr>
    	<td>border</td>
        <td>
        박스 요소의 테두리를 지정하는 단축 속성
        </td>
    </tr>
    <tr>
    	<td>margin</td>
        <td>
        border와 요소의 바깥쪽의 사이 간격의 크기 설정
        </td>
    </tr>
    <tr>
    	<td>padding</td>
        <td>
        border와 내용(content) 사이 간격의 크기 설정
        </td>
    </tr>
    <tr>
    	<td>width</td>
        <td>요소 크기의 너비</td>
    </tr>
        <tr>
    	<td>height</td>
        <td>요소 크기의 높이</td>
    </tr>
        <tr>
    	<td>background-color</td>
        <td>요소의 내용과 padding 배경 색 지정</td>
    </tr>
    </tr>
        <tr>
    	<td>background-color</td>
        <td>요소의 내용과 padding 배경 색 지정</td>
    </tr>
    </tr>
        <tr>
    	<td>color</td>
        <td>요소의 글자색 지정</td>
    </tr>
    </tr>
        <tr>
    	<td>text-shadow</td>
        <td>요소의 글자에 그림자를 적용</td>
    </tr>
</table>

</br>
</br>

**👉 글꼴 관련 속성**
<table>
	<tr>
    	<th>글꼴 관련 속성</th>
    </tr>
    <tr>
    	<td>font</td>
        <td>
        단축 속성
        </td>
    </tr>
    <tr>
    	<td>font-size</td>
        <td>
        글꼴 크기 지정
        수치에 단위를 붙여 지정
        (normal, number, length, percentage)
        </td>
    </tr>
    <tr>
    	<td>font-style</td>
        <td>글꼴 모양새를 지정. 
        italic(기울기), normal </td>
    </tr>
    <tr>
    	<td>font-family</td>
        <td>글꼴 지정 </td>
    </tr>
        <tr>
    	<td>font-weight</td>
        <td> 두께 지정 bold / noraml</td>
    </tr>
        <tr>
    	<td>line-height</td>
        <td>줄 간격을 수치로 지정</td>
    </tr>
</table>

