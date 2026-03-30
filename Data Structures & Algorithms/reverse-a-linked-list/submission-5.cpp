/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */


// x[int](x0101)    curr[x0101](x0102)
// curr  prints the address curr is holding x0101
// *curr prints int 
// &curr print x0102
// *curr = 10, changes int to 10

class Solution
{
    public:
        ListNode* reverseList(ListNode* head)
        {
            ListNode* curr = head;
            ListNode* prev = nullptr;

            while(curr)
            {
                ListNode* temp = curr->next;

                curr->next = prev;
                prev = curr;
                curr = temp;

            }

            return prev;

        }

};