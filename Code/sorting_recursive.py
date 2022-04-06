from sorting_iterative import insertion_sort

def merge(items1, items2, new_items=[]):
    """Merge given lists of items, each assumed to already be in sorted order,
    and return a new list containing all items in sorted order.
    TODO: Running time: O(n)
    TODO: Memory usage: O(n)"""
    # TODO: Repeat until one list is empty
    # TODO: Find minimum item in both lists and append it to new list
    # TODO: Append remaining items in non-empty list to new list
    if not items1 and not items2:
        return new_items
    elif not items1:
        return new_items + items2
    elif not items2:
        return new_items + items1

    if items1[0] < items2[0]:
        new_items.append(items1[0])
        items1 = items1[1:]
    else:
        new_items.append(items2[0])
        items2 = items2[1:]

    return merge(items1, items2, new_items)

    
def split_sort_merge(items):
     """Sort given items by splitting list into two approximately equal halves,
     sorting each with an iterative sorting algorithm, and merging results into
     a list in sorted order.
     TODO: Running time: O(n log n)
     TODO: Memory usage: O(n)"""
     # TODO: Split items list into approximately equal halves
     # TODO: Sort each half using any other sorting algorithm
     # TODO: Merge sorted halves into one list in sorted order
     half1 = items[:len(items)//2]
     half2 = items[len(items)//2:]
     insertion_sort(half1)
     insertion_sort(half2)

     return merge(half1, half2)
    
def merge_sort(items):
    """Sort given items by splitting list into two approximately equal halves,
    sorting each recursively, and merging results into a list in sorted order.
    TODO: Running time: O(n log n)
    TODO: Memory usage: O(n)"""
    # TODO: Check if list is so small it's already sorted (base case)
    # TODO: Split items list into approximately equal halves
    # TODO: Sort each half by recursively calling merge sort
    # TODO: Merge sorted halves into one list in sorted order
    if len(items) <= 1:
        return items
    
    mid = len(items)//2
    left = merge_sort(items[:mid])
    right = merge_sort(items[mid:])
    return merge(left, right, [])


def partition(items, low, high):
    """Return index `p` after in-place partitioning given items in range
    `[low...high]` by choosing a pivot (TODO: document your method here) from
    that range, moving pivot into index `p`, items less than pivot into range
    `[low...p-1]`, and items greater than pivot into range `[p+1...high]`.
    TODO: Running time: O(n)
    TODO: Memory usage: O(1)"""
    # TODO: Choose a pivot any way and document your method in docstring above
    # TODO: Loop through all items in range [low...high]
    # TODO: Move items less than pivot into front of range [low...p-1]
    # TODO: Move items greater than pivot into back of range [p+1...high]
    # TODO: Move pivot item into final position [p] and return index p
    pivot = items[high]
    i = low
    for j in range(low, high):
        if items[j] < pivot:
            items[i], items[j] = items[j], items[i]
            i += 1
    items[i], items[high] = items[high], items[i]
    return i


def quick_sort(items, low=None, high=None):
    """Sort given items in place by partitioning items in range `[low...high]`
    around a pivot item and recursively sorting each remaining sublist range.
    TODO: Best case running time: O(n log n)
    TODO: Worst case running time: O(n^2)
    TODO: Memory usage: O(log n)"""
    # TODO: Check if high and low range bounds have default values (not given)
    # TODO: Check if list or range is so small it's already sorted (base case)
    # TODO: Partition items in-place around a pivot and get index of pivot
    # TODO: Sort each sublist range by recursively calling quick sort
    if low is None:
        low = 0

    if high is None:
        high = len(items) - 1

    if low < high:
        p = partition(items, low, high)
        quick_sort(items, low, p-1)
        quick_sort(items, p+1, high)

    return items

items = [2, 42, 4, 234, 5, 21]
print(quick_sort(items))