import java.util.Arrays;

class LC2873 {
    public static long maximumTripletValue(int[] nums) {
        long triplet = -1;
        long maxNum = -1;
        long maxDiff = -1;

        for (int i = 0; i < nums.length; i++) {
            triplet = Math.max(triplet, (maxDiff * nums[i]));
            maxNum = Math.max(maxNum, nums[i]);
            maxDiff = Math.max(maxDiff, maxNum - nums[i]);
        }
        return triplet;
    }

    public static void main(String[] args) {
        int[] nums = { 1000000, 1, 1000000 };
        System.out.println(maximumTripletValue(nums));
    }
}