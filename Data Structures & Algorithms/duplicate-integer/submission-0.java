class Solution {
    public boolean hasDuplicate(int[] nums) {
       Set<Integer> unique = new HashSet<>();
       for (int num : nums){
            if(unique.contains(num)){
                return true;
            }
            unique.add(num);
       }
       return false;
    }
}
