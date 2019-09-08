class Solution {
public:
	int numPermsDISequence(string S) {
		int n = S.size() + 1;
		vector<vector<int>> dp(n + 1, vector<int>(n + 1, 0));
		int mod = 1e9 + 7;
		dp[1][0] = 1;

		for (int i = 2; i < n + 1; i++)
		{
			for (int j = 0; j < i; j++)
			{
				if (S[i - 2] == 'I')
					for (int k = 0; k < j; k++)
						dp[i][j] = (dp[i][j] + dp[i - 1][k] % mod) % mod;
				else
					for (int k = j; k < i; k++)
						dp[i][j] = (dp[i][j] + dp[i - 1][k] % mod) % mod;
			}
		}

		int res = 0;
		for (int i = 0; i < n + 1; i++)
			res = (res + dp[n][i] % mod) % mod;

		return res;
	}
};