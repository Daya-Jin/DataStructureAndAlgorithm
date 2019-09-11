class Solution {
public:
	ListNode* deleteDuplicates(ListNode* head) {
		ListNode* cur = head;
		if (cur == nullptr)
			return head;
		while (cur->next) {
			if (cur->next->val == cur->val)
				cur->next = cur->next->next;
			else
				cur = cur->next;
		}
		return head;
	}
};