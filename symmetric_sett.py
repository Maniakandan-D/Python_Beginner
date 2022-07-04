morning = {'java', 'c++', 'rupy', 'lisp', 'c'}
afternoon = {'python', 'c++', 'java', 'c', 'rupy'}

# possible_course = morning.symmetric_difference(afternoon)
possible_course = morning ^ afternoon
print(possible_course)
