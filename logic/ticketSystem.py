from queue import Queue

class TicketSystem:
    def __init__(self):
        self.priority_queue = Queue()
        self.general_queue = Queue()
        self.currency_exchange_queue = Queue()
        self.general_counter = 0
        self.ticket_counter = 0

    def insertar_general(self):
        self.ticket_counter += 1
        self.general_queue.enqueue("General", self.ticket_counter)

    def insertar_preferencial(self):
        self.ticket_counter += 1
        self.priority_queue.enqueue("Priority", self.ticket_counter)

    def insertar_cambio_de_moneda(self):
        self.ticket_counter += 1
        self.currency_exchange_queue.enqueue("Currency Exchange", self.ticket_counter)

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


ticket_system = TicketSystem()

ticket_system.insertar_general()
ticket_system.insertar_preferencial()
ticket_system.insertar_cambio_de_moneda()
ticket_system.insertar_general()

next_ticket = ticket_system.next_ticket()
if next_ticket:
    print(f"Próximo ticket a atender: Ticket {next_ticket.value} ({next_ticket.priority})")
else:
    print("No hay tickets en espera.")
