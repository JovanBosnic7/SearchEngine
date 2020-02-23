
class Set(object):

    def __and__(self, dict1, dict2):
        result_set = {}
        for html in dict1.keys():
            if html in dict2.keys():
                result_set[html] = dict1[html] + dict2[html]
        return result_set

    def __or__(self, dict1, dict2):
        result_set=dict1
        for html in dict2:
            if html not in result_set:
                result_set[html] = dict2[html]
            else:
                result_set[html] += dict2[html]

        return result_set

    def __diff__ (self, dic1, dic2):
        result_set = dic1
        for html in dic2:
            if html in result_set:
                del result_set[html]

        return result_set
