filepath = '/Users/Gregor/Desktop/Arbeit.ics'
new_filepath = '/Users/Gregor/Desktop/Arbeit-increment.ics'

with open(filepath) as fp:
    with open(new_filepath, 'w') as new_file:
        line = fp.readline()
        cnt = 1
        while line:
            if line.strip()[:4] == "UID:":
                print(format(int(line.strip()[-12:], 16) + 1, 'x').upper())
                new_file.write(line[:-12] + format(int(line.strip()[-12:], 16) + 1, 'x').upper() + "\n")
            elif line.strip()[:14] == "X-WR-ALARMUID:":
                print(format(int(line.strip()[-12:], 16) + 1, 'x').upper())
                new_file.write(line[:-12] + format(int(line.strip()[-12:], 16) + 1, 'x').upper() + "\n")
            else:
                new_file.write(line)
            line = fp.readline()
            cnt += 1
