class Solution {
public:
	void dfs(int idx, vector<int>& path, vector<vector<int>>& res, vector<int>& nums)
	{
		res.push_back(path);
		if (idx == nums.size())
			return;

		for (int i = idx; i < nums.size(); i++)
		{
			if (i > idx && nums[i] == nums[i - 1])
				continue;
			else
				path.push_back(nums[i]);
			dfs(i + 1, path, res, nums);
			path.pop_back();
		}
	}

	vector<vector<int>> subsetsWithDup(vector<int>& nums) {
		sort(nums.begin(), nums.end());
		vector<int> path;
		vector<vector<int>> res;
		dfs(0, path, res, nums);
		return res;
	}
};