# **📁 Vue.js 란?**

\-  MVVM 패턴에서 view model에 해당하는 화면단 라이브러리

(\* MVVM 패턴 : Model - View - View Model)

**👉 View**

\- 보이는 화면 

\- 돔(Dom) : Html 문서에 들어가는 요소의 정보를 담고 있는 데이터 트리

**👉  Model**

\- 데이터 관리

\- 데이터를 JavaScript 객체 형태로 저장

**👉  View Model(**⬅Vue.js )

\- View 와 Model 의 중간 역역

\- 돔 리스너와 데이터 바인딩을 제공하는 영역

( \* 돔 리스너 : 돔의 변경 내역에 대해 즉각적으로 반응하여 특정 로직을 수행하는 장치)

(ex)

어떤 사이트(view)에서 무언가를 검색(검색을 감지하여돔 리스너에서 로직처리), 해당 데이터를 가져와(모델) 화면에 나타냄(데이터 바인딩)

👉 Vue : 화면 요소가 변경 or 조작이 일어날 때 즉각적으로 반응하여 화면의 데이터를 갱신하여 보여주는 역할

---

### **📝 Vue.js 의 특징** 

**1)  Component 컴포넌트 기반 프레임워크** 

\- 코드 재사용이 쉬움

\- 각 영역을 컴포넌트로 구분하여 이를 조합하여 화면을 구성할 수 있다

**2) 양방향 데이터 바인딩, 단방향 데이터 흐름을 결합한 프레임워크**

\- 양방향 데이터 바인딩 : 화면에 표시되는 값과 프레임워크의 모델 데이터 값이 동기화되어 한쪽이 변경되면 다른 한쪽도 자동으로 변경됨

\- 단방향 데이터 흐름 :  컴포넌트의 단방향 통신 . 컴포넌트간 데이터 전달 시 상위→하위 방향으로만 전달

\- 가상돔 렌더링 방식 적용 : 특정 돔 요소 변경 시 화면을 다시 그리지 않고 프레임 워크에서 정의한 방식으로 화면 갱신)

(\*렌더링 : 브라우저에 웹 페이지를 그려내는 동작)

\- 리액트와 앵귤러의 장점을 모두 가진다.

Vue Angular 프레임워크

React  라이브러리