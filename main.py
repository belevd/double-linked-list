class DoubleLinkedListError(Exception):
    def __str__(self):
        return 'First and last element should be added or deleted with list method, not element method'


class DoubleLinkedElement:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

    def __repr__(self):
        return f"{self.value}"

    def delete(self):
        if self.prev is None:
            raise DoubleLinkedListError
        elif self.next is None:
            raise DoubleLinkedListError
        self.prev.next = self.next
        self.next.prev = self.prev

    def add_prev(self, value):
        if self.prev is None:
            raise DoubleLinkedListError
        elif self.next is None:
            raise DoubleLinkedListError
        prev_elem = DoubleLinkedElement(value)
        prev_elem.next = self
        prev_elem.prev = self.prev
        self.prev.next = prev_elem
        self.prev = prev_elem

    def add_next(self, value):
        if self.prev is None:
            raise DoubleLinkedListError
        elif self.next is None:
            raise DoubleLinkedListError
        next_elem = DoubleLinkedElement(value)
        next_elem.prev = self
        next_elem.next = self.next
        self.next.prev = next_elem
        self.next = next_elem

    def repr_next(self):
        if self.next is None:
            new_result = f"{self.value}"
            return new_result
        else:
            new_result = f"{self.value}, {self.next.repr_next()}"
            return new_result


class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __repr__(self):
        result = ""
        if self.head == self.tail:
            result += f"[{self.head.value}]"
        else:
            result += f"[{self.head.value}, {self.head.next.repr_next()}]"
        return result

    def add_end(self, value):
        next_elem = DoubleLinkedElement(value)
        if self.head is None:
            self.head = next_elem
        else:
            next_elem.prev = self.tail
            self.tail.next = next_elem
        self.tail = next_elem

    def add_start(self, value):
        prev_elem = DoubleLinkedElement(value)
        if self.head is None:
            self.tail = prev_elem
        else:
            prev_elem.next = self.head
            self.head.prev = prev_elem
        self.head = prev_elem

    def delete_head(self):
        self.head.next.prev = None
        self.head = self.head.next

    def delete_tail(self):
        self.tail.prev.next = None
        self.tail = self.tail.prev


new_list = DoubleLinkedList()
new_list.add_end(5)
new_list.add_start(6)
new_list.add_start(8)
new_list.add_end(9)
new_list.head.next.delete()
print(new_list)
