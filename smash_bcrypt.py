import bcrypt

def smash_bcrypt(hash_list):

    good_lines = []
    output = ''
    linecount = 0
    for given_hash in hash_list:
        linecount += 1
        print(linecount)
        if bcrypt.checkpw(str(123456).encode(),given_hash.encode()):
            print("yay! line "+str(linecount)+" matches!=========================================")
            good_lines.append(linecount)
            output += str(linecount)+","
        if len(good_lines) == 5:
            break

    bcrypt_output = output[:-1]
    return bcrypt_output


def main():
    with open("/home/chanwoo/Downloads/rockyou-samples.bcrypt.txt") as bcrypt_file:
        bcrypt_file = bcrypt_file.read().strip().split("\n")

    smash_bcrypt_export = open("/home/chanwoo/Downloads/bcrypt-lines.txt", 'w')
    smash_bcrypt_export.write(str(smash_bcrypt(bcrypt_file)))
    smash_bcrypt_export.close()

if __name__ == '__main__':
    main()
