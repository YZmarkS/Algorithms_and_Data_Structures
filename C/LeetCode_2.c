#include <stdio.h>
#include <stdlib.h>

struct ListNode {
    int val;
    struct ListNode *next;
};

typedef struct NewNodePair {
  struct ListNode *new_node;
  int carry;
} NewNodePair;

NewNodePair* mkNewNodePair(int v1, int v2, int carry) {
  NewNodePair* result = (NewNodePair*)calloc(1, sizeof(NewNodePair));
  int sub_sum = v1 + v2 + carry;

  struct ListNode* new_node = (struct ListNode*)calloc(1, sizeof(struct ListNode));
  new_node->val = sub_sum % 10;
  new_node->next = NULL;

  result->new_node = new_node;
  result->carry = sub_sum / 10;

  return result;

}

struct ListNode* reverse(struct ListNode* l) {
  struct ListNode* front;
  struct ListNode* back;
  struct ListNode* next;

  if (l == NULL) {
    return l;
  }

  // n1
  // n1 -> n2
  // n1 -> n2 -> n3


  front = l->next;
  back = l;
  back->next = NULL;
  while (front != NULL) {
    next = front->next;
    front->next = back;
    back = front;
    front = next;
  }
  return back;
}

struct ListNode* addTwoNumbers(struct ListNode* l1, struct ListNode* l2) {

  // Edge case
  if (l1->val == 0 && l1->next == NULL) {
    return l2;
  } else if (l2->val == 0 && l2->next == NULL) {
    return l1;
  }

  int carry = 0;
  struct ListNode* result = NULL;
  while (l1 != NULL && l2 != NULL) {
    NewNodePair* new_node_pair = mkNewNodePair(l1->val, l2->val, carry);
    new_node_pair->new_node->next = result;
    result = new_node_pair->new_node;
    carry = new_node_pair->carry;

    l1 = l1->next;
    l2 = l2->next;
  }

  while (l1 != NULL) {
    NewNodePair* new_node_pair = mkNewNodePair(l1->val, 0, carry);
    new_node_pair->new_node->next = result;
    result = new_node_pair->new_node;
    carry = new_node_pair->carry;

    l1 = l1->next;
  }
  while (l2 != NULL) {
    NewNodePair* new_node_pair = mkNewNodePair(0, l2->val, carry);
    new_node_pair->new_node->next = result;
    result = new_node_pair->new_node;
    carry = new_node_pair->carry;

    l2 = l2->next;
  }

  if (carry == 1) {
    NewNodePair* new_node_pair = mkNewNodePair(0, 0, carry);
    new_node_pair->new_node->next = result;
    result = new_node_pair->new_node;
  }

  return reverse(result);
}

int main() {
  struct ListNode n1, n2, n3;
  n1.val = 2;
  n1.next = &n2;
  n2.val = 4;
  n2.next = &n3;
  n3.val = 3;
  n3.next = NULL;

  struct ListNode m1, m2, m3;
  m1.val = 5;
  m1.next = &m2;
  m2.val = 6;
  m2.next = &m3;
  m3.val = 4;
  m3.next = NULL;

  struct ListNode* result = addTwoNumbers(&n1, &m1);

  while (result != NULL) {
    printf("%d ", result->val);
    result = result -> next;
  }

  return 0;

}
