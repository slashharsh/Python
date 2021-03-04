'''imports'''
import zipfile


count = 1

with open('dict.txt', 'rb') as text:
    for entry in text.readlines():
        password = entry.strip()
        try:
            with zipfile.ZipFile('cit.zip', 'r') as zf:
                zf.extractall(pwd=password)

                data = zf.namelist()[0]

                data_size = zf.getinfo(data).file_size

                print('''Password detected! - %s\n -%s\n -%s\n'''
                      % (password.decode('utf8'), data, data_size))
                break

        except:
            number = count
            print('[%s] Not the Password! - %s' %
                  (number, password.decode('utf8')))
            count += 1
            pass

