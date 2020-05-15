from edgar.stock import Stock

stockAlexion = Stock('ALXN')
stockRegeneron = Stock('REN')
stockVertex = Stock('VRTX')
stockBiomarin = Stock('BMRN')
stockIncyte = Stock('INCY')


period = 'quarterly'

filingAlexion2018Q4 = stockAlexion.get_filing(period, 2018, 4)
filingAlexion2019Q1 = stockAlexion.get_filing(period, 2019, 1)
filingAlexion2019Q2 = stockAlexion.get_filing(period, 2019, 2)
filingAlexion2019Q3 = stockAlexion.get_filing(period, 2019, 3)
filingAlexion2019Q4 = stockAlexion.get_filing(period, 2019, 4)
filingAlexion2020Q1 = stockAlexion.get_filing(period, 2020, 1)


bSheetAlexion2018Q4 = filingAlexion2018Q4.get_balance_sheets()
bSheetAlexion2019Q1 = filingAlexion2019Q1.get_balance_sheets()
bSheetAlexion2019Q2 = filingAlexion2019Q2.get_balance_sheets()
bSheetAlexion2019Q3 = filingAlexion2019Q3.get_balance_sheets()
bSheetAlexion2019Q4 = filingAlexion2019Q4.get_balance_sheets()
bSheetAlexion2020Q1 = filingAlexion2020Q1.get_balance_sheets()

filingRegeneron2018Q4 = stockRegeneron.get_filing(period, 2018, 4)
filingRegeneron2019Q1 = stockRegeneron.get_filing(period, 2019, 1)
filingRegeneron2019Q2 = stockRegeneron.get_filing(period, 2019, 2)
filingRegeneron2019Q3 = stockRegeneron.get_filing(period, 2019, 3)
filingRegeneron2019Q4 = stockRegeneron.get_filing(period, 2019, 4)
filingRegeneron2020Q1 = stockRegeneron.get_filing(period, 2020, 1)


bSheetRegeneron2018Q4 = filingRegeneron2018Q4.get_balance_sheets()
bSheetRegeneron2019Q1 = filingRegeneron2019Q1.get_balance_sheets()
bSheetRegeneron2019Q2 = filingRegeneron2019Q2.get_balance_sheets()
bSheetRegeneron2019Q3 = filingRegeneron2019Q3.get_balance_sheets()
bSheetRegeneron2019Q4 = filingRegeneron2019Q4.get_balance_sheets()
bSheetRegeneron2020Q1 = filingRegeneron2020Q1.get_balance_sheets()

filingVertex2018Q4 = stockVertex.get_filing(period, 2018, 4)
filingVertex2019Q1 = stockVertex.get_filing(period, 2019, 1)
filingVertex2019Q2 = stockVertex.get_filing(period, 2019, 2)
filingVertex2019Q3 = stockVertex.get_filing(period, 2019, 3)
filingVertex2019Q4 = stockVertex.get_filing(period, 2019, 4)
filingVertex2020Q1 = stockVertex.get_filing(period, 2020, 1)


bSheetVertex2018Q4 = filingVertex2018Q4.get_balance_sheets()
bSheetVertex2019Q1 = filingVertex2019Q1.get_balance_sheets()
bSheetVertex2019Q2 = filingVertex2019Q2.get_balance_sheets()
bSheetVertex2019Q3 = filingVertex2019Q3.get_balance_sheets()
bSheetVertex2019Q4 = filingVertex2019Q4.get_balance_sheets()
bSheetVertex2020Q1 = filingVertex2020Q1.get_balance_sheets()

filingBiomarin2018Q4 = stockBiomarin.get_filing(period, 2018, 4)
filingBiomarin2019Q1 = stockBiomarin.get_filing(period, 2019, 1)
filingBiomarin2019Q2 = stockBiomarin.get_filing(period, 2019, 2)
filingBiomarin2019Q3 = stockBiomarin.get_filing(period, 2019, 3)
filingBiomarin2019Q4 = stockBiomarin.get_filing(period, 2019, 4)
filingBiomarin2020Q1 = stockBiomarin.get_filing(period, 2020, 1)


bSheetBiomarin2018Q4 = filingBiomarin2018Q4.get_balance_sheets()
bSheetBiomarin2019Q1 = filingBiomarin2019Q1.get_balance_sheets()
bSheetBiomarin2019Q2 = filingBiomarin2019Q2.get_balance_sheets()
bSheetBiomarin2019Q3 = filingBiomarin2019Q3.get_balance_sheets()
bSheetBiomarin2019Q4 = filingBiomarin2019Q4.get_balance_sheets()
bSheetBiomarin2020Q1 = filingBiomarin2020Q1.get_balance_sheets()

filingIncyte2018Q4 = stockIncyte.get_filing(period, 2018, 4)
filingIncyte2019Q1 = stockIncyte.get_filing(period, 2019, 1)
filingIncyte2019Q2 = stockIncyte.get_filing(period, 2019, 2)
filingIncyte2019Q3 = stockIncyte.get_filing(period, 2019, 3)
filingIncyte2019Q4 = stockIncyte.get_filing(period, 2019, 4)
filingIncyte2020Q1 = stockIncyte.get_filing(period, 2020, 1)


bSheetIncyte2018Q4 = filingIncyte2018Q4.get_balance_sheets()
bSheetIncyte2019Q1 = filingIncyte2019Q1.get_balance_sheets()
bSheetIncyte2019Q2 = filingIncyte2019Q2.get_balance_sheets()
bSheetIncyte2019Q3 = filingIncyte2019Q3.get_balance_sheets()
bSheetIncyte2019Q4 = filingIncyte2019Q4.get_balance_sheets()
bSheetIncyte2020Q1 = filingIncyte2020Q1.get_balance_sheets()

