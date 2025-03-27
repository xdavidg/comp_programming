import java.util.*;

public class LC2780 {

    public int minimumIndex(List<Integer> nums) {

        int freq_count = -1;
        int most_freq = -1;
        Map<Integer, Integer> nums_count = new HashMap<>();
        for (int num : nums) {
            nums_count.put(num, nums_count.getOrDefault(num, 0) + 1);
            if (freq_count < nums_count.get(num)) {
                most_freq = num;
                freq_count = nums_count.get(num);
            }
        }

        int capacity = nums.size();

        if (capacity / 2 > freq_count)
            return -1;

        boolean left = false;
        int counts = 0;
        int i = 0;

        while (!left) {
            if (nums.get(i) == most_freq)
                counts++;
            if ((i + 1) / 2 < counts) {
                left = true;
                break;
            }
            i++;
        }

        if ((capacity - i - 1) / 2 < freq_count - counts) {
            return i;
        }
        return -1;
    }

    public static void main(String[] args) {
        LC2780 obj = new LC2780();
        List<Integer> nums = new ArrayList<>(Arrays.asList(1, 2, 2, 2));
        System.out.println(obj.minimumIndex(nums));
    }
}