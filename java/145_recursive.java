import java.util.*;

class Solution {
  private List<Integer> aa = new ArrayList<>();

  public List<Integer> postorderTraversal(TreeNode root) {
    if (root != null) {
      postorderTraversal(root.left);
      postorderTraversal(root.right);
      aa.add(root.val);
    }
    return aa;
  }
}
