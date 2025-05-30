import abc
from abc import ABC, abstractmethod

"""
This is the interface for the expression tree Node.
You should not remove it, and you can define some classes to implement it.
"""


class Node(ABC):

    @abstractmethod
    # define your fields here
    def evaluate(self) -> int:
        pass


class TreeNode(Node):

    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def evaluate(self) -> int:
        def exec(first, operator, second):
            if operator == "+":
                return first + second
            if operator == "-":
                return first - second
            if operator == "*":
                return first * second
            if operator == "/":
                return first / second

        def eval(node):
            if node.val not in {"+", "-", "*", "/"}:
                return int(node.val)
            first = eval(node.left)
            second = eval(node.right)
            return exec(first, node.val, second)
        return int(eval(self))


"""    
This is the TreeBuilder class.
You can treat it as the driver code that takes the postinfix input
and returns the expression tree represnting it as a Node.
"""


class TreeBuilder(object):
    def buildTree(self, postfix) -> 'Node':
        stack = []

        for exp in postfix:
            if exp in {"+", "-", "*", "/"}:
                second, first = stack.pop(), stack.pop()
                stack.append(TreeNode(exp, first, second))
            else:
                stack.append(TreeNode(exp))

        return stack[0]




if __name__ == '__main__':

    # Your TreeBuilder object will be instantiated and called as such:
    obj = TreeBuilder()
    expTree = obj.buildTree(["945955662","1","1","0","+","*","/"])
    ans = expTree.evaluate()
    print(ans)
