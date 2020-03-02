import hashlib

def crack_sha1(file):

    #init salts and hashvalues
    sha1_hashvalues = []
    sha1_salts = []
    #sha1_salts_and_hashvalues = []

    #update salts and hashvalues
    for line in file:
        sha1_hashvalues.append(line[-40:].rstrip())
        sha1_salts.append(line[-51:-41])


    sha1ed_passwords_dic = {}
    cracked_sha1 = []

    for password in common_passwords:
        print(password)
        for salt in sha1_salts:
            sha1ed_passwords_dic.update({hashlib.sha1((salt+password).encode()).hexdigest(): password})

    for hash in sha1_hashvalues:
        if sha1ed_passwords_dic.get(hash) is not None:
            cracked_sha1.append(sha1ed_passwords_dic.get(hash))

    output = ''

    print("cracked_sha1 length: "+str(len(cracked_sha1)))
    frequency_count = 0
    for c in common_passwords:
        print(c)
        wordcount = 0
        for w in cracked_sha1:
            if c == w:
                wordcount += 1
                frequency_count += 1
        output += str(wordcount) + "," + c + "\n"

    print(str(frequency_count / len(cracked_sha1) * 100) +"%")
    print("output done!")
    return output

common_passwords = ["123456", "12345", "123456789", "password", "iloveyou",
                    "princess", "1234567", "rockyou", "12345678","abc123",
                    "nicole", "daniel", "babygirl", "monkey", "lovely",
                    "jessica", "654321", "michael", "ashley", "qwerty",
                    "111111", "iloveu", "000000", "michelle", "tigger"]


def main():
    # setup textfile
    with open("/home/chanwoo/Downloads/rockyou-samples.sha1-salt.txt", 'r') as sha1_file:
        sha1_list = sha1_file.read().strip().split("\n")

    md5ed_values_export = open("/home/chanwoo/Downloads/salt-cracked.txt", 'w')
    md5ed_values_export.write(str(crack_sha1(sha1_list)))
    md5ed_values_export.close()


if __name__ == '__main__':
    main()