def build_profile(first, last, **user_info):
    """创建一个空字典，其中包含我们知道的一切有关用户的一切"""
    profile = {}
    profile['firet_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile


new_profiles = build_profile('bob', '泰勒',
                             school='MIt', age='25', study='math')

print(new_profiles)