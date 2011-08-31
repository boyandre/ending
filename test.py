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
