class Node:
    def __init__(self, left : Node, right : Node, name):
        self.name = name
        self.left = left
        self.right = right
    
    def traverse(self, node : Node):
        return self.__traverse__(node)
    
    def __traverse__(self, node):
        parsed_string = "("
        if node.left:
            parsed_string += self.__traverse__(node.left)
        parsed_string += " " + node.name + " "
        if node.right:
            parsed_string += self.__traverse__(node.right)
        parsed_string += ")"
        return parsed_string
    
