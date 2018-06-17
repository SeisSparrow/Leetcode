import java.util.*;

class Solution {
  private List<Integer> aa = new ArrayList<>();

  public List<Integer> preorderTraversal(TreeNode root) {
    if (root != null) {
      aa.add(root.val);
      preorderTraversal(root.left);
      preorderTraversal(root.right);
    }
    return aa;
  }
}
