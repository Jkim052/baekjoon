class Solution {
    public int solution(int price) {
        if (price < 100000){
            price = price;
        }
        else if (price < 300000) {
            price = (int) (0.95 * price);
        }
        else if (price < 500000) {
            price = (int) (0.9 * price);
        }
        else {
            price = (int) (0.8 * price);
        }
        int answer = 0;
        return price;
    }
}