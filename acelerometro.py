#algunas direcciones
MMA_i2caddr        = 0x1D
MMA8451_REG_WHOAMI = 0x0D
MMA_DEVID          = 0x1A

# checa que se conecto al MMA8451 chip
try:
    x.addres(MMA_i2caddr)
    mma_id = x.readReg(MMA8451_REG_WHOAMI)
    if not mma_id == MMA_DEVID:
        print "Wrong device found! Dev ID = " + str(mma_id)
    else:
        "MMA8451 Detected!"
except:
    print "MMA Devixce Not Connected!"

