class Solution {
public:
	vector<int> inorderTraversal(TreeNode* root) {
		vector<int> res;
		if (root == nullptr)
			return res;

		vector<TreeNode*> s;
		while (root or s.size())
		{
			while (root)
			{
				s.push_back(root);
				root = root->left;
			}

			TreeNode* vis_node = s.back();
			s.pop_back();
			res.push_back(vis_node->val);
			if (vis_node->right)
				root = vis_node->right;
		}

		return res;
	}
};