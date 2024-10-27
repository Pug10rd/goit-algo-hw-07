class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key
        self.height = 1  # Висота вузла

class AVLTree:
    def insert(self, root, key):
        # 1. Вставка звичайного вузла
        if not root:
            return TreeNode(key)
        elif key < root.val:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)

        # 2. Оновлення висоти вузла
        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))

        # 3. Отримання баланс-фактора
        balance = self.get_balance(root)

        # 4. Балансування дерева
        # Лівий лівий випадок
        if balance > 1 and key < root.left.val:
            return self.right_rotate(root)

        # Правий правий випадок
        if balance < -1 and key > root.right.val:
            return self.left_rotate(root)

        # Лівий правий випадок
        if balance > 1 and key > root.left.val:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)

        # Правий лівий випадок
        if balance < -1 and key < root.right.val:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root

    def left_rotate(self, z):
        y = z.right
        T2 = y.left
        y.left = z
        z.right = T2
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        return y

    def right_rotate(self, z):
        y = z.left
        T3 = y.right
        y.right = z
        z.left = T3
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        return y

    def get_height(self, root):
        if not root:
            return 0
        return root.height

    def get_balance(self, root):
        if not root:
            return 0
        return self.get_height(root.left) - self.get_height(root.right)

    def find_max(self, root):
        if root:   
            if root.right:
                return self.find_max(root.right)
        return root.val
    
    def find_min(self, root):
        if root:   
            if root.left:
                return self.find_min(root.left)
        return root.val
    
    def sum_all(self, root):
        if not root:
                return 0
        return root.val + self.sum_all(root.left) + self.sum_all(root.right)

# Приклад використання
avl_tree = AVLTree()
root = None
values = [3, 10, 201, 30, 99, 50, 25, 70, 56]

for value in values:
    root = avl_tree.insert(root, value)

# print("Preorder traversal of the constructed AVL tree is:")
# avl_tree.pre_order(root)

print(f'Max amount: {avl_tree.find_max(root)}')

print(f'Min amount: {avl_tree.find_min(root)}')

print(f'Whole amount: {avl_tree.sum_all(root)}')