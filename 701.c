//方法一
void TreeNode *insertIntoBST(TreeNode *root, int val){
    insert(root, val);
    return root;
}
void insert(TreeNode* root, int val)
    {
        struct TreeNode *s;
        s = (struct TreeNode *)malloc(sizeof(struct TreeNode));
        s->val = val;
        s->left = NULL;
        s->right = NULL;
        if(root == NULL)
            root = s;
        struct TreeNode* ptr = root;
        while(true)
        {
            if(val < ptr->val)
            {
                if(ptr->left == NULL)
                {
                    ptr->left = s;
                    break;
                }
                else
                    ptr = ptr->left;
            }
            else
            {
                if(ptr->right == NULL)
                {
                    ptr->right = s;
                    break;
                }
                else
                    ptr = ptr->right;
            }
        }
        return root;
    }

//方法二
struct TreeNode* insertIntoBST(struct TreeNode* root, int val) {
    if(root == NULL){
        root = (struct TreeNode *)malloc(sizeof(struct TreeNode));
        root->val = val;
        root->left = NULL;
        root->right = NULL;
    }
    if(root->val > val)
        root->left = insertIntoBST(root->left, val);
    if(root->val < val)
        root->right = insertIntoBST(root->right, val);
    return root;
    }
