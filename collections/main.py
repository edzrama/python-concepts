from collections import Counter, namedtuple, OrderedDict, defaultdict, deque

# collections: Counter, namedtuple, OrderedDict, defaultdict, deque

# Counter
my_string = "aaaaabbbbccc"
my_counter = Counter(my_string)
# type collections.Counter
print(my_counter)
# type dict_items
print(my_counter.items())
# type dict_keys
print(my_counter.keys())
# type dict_values
print(my_counter.values())
# counter to list
print(list(my_counter.elements()))

# namedtuple
Point = namedtuple('Point', 'x,y')
pt = Point(x=1, y=-4)
print(pt)
print(pt.x, pt.y)

# OrderedDict - remembers dictionary order  - no longer used since python 3

# default Dictionary - used to fill return default value for records not in the dictionary
d = defaultdict(int)
d['a'] = 1
d['b'] = 2
print(d['a'])
# c is not defined but is defaulted to 0
print(d['c'])

d_string = defaultdict(str)
d_string['a'] = 1
# return empty string
print(d_string['c'])

d_list = defaultdict(list)
# return empty list
d_list['a'] = 1
print(d_list['c'])


# deque
new_deque = deque()
new_deque.append(1)
new_deque.append(2)
new_deque.appendleft(3)
new_deque.appendleft(4)
print(new_deque)
new_deque.popleft()
print(new_deque)
new_deque.extendleft([4, 5, 6])
print(new_deque)
# If no parameter is passed ‘n’ will have the default value of 1.
# If ‘n’ is negative rotation direction is right to left.
# If ‘n’ is positive rotation direction is left to right.
new_deque.rotate(-3)
print(new_deque)
