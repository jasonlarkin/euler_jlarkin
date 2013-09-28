import sys
mood = 'terrible'
speed =1000

print int(sys.argv[1]) + 100
print sys.argv[2]=='terrible'

if sys.argv[1]>=80:
  print 'Lisence'
  if sys.argv[2]=='terrible' or int(sys.argv[1])>=80:
    print 'You are fucked'
  elif sys.argv[2]=='bad' or int(sys.argv[1])>=90:
    print 'I\'m going to fuck your face'
    write_ticket()
  else:
    print 'Let\'s try fucking my face, ok?'

