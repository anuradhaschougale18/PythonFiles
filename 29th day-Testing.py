def minimum_index(seq):
    if len(seq) == 0:
        raise ValueError("Cannot get the minimum value index from an empty sequence")
    min_idx = 0
    for i in range(1, len(seq)):
        if seq[i] < seq[min_idx]:
            min_idx = i
    return min_idx
class TestDataEmptyArray(object):
    
    @staticmethod
    def get_array():
        # complete this function
        return list()
class TestDataUniqueValues(object):

    @staticmethod
    def get_array():
        # complete this function
         return[7,9,1,2,-7,10,22]

    @staticmethod
    def get_expected_result():
        # complete this function
        return 4
       

class TestDataExactlyTwoDifferentMinimums(object):

    @staticmethod
    def get_array():
        # complete this function
         return[7,9,1,2,-7,10,22,-7] 

    @staticmethod
    def get_expected_result():
        # complete this function
        return 4

