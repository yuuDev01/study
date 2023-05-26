//출처: 프로그래머스 코딩 테스트 연습, https://school.programmers.co.kr/learn/courses/30/lessons/42748
import java.util.Arrays;

class Solution {
    public int[] solution(int[] array, int[][] commands) {
        int cnt2 =0;
        int[] answer = new int[commands.length];
        // commands 처리
        for(int[] arr : commands){
            int n1 = arr[0]; //첫번째요소
            int n2 = arr[1]; //두번째요소
            int cnt = 0;
            int[] sort = new int[n2-n1+1];
            //배열 자르기
            for(int i = n1-1; i <n2; i++){
                sort[cnt++] = array[i];
            }
            int min, temp;
            Arrays.sort(sort);
            int returnNum = arr[2]-1;
            answer[cnt2++] = sort[returnNum]; 
        }
      return answer;  
    }
}