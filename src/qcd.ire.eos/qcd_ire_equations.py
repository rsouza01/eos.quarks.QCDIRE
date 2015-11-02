

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



class IREQCDEquations:
    """ IRE QCD equations. """

    def __init__(self, m3, m2, mp):
        
        self.__m3 = m3
        self.__m2 = m2
        self.__mp = mp
        

    def omega_2(self, zeta, p, mp):
        
        return p**2. + (self.__m3/(-zeta + p^2 + self.__m2) + self.__mp)**2.
