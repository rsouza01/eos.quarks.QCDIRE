#!/usr/bin/python

# qcd_ire_equatios - QCD Infrared Renormalizable Extension EoS
# Copyright (C) 2015 Rodrigo Souza <rsouza01@gmail.com>

# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA
# 02110-1301, USA.


"""
    qcd_ire_equatios.py - Generates the EoS table.

    History:
    Version 0.1: 2015/11/02     (rsouza) - Creating the file.

    Usage:
        qcd_ire_equatios.py

    Example:
        ./qcd_ire_equatios.py

"""

import sys
import qcd_ire_equations as qcd_eqs

def main(argv):

    print("qcd.ire.eos.py")
    
    irqqcdeqs = qcd_eqs.IREQCDEquations(m3=196/1000, m2=639/1000, mp=3)
    
    
    print("omega_2 = {}".format(irqqcdeqs.omega_2(1, 1, 1)))
        
        
    

if __name__ == "__main__":
    main(sys.argv[1:])
