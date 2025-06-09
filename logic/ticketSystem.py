from cola import Cola
from lista_enlazada import ListaEnlazada
from hashmap import HashMap

class TicketSystem:
    def __init__(self):
        self.priority_cola = Cola()
        self.general_cola = Cola()
        self.currency_exchange_cola = Cola()

        self.ticket_map = HashMap()
        self.ordered_tickets = ListaEnlazada()

        self.general_counter = 0
        self.priority_counter = 0
        self.currency_counter = 0
        self.general_ticket_counter = 0

    def _crear_ticket(self, ticket_id, ticket_type):
        return [ticket_id, ticket_type]
    
    def insertar_general(self):
        self.general_counter += 1
        ticket_id = f"G-{self.general_counter}"
        ticket_data = self._crear_ticket(ticket_id, "General")
        self.general_cola.encolar(ticket_data)
        self.ticket_map.put("G", ticket_id)
        self.ordered_tickets.agregar(ticket_data)
        return ticket_id

    def insertar_preferencial(self):
        self.priority_counter += 1
        ticket_id = f"P-{self.priority_counter}"
        ticket_data = self._crear_ticket(ticket_id, "Preferencial")
        self.priority_cola.encolar(ticket_data)
        self.ticket_map.put("P", ticket_id)
        self.ordered_tickets.agregar(ticket_data)
        return ticket_id

    def insertar_cambio_de_moneda(self):
        self.currency_counter += 1
        ticket_id = f"C-{self.currency_counter}"
        ticket_data = self._crear_ticket(ticket_id, "Cambio de Moneda")
        self.currency_exchange_cola.encolar(ticket_data)
        self.ticket_map.put("C", ticket_id)
        self.ordered_tickets.agregar(ticket_data)
        return ticket_id

    def next_ticket(self):
        if not self.priority_cola.is_empty():
            ticket_data = self.priority_cola.desencolar()
            self.ticket_map.remove_ticket(ticket_data[0])
            self.ordered_tickets.eliminar(ticket_data[0])
            return ticket_data
        
        if (self.general_ticket_counter >= 2 and not self.currency_exchange_cola.is_empty()):
            self.general_ticket_counter = 0
            ticket_data = self.currency_exchange_cola.desencolar()
            self.ticket_map.remove_ticket(ticket_data[0])
            self.ordered_tickets.eliminar(ticket_data[0])
            return ticket_data
        
        if not self.general_cola.is_empty():
            self.general_ticket_counter += 1
            ticket_data = self.general_cola.desencolar()
            self.ticket_map.remove_ticket(ticket_data[0])
            self.ordered_tickets.eliminar(ticket_data[0])
            return ticket_data
        
        if not self.currency_exchange_cola.is_empty():
            ticket_data = self.currency_exchange_cola.desencolar()
            self.ticket_map.remove_ticket(ticket_data[0])
            self.ordered_tickets.eliminar(ticket_data[0])
            return ticket_data
        
        return None

    def show_status(self):
        tickets = self.ordered_tickets.mostrar()
        result = []
        for ticket in tickets:
            formatted_ticket = ticket[0] + ' ' + ticket[1]
            result.append(formatted_ticket)
        return result
    
    def cancel_ticket(self, ticket_id):
        if not self.ticket_map.exists_ticket(ticket_id):
            return False
        self.ticket_map.remove_ticket(ticket_id)
        ticket_type = ticket_id[0]
        removed = False
        if ticket_type == "G":
            removed = self.general_cola.remove_ticket_id(ticket_id)
        elif ticket_type == "P":
            removed = self.priority_cola.remove_ticket_id(ticket_id)
        elif ticket_type == "C":
            removed = self.currency_exchange_cola.remove_ticket_id(ticket_id)
        if removed:
            self.ordered_tickets.eliminar(ticket_id)
        return removed

ticket_system = TicketSystem()
print(ticket_system.insertar_general())
print(ticket_system.insertar_general())
print(ticket_system.insertar_general())
print(ticket_system.insertar_preferencial())
print(ticket_system.insertar_preferencial())
print(ticket_system.insertar_cambio_de_moneda())
print("Estado: ",ticket_system.show_status())

print(ticket_system.next_ticket())
print(ticket_system.next_ticket())
print(ticket_system.next_ticket())
print(ticket_system.next_ticket())

print(ticket_system.cancel_ticket("G-3"))
print(ticket_system.cancel_ticket("G-1"))
print("Estado: ", ticket_system.show_status())
print(ticket_system.next_ticket())

print("Estado: ", ticket_system.show_status())
