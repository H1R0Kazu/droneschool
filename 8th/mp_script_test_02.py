print 'Start AUTOTUNE script'
for chan in range(1,9):
  Script.SendRC(chan,1500,False)
  Script.SendRC(3,Script.GetParam('RC3_MIN'),

Script.Sleep(5000)

while cs.lat == 0:
  print 'Waiting for GPS'
  Script.Sleep(1000)

print 'Got GPS'
if (Script.ChangeMode ("Loiter")):
  print 'Loiter'

Script.SendRC(3,1000,False)
Script.SendRC(4,2000,False)
cs.messages.Clear)
Script.WaitFor('Arming motors',20000)

Script.SendRC(4,1500,True)
print 'Motors Armed!'
Script.SendRC(3,1700,True)

while cs.alt < 20:
  Script.Sleep(50)

Script.SendRC(3,1500,True)
if (Script.ChangeMode("AutoTune")):
  print 'AutoTune'

print 'AUTOTUNE Starting'

