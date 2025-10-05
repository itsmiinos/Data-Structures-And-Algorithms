# Last updated: 10/6/2025, 2:41:12 AM
class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.freq = 1
        self.prev = None
        self.next = None


class DLL:  # Doubly Linked List to hold nodes of same freq
    def __init__(self):
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0

    def add_node(self, node):
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node
        self.size += 1

    def remove_node(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        self.size -= 1

    def remove_last(self):
        if self.size > 0:
            last = self.tail.prev
            self.remove_node(last)
            return last
        return None


class LFUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.min_freq = 0
        self.key_node = {}
        self.freq_map = {}
        self.size = 0

    def update_freq(self, node):
        freq = node.freq
        self.freq_map[freq].remove_node(node)
        if freq == self.min_freq and self.freq_map[freq].size == 0:
            self.min_freq += 1
        node.freq += 1
        if node.freq not in self.freq_map:
            self.freq_map[node.freq] = DLL()
        self.freq_map[node.freq].add_node(node)

    def get(self, key: int) -> int:
        if key not in self.key_node:
            return -1
        node = self.key_node[key]
        self.update_freq(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return

        if key in self.key_node:
            node = self.key_node[key]
            node.val = value
            self.update_freq(node)
            return

        if self.size >= self.capacity:
            min_freq_list = self.freq_map[self.min_freq]
            to_remove = min_freq_list.remove_last()
            del self.key_node[to_remove.key]
            self.size -= 1

        new_node = Node(key, value)
        self.min_freq = 1
        if 1 not in self.freq_map:
            self.freq_map[1] = DLL()
        self.freq_map[1].add_node(new_node)
        self.key_node[key] = new_node
        self.size += 1
