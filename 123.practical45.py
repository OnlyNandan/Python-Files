sections = {}
while True:
    section = input("Enter section name (or 'q' to quit): ")
    if section == 'q':
        break
    stream = input("Enter stream name: ")
    sections[section] = stream
print('Section\tStream')
for section, stream in sections.items():
    print(section + '\t\t' + stream)
