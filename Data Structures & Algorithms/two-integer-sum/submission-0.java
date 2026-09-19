class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> hashMap = new HashMap<>();

        for (int i = 0; i < nums.length; i++){
            int num = nums[i];

            int diff = target - num;

            if (hashMap.containsKey(diff)){
                return new int[] {hashMap.get(diff), i};
            }
            hashMap.put(num,i);
        }
        return new int[] {};
    }
}
