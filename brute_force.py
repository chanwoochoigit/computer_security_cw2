import itertools
import string
import hashlib

def brute_force(lines):
    hashvalues = []
    md5ed_values_dic = {}
    cracked_md5_words = []

    for i in lines:
        hashvalues.append(i)

    for xs in itertools.product(characters, repeat=5):
        password = ''.join(xs)
        md5ed_values_dic.update({hashlib.md5(password.encode()).hexdigest(): password})
        print(password)

    print("hashing done!")

    for hash in hashvalues:
        if md5ed_values_dic.get(hash) is not None:
            cracked_md5_words.append(md5ed_values_dic.get(hash))
            print(md5ed_values_dic.get(hash))
    print(len(hashvalues))
    print(cracked_md5_words)

    output = ''
    for w1 in cracked_md5_words:
        print(w1)
        wordcount = 0
        for w2 in cracked_md5_words:
            if w1 == w2:
                wordcount += 1
                cracked_md5_words.remove(w2)

        output += str(wordcount) + "," + w1 + "\n"

    print(output)
    print("output done!")
    return output


characters = list(string.ascii_lowercase+str(0)+str(1)+str(2)+str(3)+str(4)+str(5)+str(6)+str(7)+str(8)+str(9))

crack_md5 = {}
crack_3 = {}
crack_4 = {}

def main():

    with open("/home/chanwoo/Downloads/rockyou-samples.md5.txt") as md5_file:
        md5_list = md5_file.read().strip().split("\n")

    md5ed_values_export = open("/home/chanwoo/Downloads/md5_cracked.txt", 'w')
    md5ed_values_export.write(str(brute_force(md5_list)))
    md5ed_values_export.close()

if __name__ == '__main__':
    main()
