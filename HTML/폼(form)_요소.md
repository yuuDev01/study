# **📁 HTML Form**

사용자가 입력한 테이터를 웹 사이트에 전송하는 것

HTML form은 하나이상의 위젯으로 만들어짐. (위젯 : button, textfield, radio 버튼 등)

수집된 데이터는 웹서버에 전송되기 때문에 웹서버 설정이 필요함

## **📑 `<form> `** 

: **폼 사용을 위한 필수 요소. 폼의 범위를 나타낸다.**

```
<form>

   form 하위 요소들

</form>
```

**속성** 

action 데이터 전송할 url 지정

method http방식 지정 (GET : 데이터 얻음 / POST : 데이터 전송)

## **📑  `< button >`** 

버튼 태그
```
<form>
     <button class="btn1">button 요소</button>
</form>
```

    <form>
        <button class="btn1">button 요소</button>
    </form>



## **📑` < input >` **

 입력 필드 구현을 위한 태그

`<input type="속성값">`

| type 속성값 |   |
| --- | --- |
| button  | 버튼을 정의 |
| text  | 한 줄 텍스트 입력 필드를 정의 |
| radio | 라디오 버튼 정의. (라디오 버튼 : 하나만 선택할 수 있는 버튼) |
| password | 비밀번호 입력 필드. 마스크(\*)처리 되어 표시된다. |
| submit | 제출 버튼. form요소의 action속성에 정의된 url에 데이터 전송 |
| checkbox | 체크박스 정의  |
| image | 이미지로 submit 버튼 생성/ src 속성에 이미지 url 명시 |
| reset | 모든 폼 요소에 입력된 값을 초기화 하는 리셋 버튼 |
| color | 색을 선택할 수 있는 입력 필드. |
| hidden |  사용자에게 보이지 않는 숨겨진 입력 필드.  |
| email | 이메일 주소 입력 필드. required 속성으로 유효성 검사 |
| file  | 사용자의 로컬 파일을 선택하는 컨트롤 |
| datetime-local | 사용자가 날짜와 시간을 선택할 수 있는 컨트롤 |
| range | 범위 내 숫자 선택을 할 수 있는 슬라이더 바 |
| data | 날짜를 선택할 수 있는 컨트롤 |
| tel | 전화번호 입력 필드 |
| url | url 주소 입력 필드 |
| week | 날짜 선택 입력 필드 |
| time | 시간 선택을 할 수 있는 입력 필드 |
| search | 검색어 입력을 위한 입력 필드 |

👀 **`<button>` , `<input type="button">` 차이?**

button은 스스로 닫지 않는 태그, input은 스스로 닫은 태그 `<input type="button" />`

button 태그는 이미지 삽입 등 하위 태그를 추가할 수 있지만 input은 할 수 없다.

** 📑label  요소**

** 📑select 요소**

** 📑textarea 요소**

** 📑 option요소**

** 📑fieldset 요소**

** 📑 datalist요소**