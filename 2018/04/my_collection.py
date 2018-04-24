import pickle, base64 # things needed to check for correctnes. ignore them.

# ignore this as well.
def check(subj_dict):
    """Returns true if the given dict is the one we searched for"""
    sol =  pickle.loads(base64.b64decode(b'gAN9cQAoSwBdcQEoWA0AAABNYXRlcmlhbGlzdGljcQJYBAAAAE5lYXRxA2VLAV1xBChYBgAAAEFjdGl2ZXEFWAkAAABXZWxjb21pbmdxBlgIAAAAQ3JlYXRpdmVxB1gJAAAAQW1iaXRpb3VzcQhlSwJdcQkoWAQAAABHZWVrcQpoBmgDZUsDXXELKGgHaApYBQAAAFF1aWV0cQxYAwAAAFNoeXENZUsEXXEOKGgDaAhYCwAAAEFkdmVudHVyb3VzcQ9lSwVdcRAoaAVoBmgPZUsGXXERKGgDaAhYCQAAAEV4Y2l0YWJsZXESaAVoBmgMZUsHXXETKGgSaAhoD2gMaApoBWVLCF1xFChYCQAAAFNwaXJpdHVhbHEVaAxoEmgCaAplSwldcRYoaAZoEmgPZXUu'))
    checks = [set(subj_dict.keys()) == set(sol.keys())]
    checks += [set(sol[idx]) == set(subj_dict[idx]) for idx in subj_dict]
    return all(checks)

######################################################
### Your tasks starts here!
######################################################

# the given lists to work with, don't alter them.
all_subjects = [0, 0, 1, 1, 1, 1, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 7, 8, 8, 8, 8, 8, 9, 9, 9]
all_attributes = ['Materialistic', 'Neat', 'Active', 'Welcoming', 'Creative', 'Ambitious', 'Geek', 'Welcoming', 'Neat', 'Creative', 'Geek', 'Quiet', 'Shy', 'Neat', 'Ambitious', 'Adventurous', 'Active', 'Welcoming', 'Adventurous', 'Neat', 'Ambitious', 'Excitable', 'Active', 'Welcoming', 'Quiet', 'Excitable', 'Ambitious', 'Adventurous', 'Quiet', 'Geek', 'Active', 'Spiritual', 'Quiet', 'Excitable', 'Materialistic', 'Geek', 'Welcoming', 'Excitable', 'Adventurous']

# This is the function you need to implement
def clean_up(subjects, attributes):
    """    
    This function takes a list of subject ids which correspond to attributes 
    in the second list, and forms a dictionary out of them, with the unique 
    subject id as the key and a list of their attributes as the corresponding 
    value.
    """
    return {'implement':'me'}


subject_dict = clean_up(all_subjects, all_attributes)

# if this prints out true, your solution was correct!
print("You solution was correct: " + check(subject_dict))
