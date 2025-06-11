
import streamlit as st
from ticketSystem import TicketSystem
from PIL import Image
# --- CONFIGURACIÓN DE LA PÁGINA ---
st.set_page_config(
    page_title="Gestión de Turnos Bancarios",
    layout="wide"
)

# --- INICIALIZACIÓN ---
if 'ticket_system' not in st.session_state:
    st.session_state.ticket_system = TicketSystem()

ticket_system = st.session_state.ticket_system



menu, pantalla = st.columns(2)
with menu:
    st.markdown("""
    <style>
    div.stButton > button {
        height: 64px;
        font-size: 46px;
        padding: 3px 0px;
        background-color: #FFA500;  /* Azul */
        color: white ;               /* Texto blanco */
        border-radius: 10px;
        border: none;
    }
    </style>
""", unsafe_allow_html=True)
    st.markdown("<h1 style='text-align: center; color: white;'>Menú</h1>", unsafe_allow_html=True)
    st.markdown("   ")
    colum1, colum2, colum3 = st.columns(3)
    with colum1:
        if st.button("General", use_container_width=True):
            ticket_system.insertar_general()
    with colum3:
        if st.button("Cambio de Moneda", use_container_width=True):
            ticket_system.insertar_cambio_de_moneda()
    with colum2:
       
        if st.button("Preferencial", use_container_width=True):
            ticket_system.insertar_preferencial()
        

        # Botón general para mostrar el input de cancelar
        if 'mostrar_cancelar' not in st.session_state:
            st.session_state.mostrar_cancelar = False

        if st.button("Cancelar", use_container_width=True):
            st.session_state.mostrar_cancelar = True

        # Mostrar input y botón solo si se activó "Cancelar"
        if st.session_state.mostrar_cancelar:
            ticket_id = st.text_input("Número de ticket a cancelar")
            if st.button("Cancelar Ticket", use_container_width=True):
                if ticket_id.strip() != "":
                    success = ticket_system.cancel_ticket(ticket_id.strip())
                else:
                    st.warning("Ingresa un número de ticket válido")

    st.markdown("---")
    st.markdown("<p style='text-align: center;'>Gracias por su visita</p>", unsafe_allow_html=True)

    

with pantalla:

    st.markdown("<h1 style='text-align: center; color: white;'>Pantalla de Atención</h1>", unsafe_allow_html=True)
    st.markdown("  ")
    colum1, colum2, colum3 = st.columns(3)
    with colum2:
        if st.button("Atender", use_container_width=True):
            ticket = ticket_system.next_ticket()
            if ticket:
                st.session_state.ticket_atendiendo = ticket.value

    if 'ticket_atendiendo' not in st.session_state:
        st.session_state.ticket_atendiendo = None


    image = Image.open("bancoSol2.jpg")
    col1, col2, col3 = st.columns([1, 4, 1])  # Columna del medio es más ancha
    with col2:
        st.image(image, width=600)
        tickets = ticket_system.show_status()
    max_cuadros = 6
    # Prepara la lista de valores a mostrar (rellena con vacíos si faltan)
    valores = [value for value, _ in tickets[:max_cuadros]]
    while len(valores) < max_cuadros:
        valores.append("")

    # Construye los cuadrados con HTML y CSS
    html_cuadros = "<div style='display: flex; justify-content: center; gap: 18px;'>"
    for value in valores:
        if value == st.session_state.ticket_atendiendo:
            html_cuadros += (
                f"<div style='width:70px;height:70px;display:flex;align-items:center;justify-content:center;"
                "border:3px solid #d7263d;background:#eaf6ff;"
                "font-size:2em;font-weight:bold;color:#d7263d;"
                "text-decoration:underline;box-shadow:0 0 8px #d7263d;'>"
                f"{value}</div>"
            )
        elif value != "":
            html_cuadros += (
                f"<div style='width:70px;height:70px;display:flex;align-items:center;justify-content:center;"
                "border:2px solid #FFA500;background:#f4faff;"
                "font-size:2em;font-weight:bold;color:#FFA500;'>"
                f"{value}</div>"
            )
        else:
            html_cuadros += (
                "<div style='width:70px;height:70px;display:flex;align-items:center;justify-content:center;"
                "border:2px dashed #b0c4de;background:#f4faff;'></div>"
            )
    html_cuadros += "</div>"

    st.markdown(html_cuadros, unsafe_allow_html=True)

with st.container():
    st.markdown(
        """
        <style>
        .vertical-line {
            position: fixed;
            left: 50%;
            top: 0;
            bottom: 0;
            width: 6px;
            background-color: lightgray;
            z-index: 9999;
        }
        </style>
        <div class="vertical-line"></div>
        """,
        unsafe_allow_html=True
    )
    