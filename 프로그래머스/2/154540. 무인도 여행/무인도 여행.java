import java.util.*;

class Solution {
    public int[] solution(String[] maps) {
        int x = maps.length;
        int y = maps[0].length();
        
        int[] dx = {0, 1, -1, 0 };
        int[] dy = {1, 0, 0, -1};
        
        int[][] map = new int[x][y];
        int[][] visited = new int[x][y];
        
        List<Integer> temp = new ArrayList<>();        
        //지도 생성
        for (int i = 0; i < x; i++){
            char[] z = maps[i].toCharArray();
            for (int j = 0; j < y; j++){
                if (z[j] == 'X'){
                    map[i][j] = -1;
                }
                else {
                    map[i][j] = z[j] - '0';
                }
            }
        }
        
        // 하나하나 탐색 
        for (int i = 0; i < x; i++){
            for (int j = 0; j < y; j++){
                if (visited[i][j] == 1){
                    continue;
                }
                if (map[i][j] == -1){
                    visited[i][j] = 1;
                    continue;
                }
                // 섬에 머무를수 있는 날짜
                int days = search(i, j, map, visited, dx, dy);
                temp.add(days);
            }
        }
        
        Collections.sort(temp);
        
        if (temp.size() == 0){
            int[] answer = {-1};
            return answer;
        }
        else{
            int[] answer = new int[temp.size()];
            for (int i = 0; i < temp.size(); i++){
                answer[i] = temp.get(i);
            }
            return answer;
            
        }
    }
    
    public int search(int x, int y, int[][] map, int[][] visited, int[] dx, int[] dy){
        int result = map[x][y];
        visited[x][y] = 1;

        for (int i = 0; i < 4 ; i++){
            int nextX = x + dx[i];
            int nextY = y + dy[i];
            // 밖으로 나가는거 처리
            try {
                int t = map[nextX][nextY];
            } catch (Exception e) {
                continue;
            }
            // 방문했거나 바다면 다음 탐색
            if (visited[nextX][nextY] == 1 || map[nextX][nextY] == -1){
                continue;
            }
            
            result += search(nextX, nextY, map, visited, dx, dy);
            
        }
        return result;
    }
}