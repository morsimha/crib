
def crib_2_str(c1, c2):
    found = False
    # c1_bin = bin(c1)
    # c3_bin = bin(c3)

    c1_x_c2 = (c1 ^ c2)
    # print(bin(c1))
    # print(bin(c2))
    # print(bin(c1_x_c2))
    #print(c1_x_c2)
    the_Ascii = [ord('t'), ord('h'), ord('e')]
    the_Ascii = ''.join(str(e) for e in the_Ascii)
    letterASCII = ""
    word = ""
    for index, char in enumerate(str(c1_x_c2), start=1):
        letterASCII += char + ""

        if index % 3 == 0:
        #    print("orig letter " + letterASCII)
            word += chr(int(letterASCII))
            #   print(word)
            letterASCII = ""

        if index % 9 == 0:
            #    print(word)
            word_Ascii = ["{0:0=3d}".format(ord(c)) for c in word]
            word_Ascii = ''.join(str(e) for e in word_Ascii)
      #      print("combined 3 letters " + word_Ascii)
            final = int(the_Ascii) ^ int(word_Ascii)
     #       print("XORed 3 letters " + str(final))
            word2 = ""
            letterASCII2 = ""

            for index2, char2 in enumerate(str(final), start=1):
                letterASCII2 += char2 + ""

                if index2 % 3 == 0:
                    # print(letterASCII)

                    word2 += chr(int(letterASCII2))
                    if not all(ord(c) < 128 for c in word2):
                        break
                    letterASCII2 = ""
            #     print("new word " + word2)
            else:
                print("#####################found: " + word2)
                print("index: " , index-2)
                found = True

            word = ""

        # letter = [ord(char1), ord(char2), ord(char3)]
        # letter_str=''.join(str(e) for e in the)
        # print(letter_str)
    # the_x_c1_c3 = int(the_Ascii) ^ c1_x_c3
    #
    # print(the_x_c1_c3)
    # print(chr(734009345))
    return found

if __name__ == '__main__':
    c1 = int(
        "d59fa7b9c7d208c3c7e2369b757acb831613a51cb182f536040238ac6f3afd0aee0d9186fc829aa61b66a514adfceb73a969ed05bf08ce124df6a15acd2f6fb00241df7b9ba9165cc1da6a8e1e56eefc720e7269285a55282f4a9f1c27cff26f68263fd46ccf35f59f39ed649eaeb94d00393d406e638817ad46d2b04e6d9820ceaaa89a96bb9b6f28993933203e74f24115ff37427274ae2408de",
        16)
    c2 = int(
        "c883e2eec3cf41c1c7f37a996d7cc7ca1d0ef110acd1fd60020731e46831fd00ea0191c5fec78cae0c6db05bb9ecfd3aa660a956af18c41809bfb815cb2b6eb01041df3bc2ed5808cf966bc71809fbe574086363285656662f57884560deef22793a70cd60c028a19d24f927",
        16)
    c3 = int(
        "d59fa7b9c7d208c3c7e2369b757acb831613a502a3d1b47508053bad6e2daf0bef5b8b8ab9d19ba01871ac5ba9f1ee27e86efd05bd1ad85618ecaa1e993365b0024ece7e92ec535a8e8e6f825a16f5f86340727f78144323384d881127d6f83c6b3537c57a",
        16)



    c4 = int(
        "d59fa7b9c7d208c3c7e2369e756a838b1656e019a7c1e06408062da76229b307e81a94c5ebcd8aac1f23a41ebef1ee3da174e405be13ca024decac08d82a68fc02538d638ae1165cd99f6993035be9e26f406a757c4d5534281f820327cff52a38353cd061cd23b088",
        16)
    c5 = int(
        "c899e2eddbcc08c7cbef3683677c8fca1718e055b2c7e665080568a1643cb81cf85b8c80e1d6deac0323bd13b8b9ea3da160e444ed088b1d08e6ad15d8356eb0064ec93783ea595cc69f75c70a1ee8f8780e26677a504423281f890a70d5bd38703d33c829c327f5883ee5298fabbf4a152c31136372d817ab4cdbb0542ed562c0b2a99a8fba9226379d32286f3c69fb0c09fd32547e69a92a12957371e8c2251c8338dfdbeed8e0a457c0f2d0d9",
        16)
    c6 = int(
        "c891e2e9cedd08ca8af7738e6039ca995813eb01a7d0f1724b4b3cac6f68b402e70e958cf7c38aa60923a51ea9edea21bb27e857af5bdf1e08bfac13c92f6fe21345d563cc",
        16)

    c7 = int(
        "c499b6fcd0d50fc38ae07f867c7cd19e1d0ef155b6d0f578140d27b6673bfd07ff5b9a84fac9deaa0377a65baffcee37a965e540ea0bc71704f1bb1fc13324b01348c83790eb4247dcda6a821913fbe57e136b306b5151283c5a9e4573d3f86f7d3835c37dde28b69d3aa06a94b2b4410221780f6479d819a75fc4a142609474c7a1ecd19eab84263d962f6a74357ebf4009f636556020b02212983734e8d56d59893ece8bf7d8eaf7",
        16)
    c8 = int(
        "d59fa7b9d1d902d1d8ea628f3476c5ca0c1ee055b1dbe762020668a06f38b800ef08d88af78293a20e6ba015b8b9fc36bc73e04bad088b0205febb5ace2278f54747c87987f65744c2832784121af4ec7204267469505c3f771f8f0474def96f773a70d36ccf33b08876eb6c82fcb64d122162406e638b0fb042d1b1536bd020c6aaecdb9fa496683f9d676a61337fbf430eb131557b65b56b15956325e0d8620ac22fdf9af19deee155d7b7c0c2bdc2d99b420828cd1953781fc8a1dca225b6b89d0aab",
        16)
    c9 = int(
        "d59fa7b9d0d902c1c3f57f987339d09e1902ec1aac82e37912072ce46229ab0bab0f97c5f2cc91b44d62a71ffdecfc36e873e140ea1ed3170eebef09dc337ef90947de3787e94644c18362835a19e3ab630863307c4b51282852841173d2f328382724c17dc52ebbdc22ef2988a9b947042662067f669402e24fd6a75577c4748fa5ecd79ea184673b9d65",
        16)
    c10 = int(
        "cd9ea9fc82d315cccff136847b6dcc98581be416aacbfa73144768b0622dfd2be5129f88f88293a20e6ba015b8b9e620e866a946a516c91f03febb13d6292aff0100c07281ec5746c799668b5a1af4ef37056a756b4d422f385e814574ceff3c612724c564df",
        16)

    messages = {"c1":c1, "c2":c2, "c3":c3, "c4":c4, "c5":c5, "c6":c6, "c7":c7, "c8":c8, "c9":c9, "c10":c10}

    for name, message in messages.items():
        for name2, message2 in messages.items():
            if name is not name2:
                found = crib_2_str(message, message2)
                if found:
                    print(f"for message {name} and {name2}\n")