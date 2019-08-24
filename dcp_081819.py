import heapq

# return a new sorted merged list from K sorted lists, each with size N.
# For example, if we had [[10, 15, 30], [12, 15, 20], [17, 20, 32]], the result should be [10, 12, 15, 15, 17, 20, 20, 30, 32].


def merge(lists):
    merged_list = []

    # init heap
    # you know that the first element of each list is the smallest in that list
    # create tuples as follows (Value of first element, which list is it in, index for that value (always 0 at first))
    heap = [(lst[0], i, 0) for i, lst in enumerate(lists) if lst]
    # [(12, 0, 0), (10, 1, 0), (17, 2, 0)]
    print(heap)
    # when you heapify, it sorts the tuples by value
    heapq.heapify(heap)
    # [(10, 1, 0), (12, 0, 0), (17, 2, 0)]
    print(heap)

    # update the heap to contain the lowest value left of the lists
    while heap:
        # get the lowest value
        val, list_idx, element_idx = heapq.heappop(heap)
        merged_list.append(val)

        # move to the next one in that list, if applicable
        # if no more left, next heap pop (above) automatically picks the next lowest value in a different list
        next_idx = element_idx+1
        if next_idx < len(lists[list_idx]):
            next_tuple = (lists[list_idx][next_idx], list_idx, next_idx)
            heapq.heappush(heap, next_tuple)
            heapq.heapify(heap)

    return merged_list

    # slightly modified
input = [[12, 15, 30], [10, 15, 20], [17, 20, 32]]
print(merge(input))
