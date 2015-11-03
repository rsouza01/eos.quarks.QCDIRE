

# qcd_ire_equations - QCD Infrared Renormalizable Extension EoS
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

import math


class IREQCDParameters:

    def __init__(self, m3, m2, m0, Nf, Nc):

        self.m3 = m3
        self.m2 = m2
        self.m0 = m0

        self.Nf = Nf
        self.Nc = Nc


class IREQCDEquations:
    """ IRE QCD equations. """

    def __init__(self, parameters):
        
        self.__m3 = parameters.m3
        self.__m2 = parameters.m2
        self.__m0 = parameters.m0

        self.__Nf = parameters.Nf
        self.__Nc = parameters.Nc

    def omega_2(self, zeta, p):
        
        return p**2. + (self.__m0 + (self.__m3/(-zeta + p**2. + self.__m2)))**2.

    def function_f(self, p, theta, mu):

        # print("theta={}, mu={}, p={}".format(theta, mu, p))

        zeta = complex(mu, theta)

        numerator = self.omega_2(zeta**2., p) - zeta**2.
        denominator = self.omega_2(-theta**2., p) + theta**2.

        modulus = abs(numerator / denominator)

        return p**2. * math.log(modulus).real

    def output_header(self):
        header_format = \
            ("#---------------------------------------------------------------------------------------------\n"
             "#                     QCD IRE EoS\n"
             "#---------------------------------------------------------------------------------------------\n"
             "# N_f  : {}\n"
             "# N_c  : {}\n"
             "#\n"
             "# M_3  : {}\n"
             "# m_2  : {}\n"
             "# m_0  : {}\n"
             "#---------------------------------------------------------------------------------------------\n")

        print(header_format.format(self.__Nf,
                                   self.__Nc,
                                   self.__m3,
                                   self.__m2,
                                   self.__m0))
