
from queue import Queue

class TicketSystem:
    def __init__(self):
        self.priority_queue = Queue()
        self.general_queue = Queue()
        self.currency_exchange_queue = Queue()
        self.general_counter = 0
        self.priority_counter = 0
        self.general_ticket_counter = 0
        self.currency_counter = 0

    def insertar_general(self):
        self.general_ticket_counter += 1
        ticket_id = f"G-{self.general_ticket_counter}"
        self.general_queue.enqueue("General", ticket_id)
        return ticket_id

    def insertar_preferencial(self):
        self.priority_counter += 1
        ticket_id = f"P-{self.priority_counter}"
        self.priority_queue.enqueue("Preferencial", ticket_id)
        return ticket_id

    def insertar_cambio_de_moneda(self):
        self.currency_counter += 1
        ticket_id = f"C-{self.currency_counter}"
        self.currency_exchange_queue.enqueue("Cambio de Moneda", ticket_id)
        return ticket_id

    def next_ticket(self):
        if self.priority_queue.head is not None:
            return self.priority_queue.dequeue()
        elif self.general_counter >= 2 and self.currency_exchange_queue.head is not None:
            self.general_counter = 0
            return self.currency_exchange_queue.dequeue()
        elif self.general_queue.head is not None:
            self.general_counter += 1
            return self.general_queue.dequeue()
        elif self.currency_exchange_queue.head is not None:
            return self.currency_exchange_queue.dequeue()
        else:
            return None

    def cancel_ticket(self, ticket_to_cancel):
        if self.priority_queue.remove_ticket(ticket_to_cancel):
            return True
        if self.general_queue.remove_ticket(ticket_to_cancel):
            return True
        if self.currency_exchange_queue.remove_ticket(ticket_to_cancel):
            return True
        return False

    def show_status(self):
        status = []
        general_counter = 0
        priority_list = self.priority_queue.list_all()
        general_list = self.general_queue.list_all()
        currency_list = self.currency_exchange_queue.list_all()
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
