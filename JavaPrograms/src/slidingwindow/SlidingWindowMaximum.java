package slidingwindow;

import java.util.Deque;
import java.util.LinkedList;

public class SlidingWindowMaximum {
    public int[] maxSlidingWindow(int[] nums, int k) {

        int[] ans = new int[nums.length - k + 1];
        int j = 0;
        Deque<Integer> q = new LinkedList<>();

        for (int i = 0; i < nums.length; i++) {

            // if left value is out of bounds, remove left value

            if (!q.isEmpty() && q.peekFirst() < i - k + 1) {
                q.pollFirst();
            }


            // Remove Smaller values from last
            while (!q.isEmpty() && nums[i] > nums[q.peekLast()]) {
                q.pollLast();
            }
            q.add(i);

            if (i >= k - 1) {
                ans[j++] = nums[q.peekFirst()];
            }

        }
        return ans;

    }
}