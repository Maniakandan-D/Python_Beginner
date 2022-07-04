required_skills = ['python', 'java', 'linux']

candidates = {
    'mani': {'python', 'java', 'linux', 'java script', 'github', 'windows'},
    'gowtham': {'java script', 'github', 'windows', 'full stock'},
    'dhilip': {'html', 'linux', 'java script', 'github'},
    'ashwin': {'pascal', 'linux', 'c++', 'java', 'python'},
    'saba': {'html', 'linux', 'c++', 'java', 'python', 'c'},
    'raja': {'css', 'github', 'windows', 'pascal', 'c', 'lisp', 'modula-2', 'perl'},
}

interviewees = set()
for candidates, skills in candidates.items():
    # if skills.issuperset(required_skills):
    if skills > set(required_skills):
        interviewees.add(candidates)

print(interviewees)
