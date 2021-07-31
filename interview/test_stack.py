import pytest
import stack

LENGTH = 3

class TestStack:
    def setup_class(self):
        pass

    def setup(self):
        pass

    def test_push(self):
        my_stack = stack.Stack()
        assert my_stack.stack == []
        val_list = [i for i in range(LENGTH)]
        for i, val in enumerate(val_list):
            my_stack.push(val)
            assert my_stack.stack == val_list[:i+1]

    def test_size(self):
        my_stack = stack.Stack()
        val_list = [i for i in range(LENGTH)]
        for i, val in enumerate(val_list):
            my_stack.push(val)
            assert my_stack.size() == i + 1

    def test_is_empty(self):
        my_stack = stack.Stack()
        assert my_stack.is_empty() is True
        my_stack.push('test_value')
        assert my_stack.is_empty() is False

    def test_pop(self):
        my_stack = stack.Stack()
        assert my_stack.pop() is None
        length = LENGTH
        val_list = [i for i in range(length)]
        for val in val_list:
            my_stack.push(val)
        for val in val_list[::-1]:
            assert my_stack.pop() == val
            length -= 1
            assert my_stack.size() == length

    def test_peek(self):
        my_stack = stack.Stack()
        assert my_stack.peek() is None
        length = 0
        val_list = [i for i in range(LENGTH)]
        for val in val_list:
            my_stack.push(val)
            length += 1
            assert my_stack.peek() == val
            assert my_stack.size() == length
        assert my_stack.peek() == val_list[-1]
        assert my_stack.size() == LENGTH


