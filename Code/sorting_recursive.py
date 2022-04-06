from sorting_iterative import insertion_sort

def merge(items1, items2, new_items=[]):
    """Merge given lists of items, each assumed to already be in sorted order,
    and return a new list containing all items in sorted order.
    TODO: Running time: O(n)
    TODO: Memory usage: O(n)"""
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