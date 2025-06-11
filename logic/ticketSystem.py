
from cola import ColaPrioridad

class TicketSystem:
    def __init__(self):
        self.priority_cola = ColaPrioridad()
        self.general_cola = ColaPrioridad()
        self.currency_exchange_cola = ColaPrioridad()
        self.general_counter = 0
        self.priority_counter = 0
        self.general_ticket_counter = 0
        self.currency_counter = 0

    def insertar_general(self):
        self.general_ticket_counter += 1
        ticket_id = f"G-{self.general_ticket_counter}"
        self.general_cola.encolar("General", ticket_id)
        return ticket_id

    def insertar_preferencial(self):
        self.priority_counter += 1
        ticket_id = f"P-{self.priority_counter}"
        self.priority_cola.encolar("Preferencial", ticket_id)
        return ticket_id

    def insertar_cambio_de_moneda(self):
        self.currency_counter += 1
        ticket_id = f"C-{self.currency_counter}"
        self.currency_exchange_cola.encolar("Cambio de Moneda", ticket_id)
        return ticket_id

    def next_ticket(self):
        if self.priority_cola.head is not None:
            return self.priority_cola.desencolar()
        elif self.general_counter >= 2 and self.currency_exchange_cola.head is not None:
            self.general_counter = 0
            return self.currency_exchange_cola.desencolar()
        elif self.general_cola.head is not None:
            self.general_counter += 1
            return self.general_cola.desencolar()
        elif self.currency_exchange_cola.head is not None:
            return self.currency_exchange_cola.desencolar()
        else:
            return None

    def cancel_ticket(self, ticket_to_cancel):
        if self.priority_cola.remove_ticket(ticket_to_cancel):
            return True
        if self.general_cola.remove_ticket(ticket_to_cancel):
            return True
        if self.currency_exchange_cola.remove_ticket(ticket_to_cancel):
            return True
        return False

    def show_status(self):
        status = []
        general_counter = 0
        priority_list = self.priority_cola.mostrar()
        general_list = self.general_cola.mostrar()
        currency_list = self.currency_exchange_cola.mostrar()
        i, j, k = 0, 0, 0

        while i < len(priority_list) or j < len(general_list) or k < len(currency_list):
            if i < len(priority_list):
                status.append(priority_list[i])
                i += 1
            elif general_counter >= 2 and k < len(currency_list):
                status.append(currency_list[k])
                k += 1
                general_counter = 0
            elif j < len(general_list):
                status.append(general_list[j])
                j += 1
                general_counter += 1
            elif k < len(currency_list):
                status.append(currency_list[k])
                k += 1
        return status
