class Vector:
    """Implementation of Vector class"""
    def __init__(self, values=None):
        assert type(values) in [list, int, tuple], self.__doc__
        if type(values) == int:
            self.values = self.generate_vect_from_range(range_=(0, values))
        elif type(values) == tuple:
            self.values = self.generate_vect_from_range(range_=values)
        elif type(values) == list:
            self.values = values
        self.shape = self.get_shape_of_vector(self.values)

    @staticmethod
    def generate_vect_from_range(range_):
        mylist = []
        for iterator in range(*range_):
            mylist.append([float(iterator)])
        return mylist

    @staticmethod
    def get_shape_of_vector(values):
        shape_ = ()
        # All element of values are float, [float0, float1, ...]
        if all(isinstance(value, float) for value in values):
            shape_ = (1, len(values))
        # All values are list : [[], [], ...]
        elif all(isinstance(value, list) for value in values):
            first_value_len = len(values[0])
            assert all(len(value) == first_value_len for value in values), \
                   'Values must be of uniforme length.'
            shape_ = (len(values), len(values[0]))
        else:
            raise AssertionError('Elements of vector must be either:\n\
- list of floats:\t\t[0.0, 1.0, 2.0, ...]\n\
- list of list of floats:\t[[0.0], [1.0] , ...] or [[0.0, 0.5], [1.0, 1.5]]')
        return shape_

    # add : only vectors of same dimensions.
    def __add__(self):
        pass

    def __radd__(self):
        pass

    # sub : only vectors of same dimensions.
    def __sub__(self):
        pass

    def __rsub__(self):
        pass

    # div : only scalars.
    def __truediv__(self):
        pass

    def __rtruediv__(self):
        pass

    # mul : only scalars.
    def __truediv__(self):
        pass

    def __rtruediv__(self):
        pass

    def dot(self):
        # produce a dot product between two vectors of same shape
        pass

    def T(self):
        # returns the transpose vector.
        # a column vector into a row vector, or a row vector
        # into a column vector)
        pass

    def __str__(self) -> str:
        return f'Shape : {self.shape}\nVector : {self.values}'

    def __repr__(self) -> str:
        pass
