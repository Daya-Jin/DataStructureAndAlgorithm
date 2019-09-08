class Solution {
public:
	void reverse(vector<int>& nums, int start, int end) {
		while (start < end)
		{
			int tmp = nums[start];
			nums[start] = nums[end];
			nums[end] = tmp;
			start += 1; end -= 1;
		}
	}

	void rotate(vector<int>& nums, int k) {
		int n = nums.size();
		k %= n;

		reverse(nums, 0, n - k - 1);
		reverse(nums, n - k, n - 1);
		reverse(nums, 0, n - 1);
	}
};