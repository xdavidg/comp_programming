import java.util.*;

public class LC3191 {
    public static void main(String[] args) {
        int[] nums = { 0, 1, 1, 1, 0, 0 };
        int operations = 0;

        for (int i = 0; i < nums.length - 2; i++) {
            if (nums[i] == 0) {
                nums[i] ^= 1;
                nums[i + 1] ^= 1;
                nums[i + 2] ^= 1;
                operations++;
            }
        }
        if (nums[nums.length - 1] == nums[nums.length - 2] && nums[nums.length - 1] == 1) {
            System.out.println(operations);
        } else {
            System.out.println(-1);
            System.out.println(Arrays.toString(nums));
        }

    }
}