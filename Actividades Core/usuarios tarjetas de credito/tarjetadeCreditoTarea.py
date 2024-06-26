class TarjetaCredito:

  
   def __init__(self, saldo_pagar, limite_credito, intereses):

      self.saldo_pagar = saldo_pagar
      self.limite_credito = limite_credito
      self.interes = intereses
      
         
   def compra(self, monto):
      if (monto+self.saldo_pagar) < self.limite_credito:
         self.saldo_pagar += monto #el saldo aumenta con el monto ya que tiene cupo
         
      else:
         print( "Tarjeta Rechazada, has alcanzado tu límite de crédito")
      print(f"Total Comprado hasta ahora: {self.saldo_pagar}")

   def pago(self, monto):
      self.saldo_pagar -= monto
      print(f"Pagaste: {monto} Redujiste tu deuda, ahora solo debes: {self.saldo_pagar}")
      

   def cobrar_interes(self):
      print(f"Este es el saldo a pagar: {self.saldo_pagar}")
      self.saldo_pagar += self.saldo_pagar * 0.02
      print(f"Tu saldo a pagar sumado con intereses ahora es: {self.saldo_pagar}")

   def mostrar_info_tarjeta(self):
      print(f"Saldo a Pagar: ${self.saldo_pagar}")
