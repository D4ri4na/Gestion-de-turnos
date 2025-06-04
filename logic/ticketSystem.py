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

    def insertar_preferencial(self):
        self.priority_counter += 1
        ticket_id = f"P-{self.priority_counter}"
        self.priority_queue.enqueue("Priority", ticket_id)

    def insertar_cambio_de_moneda(self):
        self.currency_counter += 1
        ticket_id = f"C-{self.currency_counter}"
        self.currency_exchange_queue.enqueue("Currency Exchange", ticket_id)

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
        print("--- Tickets por atender ---")
        order_number = 1
        general_counter = 0
        priority_current = self.priority_queue.head
        general_current = self.general_queue.head
        currency_current = self.currency_exchange_queue.head
        
        while (priority_current is not None or general_current is not None or currency_current is not None):
            if priority_current is not None:
                print(f"{order_number}. Ticket {priority_current.value} ({priority_current.priority})")
                priority_current = priority_current.next
                order_number += 1
            elif general_counter >= 2 and currency_current is not None:
                print(f"{order_number}. Ticket {currency_current.value} ({currency_current.priority})")
                currency_current = currency_current.next
                general_counter = 0
                order_number += 1
            elif general_current is not None:
                print(f"{order_number}. Ticket {general_current.value} ({general_current.priority})")
                general_current = general_current.next
                general_counter += 1
                order_number += 1
            elif currency_current is not None:
                print(f"{order_number}. Ticket {currency_current.value} ({currency_current.priority})")
                currency_current = currency_current.next
                order_number += 1

ticket_system = TicketSystem()

ticket_system.insertar_general()
ticket_system.insertar_preferencial()
ticket_system.insertar_cambio_de_moneda()
ticket_system.insertar_general()
ticket_system.insertar_preferencial()
ticket_system.insertar_general()
ticket_system.insertar_general()
ticket_system.insertar_cambio_de_moneda()
ticket_system.show_status()
ticket_system.cancel_ticket("G-2")
ticket_system.show_status()