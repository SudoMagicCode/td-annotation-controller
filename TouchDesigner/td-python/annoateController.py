class PosScaleAdjust:

	def __init__(self, my_op) -> None:
		self.Owner_op = my_op
		self.Updating_op = False
		
	
	def Parse_par_change(self, par:callable) -> None:
		
		try:
			func = getattr(self.Owner_op, par.name)
			func(par)
		
		except Exception as e:
			print(e)
			pass

	@property
	def _get_target(self) -> callable:
		return self.Owner_op.par.Targetop.eval()
			
	def Targetop(self, par:callable) -> None:
		self.Updating_op = True
		print(par.eval())
		if par.eval() != None:
		
			self.Owner_op.par.Sizew = par.eval().nodeWidth
			self.Owner_op.par.Sizeh = par.eval().nodeHeight
			self.Owner_op.par.Networkpositionx = par.eval().nodeX
			self.Owner_op.par.Networkpositiony = par.eval().nodeY
			self.Owner_op.par.Title = par.eval().par.Titletext.eval()
		
		else:
			self.Owner_op.par.Sizew = 0
			self.Owner_op.par.Sizeh = 0
			self.Owner_op.par.Networkpositionx = 0
			self.Owner_op.par.Networkpositiony = 0
			self.Owner_op.par.Title = ''			
	
		self.Updating_op = False
		
	
	def Sizew(self, par:callable) -> None:
		if self.Updating_op:
			pass
		else:
			self._get_target.nodeWidth = par.eval()
		
	def Sizeh(self, par:callable) -> None:
		if self.Updating_op:
			pass
		else:
			self._get_target.nodeHeight = par.eval()
		
	def Networkpositionx(self, par:callable) -> None:
		if self.Updating_op:
			pass
		else:
			self._get_target.nodeX = par.eval()		
		
	def Networkpositiony(self, par:callable) -> None:
		if self.Updating_op:
			pass
		else:
			self._get_target.nodeY = par.eval()		