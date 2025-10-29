def agreement_checker(subject, verb):
    singular_subjects = ['cat', 'dog', 'John', 'Mary']
    plural_subjects = ['dogs']
    singular_verbs = ['sees', 'barks', 'eats']
    plural_verbs = ['see']

    if (subject in singular_subjects and verb in singular_verbs) or \
       (subject in plural_subjects and verb in plural_verbs):
        return "Agreement OK"
    else:
        return "Agreement Error"

# Example usage
print(agreement_checker('cat', 'sees'))  # Agreement OK
print(agreement_checker('dogs', 'see'))  # Agreement OK
print(agreement_checker('cat', 'see'))   # Agreement Error
