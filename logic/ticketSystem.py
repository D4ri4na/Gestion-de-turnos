from cola_circular import ColaCircular

class TicketSystem:
    def __init__(self):
        self.cola = ColaCircular()
        self.general_ticket_counter = 0
        self.priority_counter = 0
        self.currency_counter = 0

    def insertar_general(self):
        self.general_ticket_counter += 1
        ticket_id = f"G-{self.general_ticket_counter}"
        self.cola.encolar(ticket_id)
        return ticket_id

    def insertar_preferencial(self):
        self.priority_counter += 1
        ticket_id = f"P-{self.priority_counter}"
        self.cola.encolar_al_principio(ticket_id)
        return ticket_id

    def insertar_cambio_de_moneda(self):
        self.currency_counter += 1
        ticket_id = f"C-{self.currency_counter}"
        if self.cola.general_counter >= 2:
            self.cola.encolar(ticket_id)
            self.cola.general_counter = 0  # Reiniciar el contador de tickets generales
        else:
            self.cola.encolar_al_final(ticket_id)
        return ticket_id

    def next_ticket(self):
        if self.cola.esta_vacia():
            return None
        ticket = self.cola.desencolar()
        if ticket.value.startswith("G-"):
            self.cola.general_counter += 1
        return ticket.value

    def cancel_ticket(self, ticket_to_cancel):
        return self.cola.remove_ticket(ticket_to_cancel)

    def show_status(self):
        return self.cola.mostrar()

# Ejemplo de uso
ticket_system = TicketSystem()
print("Insertar General:", ticket_system.insertar_general())
print("Insertar Cambio de Moneda:", ticket_system.insertar_cambio_de_moneda())
print("Insertar Preferencial:", ticket_system.insertar_preferencial())
print("Insertar General:", ticket_system.insertar_general())
print("Insertar General:", ticket_system.insertar_general())
print("Próximo Ticket:", ticket_system.next_ticket())
print("Estado Actual:", ticket_system.show_status())
