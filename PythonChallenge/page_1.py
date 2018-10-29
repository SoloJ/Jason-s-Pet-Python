
coded_message = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
coded_message_list = list(coded_message)
alphabet = "abcdefghijklmnopqrstuvwxyz"
alphabet1 = "cdefghijklmnopqrstuvwxyzab"
alphabet_array = list(alphabet)
url_map = "map"
length_of_message = len(coded_message_list)
from string import maketrans
#n = 0
#z = 0
#while 203 > n:
   # while z < 26:
   #     if coded_message_list[n] in alphabet_array[z]:
   #         coded_message_list[n] = alphabet_array[z+2]
    #        n = n + 1
    #        z = 0
    #    else:
    #        z = z + 1
  #  z = 0
 #   n = n + 1

#print("".join(coded_message_list))

transtab = maketrans(alphabet, alphabet1)
print url_map.translate(transtab)

