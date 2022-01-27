# O(N) time
class ListNode:
  def __init__(self, val, next=None):
    self.val = val
    self.next = next

  def reverse_linked_list(self, head):
      prev = None
      current = head
  
      while(current):
          temp = current.next
          current.next = prev
          prev = current
          current = temp
      return prev
