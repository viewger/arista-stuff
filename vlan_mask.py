#!/usr/bin/env python3

#########################################################################
#                                                                       #
# Takes a range of VLANs and generates a compressed list in the form of #
# (starting VLAN, mask) representation. Can be useful to generate       #
# configuration files for networking devices.                           #
#                                                                       #
# === EXAMPLE: ===                                                      #
# For the VLAN List: 2-5, 33, 37, 67-78, 333-1234                       #
#                                                                       #
# theVlanList = set (range (2,6))     | \                               #
#                          { 33, 37 } | \                               #
#               set (range (67,79))   | \                               #
#               set (range (333,1235))                                  #
#                                                                       #
# === NOTE: ===                                                         #
# The "+1" for the range ending values, because range() ends _before_   #
# the final value, without reaching it!                                 #
#                                                                       #
# === RESULTS: ===                                                      #
# $ /usr/bin/python3 vlan_mask.py                                       #
#     vlan  512  mask  3584                                             #
#     vlan  384  mask  3968                                             #
#     vlan  1024  mask  3968                                            #
#     vlan  1152  mask  4032                                            #
#     vlan  352  mask  4064                                             #
#     vlan  336  mask  4080                                             #
#     vlan  1216  mask  4080                                            #
#     vlan  68  mask  4092                                              #
#     vlan  72  mask  4092                                              #
#     vlan  2  mask  4094                                               #
#     vlan  4  mask  4094                                               #
#     vlan  76  mask  4094                                              #
#     vlan  334  mask  4094                                             #
#     vlan  1232  mask  4094                                            #
#     vlan  33  mask  4095                                              #
#     vlan  37  mask  4095                                              #
#     vlan  67  mask  4095                                              #
#     vlan  78  mask  4095                                              #
#     vlan  333  mask  4095                                             #
#     vlan  1234  mask  4095                                            #
#                                                                       #
#########################################################################

### Define your VLAN list here ###
theVlanList = set (range (2,6))     | \
                         { 33, 37 } | \
              set (range (67,79))   | \
              set (range (333,1235))

### Nothing to change below this line ###
for maskLen in range (1, 13):
  segLen = 2 ** (12 - maskLen)
  segNum = int (4096 / segLen)

  for segNr in range (1, segNum):
    vlanFirst = segNr * segLen
    vlanLast = (segNr + 1) * segLen
    aVlanList = set (range (vlanFirst, vlanLast))

    if (theVlanList & aVlanList) == aVlanList :
        print ("vlan ", vlanFirst, " mask ", 4096 - segLen)
        theVlanList = theVlanList - aVlanList
        if theVlanList == { }:
          break
