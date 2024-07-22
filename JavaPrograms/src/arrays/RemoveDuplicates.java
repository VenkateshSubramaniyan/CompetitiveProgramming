package arrays;

public class RemoveDuplicates {

    public static void main(String[] args) {
//        int[] nums = {1,1,1,2,2,3};
        int[] nums = {0, 0, 1, 1, 1, 1, 2, 3, 3};
        System.out.println(removeDuplicates(nums));
    }

    public static int removeDuplicates(int[] nums) {

        int slow = 0;
        int fast = 1;
        int count = 0;
        if (nums.length == 1) count = 1;

        while (fast <= nums.length - 1) {
            if (nums[slow] + 1 == nums[fast]) {
                count++;
                slow = fast;
                fast++;

            } else if (nums[slow] == nums[fast]) {
                count++;
                slow = fast;
                fast++;
                while (nums[slow] + 1 == nums[fast] && fast <= nums.length - 1) fast++;

            } else {

            }

        }

        return count;

//
//
//        int left=1;
//        int right=nums.length-1;
//        int count=0;
//
//        while(left<right){
//            if( left+2<nums.length-1 && nums[left]==nums[left+2] ){
//                int swapper=left;
//                while (swapper<=right){
//                    nums[swapper]=nums[swapper+1];
//                }
//                right--;
//            }else {
//                left++;
//            }
//
//        }
//
//

    }
}
