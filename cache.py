"""
Implement least-recently used cache.
The structure you'll implement should be used as decorator for functions

>>> @lru_cache
... def heavy_func(...):
...     ...

Functions decorated with lru_cache should not run when called, but return
 cached result instead.

Optional argument with "calls to remember" can be passed while decorating:

>>> @lru_cache(10)
... def func(...):
...     ...

 which forces lru_cache to remember only last 10 calls to this function

When used without argument, some default call limit should be used
When there's no space for new result, oldest call result should be evicted.
You can use `functools.lru_cache` as reference interface
 but can't use it directly.

Write tests for your implementation,
 using any standart testing library is a plus.


Bonus: make your cache persistent, so caching works between python runs,
 and cached data saved in filesystem. You may assume single-thread usage
 of your code.
"""
