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

import re
import pyaes

class Decode:
    def __init__(self, file):
        self.file = file

    def return_data(self, details):
        open_file = open(file, "r")
        data = open_file.read()
        line = re.findall(details + ".*", data)
        if len(line) != 0:
            str = "".join(line)
            array = str.split(":")
            password = array[2]
            username = array[1]
            return username, password
        else:
            print "ERROR: Account info for %s does not exists \n" % details

    def decode(self):
        details = raw_input("Please enter account info: ").lower()
        key = raw_input("Enter 16 bit encryption key: ")
        try:
            password = self.return_data(details)[1]
            username = self.return_data(details)[0]
        except IOError:
            print "ERROR: File does not exist or you don't have read permission"
        else:
            try:
                aes = pyaes.AESModeOfOperationOFB(key)
                decoded = aes.decrypt(password)
                print "Username for the %s account is %s with password: " % (details, username), decoded
            except ValueError:
                print "ERROR: Key must have 16 characters"
