#### **📝display 속성** :요소가 화면에서 어떻게 보여지도록 배치할지 결정하는 속성

> **속성값**

> **1\. 인라인 , 블록라인   
>   
> inline**  
> 해당 요소가 인라인 요소처럼 됨. 요소 내용만큼만 너비를 차지함  
> width, height 속성 적용x  
>   
> **block**  
> 해당 요소가 블럭 요소처럼 됨.   해당 라인의 너비를 모두 차지한다.  
>   
> **inlink-block**  
> 해당 요소가 인라인 요소처럼 배치되지만 블럭 요소의 성질을 가짐  
> 너비(width, height)를 적용할 수 있음  
> 
> ---
> 
>   
> 
> 👉 **span, div 태그** 
> 
>     <div\>블럭 요소 테스트</div\>
> 
>     <span\>인라인 요소 테스트</span\>
> 
> [##_Image|kage@ndTtg/btsgQoZtEiM/YyemETLLiKzyR2LWKA1yC1/img.png|CDM|1.3|{"originWidth":756,"originHeight":63,"style":"alignCenter"}_##]
> 
>   
>   
> 👉**span 태그 display 속성값을 block으로 지정**
> 
> div{
> 
>     border: 1px solid ;
> 
> }
> 
>   
> 
> span{
> 
>     display: block;
> 
>     border: 1px solid;
> 
> }
> 
> [##_Image|kage@dqKwJO/btsgTjXNt94/XvZdiXM7E7RnTdpSpcU18K/img.png|CDM|1.3|{"originWidth":756,"originHeight":64,"style":"alignCenter"}_##]  
>   
>   
>   
>   
> 
> ---
> 
>   
>   
> **2\. 자식 요소 배치 - 요소 내부 배치를 설정한다.**  
> **flew**  
> Flexible Box Layout  
> 단방향 레이아웃(1차원)  
> [##_Image|kage@bDqDW5/btsg1bxGFK3/gGfQGOCqi2ZYX8Xvyow2V1/img.png|CDM|1.3|{"originWidth":524,"originHeight":295,"style":"alignLeft","width":291,"height":164,"caption":"1. 속성값X&nbsp; &nbsp;2. display :flex 속성값"}_##]**  
> grid**  
> 두 방향(행렬) 2차원 레이아웃  
> flex 더 복잡한 레이아웃을 적용할 수 있다.  
>   
>   
> **table**  
> 요소를 table 처럼 배치  
> 동일한 간격과 넓이를 가질 수 있다.  
>   
> **  
> flow**  
>   
> **3\. 박스 배치**  
> **none**   
> 눈에 보이지 않음  
>   
>