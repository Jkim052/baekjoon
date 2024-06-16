class Solution {
    static int check (String bab){
        bab = bab.replace("aya", "1");
        bab = bab.replace("ye", "1");
        bab = bab.replace("ma", "1");
        bab = bab.replace("woo", "1");
        bab = bab.replace("1", "");
        if (bab.length() != 0) {
            return 0;
        }
        else{
            return 1;
        }
    }
    public int solution(String[] babbling) {
        int ans = 0;
        for (int i = 0; i < babbling.length; i++){
           ans += check(babbling[i]);
    }
        return ans;
    }
}