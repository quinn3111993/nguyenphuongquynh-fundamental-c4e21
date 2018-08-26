import pyexcel

# 1.prepare data

data = [
    {
        'name': 'Huy',
        'age': 29,
    },
    {
        'name': "Quan",
        'age': 19,
    },
    {
        'name': "Duc",
        'age': 18,
    }
]

# 2.save
pyexcel.save_as(records=data, dest_file_name="sample.xlsx")
