"""
Generador del Documento Oficial Word (.docx) para el Taller 6.
Diseñado con formato institucional de alta calidad para UNIPUTUMAYO.
Stack: React 18, Vite, TypeScript, ConfigCat SDK, Render.
"""

import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import OxmlElement, parse_xml
from docx.oxml.ns import nsdecls, qn

def set_cell_background(cell, color_hex):
    shading_elm = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{color_hex}"/>')
    cell._tc.get_or_add_tcPr().append(shading_elm)

def set_cell_margins(cell, top=100, bottom=100, left=150, right=150):
    tcPr = cell._tc.get_or_add_tcPr()
    tcMar = OxmlElement('w:tcMar')
    for m, val in [('top', top), ('bottom', bottom), ('left', left), ('right', right)]:
        node = OxmlElement(f'w:{m}')
        node.set(qn('w:w'), str(val))
        node.set(qn('w:type'), 'dxa')
        tcMar.append(node)
    tcPr.append(tcMar)

def add_callout(doc, text, title="NOTA IMPORTANTE", border_color="0A2540", bg_color="F0F4F8"):
    tbl = doc.add_table(rows=1, cols=1)
    tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    cell = tbl.cell(0, 0)
    set_cell_background(cell, bg_color)
    set_cell_margins(cell, top=140, bottom=140, left=200, right=180)
    
    tcPr = cell._tc.get_or_add_tcPr()
    tcBorders = parse_xml(f'''
        <w:tcBorders {nsdecls("w")}>
            <w:top w:val="none"/>
            <w:left w:val="single" w:sz="24" w:space="0" w:color="{border_color}"/>
            <w:bottom w:val="none"/>
            <w:right w:val="none"/>
        </w:tcBorders>
    ''')
    tcPr.append(tcBorders)
    
    p = cell.paragraphs[0]
    p.paragraph_format.space_before = Pt(2)
    p.paragraph_format.space_after = Pt(2)
    run_t = p.add_run(f"📌 {title}: ")
    run_t.bold = True
    run_t.font.name = "Arial"
    run_t.font.size = Pt(10)
    run_t.font.color.rgb = RGBColor(10, 37, 64)
    
    run_b = p.add_run(text)
    run_b.font.name = "Arial"
    run_b.font.size = Pt(10)
    run_b.font.color.rgb = RGBColor(40, 50, 60)
    doc.add_paragraph()

def style_header(row, col_widths, bg_color="0A2540"):
    for i, cell in enumerate(row.cells):
        set_cell_background(cell, bg_color)
        set_cell_margins(cell, top=120, bottom=120, left=140, right=140)
        cell.width = Inches(col_widths[i])
        for p in cell.paragraphs:
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            for run in p.runs:
                run.bold = True
                run.font.name = "Arial"
                run.font.size = Pt(9.5)
                run.font.color.rgb = RGBColor(255, 255, 255)

def style_row(row, col_widths, is_even=False):
    bg_color = "F8FAFC" if is_even else "FFFFFF"
    for i, cell in enumerate(row.cells):
        set_cell_background(cell, bg_color)
        set_cell_margins(cell, top=80, bottom=80, left=120, right=120)
        cell.width = Inches(col_widths[i])
        for p in cell.paragraphs:
            for run in p.runs:
                run.font.name = "Arial"
                run.font.size = Pt(9)
                run.font.color.rgb = RGBColor(40, 40, 40)

def main():
    doc = docx.Document()
    
    for section in doc.sections:
        section.top_margin = Inches(1.0)
        section.bottom_margin = Inches(1.0)
        section.left_margin = Inches(1.0)
        section.right_margin = Inches(1.0)

    # ========================== PORTADA ==========================
    p_inst = doc.add_paragraph()
    p_inst.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_inst = p_inst.add_run("INSTITUCIÓN UNIVERSITARIA DEL PUTUMAYO – UNIPUTUMAYO\nFACULTAD DE INGENIERÍA\nTECNOLOGÍA EN DESARROLLO DE SOFTWARE")
    r_inst.bold = True
    r_inst.font.name = "Arial"
    r_inst.font.size = Pt(12)
    r_inst.font.color.rgb = RGBColor(10, 37, 64)
    p_inst.paragraph_format.space_after = Pt(35)

    p_title = doc.add_paragraph()
    p_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_title = p_title.add_run("INFORME TÉCNICO - TALLER 6:\nCONTINUOUS DEPLOYMENT, SPRINT REVIEW & RETROSPECTIVE")
    r_title.bold = True
    r_title.font.name = "Arial"
    r_title.font.size = Pt(16)
    r_title.font.color.rgb = RGBColor(0, 102, 204)
    p_title.paragraph_format.space_after = Pt(18)

    p_sub = doc.add_paragraph()
    p_sub.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_sub = p_sub.add_run(
        "Servicio de Feature Flags: ConfigCat\n"
        "Stack Tecnológico: React 18, Vite, TypeScript, ConfigCat SDK, Render\n"
        "Caso Técnico: 'Pagos Express en Liquidación de Trámites Catastrales'"
    )
    r_sub.font.name = "Arial"
    r_sub.font.size = Pt(10.5)
    r_sub.font.italic = True
    r_sub.font.color.rgb = RGBColor(70, 80, 90)
    p_sub.paragraph_format.space_after = Pt(70)

    p_meta = doc.add_paragraph()
    p_meta.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_meta = p_meta.add_run(
        "ESTUDIANTE:\nFranklin Sneider Córdoba De La Cruz\n\n"
        "DOCENTE:\nJuan Pablo\n\n"
        "ASIGNATURA / DIPLOMADO:\nIntegración Continua, Continuous Deployment & DevOps\n\n"
        "MOCOA, PUTUMAYO, COLOMBIA\nOCTUBRE DE 2026"
    )
    r_meta.bold = True
    r_meta.font.name = "Arial"
    r_meta.font.size = Pt(10.5)
    r_meta.font.color.rgb = RGBColor(30, 40, 50)
    
    doc.add_page_break()

    # ========================== SECCIÓN 1 ==========================
    doc.add_heading("1. INTRODUCCIÓN Y OBJETIVO", level=1)
    p1 = doc.add_paragraph(
        "El presente informe documenta la adaptación práctica de las ceremonias ágiles de Scrum (Sprint Review y Sprint Retrospective) "
        "al modelo de Continuous Deployment (CD) y Trunk-Based Development (TBD), resolviendo el caso técnico de 'Pagos Express' mediante "
        "el desacople entre despliegue y liberación con Feature Flags y una estrategia de liberación controlada."
    )
    p1.paragraph_format.space_after = Pt(12)

    # ========================== SECCIÓN 2 ==========================
    doc.add_heading("2. ADAPTACIÓN DEL SPRINT REVIEW A CONTINUOUS DEPLOYMENT", level=1)
    
    doc.add_heading("2.1 Principios Comparativos", level=2)
    doc.add_paragraph(
        "• Review Clásico: Demostración de un incremento acumulado al final de una iteración de dos semanas; enfoque de 'todo o nada' "
        "habitualmente presentado en local o staging; feedback tardío centrado en 'qué construimos'.\n\n"
        "• Review en CD + TBD: Demostración de valor incremental que ya reside en el entorno de producción real (Render). Las funcionalidades "
        "están desacopladas mediante Feature Toggles (ConfigCat), permitiendo validación empírica y feedback continuo centrado en 'qué valor e impacto recibieron los usuarios'."
    )

    doc.add_heading("2.2 Ficha Técnica de Demostración (Caso: Pagos Express)", level=2)
    doc.add_paragraph(
        "• Problema Resuelto: Elimina la fricción y abandono en la liquidación de trámites catastrales mediante un checkout rápido de 1 clic "
        "con firma digital autorizada, evitando formularios bancarios repetitivos.\n\n"
        "• Estado en Producción: Código integrado a la rama main y desplegado en Render, aislado detrás del flag pagos-express-v1 (en estado OFF).\n\n"
        "• Flujo de la Demo en Vivo:\n"
        "  1. Estado OFF: Se proyecta la aplicación en Render mostrando la pasarela estándar ('Completar formulario y Pagar') con el flag inactivo.\n"
        "  2. Conmutación: Se conmuta el toggle pagos-express-v1 a ON en la consola de ConfigCat y se publica el cambio.\n"
        "  3. Estado ON: Sin requerir nuevo commit, compilación ni redespliegue, la interfaz actualiza dinámicamente el componente a 'Pagar en 1 Clic con Pagos Express'.\n\n"
        "• Métricas de Éxito: Reducción del tiempo de liquidación (de 3 minutos a menos de 10 segundos), tasa de conversión en pasarela y tasa de error técnico inferior al 0.5%.\n\n"
        "• Pregunta de Validación al PO/Stakeholders: “¿La confirmación en un clic resuelve la necesidad del ciudadano antes de abrir el tráfico al 100%?”"
    )

    # ========================== SECCIÓN 3 ==========================
    doc.add_heading("3. ADAPTACIÓN DE LA SPRINT RETROSPECTIVE", level=1)
    
    doc.add_heading("3.1 Nuevos Focos de Inspección Obligatoria", level=2)
    doc.add_paragraph(
        "En Continuous Deployment, la Retrospectiva deja de ser una dinámica abstracta y analiza métricas técnicas de flujo:\n"
        "• Salud del Pipeline: Tasa de builds rotos, tiempos de auto-deploy, estabilidad de health checks y presencia de rollbacks.\n"
        "• Disciplina TBD: Integraciones diarias a main, tiempo de vida de ramas (< 24 horas) e higiene/retiro de feature flags.\n"
        "• Flujo de Valor: Lead Time for Changes y tiempo efectivo en que el usuario recibe valor."
    )

    doc.add_heading("3.2 Diagnóstico del Caso (Sprint Retrospective)", level=2)
    doc.add_paragraph(
        "• Salud del Pipeline: Se presentó un fallo de health check por 11 minutos durante el último deploy automático que requirió rollback manual; "
        "existencia de tests intermitentes (flaky tests) en el CI.\n"
        "• Disciplina TBD: Se redujo el ritmo a solo 4 integraciones en el sprint; una rama permaneció abierta 4 días para sortear el test flaky del CI.\n"
        "• Higiene de Toggles: Existen 3 feature toggles con más de 45 días de vida sin retirar del código base.\n"
        "• Flujo de Valor: Presión comercial por activar el toggle al 20% en viernes sin instrumentar métricas de error de pasarela ni conversión."
    )

    doc.add_heading("3.3 Matriz de Retrospectiva (Estructura Miro)", level=2)
    tbl_retro = doc.add_table(rows=1, cols=3)
    tbl_retro.alignment = WD_TABLE_ALIGNMENT.CENTER
    col_w_retro = [2.1, 2.2, 2.2]
    
    r_hdr = tbl_retro.rows[0].cells
    r_hdr[0].text = "🟢 Lo que funcionó bien"
    r_hdr[1].text = "🟡 Lo que generó fricción"
    r_hdr[2].text = "🔴 Lo que rompió el flujo / miedo"
    style_header(tbl_retro.rows[0], col_w_retro, bg_color="0A2540")

    r_row = tbl_retro.add_row()
    r_row.cells[0].text = "• Despliegue automático a Render cumpliendo DoD técnico.\n• Aislamiento efectivo de código sin riesgo al usuario final mediante pagos-express-v1 en ConfigCat."
    r_row.cells[1].text = "• Tests flaky en CI que demoraron integraciones.\n• Presión comercial del PO por activar en viernes sin observabilidad.\n• Solo 4 integraciones en el sprint."
    r_row.cells[2].text = "• Caída de 11 minutos por health check fallido.\n• Rollback manual no automatizado.\n• Acumulación de 3 toggles obsoletos (+45 días)."
    style_row(r_row, col_w_retro)

    doc.add_paragraph().paragraph_format.space_after = Pt(10)

    doc.add_heading("3.4 Tres Acciones de Mejora Obligatorias", level=2)
    doc.add_paragraph(
        "1. Acción 1 (Estabilidad de Pipeline): Cuarentenar de inmediato el test flaky del CI y configurar auto-rollback en Render ante fallos de health check. (Responsable: Developers).\n\n"
        "2. Acción 2 (Higiene de Toggles): Incorporar al Definition of Done (DoD) que todo toggle con más de 30 días en producción se priorice obligatoriamente como tarea de limpieza en el backlog. (Responsable: Equipo / PO).\n\n"
        "3. Acción 3 (DoR de Liberación): Definir como criterio en el Definition of Ready (DoR) que ninguna funcionalidad se active a usuarios externos sin dashboards activos de errores HTTP 5xx y latencia. (Responsable: PO + Devs)."
    )

    # ========================== SECCIÓN 4 ==========================
    doc.add_heading("4. POLÍTICA DE LIBERACIÓN SEGURA DE VALOR", level=1)
    
    doc.add_heading("4.1 Evaluación: ¿Activar al 20% el viernes?", level=2)
    doc.add_paragraph(
        "• Decisión: RECHAZAR LA ACTIVACIÓN.\n"
        "• Justificación Técnica: Incumple las ventanas seguras de despliegue (no liberar antes del fin de semana sin guardia técnica activa); "
        "existe un antecedente reciente de fallo en health check; y no existe telemetría para monitorear caídas o transacciones bancarias fallidas."
    )

    doc.add_heading("4.2 Estrategia de Liberación Progresiva (Canary Rollout)", level=2)
    doc.add_paragraph(
        "1. Fase 0 (Interno / Dogfooding - Lunes): Activación al 100% exclusivamente para correos y cuentas del equipo de desarrollo, QA y Product Owner en ConfigCat.\n"
        "2. Fase 1 (Canary 5% - Martes): Activación para el 5% de usuarios reales en horario laboral diurno, manteniendo monitoreo activo por 24 horas.\n"
        "3. Fase 2 (Escalado Gradual - Miércoles a Jueves): Si la tasa de transacciones fallidas permanece inferior al 0.5%, escalar progresivamente a 20%, 50% y finalmente 100%."
    )

    doc.add_heading("4.3 Protocolo de Monitoreo y Rollback Inmediato", level=2)
    doc.add_paragraph(
        "• Métricas bajo Observación: Tasa de errores HTTP 5xx, latencia p95 (umbral máximo 800 ms) y tasa de pagos fallidos en pasarela.\n"
        "• Criterio de Rollback: Si los errores superan el 1% o la latencia excede el umbral, se conmuta el toggle pagos-express-v1 a OFF inmediatamente desde ConfigCat, "
        "neutralizando el impacto en menos de 60 segundos sin necesidad de un nuevo deploy o commit."
    )

    # ========================== SECCIÓN 5 ==========================
    doc.add_heading("5. CONCLUSIONES Y CIERRE", level=1)
    doc.add_paragraph(
        "1. El Continuous Deployment exige desacoplar el despliegue técnico (automatizado por el pipeline hacia Render) de la liberación de valor (controlada por el Product Owner mediante ConfigCat).\n"
        "2. El Sprint Review deja de ser una entrega de fin de ciclo para convertirse en una sesión de validación de valor e hipótesis sobre el entorno de producción real.\n"
        "3. La Sprint Retrospective se transforma en un espacio de auditoría del pipeline, asegurando ramas cortas, pruebas estables y eliminación de deuda técnica en toggles."
    )

    add_callout(
        doc,
        "“Desplegar a producción ya no es un evento de cierre de sprint, sino una rutina continua e invisible; el Review valida el impacto del valor real y la Retrospectiva protege la salud del pipeline y la disciplina diaria de integración.”",
        title="FRASE X OFICIAL",
        border_color="00D4B2",
        bg_color="F0FFF4"
    )

    output_path = r"c:\Users\Usuario\OneDrive\Escritorio\taller 6\INFORME_TALLER_6_CONTINUOUS_DEPLOYMENT.docx"
    doc.save(output_path)
    print("Documento oficial Word actualizado con éxito en:", output_path)

if __name__ == "__main__":
    main()
