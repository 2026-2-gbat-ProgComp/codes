rede = [  { 'nome' : 'm1', 
			'ips'  : [ { 'ip': '200.17.143.126', 'mascara': 24 } ],
			'rotas': [ {
						 'destino': '0.0.0.0', 'mascara': 0,
						 'roteador': '200.17.143.31'
					   }
					 ]
		  },
		  { 'nome' : 'm2', 
			'ips'  : [ { 'ip': '200.17.143.19', 'mascara': 24 } ],
			'rotas': [ {
						 'destino': '0.0.0.0', 'mascara': 0,
						 'roteador': '200.17.143.31'
					   }
					 ]
		  },
		  { 'nome' : 'm3', 
			'ips'  : [ { 'ip': '200.17.143.119', 'mascara': 24 } ],
			'rotas': [ {
						 'destino': '0.0.0.0', 'mascara': 0,
						 'roteador': '200.17.143.31'
					   }
					 ]
		  },		  
		  { 'nome' : 'r1', 
			'ips'  : [ { 'ip': '16.12.15.1', 'mascara': 8 },
					   { 'ip': '200.17.143.31', 'mascara': 24 } ],
			'rotas': [ {
						 'destino': '0.0.0.0', 'mascara': 0,
						 'roteador': '16.12.15.2'
					   }
					 ]
		  },
		  { 'nome' : 'm4', 
			'ips'  : [ { 'ip': '16.12.15.5', 'mascara': 8 } ],
			'rotas': [ {
						 'destino': '0.0.0.0', 'mascara': 0,
						 'roteador': '16.12.15.2'
					   }
					 ]
		  },		  
		  { 'nome' : 'r2', 
			'ips'  : [ { 'ip': '16.12.15.2', 'mascara': 8 },
					   { 'ip': '168.151.93.2', 'mascara': 16 }, 					   
					   { 'ip': '231.116.193.21', 'mascara': 24 }
					 ],
			'rotas': [ {
						 'destino': '200.17.143.0', 'mascara': 24,
						 'roteador': '16.12.15.1'
					   }
					 ]
		  },		
		  { 'nome' : 'm5', 
			'ips'  : [ { 'ip': '231.116.193.22', 'mascara': 24 } ],
			'rotas': [ {
						 'destino': '0.0.0.0', 'mascara': 0,
						 'roteador': '231.116.193.21'
					   }
					 ]
		  },		  
		  { 'nome' : 'm6', 
			'ips'  : [ { 'ip': '231.116.193.122', 'mascara': 24 } ],
			'rotas': [ {
						 'destino': '0.0.0.0', 'mascara': 0,
						 'roteador': '231.116.193.21'
					   }
					 ]
		  },
		  { 'nome' : 'm7', 
			'ips'  : [ { 'ip': '231.116.193.71', 'mascara': 24 } ],
			'rotas': [ {
						 'destino': '0.0.0.0', 'mascara': 0,
						 'roteador': '231.116.193.21'
					   }
					 ]
		  },		  
		  { 'nome' : 'm8', 
			'ips'  : [ { 'ip': '168.151.93.42', 'mascara': 16 } ],
			'rotas': [ {
						 'destino': '0.0.0.0', 'mascara': 0,
						 'roteador': '168.151.93.2'
					   }
					 ]
		  }
	]

ip_origem, ip_destino, dado = leia_envio()
while dado:
    if valida_ip(ip_origem) and valida_ip(ip_destino):
        envia_pacote() 
    ip_origem, ip_destino, dado = leia_envio()