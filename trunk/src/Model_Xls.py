# -*- coding: utf-8 -*-
"""
	Model Xls stores data related to xls file reading
"""
class Model_Xls(object):
	"""
		ModelXls class that stores infomation about xls file reading 
	"""
	def __init__(self, file_name = "./Inscritos_2010-2011 (formato Excel xls).xls"):
		"""
			contructor of class model xls intialises the dictionary with columns index of year 
			and data about xls file
		"""
		self.COL_YEAR_95_96 = 7
		self.COL_YEAR_96_97 = 10
		self.COL_YEAR_97_98 = 13
		self.COL_YEAR_98_99 = 16
		self.COL_YEAR_99_00 = 19
		self.COL_YEAR_00_01 = 22
		self.COL_YEAR_01_02 = 25
		self.COL_YEAR_02_03 = 28
		self.COL_YEAR_03_04 = 31
		self.COL_YEAR_04_05 = 34
		self.COL_YEAR_05_06 = 37
		self.COL_YEAR_06_07 = 40
		self.COL_YEAR_07_08 = 43
		self.COL_YEAR_08_09 = 47
		self.COL_YEAR_09_10 = 50
		self.COL_YEAR_10_11 = 53
		self.Dic_Year={self.COL_YEAR_95_96:'1995/96', 
			self.COL_YEAR_96_97:'1996/97', 
			self.COL_YEAR_97_98:'1997/98', 
			self.COL_YEAR_98_99:'1998/99', 
			self.COL_YEAR_99_00:'1999/00', 
			self.COL_YEAR_00_01:'2000/01', 
			self.COL_YEAR_01_02:'2001/02', 
			self.COL_YEAR_02_03:'2002/03', 
			self.COL_YEAR_03_04:'2003/04', 
			self.COL_YEAR_04_05:'2004/05', 
			self.COL_YEAR_05_06:'2005/06', 
			self.COL_YEAR_06_07:'2006/07', 
			self.COL_YEAR_07_08:'2007/08', 
			self.COL_YEAR_08_09:'2008/09', 
			self.COL_YEAR_09_10:'2009/10', 
			self.COL_YEAR_10_11:'2010/11'
		}
		self.file_name = file_name
		self.sheet = 30
		self.sheet = self.open_Book()
		self.l_major_data = []
		self.l_years_major = []
		self.uni, self.fac, self.niv = '', '', ''