public class LC2401 {
    public static void main(String[] args) {
        int[] nums = { 1, 3, 8, 48, 10 };

        System.out.println(nice_sub(nums));
    }

    public static int nice_sub(int[] nums) {
        int curr, left, max_length;
        curr = left = max_length = 0;

        for (int right = 0; right < nums.length; right++) {
            while ((curr & nums[right]) != 0) {
                curr = curr ^ nums[left++];
            }
            curr = curr | nums[right];
            max_length = Math.max(max_length, right - left + 1);
        }

        return max_length;
    }
}