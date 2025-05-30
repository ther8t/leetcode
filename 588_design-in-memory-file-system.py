import re

TYPE_D, TYPE_F = "d", "f"


class TreeNode:
    def __init__(self, name, type, contents=None):
        self.name = name
        self.type = type
        self.contents = contents
        self.children = {}

    def add_child(self, node):
        self.children[node.name] = node


class FileSystem:

    def __init__(self):
        self.root = TreeNode("", TYPE_D)

    def ls(self, path: str):
        if path[-1] == "/":
            path = path[:-1]
        temp = self.root
        path = re.split("\/", path)
        ptr = 0
        while ptr + 1 < len(path):
            temp = temp.children[path[ptr + 1]]
            ptr += 1

        if temp.type == TYPE_D:
            return sorted(temp.children.keys())
        else:
            return sorted([temp.name])

    def mkdir(self, path: str) -> None:
        temp = self.root
        path = re.split("\/", path)
        ptr = 0
        while ptr < len(path) - 1:
            if path[ptr + 1] in temp.children:
                temp = temp.children[path[ptr + 1]]
            else:
                temp.add_child(TreeNode(path[ptr + 1], TYPE_D))
                temp = temp.children[path[ptr + 1]]
            ptr += 1

    def addContentToFile(self, filePath: str, content: str) -> None:
        temp = self.root
        path = re.split("\/", filePath)
        file_name = path[-1]
        path = path[:-1]
        ptr = 0
        while ptr + 1 < len(path):
            if path[ptr + 1] in temp.children:
                temp = temp.children[path[ptr + 1]]
            else:
                temp.add_child(TreeNode(path[ptr + 1], TYPE_D))
                temp = temp.children[path[ptr + 1]]
            ptr += 1
        if file_name in temp.children:
            temp = temp.children[file_name]
            temp.contents += content
        else:
            temp.add_child(TreeNode(file_name, TYPE_F, content))

    def readContentFromFile(self, filePath: str) -> str:
        temp = self.root
        path = re.split("\/", filePath)
        ptr = 0
        while ptr + 1 < len(path):
            temp = temp.children[path[ptr + 1]]
            ptr += 1
        return temp.contents

# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.ls(path)
# obj.mkdir(path)
# obj.addContentToFile(filePath,content)
# param_4 = obj.readContentFromFile(filePath)


if __name__ == '__main__':
    fs = FileSystem()
    print(fs.ls("/"))
    fs.mkdir("/a/b/c")
    fs.addContentToFile("/a/b/c/d", "hello")
    print(fs.ls("/"))
    print(fs.readContentFromFile("/a/b/c/d"))
