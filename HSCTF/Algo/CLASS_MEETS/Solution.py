import pwn

host = "class-meets.hsc.tf"
port = 1337

s = pwn.remote(host, port)
s.recvuntil("!\n")

while True:
  start = s.recvline().strip().decode()
  print(start)
  end = s.recvline().strip().decode()
  print(end)
  student1 = s.recvline().strip().decode()
  print(student1)
  student2 = s.recvline().strip().decode()
  print(student2)

  monthStart = int(start.split(" ")[0][1:])
  dayStart = int(start.split(" ")[1][1:])
  monthEnd = int(end.split(" ")[0][1:])
  dayEnd = int(end.split(" ")[1][1:])

  inpersonS1 = int(student1.split(" ")[0][1:])
  virtualS1 = int(student1.split(" ")[1][1:])
  inpersonS2 = int(student2.split(" ")[0][1:])
  virtualS2 = int(student2.split(" ")[1][1:])

  startInDays = 30 * monthStart + dayStart + 1
  endInDays = 30 * monthEnd + dayEnd + 1

  dayPassed = startInDays - 1
  count = 0

  weekendPassed = 0
  for i in range(1, startInDays):
    isWeekend = i % 7 == 0 or i % 7 == 6
    if isWeekend: weekendPassed += 1


  dayPassed -= weekendPassed

  for day in range(startInDays, endInDays + 1):
    isWeekend =  day % 7 == 0 or day % 7 == 6
    if isWeekend:
      continue
    if dayPassed % (inpersonS1 + virtualS1) < inpersonS1:
      s1 = "In person"
    else:
      s1 = "Virtual"
    if dayPassed % (inpersonS2 + virtualS2) < inpersonS2:
      s2 = "In person"
    else:
      s2 = "Virtual"
    if s1 == s2:
      count += 1
    dayPassed += 1
    
  s.sendline(str(count))
  print(s.recvline())
  print(s.recvline())
  print(s.recvline())
