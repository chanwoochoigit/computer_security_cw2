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

    #for i in range(len(sha1_salts)):
    #    sha1_salts_and_hashvalues.append(sha1_salts[i]+sha1_hashvalues[i])
    #    print(sha1_salts_and_hashvalues[i])

    """
    count = 0
    password_frequency = {
        "123456": 0, "12345": 0, "123456789": 0, "password": 0, "iloveyou": 0,
        "princess": 0, "1234567": 0, "rockyou": 0, "12345678": 0, "abc123": 0,
        "nicole": 0, "daniel": 0, "babygirl": 0, "monkey": 0, "lovely": 0,
        "jessica": 0, "654321": 0, "michael": 0, "ashley": 0, "qwerty": 0,
        "111111": 0, "iloveu": 0, "000000": 0, "michelle": 0, "tigger": 0
    }
    """
    sha1ed_passwords = {}
    cracked_sha1 = []


    for password in common_passwords:
        print(password)
        for salt in sha1_salts:
            sha1ed_passwords.update({hashlib.sha1((salt+password).encode()).hexdigest(): password})

    for hash in sha1_hashvalues:
        if sha1ed_passwords.get(hash) is not None:
            cracked_sha1.append(sha1ed_passwords.get(hash))

    output = ''
    for w1 in cracked_sha1:
        print(w1)
        wordcount = 0
        for w2 in cracked_sha1:
            if w1 == w2:
                wordcount += 1
                cracked_sha1.remove(w2)

        output += str(wordcount) + "," + w1 + "\n"

    print(output)
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