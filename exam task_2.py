def max_val(t):
    """ t, tuple or list
        Each element of t is either an int, a tuple, or a list
        No tuple or list is empty
        Returns the maximum int in t or (recursively) in an element of t """

    # If t is an integer, return the integer itself
    if isinstance(t, int):
        return t

    # If t is a tuple or list, recursively find the maximum value in its elements
    elif isinstance(t, (tuple, list)):
        # initializing max_value equal to infinity so program's first maximum is equal to infinity
        max_value = float('-inf')
        for element in t:
            current_max = max_val(element)
            # recursively using the function max_value to find max in the tuple , list
            max_value = max(max_value, current_max)
        return max_value


# Test cases
print(max_val((5, (1, 2), [[1], [2]])))  # Should print 5
print(max_val((5, (1, 2), [[67], [9]])))  # Should print 9
