class Solution {
    public int singleNumber(int[] nums) {

        // HashSet<Integer> seen = new HashSet<Integer>();

        // for(int num : nums){
        //     if(seen.contains(num)){
        //         seen.remove(num);
        //     }else{
        //         seen.add(num);
        //     }
        // }
        // return seen.iterator().next();

        int res = 0;

        for(int num: nums){
            res ^= num;
        }
        return res;
        
    }
}
