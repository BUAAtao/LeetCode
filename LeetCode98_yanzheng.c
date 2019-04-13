/**
 *解题思路：中序遍历，链栈
 * Definition for binary tree
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
  * };
 */
int flag;
struct Node{//创建一个链栈节点
    int val;
    struct Node *next;
};
struct Stack{//创建一个链栈
    struct Node *top;//指向链栈栈顶节点
    int count;//记录链栈的节点个数
};
void InitStack(struct Stack *stack){//初始化一个空栈
    stack->count = 0;
    stack->top = NULL;
}
void PushStack(struct Stack *stack,int val){//压栈
    struct Node *node;
    node = (struct Node *)malloc(sizeof(struct Node));
    if(stack->count > 0){
        if(stack->top->val < val){//若不是第一个进栈的节点，则判断与栈顶节点的值大小，若小于栈顶节点值则说明不是二叉搜索树
            node->val = val;
            node->next = stack->top;
            stack->top = node;
            stack->count++;
        }else{
            flag = -1;//若不是二叉搜索树设置全局标志位flag为-1;
            return;
        }
    }else{//第一个值进栈
        node->val = val;
        node->next = stack->top;
        stack->top = node;
        stack->count++;
    }
}
void Inorder(struct TreeNode *root,struct Stack *stack){//中序遍历
    if(root == NULL){
        return;
    }
    Inorder(root->left,stack);
    PushStack(stack,root->val);
    Inorder(root->right,stack);
}
bool isValidBST(struct TreeNode *root) {
    flag = 0;
    struct Stack *stack;
    stack = (struct Stack *)malloc(sizeof(struct Stack));
    InitStack(stack);
    Inorder(root,stack);
    if(flag == -1){
        return 0;
    }
    return 1;
}
