class Node:
    def __init__(self, line1, line2):
        self.line1 = line1
        self.line2 = line2
    def __repr__(self):
        return f"Node(line1 = '{self.line1}', line2 = '{self.line2}')"
nodes = [
    Node("Apple Banana", "Mango Pineapple"),
    Node("Pen Pencil", "Book Page"),
    Node("Mobile Laptop", "Desktop, Console")
]
def search_word_in_nodes(word,nodes):
    results = []
    for idx, node in enumerate(nodes):
        if word in node.line1:
            results.append((idx, 'line1', node))
        elif word in node.line2:
            results.append((idx, 'line2', node))
    return results
search_word = "Book"
found_nodes = search_word_in_nodes(search_word, nodes)
if found_nodes:
    for node_index, line_found, node in found_nodes:
        print(f"Found in node {node_index} in line {line_found}")
        print(f"Full node: {node}")
else:
    print("Word not found in any node")