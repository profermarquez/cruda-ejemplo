from django.db import models

class Venta(models.Model):
    PAIS_CHOICES = [
        ('Argentina', 'Argentina'),
        ('Brasil', 'Brasil'),
        ('Chile', 'Chile'),
        # Agrega más países si es necesario
    ]

    FORMA_VENTA_CHOICES = [
        ('Online', 'Online'),
        ('Presencial', 'Presencial'),
    ]

    FORMA_PAGO_CHOICES = [
        ('Efectivo', 'Efectivo'),
        ('Tarjeta de Crédito', 'Tarjeta de Crédito'),
        ('Transferencia', 'Transferencia'),
    ]

    pais = models.CharField(max_length=50, choices=PAIS_CHOICES)
    forma_venta = models.CharField(max_length=50, choices=FORMA_VENTA_CHOICES)
    forma_pago = models.CharField(max_length=50, choices=FORMA_PAGO_CHOICES)
    producto = models.CharField(max_length=100)
    vendedor = models.CharField(max_length=100)
    fecha = models.DateField()
    ventas = models.DecimalField(max_digits=10, decimal_places=2)
    cantidad = models.PositiveIntegerField()
    comision = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"{self.producto} vendido por {self.vendedor}"
