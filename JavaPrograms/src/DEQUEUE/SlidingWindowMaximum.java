package DEQUEUE;

import java.util.*;

public class SlidingWindowMaximum {

    public static void main(String[] args) {
        int[] nums = {1, 3, -1, -3, 5, 3, 6, 7};
        int k = 3;
        System.out.println(Arrays.toString(maxSlidingWindow(nums, k)));

    }

    public static int[] maxSlidingWindow(int[] nums, int k) {

        PriorityQueue<Integer> maxPQ = new PriorityQueue<>((o1, o2) -> (o2 - o1)); // stores values
        int n = nums.length;
        int[] result = new int[n - k + 1];
        if (nums.length == 0 || k == 0) {
            return new int[0];
        }

        for (int i = 0; i < k; i++) {
            maxPQ.add(nums[i]);
        }
        result[0] = maxPQ.peek();
        for (int i = k; i < nums.length; i++) {
            maxPQ.remove(nums[i - k]);
            maxPQ.add(nums[i]);
            result[i - k + 1] = maxPQ.peek();
        }

        return result;

    }

}
