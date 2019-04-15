class Solution:
    def simplifyPath(self, path: str) -> str:
        path = path.split('/')
        stack = []
        for p in path:
            if p == '' or p == '.':
                continue
            elif p == '..':
                if stack:        #空链表不能使用pop(),此步骤防止开头为'..'
                    stack.pop()
            else:
                stack.append(p)
        return '/'+ '/'.join(stack)
