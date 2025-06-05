
import streamlit as st
from ticketSystem import TicketSystem

# --- CONFIGURACIÓN DE LA PÁGINA ---
st.set_page_config(
    page_title="Gestión de Turnos Bancarios",
    layout="wide"
)

# --- INICIALIZACIÓN ---
if 'ticket_system' not in st.session_state:
    st.session_state.ticket_system = TicketSystem()

ticket_system = st.session_state.ticket_system

# --- INTERFAZ ---
st.markdown("<h1 style='text-align: center;'>🎫 Sistema de Gestión de Turnos Bancarios</h1>", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.header("🎫 Registrar nuevo ticket")
    tipo = st.radio("Selecciona el tipo de atención", ["General", "Preferencial", "Cambio de moneda"])
    if st.button("Registrar Ticket"):
        if tipo == "General":
            ticket_system.insertar_general()
            st.success("🎟️ Ticket General registrado")
        elif tipo == "Preferencial":
            ticket_system.insertar_preferencial()
            st.success("♿ Ticket Preferencial registrado")
        else:
            ticket_system.insertar_cambio_de_moneda()
            st.success("💱 Ticket de Cambio de Moneda registrado")

    st.markdown("---")

    st.header("❌ Cancelar ticket")
    ticket_id = st.text_input("Número de ticket a cancelar")
    if st.button("Cancelar Ticket"):
        if ticket_id.strip() != "":
            success = ticket_system.cancel_ticket(ticket_id.strip())
            if success:
                st.success(f"Ticket {ticket_id} cancelado correctamente")
            else:
                st.warning(f"No se encontró el ticket {ticket_id}")
        else:
            st.warning("Ingresa un número de ticket válido")

with col2:
    st.header("⏭️ Atender próximo ticket")
    if st.button("Atender"):
        ticket = ticket_system.next_ticket()
        if ticket:
            st.success(f"Atendiendo ticket: {ticket.value} ({ticket.priority})")
        else:
            st.info("No hay tickets por atender")

with col3:
    st.header("📋 Estado actual de la fila de espera")
    tickets = ticket_system.show_status()
    if tickets:
        for i, (value, priority) in enumerate(tickets, start=1):
            st.write(f"{i}. Ticket {value} ({priority})")
    else:
        st.info("No hay tickets en espera.")
