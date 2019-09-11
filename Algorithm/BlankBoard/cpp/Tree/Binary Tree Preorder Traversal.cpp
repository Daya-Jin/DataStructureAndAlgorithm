class Solution {
public:
	vector<int> preorderTraversal(TreeNode* root) {
		vector<int> res;
		if (root == nullptr)
			return res;

		vector<TreeNode*> s;
		s.push_back(root);

		while (s.size())
		{
			TreeNode* vis_node = s.back();
			s.pop_back();
			res.push_back(vis_node->val);
			if (vis_node->right)
				s.push_back(vis_node->right);
			if (vis_node->left)
				s.push_back(vis_node->left);
		}

		return res;
	}
};