class Graph:
	def __init__(self,v):
		self.v=v
		self.graph=[[0 for r in range(v)] for c in range(v)]
	def Print(self,d):
		for i in range(self.v):
			print(f"Dis from src 0 to {i} is {d[i]}")
	def mind(self,d,spt):
		m = 99999
		for v in range(self.v):
			if (d[v] < m and spt[v] == False):
				m = d[v]
				mi = v
		return mi
	def dij(self,src):
		d=[99999]*self.v
		spt = [False]*self.v
		d[src]=0
		for c in range(self.v):
			u=self.mind(d,spt)
			spt[u]=True
			for v in range(self.v):
				if(self.graph[u][v] > 0 and spt[v] == False and d[v] >d[u] + self.graph[u][v]):
					d[v] = d[u]+self.graph[u][v]
		self.Print(d)
g=Graph(6)
g.graph =[[0,4,4,0,0,0],[4,0,1,0,0,0],[4,1,0,3,2,6],[0,0,3,0,0,2],[0,0,2,0,0,1],[0,0,6,2,1,0]]
g.dij(0)		
