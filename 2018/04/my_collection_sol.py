# the given lists
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
    # create the empty dict that we will keep adding the stuff into one by one
    subject_dict = dict()
    # idx is the counter going from 0 to 38
    # using enumerate saves as the line: subj_id = subjects[idx]
    for idx, subj_id in enumerate(subjects):
        # if this is the first time we encounter this subject id, add it to the dict
        # the value is an empty list for now, we will now add all the attributes
        if subj_id not in subject_dict:
            subject_dict[subj_id] = []
        # add the current attribute to the list of the subject
        subject_dict[subj_id].append(attributes[idx])

    return subject_dict

# So nice, tidy and clean.
subject_dict = clean_up(all_subjects, all_attributes)

print(subject_dict)