import java.util.*;

class Solution {
  private List<Integer> aa = new ArrayList<>();

  public List<Integer> inorderTraversal(TreeNode root) {
    if (root != null) {
      inorderTraversal(root.left);
      aa.add(root.val);
      inorderTraversal(root.right);
    }
    return aa;
  }
}
