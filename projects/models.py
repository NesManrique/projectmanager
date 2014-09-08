from django.db import models

class Project(models.Model):

	VERTICALES = (
		('BD','Base de Datos'),
		('IF','Infraestructura'),
		('JW','JavaWeb'),
		('PL','PL/SQL'),
		('MW','Middleware'),
		('AN','Analisis'),
	)

	STATUS = (
		('Potencial','Potencial'),
		('Aprobado','Aprobado'),
		('Ejecucion','En Ejecucion'),
	)

	DETALLE = (
		('Potencial',(
				('Analisis','En Analisis'),
				('PropVentas','Propuesta enviada a ventas'),
			)
		),
		('Aprobado',(
				('CoordInic','En Coordinaciones de Inicio'),
				('EsperaYV','En espera por YV'),
				('EsperaCliente','En espera por Cliente'),
		  	)
		),
		('Ejecucion',(
				('ST','Satisfactoria a Tiempo'),
				('SR','Satisfactoria con Riesgo'),
				('DE','Desviado'),
				('RI','En Riesgo'),
		  	)
		),
		('unknown','Desconocido'),
	)

	creado = models.DateTimeField(auto_now_add=True)
	modificado = models.DateTimeField(auto_now=True)
	titulo = models.CharField(max_length=200)
	cliente = models.CharField(max_length=200)
	verticales = models.CharField(choices=VERTICALES,max_length=500,blank=True)
	inicio = models.DateField(blank=True,null=True)
	fin = models.DateField(blank=True,null=True)
	horas_asig = models.IntegerField(blank=True)
	horas_sem = models.IntegerField(blank=True)
	horas_acum = models.IntegerField(blank=True)
	horas_totales = models.IntegerField(blank=True)
	status = models.CharField(choices=STATUS,max_length=200, blank=True, default='Potencial')
	detalle = models.CharField(choices=DETALLE,max_length=200, blank=True, default='unknown')
	consultores = models.CharField(max_length=500)
	lider = models.CharField(max_length=100)

	class Meta:
		ordering = ('cliente','titulo')

	def save (self,*args,**kwargs):
		self.horas_totales=self.horas_sem+self.horas_acum
		super(Project,self).save(*args,**kwargs)

class Update(models.Model):
	proyecto = models.ForeignKey(Project, related_name='updates')
	creado = models.DateTimeField(auto_now_add=True)
	modificado = models.DateTimeField(auto_now_add=True)
	fecha_detalle = models.DateField()
	resumen = models.CharField(max_length=500,blank=True)
	descripcion = models.TextField()
