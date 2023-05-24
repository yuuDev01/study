# **📁 테이블(table)** 

**행과 열로 구성된 2차원 데이터**


### **👉 테이블의 기본 구조**

```
    <table>
        <tr>
            <th>th (1,1)</th>  
            <th>th (1,2)</th>  
        </tr>
        <tr>
            <td>td1 (2,1)</td>
            <td>td1 (2,2)</td>
        </tr>
        <tr>
            <td>td2 (3,1)</td>
            <td>td2 (3,2)</td>
        </tr>      
    </table>
```

**👉 실행 결과**
<table>
        <tr>
            <th>th (1,1)</th>  
            <th>th (1,2)</th>  
        </tr>
        <tr>
            <td>td1 (2,1)</td>
            <td>td1 (2,2)</td>
        </tr>
        <tr>
            <td>td2 (3,1)</td>
            <td>td2 (3,2)</td>
        </tr>      
    </table>



---

## **🔍 구성 요소**

### **📑 `<table> `** 

테이블을 만들기 위해 필요한 태그

`<table>~</table>` 사이에 자식요소  `<tr>` 태그가 하나 이상 들어간다. 

### **📑 ` <tr> `** 

#### 테이블의 행을 정의한다. 

자식요소로 < td > 와 < th >요소를 사용하여 행의 셀을 설정할 수 있다.

### **📑 ` <th>`**

테이블의 제목 셀을 정의한다.

### **📑 ` <td>`**

테이블의 셀 내용을 정의한다.

▪ rowspan 속성 :  세로 셀 병합
▪ colspan  속성 :  가로 셀 병합


### **📑 ` <caption>` **
테이블의 제목이나 설명을 나타낼 때 사용
</br>

### **📑  테이블의 세부구조  - 태그 생략 가능, 영역의 구분을 원할 때 사용**

▪`<thead>` 머리글. 테이블 상단 열의 head를 정의하는 일련의 행을 정의

▪`<tbody>` 본문. 테이블의 tr을 묶어서 테이블 본문을 구성한다.

▪`<tfoot>` 꼬리말. 테이블의 하단에서 tbody의 행을 요약한다. 

>ex)

```
    <table>
        <caption>테이블 caption 요소</caption>
        <tr>         
        </tr>
        <thead>
            <tr>
                <th colspan="2">thead th 요소</th>           
            </tr>
        </thead>
        <tbody>
            <tr>
                <td>td1</td>
                <td>td1</td>
            </tr>
            <tr>
                <td>td2</td>
                <td>td2</td>
            </tr>   
            <tr>
                <td rowspan="3">td3</td>
                <td>td3</td>
            </tr>      
            <tr>
                <td>td4</td>
            </tr>  
            <tr>
                <td>td5</td>
            </tr>  
        </tbody>
        <tfoot>
            <tr>
                <td>footer</td>
                <td>footer</td>
            </tr>
        </tfoot>
    </table>
```

**👉 실행 결과**
 <table>
        <caption>테이블 caption 요소</caption>
        <tr>         
        </tr>
        <thead>
            <tr>
                <th colspan="2">thead th 요소</th>           
            </tr>
        </thead>
        <tbody>
            <tr>
                <td>td1</td>
                <td>td1</td>
            </tr>
            <tr>
                <td>td2</td>
                <td>td2</td>
            </tr>   
            <tr>
                <td rowspan="3">td3</td>
                <td>td3</td>
            </tr>      
            <tr>
                <td>td4</td>
            </tr>  
            <tr>
                <td>td5</td>
            </tr>  
        </tbody>
        <tfoot>
            <tr>
                <td>footer</td>
                <td>footer</td>
            </tr>
        </tfoot>
    </table>

</br>
</br>

### **📑 테이블의 열 정보**

▪`<col>` 테이블의 열에 속하는 칸에 공통된 의미를 부여할 때 사용

- span 속성 : 의미를 부여할 열을 나타냄, 속성값으로 열 번호(1,2,...)를 넣는다.

`<colgroup>` 테이블의 열을 그룹으로 묶음

```
<colgroup>
    <col span="열 번호" />
    <col span="열 번호"  />  
</colgroup>
```


> ex)

**◼ html**

```
    <table>
        <colgroup>
            <col span="1" class="col1"> 
            <col span="2" class="col2"> 
        </colgroup>
        <tr>
            <th>1열</th>  
            <th>2열</th>  
        </tr>
        <tr>
            <td>td1 요소</td>
            <td>td1 요소</td>
        </tr>
        <tr>
             <td>td2 요소</td>
             <td>td2 요소</td>
        </tr>      
    </table>
```


**👉 실행 결과**
<table>
        <colgroup>
            <col span="1" class="col1"> 
            <col span="2" class="col2"> 
        </colgroup>
        <tr>
            <th>1열</th>  
            <th>2열</th>  
        </tr>
        <tr>
            <td>td1 요소</td>
            <td>td1 요소</td>
        </tr>
        <tr>
             <td>td2 요소</td>
             <td>td2 요소</td>
        </tr>      
    </table>