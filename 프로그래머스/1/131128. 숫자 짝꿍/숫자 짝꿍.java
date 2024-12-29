import java.util.*;

class Solution {
    public String solution(String X, String Y) {
        StringBuilder sb = new StringBuilder();

		for (int i = 9; i > -1; i--) {
			int finalI = i;
			long xmin = X.chars().filter(ch -> ch == finalI + '0').count();
			long ymin = Y.chars().filter(ch -> ch == finalI + '0').count();

			long min = (xmin > ymin) ? ymin : xmin;

			for (int j = 0; j < min ; j++){
                if (sb.length() == 0 && i == 0){
                    sb.append(i);
                    break;
                }
				sb.append(i);
			}
		}
        if (sb.length() == 0){
            return "-1";
        }
        return sb.toString();
	}
}
