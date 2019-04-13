
struct TreeNode* findMaxNode(struct TreeNode* root){
    if(!root)        //若树空则返回NULL
        return NULL;
    while(root->right != NULL)
        root = root->right;
    return root;
}

struct TreeNode* deleteNode(struct TreeNode* root, int key) {
    if(root == NULL)     //树为空
        return root;
    if(root->val > key)
        root->left = deleteNode(root->left, key);
    else if(root->val < key)
        root->right = deleteNode(root->right, key);
    else if(root->val == key)           //将删除双儿子节点的情况改为删除一个儿子节或无儿子节点的情况
    {
        struct TreeNode *tem;

        if(root->left && root->right) //删除的节点是双儿子节点 则用左子树的最大值取代该位置并删除掉该节点
        {
            tem = findMaxNode(root->left);
            root->val = tem->val;
            root->left = deleteNode(root->left, tem->val);
        }
        else        //删除的节点只有一个子节点或者无子节点
        {
            tem = root;
            if(root->left)
                root = root->left;
            else
                root = root->right;  //这里包含了无子树的情况，因为要么有右子树或者其为空
            free(tem);
        }
    }
    return root;
}
