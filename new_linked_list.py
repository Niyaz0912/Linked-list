from double_linked_list import LinkedList, Node


class NewLinkedList(LinkedList):

    def print_ll_from_tail(self):
        current_node = self.tail
        while current_node is not None:
            print(current_node.data)
            current_node = current_node.prev_node
        return "Список выведен с хвоста"

    def insert_at_index(self, data, index):
        if index == 0:
            return self.insert_at_head(data)
        elif index >= self.len_ll():
            return self.insert_at_tail(data)
        else:
            new_node = Node(data)
            current_node = self.head
            for _ in range(index - 1):
                current_node = current_node.next_node
            new_node.next_node = current_node.next_node
            new_node.prev_node = current_node
            current_node.next_node.prev_node = new_node
            current_node.next_node = new_node
            return f"Узел с данными {data} добавлен на позицию {index}"

    def remove_node_index(self, index):
        if index == 0:
            return self.remove_from_head()
        elif index >= self.len_ll() - 1:
            return self.remove_from_tail()
        else:
            current_node = self.head
            for _ in range(index):
                current_node = current_node.next_node
            removed_node = current_node
            current_node.prev_node.next_node = current_node.next_node
            current_node.next_node.prev_node = current_node.prev_node
            return f"Были удалены данные {removed_node.data} по индексу {index}"

    def remove_node_data(self, data):
        current_node = self.head
        while current_node is not None:
            if current_node.data == data:
                if current_node == self.head:
                    return self.remove_from_head()
                elif current_node == self.tail:
                    return self.remove_from_tail()
                else:
                    removed_node = current_node
                    current_node.prev_node.next_node = current_node.next_node
                    current_node.next_node.prev_node = current_node.prev_node
                    return f"Были удалены данные {removed_node.data} по данным узла"
            current_node = current_node.next_node
        return f"Узел с данными {data} не найден"

    def len_ll(self):
        count = 0
        current_node = self.head
        while current_node is not None:
            count += 1
            current_node = current_node.next_node
        return count

    def contains_from_head(self, data):
        current_node = self.head
        while current_node is not None:
            if current_node.data == data:
                return True
            current_node = current_node.next_node
        return False

    def contains_from_tail(self, data):
        current_node = self.tail
        while current_node is not None:
            if current_node.data == data:
                return True
            current_node = current_node.prev_node
        return False

    def contains_from(self, data, start):
        if start == "head":
            return self.contains_from_head(data)
        elif start == "tail":
            return self.contains_from_tail(data)
        else:
            return False


my_ll = NewLinkedList()
my_ll.insert_at_head(1)
my_ll.insert_at_head(2)
my_ll.insert_at_head(3)
my_ll.insert_at_tail(4)
my_ll.insert_at_tail(5)


my_ll.insert_at_index(6, 2)
my_ll.remove_node_index(3)
my_ll.remove_node_data(4)
my_ll.len_ll()
my_ll.contains_from_head(3)
my_ll.contains_from_tail(5)
my_ll.contains_from(6, "head")

my_ll.print_ll_from_head()
my_ll.print_ll_from_tail()
