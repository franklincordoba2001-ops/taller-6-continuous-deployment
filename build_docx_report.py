"""
Generador del Documento Oficial Word (.docx) para el Taller 6.
Diseñado con formato institucional de alta calidad para UNIPUTUMAYO.
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
    
    # Left border only
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

def style_row(row, col_widths, is_even=False, align_left=True):
    bg_color = "F8FAFC" if is_even else "FFFFFF"
    for i, cell in enumerate(row.cells):
        set_cell_background(cell, bg_color)
        set_cell_margins(cell, top=80, bottom=80, left=120, right=120)
        cell.width = Inches(col_widths[i])
        for p in cell.paragraphs:
            if not align_left or i == 0:
                p.alignment = WD_ALIGN_PARAGRAPH.LEFT
            for run in p.runs:
                run.font.name = "Arial"
                run.font.size = Pt(9)
                run.font.color.rgb = RGBColor(40, 40, 40)

def main():
    doc = docx.Document()
    
    # Page setup (margins)
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
    p_inst.paragraph_format.space_after = Pt(40)

    p_title = doc.add_paragraph()
    p_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_title = p_title.add_run("TALLER 6:\nSPRINT REVIEW, RETROSPECTIVE Y LIBERACIÓN SEGURA EN CONTINUOUS DEPLOYMENT")
    r_title.bold = True
    r_title.font.name = "Arial"
    r_title.font.size = Pt(17)
    r_title.font.color.rgb = RGBColor(0, 102, 204)
    p_title.paragraph_format.space_after = Pt(20)

    p_sub = doc.add_paragraph()
    p_sub.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_sub = p_sub.add_run("Resolución de Caso Real: 'La funcionalidad de Pagos Express ya está en main, pero nadie se atreve a activarla'\nAdopción de Trunk-Based Development, ConfigCat Feature Flags y Auto-Deploy en Render")
    r_sub.font.name = "Arial"
    r_sub.font.size = Pt(11)
    r_sub.font.italic = True
    r_sub.font.color.rgb = RGBColor(70, 80, 90)
    p_sub.paragraph_format.space_after = Pt(80)

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

    # ========================== INTRODUCCIÓN Y APERTURA ==========================
    h1 = doc.add_heading("1. Apertura y Conexión con el Nuevo Flujo", level=1)
    h1.paragraph_format.space_before = Pt(15)
    h1.paragraph_format.space_after = Pt(8)

    p_intro = doc.add_paragraph(
        "Con la consolidación de nuestro pipeline de Continuous Deployment (CD), cada integración exitosa en la rama principal (main) "
        "se compila, prueba y despliega automáticamente a producción en Render. Asimismo, disponemos de ConfigCat para proteger funcionalidades "
        "incompletas o en fase de prueba mediante Feature Flags. En este contexto, surge la necesidad ineludible de transformar radicalmente "
        "las ceremonias tradicionales de Scrum para adaptarlas a este nuevo ritmo continuo."
    )
    p_intro.paragraph_format.space_after = Pt(10)

    add_callout(
        doc,
        "¿Cómo cambian el Sprint Review y la Retrospectiva cuando desplegamos varias veces por semana? "
        "El Review deja de ser una entrega de código estático para convertirse en una demostración científica de valor en producción, "
        "mientras que la Retrospectiva pasa de ser una conversación subjetiva a una rigurosa auditoría de la salud del pipeline y de la disciplina TBD.",
        title="CAMBIO DE PARADIGMA CENTRAL",
        border_color="0066CC"
    )

    doc.add_heading("Pregunta de Arranque del Taller", level=2)
    doc.add_paragraph(
        "“¿Qué parte del Review o de la Retro actual se siente más ‘antigua’ o poco útil con este nuevo flujo?”\n\n"
        "1. En el Sprint Review: Se siente obsoleto esperar 14 días para mostrar un incremento empaquetado en una máquina local. "
        "Si el software ya se despliega continuamente, el feedback diferido 'todo o nada' carece de sentido y destruye la agilidad.\n"
        "2. En la Sprint Retrospective: Se siente anticuado enfocarse exclusivamente en percepciones interpersonales o estimaciones de puntos de historia, "
        "ignorando los datos reales de ingeniería: tiempo de vida de las ramas, fallos en el pipeline de CI/CD, duraciones de despliegue y deuda técnica de toggles."
    )

    # ========================== CASO DE ESTUDIO ==========================
    doc.add_heading("2. Diagnóstico y Resolución del Caso de Estudio", level=1)
    doc.add_paragraph(
        "Título del Caso: “La funcionalidad de ‘Pagos Express’ ya está en main, pero nadie se atreve a activarla”\n"
        "Contexto: El equipo completó la historia 'Pagos Express con un solo clic', integrada a main hace 9 días bajo el flag 'pagos-express-v1' (OFF al 100%). "
        "A continuación, se presenta la matriz de análisis y decisiones tomadas frente a los 7 hechos problemáticos identificados:"
    )

    # Tabla de Hechos Problemáticos
    tbl_facts = doc.add_table(rows=1, cols=4)
    tbl_facts.alignment = WD_TABLE_ALIGNMENT.CENTER
    col_w_facts = [0.5, 2.2, 1.8, 2.0]
    
    hdr_cells = tbl_facts.rows[0].cells
    hdr_cells[0].text = "#"
    hdr_cells[1].text = "Hecho Problemático"
    hdr_cells[2].text = "Impacto / Riesgo"
    hdr_cells[3].text = "Decisión y Solución Técnica"
    style_header(tbl_facts.rows[0], col_w_facts)

    facts_data = [
        ("1", "PO quiere activar el toggle al 20% este viernes por presión de marketing.", "Riesgo alto de caída sin validación previa.", "Rollout Canario en 4 etapas: Interno -> 5% -> 20% comercial."),
        ("2", "Último deploy automático falló health check 11 minutos; rollback manual.", "Falta de resiliencia y downtime en Render.", "Reingeniería de /health con Liveness/Readiness no bloqueantes (<10ms)."),
        ("3", "3 Feature Toggles llevan > 45 días activos y nadie los ha limpiado.", "Deuda técnica y código muerto acumulado.", "Política v3.0: caducidad a 30 días y ejecución de cleanup."),
        ("4", "Solo 4 integraciones a main en el sprint (lejos de la meta diaria).", "Pérdida de cadencia TBD y acumulación de ramas.", "Vertical slicing fino (<200 líneas) y protección con toggles."),
        ("5", "Rama viva 4 días por test flaky que ponía el CI en rojo.", "Miedo del equipo a integrar y retraso en entrega.", "Protocolo de cuarentena inmediata y test determinista con mocks."),
        ("6", "No existe métrica de conversión o error para observar el toggle.", "Ceguera operativa al encender la funcionalidad.", "Módulo de telemetría (/api/v1/metrics) con Golden Signals."),
        ("7", "Stakeholder anunció que 'Pagos Express ya está listo'.", "Confusión entre deploy técnico y release comercial.", "Alineación en Playbook: Despliegue ≠ Lanzamiento comercial.")
    ]

    for idx, (f_num, f_desc, f_risk, f_sol) in enumerate(facts_data):
        row = tbl_facts.add_row()
        row.cells[0].text = f_num
        row.cells[1].text = f_desc
        row.cells[2].text = f_risk
        row.cells[3].text = f_sol
        style_row(row, col_w_facts, is_even=(idx % 2 == 1))

    doc.add_paragraph().paragraph_format.space_after = Pt(10)

    # ========================== SECCIÓN 1: SPRINT REVIEW ==========================
    doc.add_heading("3. Adaptación del Sprint Review al Continuous Deployment", level=1)
    
    doc.add_heading("3.1 Principios del Nuevo Review", level=2)
    tbl_comp = doc.add_table(rows=1, cols=3)
    tbl_comp.alignment = WD_TABLE_ALIGNMENT.CENTER
    col_w_comp = [2.0, 2.2, 2.3]
    
    c_hdr = tbl_comp.rows[0].cells
    c_hdr[0].text = "Dimensión"
    c_hdr[1].text = "Review Clásico (Scrum Antiguo)"
    c_hdr[2].text = "Review en CD + TBD (Flujo Moderno)"
    style_header(tbl_comp.rows[0], col_w_comp)

    comp_data = [
        ("Entorno de Demostración", "Local o Staging aislado y desactualizado.", "Producción real en Render con datos vivos."),
        ("Naturaleza de Entrega", "Todo o nada (incremento monolítico).", "Valor incremental gobernado por Feature Flags."),
        ("Frecuencia de Feedback", "Diferido cada 2-3 semanas.", "Continuo, inmediato y basado en telemetría."),
        ("Foco de la Reunión", "¿Qué construimos? (Puntos quemados).", "¿Qué valor recibieron los usuarios y qué dicen los datos?")
    ]

    for idx, (dim, cla, mod) in enumerate(comp_data):
        row = tbl_comp.add_row()
        row.cells[0].text = dim
        row.cells[1].text = cla
        row.cells[2].text = mod
        style_row(row, col_w_comp, is_even=(idx % 2 == 1))

    doc.add_paragraph().paragraph_format.space_after = Pt(10)

    doc.add_heading("3.2 Simulación de Sprint Review: 3 Incrementos Reales", level=2)
    
    doc.add_heading("Incremento 1: Módulo de Pagos Express con un Clic (Toggle)", level=3)
    doc.add_paragraph(
        "• Problema resuelto: Reduce la fricción de compra eliminando 3 pantallas de llenado de formularios.\n"
        "• Estado de activación: Protegido por el toggle 'pagos-express-v1' (ConfigCat).\n"
        "• Demo en vivo en Render: Se demuestra la alternancia entre el flujo estándar de 3 pasos (Toggle OFF) "
        "y el flujo Express tokenizado con 1 solo clic (Toggle ON).\n"
        "• Métrica de valor: Latencia reducida de 450 ms a 42 ms. Tasa de éxito del 100%.\n"
        "• Pregunta al PO: “¿Considera que este flujo cumple los criterios para habilitarse al 20% comercial?” -> Aprobado bajo monitoreo."
    )

    doc.add_heading("Incremento 2: Healthcheck Proactivo con Liveness & Readiness Probes", level=3)
    doc.add_paragraph(
        "• Problema resuelto: Soluciona el incidente de 11 minutos de inactividad durante el despliegue automático.\n"
        "• Estado de activación: Activo al 100% en producción.\n"
        "• Demo en vivo: Endpoint /health responde 200 OK en 4 ms sin dependencias bloqueantes.\n"
        "• Métrica de valor: Cero fallos de orquestación en los últimos 15 despliegues a Render."
    )

    doc.add_heading("Incremento 3: Telemetría y Observabilidad de Pagos en Tiempo Real", level=3)
    doc.add_paragraph(
        "• Problema resuelto: Elimina la ceguera operativa antes de encender funcionalidades comerciales.\n"
        "• Estado de activación: Activo al 100% en producción.\n"
        "• Demo en vivo: Endpoint /api/v1/metrics expone tasas de error, conversiones y tiempos de respuesta.\n"
        "• Métrica de valor: Permite activar el Kill-Switch automático si el error rate supera el 1.5%."
    )

    # ========================== SECCIÓN 2: SPRINT RETROSPECTIVE ==========================
    doc.add_heading("4. Adaptación de la Sprint Retrospective", level=1)
    
    doc.add_heading("4.1 Nuevos Focos Obligatorios de la Retro", level=2)
    doc.add_paragraph(
        "1. Salud del Pipeline: 3 roturas de CI por tests inestables; tiempo medio de build: 1m 45s; 1 rollback manual crítico por healthcheck colgado.\n"
        "2. Disciplina TBD: Solo 4 integraciones en el sprint (meta: diaria); 1 rama vivió 4 días por miedo al CI rojo; 3 toggles técnicos acumulaban > 45 días sin retirar.\n"
        "3. Flujo de Valor: Lead Time for Changes se infló a 9 días; el valor no había llegado al usuario final por temor a la activación sin métricas."
    )

    doc.add_heading("4.2 Tablero de Retrospectiva (Miro)", level=2)
    tbl_retro = doc.add_table(rows=1, cols=3)
    tbl_retro.alignment = WD_TABLE_ALIGNMENT.CENTER
    col_w_retro = [2.1, 2.2, 2.2]
    
    r_hdr = tbl_retro.rows[0].cells
    r_hdr[0].text = "🟢 Lo que Funcionó Bien"
    r_hdr[1].text = "🟡 Lo que Generó Fricción"
    r_hdr[2].text = "🔴 Lo que Rompió el Flujo / Causó Miedo"
    style_header(tbl_retro.rows[0], col_w_retro, bg_color="1A365D")

    r_row = tbl_retro.add_row()
    r_row.cells[0].text = "• Auto-deploy a Render rápido y fluido.\n• Uso de ConfigCat para aislar el código en main.\n• Linter Ruff ejecutándose en < 3s."
    r_row.cells[1].text = "• Presión comercial del PO sin métricas previas.\n• 3 toggles obsoletos que confundían el código.\n• Tiempos muertos esperando revisiones de PR."
    r_row.cells[2].text = "• Test flaky bloqueó una rama por 4 días.\n• Healthcheck colgado provocó 11 min de caída.\n• Anuncio comercial prematuro sin release real."
    style_row(r_row, col_w_retro)

    doc.add_paragraph().paragraph_format.space_after = Pt(10)

    doc.add_heading("4.3 Acciones de Mejora Oficiales (Máximo 3 Acciones Concretas)", level=2)
    tbl_act = doc.add_table(rows=1, cols=4)
    tbl_act.alignment = WD_TABLE_ALIGNMENT.CENTER
    col_w_act = [1.8, 1.4, 1.1, 2.2]
    
    a_hdr = tbl_act.rows[0].cells
    a_hdr[0].text = "Acción de Mejora"
    a_hdr[1].text = "Responsable"
    a_hdr[2].text = "Plazo"
    a_hdr[3].text = "Definition of Done (DoD)"
    style_header(tbl_act.rows[0], col_w_act)

    act_data = [
        ("1. Cuarentena y Erradicación de Tests Flaky", "Franklin Córdoba (Tech Lead)", "Inmediato", "Tests inestables aislados en < 2h. Suite CI 100% determinista en < 15s."),
        ("2. Healthcheck Desacoplado y Resiliente", "DevOps Engineer", "24 Horas", "Endpoint /health responde en < 10ms sin dependencias bloqueantes."),
        ("3. Política de Limpieza de Toggles Obsoletos", "PO + Dev Team", "Fin de Sprint", "Eliminar los 3 toggles > 45 días. Caducidad máxima de 30 días en Playbook.")
    ]

    for idx, (ac, resp, plz, dod) in enumerate(act_data):
        row = tbl_act.add_row()
        row.cells[0].text = ac
        row.cells[1].text = resp
        row.cells[2].text = plz
        row.cells[3].text = dod
        style_row(row, col_w_act, is_even=(idx % 2 == 1))

    doc.add_paragraph().paragraph_format.space_after = Pt(10)

    # ========================== SECCIÓN 3: LIBERACIÓN SEGURA ==========================
    doc.add_heading("5. Liberación Segura de Valor (Canary Rollout)", level=1)
    
    doc.add_paragraph(
        "Se diseñó una estrategia de liberación progresiva para 'pagos-express-v1' que permite conciliar "
        "la urgencia comercial de la campaña con la estabilidad absoluta del sistema en producción:"
    )

    tbl_canary = doc.add_table(rows=1, cols=4)
    tbl_canary.alignment = WD_TABLE_ALIGNMENT.CENTER
    col_w_canary = [1.2, 1.8, 1.8, 1.7]
    
    cn_hdr = tbl_canary.rows[0].cells
    cn_hdr[0].text = "Fase"
    cn_hdr[1].text = "Audiencia Objetivo"
    cn_hdr[2].text = "Propósito"
    cn_hdr[3].text = "Criterio de Avance"
    style_header(tbl_canary.rows[0], col_w_canary)

    canary_data = [
        ("Fase 0: Alpha", "Usuarios internos (@empresa.com)", "Validar integración en Render sin riesgo a clientes.", "100% compras internas exitosas."),
        ("Fase 1: Beta", "5% usuarios aleatorios reales", "Monitoreo intensivo de 2 horas en vivo.", "Error rate < 0.5%, latencia < 600ms."),
        ("Fase 2: Comercial", "20% usuarios (Campaña Marketing)", "Satisfacer la campaña del PO bajo control.", "Conversión > 92% tras 6 horas."),
        ("Fase 3: Expansión", "50% de la base de usuarios", "Validar comportamiento a escala media.", "Estabilidad tras 24 horas."),
        ("Fase 4: 100% GA", "Todos los usuarios", "Disponibilidad general y agenda de cleanup.", "Cierre formal del release.")
    ]

    for idx, (fs, aud, prp, crt) in enumerate(canary_data):
        row = tbl_canary.add_row()
        row.cells[0].text = fs
        row.cells[1].text = aud
        row.cells[2].text = prp
        row.cells[3].text = crt
        style_row(row, col_w_canary, is_even=(idx % 2 == 1))

    doc.add_paragraph().paragraph_format.space_after = Pt(10)

    add_callout(
        doc,
        "Si durante el rollout el Error Rate supera el 1.5% o la latencia supera 1.5 segundos, "
        "cualquier miembro del equipo o el PO apaga el toggle 'pagos-express-v1' a 0% en ConfigCat inmediatamente. "
        "Tiempo de mitigación: < 30 segundos, sin necesidad de redeploy ni de rollback de contenedor.",
        title="PROTOCOLO DE KILL-SWITCH INMEDIATO",
        border_color="CC0000",
        bg_color="FFF5F5"
    )

    # ========================== SECCIÓN 4: PLAYBOOK Y CIERRE ==========================
    doc.add_heading("6. Actualización del Playbook y Cierre de Fase 1", level=1)
    doc.add_paragraph(
        "Se procedió a la actualización oficial del documento 'SCRUM_TBD_PLAYBOOK_v3.md', integrando formalmente:\n"
        "• El protocolo y estructura del nuevo Sprint Review en Continuous Deployment.\n"
        "• El protocolo y los 3 ejes obligatorios de la nueva Sprint Retrospective.\n"
        "• La política de gobernanza y ciclo de vida de Feature Toggles (expiración a los 30 días).\n"
        "• El protocolo de cuarentena de tests flaky.\n"
        "• El cierre al 100% de la Fase 1 del diplomado."
    )

    add_callout(
        doc,
        "“A partir de este taller, el Sprint Review deja de ser una entrega de código para convertirse en una validación científica "
        "de valor en producción, y la Retrospectiva pasa de discutir impresiones a optimizar matemáticamente la salud del pipeline y el flujo continuo.”",
        title="RONDA FINAL - FRASE DE TRANSFORMACIÓN",
        border_color="00AA66",
        bg_color="F0FFF4"
    )

    # ========================== EVIDENCIAS TÉCNICAS ==========================
    doc.add_heading("7. Evidencias de Validación Técnica Automatizada", level=1)
    doc.add_paragraph(
        "A continuación, se certifica la ejecución exitosa de la suite completa de pruebas unitarias y de integración "
        "en el entorno local y en el pipeline de GitHub Actions:"
    )

    p_code = doc.add_paragraph()
    r_code = p_code.add_run(
        "============================= test session starts =============================\n"
        "collected 13 items\n\n"
        "tests/test_health.py::test_root_endpoint PASSED                          [  7%]\n"
        "tests/test_health.py::test_health_check_proactive PASSED                 [ 15%]\n"
        "tests/test_health.py::test_metrics_endpoint PASSED                       [ 23%]\n"
        "tests/test_health.py::test_toggles_admin_audit PASSED                    [ 30%]\n"
        "tests/test_health.py::test_cleanup_stale_toggles PASSED                  [ 38%]\n"
        "tests/test_payments.py::test_standard_checkout_when_toggle_is_off PASSED [ 46%]\n"
        "tests/test_payments.py::test_express_checkout_when_toggle_is_on PASSED   [ 53%]\n"
        "tests/test_payments.py::test_checkout_invalid_amount PASSED              [ 61%]\n"
        "tests/test_payments.py::test_flaky_test_elimination_deterministic PASSED [ 69%]\n"
        "tests/test_toggles.py::test_default_toggle_state_is_off PASSED           [ 76%]\n"
        "tests/test_toggles.py::test_toggle_override_to_on PASSED                 [ 84%]\n"
        "tests/test_toggles.py::test_internal_user_canary_whitelisting PASSED     [ 92%]\n"
        "tests/test_toggles.py::test_user_specific_override PASSED                [100%]\n\n"
        "======================== 13 passed in 0.51s ========================\n"
        "Ruff Linter: All checks passed! (0 errors, 0 warnings)"
    )
    r_code.font.name = "Consolas"
    r_code.font.size = Pt(8.5)
    r_code.font.color.rgb = RGBColor(20, 30, 40)

    output_path = r"c:\Users\Usuario\OneDrive\Escritorio\taller 6\INFORME_TALLER_6_CONTINUOUS_DEPLOYMENT.docx"
    doc.save(output_path)
    print("Documento guardado exitosamente en:", output_path)

if __name__ == "__main__":
    main()
