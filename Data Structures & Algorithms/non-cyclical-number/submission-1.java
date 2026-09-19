class Solution {
    public boolean isHappy(int n) {
        HashSet<Integer> visited = new HashSet<Integer>();

        while(!visited.contains(n)){
            visited.add(n);
            n = sumOfSquares(n);
            if (n == 1){
                return true;
            }
        }
        return false;
    }

    public int sumOfSquares(int n){
        int result = 0;

        while(n!=0){
            int digit = n % 10;
            digit = digit * digit;
            result += digit;
            n = n / 10;
        }
        return result;
    }
}
