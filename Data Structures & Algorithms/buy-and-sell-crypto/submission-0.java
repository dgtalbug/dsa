class Solution {
    public int maxProfit(int[] prices) {

       int left = 0, right = 0 ;
       int maxProfit = 0;

       while (right < prices.length - 1){
         if(prices[left] < prices[right]){
            int profit = prices[right] - prices[left];
            maxProfit = Math.max(profit, maxProfit);
         }else{
            left = right;
         }
        right++;
       }
       return maxProfit;
        
        
    }
}
