# AES Encoder/decoder
#
#  The MIT License (MIT)
#
# Copyright (c) 2017 Florian Madar
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

import EncoderDecoder

file1 = "encrypted.txt"


def menu():
    meniu = 1
    while meniu:
        print "### MENU ###"
        print "1. Encode message"
        print "2. Decode message"
        print "3. List accounts saved in database"
        print "4. Search"
        print "5. Exit"
        choose = raw_input("Enter a number corresponding: ")
        if choose == "1":
            e = EncoderDecoder.Encode(file1)
            e.encode()
            print "\n"
        elif choose == "2":
            d = EncoderDecoder.Decode(file1)
            d.decode()
            print "\n"
        elif choose == "3":
            l = EncoderDecoder.ListAndSearch(file1)
            l.list_accounts()
            print "\n"
        elif choose == "4":
            s = EncoderDecoder.ListAndSearch(file1)
            s.search()
            print "\n"
        elif choose == "5":
            return
        else:
            print "Invalid option"
            print "\n"


def main():
    menu()


if __name__ == '__main_':
    main()
main()
