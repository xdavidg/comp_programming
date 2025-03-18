// package Java_Practice;  // Either keep this and use java Java_Practice.LC1
// or remove it and use java LC1

import java.util.HashMap;
import java.util.Map;

public class LC1 {
    public static void main(String[] args) {
        int[] nums = { 2, 7, 11, 5 };
        int target = 9;

        int[] result = twoSum(nums, target);

        if (result != null) {
            System.out.println("[" + result[0] + ", " + result[1] + "]");
        } else {
            System.out.println("None.");
        }
    }

    public static int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> diff_map = new HashMap<>();

        for (int i = 0; i < nums.length; i++) {
            int complement = target - nums[i];

            if (diff_map.containsKey(complement)) {
                return new int[] { diff_map.get(complement), i };
            }
            diff_map.put(nums[i], i);
        }

        return null;
    }
}