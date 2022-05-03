#!python


def counting_sort(numbers):
    """Sort given numbers (integers) by counting occurrences of each number,
    then looping over counts and copying that many numbers into output list.
    Running time: O(n+k) where n is number of elements in list and k is range of said elements
    Memory usage: O(k) where k is range of elements"""

    low = min(numbers)
    high = max(numbers)

    counts = [0] * (high - low + 1)

    for num in numbers:
        counts[num - low] += 1
    
    numbers.clear()

    for i in range(len(counts)):
        numbers += [i + low] * counts[i]



def bucket_sort(numbers, num_buckets=10):
    """Sort given numbers by distributing into buckets representing subranges,
    then sorting each bucket and concatenating all buckets in sorted order.
    Running time: O(n+k) where n is number of elements in list and k is number of buckets
    Memory usage: O(n+k) where n is number of elements in list and k is number of buckets"""

    low = min(numbers)
    high = max(numbers)

    buckets = [[] for _ in range(num_buckets)]

    for num in numbers:
        buckets[int((num - low) // (high - low))].append(num)

    numbers.clear()

    for bucket in buckets:
        bucket.sort()
        numbers += bucket
    

