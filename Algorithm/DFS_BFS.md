**📎탐색 알고리즘 (Search Algorithim)** : 수많은 데이터 중 원하는 데이터를 찾기 위한 알고리즘
<br/>

# 📝 그래프(Graph)
> **G = (V,E)**
V(G) :그래프의 vertex들의 집합.  (  vertex =  node = 정점 )
V(E) : 그래프의 edge(간선)들의 집합
path : 한 노드에서 다른 노드로 가는 방법



### ✏ 그래프 표현
1. 인접 행렬(adjacency matrix) 
👉 2차원 배열로 나타낸다.
👉 graph[i][j] = 0 또는 1 ( 간선이 존재하면 1, 없으면 0)


2. 인접 리스트(adjacency list) 
👉 linked list로 표현


<br/>
<br/>

---

# 📝DFS(Depth-First Search)
👉 깊이 우선 탐색
👉 Stack

![](https://velog.velcdn.com/images/dev____123/post/95b53095-ccd4-4879-8f93-af080c2ab458/image.png)
: LIFO(List In First Out) 마지막에 들어온 데이터가 가장 먼저 나옴

> **파이썬에서 스택 구현 - 리스트 사용**
- 삽입 : 리스트명.append() #가장 뒤쪽에 데이터를 넣음
- 삭제 : 리스트명.pop() # 가장 뒤쪽 데이터를 꺼냄


#### 👉 동작 과정
탐색 시작노트(V) 방문. stack에 삽입 및 방문처리 - V의 인접노드 방문 W방문. stack에 삽입 및 방문처리 / 만약 방문할 인접 노드가 없으면 back tracking (방문하지 않은 노드가 없을 때 까지 반복)

#### 👉 재귀함수 또는 stack으로 표현 가능









<br/>
<br/>

---


# 📝BFS(Breadth-Frist Search)
#### 👉 너비 우선 탐색
#### 👉 Queue 

![](https://velog.velcdn.com/images/dev____123/post/83048a32-bc3b-4290-99aa-f07eae7ca87b/image.png)
: FIFO ( First In First Out) 먼저 들어온 데이터가 먼저 나옴

>**파이썬에서 큐 구현 - deque라이브러리 사용**
from collections import deque
queue = deque()
- 삽입 : 리스트명.append() # 가장 뒤쪽에 데이터를 넣음
- 삭제 : 리스트명.popeft() # 가장 앞쪽 데이터를 꺼냄


#### 👉 그래프 각 Level을 방문
#### 👉 동작 과정
탐색 시작노트(V) 방문. queue에 삽입 및 방문처리 - queue에서 노드을 꺼내어 인접 노드 중 방문하지 않는 인접노드를 모두 queue에 삽입 및 방분처리(이 과정 반복)


