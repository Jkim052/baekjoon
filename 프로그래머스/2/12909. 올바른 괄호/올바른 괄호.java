import java.util.*;

class Solution {
    boolean solution(String s) {
        boolean answer = true;
        
        char[] charList = s.toCharArray();
        
        Stack<Character> stack = new Stack<>();

        
        for (char i : charList) {
            if (i == '(') {
                stack.push(i);
            }
            else {
                if (stack.size() == 0){
                    return false;
                }
                else {
                    stack.pop();
                }
            }
        }
        if (stack.isEmpty()){
            return true;
        }


        // [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
        System.out.println("Hello Java");

        return false;
    }
    
}