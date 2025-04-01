from reportlab.lib.pagesizes import letter, landscape
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Spacer, Image, Paragraph
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.lib.styles import getSampleStyleSheet
import os
import sys

# Datos de prueba (se pueden cargar desde una base de datos o archivo)
factura_info = [["Nro. Factura:", "F002"], ["Vendedor:", "V002"], ["Cliente:", "C002"], ["Fecha:", "2025-02-15"], ["Forma de Pago:", "E"], ["Estado:", "A"], ["Total IVA:", "1,001,000"], ["Total Factura:", "6,006,000"]]
cliente_info = [["Cliente:", "C002"], ["Nombre:", "Juan Pérez"], ["Dirección:", "Calle 123"], ["Teléfono:", "123456789"], ["Email:", "juan@email.com"]]
detalle_factura = [
    ["Nro. Factura", "Código Producto", "Precio Producto", "IVA", "Cantidad", "Subtotal"],
    ["F002", "P001", "500,000", "20%", "10", "6,000,000"],
    ["F002", "P002", "1,000", "20%", "5", "6,000"]
]

# Función para generar el PDF
def generar_pdf_factura():
    directorio = "reportesPDF"
    archivo_pdf = os.path.join(directorio, "factura.pdf") 

    #archivo_pdf = "Factura.pdf"
    doc = SimpleDocTemplate(archivo_pdf, pagesize=landscape(letter),
                            leftMargin=30, rightMargin=30,
                            topMargin=30, bottomMargin=30)
    elementos = []

    # Agregar el logo en la parte superior derecha
    logo_path = "logo.jpg"  # Asegúrate de que el archivo existe en la misma carpeta
    try:
        logo = Image(logo_path, width=1.5 * inch, height=0.7 * inch)
        logo.hAlign = 'RIGHT'
        elementos.append(logo)
    except:
        print("⚠️ No se encontró el logo. Se generará sin él.")

    # Espaciado después del logo
    elementos.append(Spacer(1, 10))

    # Agregar título de la factura
    estilo = getSampleStyleSheet()
    titulo = Paragraph("<b>FACTURA DE VENTA</b>", estilo["Title"])
    elementos.append(titulo)
    elementos.append(Spacer(1, 12))

    # Sección: Datos de la Factura
    tabla_factura = Table(factura_info, colWidths=[120, 200])
    tabla_factura.setStyle(TableStyle([
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ('BACKGROUND', (0, 0), (-1, 0), colors.lightgrey),
        ('TEXTCOLOR', (0, 0), (-1, -1), colors.black),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (-1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 0), (-1, -1), 10),
        ('LEFTPADDING', (0, 0), (-1, -1), 6),
        ('RIGHTPADDING', (0, 0), (-1, -1), 6),
    ]))
    elementos.append(tabla_factura)
    elementos.append(Spacer(1, 12))

    # Sección: Datos del Cliente
    tabla_cliente = Table(cliente_info, colWidths=[120, 300])
    tabla_cliente.setStyle(TableStyle([
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ('BACKGROUND', (0, 0), (-1, 0), colors.lightgrey),
        ('TEXTCOLOR', (0, 0), (-1, -1), colors.black),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (-1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 0), (-1, -1), 10),
        ('LEFTPADDING', (0, 0), (-1, -1), 6),
        ('RIGHTPADDING', (0, 0), (-1, -1), 6),
    ]))
    elementos.append(tabla_cliente)
    elementos.append(Spacer(1, 12))

    # Sección: Detalle de la Factura
    tabla_detalle = Table(detalle_factura, colWidths=[100, 120, 120, 60, 80, 120])
    tabla_detalle.setStyle(TableStyle([
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ('BACKGROUND', (0, 0), (-1, 0), colors.green),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 0), (-1, -1), 10),
        ('LEFTPADDING', (0, 0), (-1, -1), 6),
        ('RIGHTPADDING', (0, 0), (-1, -1), 6),
    ]))
    elementos.append(tabla_detalle)

    # Generar el PDF
    doc.build(elementos)
    print(f"✅ PDF generado correctamente: {archivo_pdf}")

# Llamar a la función para generar el PDF
generar_pdf_factura()

# Ejemplo de uso después de generar el PDF
                 
directorio = "reportesPDF"
archivo_pdf = os.path.join(directorio, "factura.pdf") 

def abrir_pdf(archivo_pdf):
    try:
        if sys.platform == "win32":  # Windows
            os.startfile(archivo_pdf)
        elif sys.platform == "darwin":  # macOS
            os.system(f"open {archivo_pdf}")
        elif sys.platform.startswith("linux"):  # Linux
            os.system(f"xdg-open {archivo_pdf}")
        else:
            print("⚠ No se pudo abrir el PDF automáticamente.")
    except Exception as e:
        print(f"❌ Error al abrir el PDF: {e}")

abrir_pdf(archivo_pdf)