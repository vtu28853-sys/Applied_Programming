import java.util.*;

class Solution {
    public int[] runningSum(int[] nums) {
        for (int i = 1; i < nums.length; i++) {
            nums[i] += nums[i - 1];
        }
        return nums;
    }
}

public class Main {
    public static void main(String[] args) {
        Solution sol = new Solution();

        int[] nums1 = {1, 2, 3, 4};
        System.out.println(Arrays.toString(sol.runningSum(nums1))); // [1, 3, 6, 10]

        int[] nums2 = {1, 1, 1, 1, 1};
        System.out.println(Arrays.toString(sol.runningSum(nums2))); // [1, 2, 3, 4, 5]

        int[] nums3 = {3, 1, 2, 10, 1};
        System.out.println(Arrays.toString(sol.runningSum(nums3))); // [3, 4, 6, 16, 17]
    }
}