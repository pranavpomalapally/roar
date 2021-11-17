
Kp, Ki, Kd = 0, 0, 0
P, I, D = None, None

maxspeeda = 255
maxspeedb = 255
basespeeda = 150
basespeedb = 150


def PID_control():
  position = readData()
  error = 3500 - position

  P = error
  I = I + error
  D = error - lastError
  lastError = error
  motorspeed = P*Kp + I*Ki + D*Kd
  
  motorspeeda = basespeeda + motorspeed
  motorspeedb = basespeedb - motorspeed
  
  if (motorspeeda > maxspeeda):
    motorspeeda = maxspeeda
  if (motorspeedb > maxspeedb):
    motorspeedb = maxspeedb

  if (motorspeeda < 0):
    motorspeeda = 0

  if (motorspeedb < 0):
    motorspeedb = 0

  print(motorspeeda, motorspeedb)
  set_motors(motorspeeda, motorspeedb)

def readData():
  return None

def setMotors(val1, val2):
  return None