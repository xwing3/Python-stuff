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

### List accounts

import re


class ListAndSearch:
    def __init__(self, file):
        self.file = file

    def list_accounts(self, file):
        try:
            open_file = open(file, "r")
            data = open_file.read().splitlines()
            print "###Acounts###"
            for i in data:
                str = "".join(i)
                array = str.split(":")
                username = array[0]
                print "Account name: ", username
        except IOError:
            print "ERROR: File does not exist or you don't have read permission"

    ### Search for account name

    def search(self, file):
        details = raw_input("Please enter account info: ").lower()
        try:
            open_file = open(file, "r")
            data = open_file.read()
        except IOError:
            print "File does not exist or access is denied"
        else:
            line = re.findall(".*" + details + ".*", data)
            for i in line:
                str = "".join(i)
                array = str.split(":")
                account = array[0]
                username = array[1]
                print "Account name=%s and username=%s" % (account, username)
