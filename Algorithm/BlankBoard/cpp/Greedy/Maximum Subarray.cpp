/*https://leetcode.com/problems/maximum-subarray/
思路：线性扫描，维护一个最大和与当前和。若当前和小于 0 ，则将cur_sum置零重新开始加和。*/


int maxSubArray(vector<int>& nums) {
	int res=-0x80000000;
	int cur_sum=0;
	
	for(int i=0;i<nums.size();i++)
	{
		if(cur_sum<0)
			cur_sum=nums[i];
		else
			cur_sum+=nums[i];
		res=max(res,cur_sum);
	}
	return res;
}