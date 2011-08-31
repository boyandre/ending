# test.py is part of ending
#
# Copyright 2011 Philipp Waehnert <phil.wnrt@googlemail.com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from LineEnding import LineEnding, check_file

f = open('testfiles/mac-test.txt', 'r')
assert check_file(f).get_ending() == LineEnding.MAC
f.close()

f = open('testfiles/unix-test.txt', 'r')
assert check_file(f).get_ending() == LineEnding.UNIX
f.close()

f = open('testfiles/windows-test.txt', 'r')
assert check_file(f).get_ending() == LineEnding.WINDOWS
f.close()

f = open('testfiles/windows-mac-test.txt', 'r')
assert check_file(f).get_ending() == LineEnding.MIXED
f.close()

f = open('testfiles/unix-windows-test.txt', 'r')
assert check_file(f).get_ending() == LineEnding.MIXED
f.close()

f = open('testfiles/unix-mac-test.txt', 'r')
assert check_file(f).get_ending() == LineEnding.MIXED
f.close()
