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

import pyaes


class Encode:
    def __init__(self, filename):
        self.filename = filename

    def write_report(self, data, filename):
        with open(filename, "a") as input_file:
            input_file.write(data + "\n")

    def encode(self):
        details = raw_input("Please enter account info: ").lower()
        username = raw_input("Enter username that will be encoded: ")
        message = raw_input("Enter password that will be encoded: ")
        key = raw_input("Enter a 16 characters encryption key: ")
        try:
            aes = pyaes.AESModeOfOperationOFB(key)
            encoded_password = aes.encrypt(message)
            data = details + ":" + username + ":" + encoded_password
            self.write_report(data, self.filename)
        except ValueError:
            print "ERROR: Key must have 16 characters"
