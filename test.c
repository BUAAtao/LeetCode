/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
struct TreeNode* deleteNode(struct TreeNode* root, int key) {
    struct TreeNode* q;
    struct TreeNode* s;
    searchBST(root, key);
    if( root->right == NULL ){
        q = root;
        root = root->left;
        free(q);
    }
    else if( root->left == NULL ){
        q = root;
        root = root->right;
        free(q);
    }
    else{
        q = root;
        s = root->left;
        while( s->right ){
            q = s;
            s = s->right;
        }
        root->val = s->val;
        if( q != root )
            q->right = s->left;
        else
            q->left = s->left;
        free(s);
    }
    return root;
}
struct TreeNode* searchBST(struct TreeNode* root, int key) {
    if(root == NULL||root->val == key)
        return root;
    else if(root->val > key)
        return searchBST(root->left, key);
    else
        return searchBST(root->right, key);
}










//C++修改
 struct TreeNode* deleteNode(struct TreeNode* root, int key) {
        if(root == NULL){
            return NULL;
        }
        struct TreeNode* node = root;
        struct TreeNode* lastNode=root;
            if(key < node->val){
                //删除节点的值小于当前节点，删除节点在左子树上
                root->left = deleteNode(root->left,key);
            }else if(key > node->val){
                //删除节点的值大于当前节点，删除的节点在右子树上
                root.right= deleteNode(root->right,key);
            }else{
                if(root->left == NULL || root->right == NULL){
                    //无子节点或仅有一个子节点
                    root = root->left == NULL ? root->right:root->left;
                }else{
                    //同时有左节点和右节点
                    struct TreeNode* cur = root->right;
                    while (cur->left != NULL) {
                    //找到右分支的最小值
                        cur = cur->left;
                    }
                root->val = cur->val;
                root->right = deleteNode(root->right, cur->val);
                }

        }
        return root;
    }
