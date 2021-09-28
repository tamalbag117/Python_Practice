# let,s learn set in python
s = set()
print(type(s))
s_from_list = ([2, 4, 5, 6, "name"])
print(s_from_list)
s.add(5)
s.add(9)
s.add(5)
s.add("name")
print(s)  # it print 5 only one time because it retain unique value
# union
s1_from_list = s.union({5, 9, "name", "hi", "hallow"})
print(s, s1_from_list)
# intersection
s1_from_list = s.intersection({"name", "hi"})
print(s, s1_from_list)
s1_from_list = s.union(s_from_list)
print(s, s1_from_list)
print(max(str(s1_from_list)))

