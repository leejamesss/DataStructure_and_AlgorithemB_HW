class Node:
    def __init__(self, weight, char=None):
        self.weight = weight
        self.char = char
        self.left = None
        self.right = None

    # 定义小于运算符，用于节点之间的比较
    def __lt__(self, other):
        if self.weight != other.weight:
            return self.weight < other.weight
        else:
            return self.char < other.char


def build_huffman_tree(weights):
    """
    根据权值列表weights构造哈夫曼编码树
    """
    nodes = [Node(weight, char) for char, weight in weights]
    while len(nodes) > 1:
        # 找到两个权值最小的节点
        node1 = min(nodes)
        nodes.remove(node1)
        node2 = min(nodes)
        nodes.remove(node2)

        # 构造新的父节点，权值为子节点的和
        parent_node = Node(node1.weight + node2.weight)
        parent_node.left = node1
        parent_node.right = node2

        # 将新的父节点插入到节点列表中
        nodes.append(parent_node)

    # 返回根节点
    return nodes[0]


def encode_huffman(root, code="", codes={}):
    """
    计算每个字符对应的哈夫曼编码
    """
    if root is None:
        return
    if root.char is not None:
        # 如果当前节点是叶子节点，则将其对应的编码保存下来
        codes[root.char] = code
    encode_huffman(root.left, code + "0", codes)
    encode_huffman(root.right, code + "1", codes)


def decode_huffman(root, bit_string):
    """
    将01编码串解码成原始字符串
    """
    current_node = root
    decoded_string = ""
    for bit in bit_string:
        if bit == "0":
            current_node = current_node.left
        else:
            current_node = current_node.right
        if current_node.char is not None:
            decoded_string += current_node.char
            current_node = root
    return decoded_string


if __name__ == '__main__':
    n = int(input())
    weights = []
    for i in range(n):
        char, weight = input().split()
        weights.append((char, int(weight)))

    # 构造哈夫曼编码树并计算每个字符对应的编码
    root = build_huffman_tree(weights)
    codes = {}
    encode_huffman(root, "", codes)

    # 读取输入并进行编码或解码
    while True:
        try:
            s = input().strip()
            if s.isdigit():
                # 如果输入是01编码串，则进行解码
                decoded_string = decode_huffman(root, s)
                print(decoded_string)
            else:
                # 如果输入是字母串，则进行编码
                encoded_string = "".join(codes[char] for char in s)
                print(encoded_string)
        except:
            break
