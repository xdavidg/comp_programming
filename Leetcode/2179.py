def goodTriplets(nums1, nums2):
    value_to_index = {num: i for i, num in enumerate(nums1)}
    sorted_indices = []
    total_triplets = 0

    for val in nums2:
        index_in_nums1 = value_to_index[val]

        left_count = _binary_search_insert_position(sorted_indices, index_in_nums1)

        right_count = (len(nums1) - 1 - index_in_nums1) - (
            len(sorted_indices) - left_count
        )

        total_triplets += left_count * right_count

        insert_pos = _binary_search_insert_position(sorted_indices, index_in_nums1)
        sorted_indices.insert(insert_pos, index_in_nums1)
    
    return total_triplets


def _binary_search_insert_position(self, lst, target):
    low, high = 0, len(lst)

    while low < high:
        mid = (low + high) // 2
        if lst[mid] < target:
            low = mid + 1
        else:
            high = mid

    return low


def main():
    pass


if __name__ == "__main__":
    main()
