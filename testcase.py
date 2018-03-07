import tax_cal


c1 = tax_cal.Couple(1, 300000, 108000)
c1.result(True)

c2 = tax_cal.Couple(2, 600000, 0)
c2.result(True)

c3 = tax_cal.Couple(3, 1200000, 1200000)
c3.result(False)

c4 = tax_cal.Couple(4, 420000, 240000)
c4.result(False)

c5 = tax_cal.Couple(5, 0, 840000)
c5.result(True)

c6 = tax_cal.Couple(6, 108000, 400000)
c6.result(True)

c7 = tax_cal.Couple(7, 126000, 126000)
c7.result(False)

c8 = tax_cal.Couple(8, 336000, 156000)
c8.result(False)

c9 = tax_cal.Couple(9, 156000, 0)
c9.result(True)

c10 = tax_cal.Couple(10, 200000, 200000)
c10.result(False)


c11 = tax_cal.Couple(11, 90000, 500000)
c11.result(True)

c12 = tax_cal.Couple(11, 130000, 160000)
c12.result(True)

c13 = tax_cal.Couple(12, 156000, 160000)
c13.result(True)

tax_cal.Accuracy()
c1.print_detail()
c2.print_detail()


