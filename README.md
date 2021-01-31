# double-linked-list
Variant of realization for double linked list with some additional functional

First of all, you should create List with class `DoubleLinkedList`.

## Add element
To add new elements you should use `add_end(value)` or `add_start(value)` methods of list.
Or you can also you methodos `add_prev(value)` and `add_next(value)` of current element to add new element before or after it.

## Delete element
To remove elements from start or end of list `use delete_head()` or `delete_tail()`.
You can also use element's method `delete()` to remove current element.
### Remember! 
You can't use `delete()` for head or tail of list. It will raise the exception

## Reference
To reference first element of list use `list.head`. For next element use `current_element.next`
For access previous element use `current_element.prev`. To access last element, use `list.tail`

If next or previsous element is None, you have reached tail or head of list.

## Print
You can print list. It will display like regular list in Python
