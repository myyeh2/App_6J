import numpy as np 
import matplotlib.pylab as plt

t = np.arange(0, 50.5, 0.5) 

#  y0_Acceleration  
y0 = [
        -0.5000,        -0.4341,        -0.3201,        -0.1748,        -0.0186,
         0.1276,         0.2460,         0.3239,         0.3555,         0.3416,
         0.2885,         0.2067,         0.1082,         0.0058,        -0.0890,
        -0.1663,        -0.2188,        -0.2420,        -0.2351,        -0.2006,
        -0.1443,        -0.0746,        -0.0010,         0.0669,         0.1209,
         0.1557,         0.1686,         0.1603,         0.1337,         0.0939,
         0.0466,        -0.0021,        -0.0467,        -0.0825,        -0.1060,
        -0.1153,        -0.1104,        -0.0926,        -0.0649,        -0.0315,
         0.0031,         0.0346,         0.0593,         0.0748,         0.0799,
         0.0751,         0.0619,         0.0425,         0.0198,        -0.0033,
        -0.0242,        -0.0407,        -0.0512,        -0.0548,        -0.0517,
        -0.0426,        -0.0291,        -0.0131,         0.0032,         0.0178,
         0.0290,         0.0359,         0.0379,         0.0352,         0.0286,
         0.0192,         0.0083,        -0.0027,        -0.0125,        -0.0200,
        -0.0247,        -0.0260,        -0.0242,        -0.0196,        -0.0130,
        -0.0054,         0.0023,         0.0091,         0.0142,         0.0172,
         0.0179,         0.0164,         0.0132,         0.0086,         0.0034,
        -0.0018,        -0.0064,        -0.0098,        -0.0118,        -0.0123,
        -0.0113,        -0.0090,        -0.0058,        -0.0022,         0.0014,
         0.0046,         0.0069,         0.0082,         0.0085,         0.0077,
         0.0060,        
] 
#   y1_Acceleration
y1 = [
        -1.0000,        -0.8582,        -0.6278,        -0.3437,        -0.0432,
         0.2381,         0.4697,         0.6288,         0.7022,         0.6872,
         0.5914,         0.4318,         0.2324,         0.0203,        -0.1773,
        -0.3373,        -0.4435,        -0.4875,        -0.4698,        -0.3980,
        -0.2855,        -0.1489,        -0.0060,         0.1261,         0.2331,
         0.3045,         0.3347,         0.3229,         0.2735,         0.1951,
         0.0994,        -0.0008,        -0.0928,        -0.1662,        -0.2136,
        -0.2316,        -0.2205,        -0.1843,        -0.1293,        -0.0637,
         0.0040,         0.0659,         0.1152,         0.1471,         0.1592,
         0.1514,         0.1263,         0.0879,         0.0421,        -0.0052,
        -0.0481,        -0.0817,        -0.1028,        -0.1099,        -0.1034,
        -0.0851,        -0.0584,        -0.0269,         0.0052,         0.0341,
         0.0567,         0.0709,         0.0756,         0.0709,         0.0582,
         0.0395,         0.0176,        -0.0047,        -0.0247,        -0.0400,
        -0.0494,        -0.0521,        -0.0484,        -0.0393,        -0.0262,
        -0.0112,         0.0040,         0.0175,         0.0278,         0.0341,
         0.0358,         0.0332,         0.0268,         0.0177,         0.0072,
        -0.0033,        -0.0126,        -0.0196,        -0.0237,        -0.0247,
        -0.0226,        -0.0181,        -0.0117,        -0.0045,         0.0026,
         0.0089,         0.0136,         0.0164,         0.0170,         0.0155,
         0.0123,        
] 

plt.figure(figsize = (8, 4))
plt.subplots_adjust(bottom = 0.2, left = 0.2) 

plt.plot(t, y0, 'r-', label = r'$Point_0$', lw = 3)
plt.plot(t, y1, 'b-', label = r'$Point_0$', lw = 3) 

plt.xlabel(r'$Time(Sec)$').set_fontsize(16) 
plt.ylabel(r'$Amplitude$').set_fontsize(16)
plt.title("$***Time*and*Acceleration***$").set_fontsize(16) 

plt.grid(axis = 'both') 
plt.legend(loc = 'best') 

plt.show(); 