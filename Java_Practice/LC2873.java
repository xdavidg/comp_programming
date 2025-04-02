import java.util.Arrays;

class LC2873 {
    public static long maximumTripletValue(int[] nums) {
        int[] small = { -1, Integer.MAX_VALUE };
        int[] big = { -1, -1 };
        int mid = -1;
        int answer = 0;

        for (int i = 0; i < nums.length; i++) {
            if (nums[i] > big[1]) {
                big[1] = nums[i];
                big[0] = i;
            } else if (nums[i] < small[1]) {
                small[1] = nums[i];
                small[0] = i;
            }
        }
        if (small[0] > big[0]) {
            for (int i = small[0]; i < nums.length; i++) {
                if (nums[i] > mid)
                    mid = nums[i];
            }
            if (mid == -1)
                answer = 0;
            else
                answer = (big[1] - small[1]) * mid;
        } else if (big[0] > small[0]) {
            for (int i = 0; i < small[0]; i++) {
                if (nums[i] > mid)
                    mid = nums[i];
            }
            if (mid == -1)
                answer = 0;
            else
                answer = (mid - small[1]) * big[1];
        }
        if (answer > 0) {
            return answer;
        } else {
            return 0;
        }
    }

    public static void main(String[] args) {
        int[] nums = { 1, 10, 3, 4, 19 };
        System.out.println(maximumTripletValue(nums));
    }
}