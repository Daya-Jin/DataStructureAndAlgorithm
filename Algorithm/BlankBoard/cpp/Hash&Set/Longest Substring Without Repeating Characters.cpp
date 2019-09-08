class Solution {
public:
	int lengthOfLongestSubstring(string s) {
		int res = 0;
		int left = 0;
		unordered_map<char, int> lookup;

		for (int i = 0; i < s.size(); i++)
		{
			if (lookup.find(s[i]) == lookup.end())
				lookup[s[i]] = i;
			else
			{
				if (lookup[s[i]] >= lookup[s[left]])
					left = lookup[s[i]] + 1;
				lookup[s[i]] = i;
			}

			if (i - left + 1 > res)
				res = i - left + 1;
		}
		return res;
	}
};