fp = open("io_test.txt","w",encoding="UTF-8")

fp.write("wer\n")

str =input("wr>>>>")
fp.write(str)

fp.close()