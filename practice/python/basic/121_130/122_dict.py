import datetime

sample_dict = {
    'sample1': {
        'open': ["08:00:00", "12:00:00"],
        'close': ["12:00:00", "16:00:00"]
    },
    'sample2': {
        'open': ["08:00:00", "12:00:00"],
        'close': ["12:00:00", "16:00:00"]
    }
}

# print(sample_dict)

for key in sample_dict:
    tmp_dict = sample_dict[key].copy()
    for item in sample_dict[key]:
        sample_dict[key][item] = [datetime.datetime.strptime(val, "%H:%M:%S").time() for val in sample_dict[key][item]]
        tmp_dict[item+"_serial"] = [val.hour * 60 + val.minute for val in sample_dict[key][item]]
    sample_dict[key] = tmp_dict

print(sample_dict)
