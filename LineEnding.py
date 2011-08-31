class LineEnding:
  NOT_SET = -1
  MIXED = 0
  WINDOWS = 1
  UNIX = 2
  MAC = 3
  UNKNOWN = 4
  
  def __init__(self):
    self.value = LineEnding.NOT_SET

  def __str__(self):
    if self.value == LineEnding.NOT_SET or self.value == LineEnding.UNKNOWN:
      return "Unknown"
    elif self.value == LineEnding.MIXED:
      return "       Mixed line endings"
    elif self.value == LineEnding.WINDOWS:
      return "'\\r\\n' Windows-style line endings"
    elif self.value == LineEnding.UNIX:
      return "'\\n'   Unix-style line endings"
    elif self.value == LineEnding.MAC:
      return "'\\r'   Mac-style line endings"

  def set_ending(self, value):
    if self.value == LineEnding.NOT_SET:
      self.value = value
    elif self.value != value:
      self.value = LineEnding.MIXED

  def get_ending(self):
    return self.value

  def test_line(self, line):
    if len(line) == 1:
      if line[-1] == '\n':
        self.set_ending(LineEnding.UNIX)
      elif line[-1] == '\r':
        self.set_ending(LineEnding.MAC)
    elif len(line) > 1:
      if line[-1] == '\n':
        if line[-2] == '\r':
          self.set_ending(LineEnding.WINDOWS)
        else:
          self.set_ending(LineEnding.UNIX)
      elif line[-1] == '\r':
        self.set_ending(LineEnding.MAC)
      else:
        self.set_ending(LineEnding.UNKNOWN)
