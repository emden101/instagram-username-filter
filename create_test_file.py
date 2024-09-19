# create_test_file.py
def generate_test_file(filename, num_usernames):
    with open(filename, 'w') as f:
        for i in range(num_usernames):
            f.write(f'user{i}\n')

# Generate a file with 1000 usernames
generate_test_file('test_usernames.txt', 1000)
