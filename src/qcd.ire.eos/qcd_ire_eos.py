#!/usr/bin/python

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


"""
    qcd_ire_eos.py - Generates the EoS table.

    History:
    Version 0.1: 2015/11/02     (rsouza) - Creating the file.

    Usage:
        qcd_ire_eos.py

    Example:
        ./qcd_ire_eos.py

"""

import sys
import scipy.integrate as integrate
import numpy as np
import qcd_ire_equations as qcd_eqs


def main(argv):
    print("qcd.ire.eos.py")

    irq_qcd_parameters = qcd_eqs.IREQCDParameters(m3=0.196,
                                                  m2=0.639,
                                                  m0=0.014,
                                                  Nc=3.,
                                                  Nf=2.)

    irq_qcd_eqs = qcd_eqs.IREQCDEquations(irq_qcd_parameters)

    irq_qcd_eqs.output_header()

    mu = .3
    correct_eval = 3.30332e-16

    limits_p = [0, mu]
    limits_theta = [0, np.inf]
    nquad_options = [{'limit': 10000}, {'limit': 10000}]
    function_f_args = (mu,)

    ans_dblquad, err_dblquad = integrate.dblquad(irq_qcd_eqs.function_f,
                                                 0, np.inf,  # p integration limit
                                                 lambda x: 0, lambda x: mu,  # theta integration limit
                                                 function_f_args)

    ans_nquad, err_nquad = integrate.nquad(func=irq_qcd_eqs.function_f,
                                           ranges=[limits_p, limits_theta],
                                           args=function_f_args,
                                           opts=nquad_options)

    # log_Z = (2. * 4. / (2. * np.pi) ** 3.) * irq_qcd_parameters.Nf * irq_qcd_parameters.Nc * ans
    log_Z_ans_dblquad = (1. / 2 * np.pi ** 3.) * irq_qcd_parameters.Nf * irq_qcd_parameters.Nc * ans_dblquad
    log_Z_ans_nquad = (1. / 2 * np.pi ** 3.) * irq_qcd_parameters.Nf * irq_qcd_parameters.Nc * ans_nquad

    print("log_Z_ans_dblquad = {} * (V/T)".format(log_Z_ans_dblquad))
    print("log_Z_ans_nquad = {} * (V/T)".format(log_Z_ans_nquad))
    print("correct_eval = {}".format(correct_eval))
    print("log_Z_ans_dblquad/correct_eval = {}".format(log_Z_ans_dblquad / correct_eval))
    print("log_Z_ans_nquad/correct_eval = {}".format(log_Z_ans_nquad / correct_eval))


if __name__ == "__main__":
    main(sys.argv[1:])
