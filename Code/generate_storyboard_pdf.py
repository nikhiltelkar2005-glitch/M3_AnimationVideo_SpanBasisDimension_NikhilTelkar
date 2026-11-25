"""
Generate the 6-Scene Storyboard PDF required for the M3 Internal Assessment.
"""

from reportlab.lib import colors
from reportlab.lib.pagesizes import A4, landscape
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle


def build_storyboard(output_pdf="Storyboard_Span_Basis_Dimension.pdf"):
    doc = SimpleDocTemplate(
        output_pdf,
        pagesize=landscape(A4),
        leftMargin=0.55 * inch,
        rightMargin=0.55 * inch,
        topMargin=0.5 * inch,
        bottomMargin=0.5 * inch,
    )

    styles = getSampleStyleSheet()
    title_style = ParagraphStyle(
        "TitleCustom", parent=styles["Heading1"],
        fontSize=18, textColor=colors.HexColor("#0D47A1"), spaceAfter=4
    )
    sub_style = ParagraphStyle(
        "SubCustom", parent=styles["Normal"],
        fontSize=10.5, textColor=colors.HexColor("#333333"), spaceAfter=10
    )
    cell_style = ParagraphStyle(
        "CellCustom", parent=styles["Normal"],
        fontSize=9.2, leading=12.5, textColor=colors.HexColor("#111111")
    )
    head_style = ParagraphStyle(
        "HeadCustom", parent=styles["Normal"],
        fontSize=9.5, leading=12, textColor=colors.white, fontName="Helvetica-Bold"
    )

    story = [
        Paragraph("M3 Internal Assessment • 6-Scene Storyboard", title_style),
        Paragraph(
            "<b>Topic:</b> Span, Basis, and Dimension (Linear Algebra) &nbsp;|&nbsp; "
            "<b>Duration:</b> 6:27 (387s, 1080p MP4 with narration) &nbsp;|&nbsp; "
            "<b>Learning Objective:</b> By the end of this video, the viewer will be able to explain how vectors span a subspace, "
            "why a basis is a minimal spanning set, and what dimension counts.",
            sub_style
        ),
        Spacer(1, 6),
    ]

    rows = [
        [
            Paragraph("Scene & Timing", head_style),
            Paragraph("Purpose", head_style),
            Paragraph("Visual & Animation Plan", head_style),
            Paragraph("On-Screen Math & Caption Plan", head_style),
        ],
        [
            Paragraph("<b>1. Hook / Context</b><br/>0:00 – 1:05 (65s)", cell_style),
            Paragraph("Spark curiosity and motivate why spanning & directions matter.", cell_style),
            Paragraph("0:00–0:07: Opening title card (Title, Course, Student Name/ID).<br/>0:07–1:05: 2D grid showing target p = (4,3); v₁ = (2,1) stuck on a 1D line; adding v₂ = (1,2) reaches p.", cell_style),
            Paragraph("Compare 1 vector (trapped on 1D line) vs 2 vectors c₁v₁ + c₂v₂. Introduce the 3 core questions: Span, Basis, Dimension.", cell_style),
        ],
        [
            Paragraph("<b>2. Concept Introduction</b><br/>1:05 – 2:11 (66s)", cell_style),
            Paragraph("State the learning goal, formal definitions, and notation.", cell_style),
            Paragraph("Learning Objective banner at top, followed by 4 color-coded definition cards appearing sequentially.", cell_style),
            Paragraph("Define linear combination c₁v₁ + ... + cₖvₖ, Span{v₁,...,vₖ}, Subspace (contains 0, closed under + and scaling), Basis (spans + linearly independent), and dim(W).", cell_style),
        ],
        [
            Paragraph("<b>3. Visual Intuition</b><br/>2:11 – 3:30 (79s)", cell_style),
            Paragraph("Build geometric intuition in 2D and 3D before matrix algebra.", cell_style),
            Paragraph("Case 1: 1 vector sweeps a 1D line. Case 2: 2 non-collinear vectors tile R² with a skewed grid. Case 3: Collinear trap (v₂ = 2v₁ collapses to 1D) + rotating 3D plane in R³.", cell_style),
            Paragraph("Show dim = 1 for a line, dim = 2 for a plane, and explain why collinear vectors add 0 new dimensions.", cell_style),
        ],
        [
            Paragraph("<b>4. Worked Example</b><br/>3:30 – 5:07 (97s)", cell_style),
            Paragraph("Demonstrate step-by-step how to find a basis and dimension algebraically.", cell_style),
            Paragraph("Setup 3 vectors in R³: v₁=(1,0,1), v₂=(0,1,1), v₃=(2,1,3). Animate column matrix A and row operations R₃←R₃−R₁, R₃←R₃−R₂ with green pivot boxes.", cell_style),
            Paragraph("2 pivots (Col 1 & 2), 1 zero row. Verify 2v₁ + v₂ = v₃ explicitly. Conclude Basis B = {v₁, v₂} and dim(W) = 2.", cell_style),
        ],
        [
            Paragraph("<b>5. Interpretation</b><br/>5:07 – 6:00 (53s)", cell_style),
            Paragraph("Connect the RREF algebra back to 3D geometry.", cell_style),
            Paragraph("Rotating 3D plot of the plane z = x + y in R³ containing v₁, v₂, and v₃=(2,1,3) lying flat inside the same plane.", cell_style),
            Paragraph("Explain z = x + y for all 3 vectors. Highlight that {v₁, v₂} and {v₁, v₃} are both valid bases — bases aren't unique, but dim(W) = 2 always is.", cell_style),
        ],
        [
            Paragraph("<b>6. Summary & Credits</b><br/>6:00 – 6:27 (27s)", cell_style),
            Paragraph("Reinforce takeaways and display credits/AI disclosure.", cell_style),
            Paragraph("3 takeaway cards (Span, Basis, Dimension), followed by Closing Frame with Quick Recap, References, and Production/AI Disclosure.", cell_style),
            Paragraph("Cite Gilbert Strang, 3Blue1Brown, M3 Notes; disclose Python/Matplotlib/FFmpeg & AI assistance for scripting/code.", cell_style),
        ],
    ]

    table = Table(rows, colWidths=[1.45 * inch, 1.75 * inch, 3.35 * inch, 3.35 * inch], repeatRows=1)
    table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#1F4E79")),
        ("GRID", (0, 0), (-1, -1), 0.6, colors.HexColor("#B0BEC5")),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("TOPPADDING", (0, 0), (-1, -1), 6),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
        ("LEFTPADDING", (0, 0), (-1, -1), 6),
        ("RIGHTPADDING", (0, 0), (-1, -1), 6),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, colors.HexColor("#F5F8FA")]),
    ]))
    story.append(table)
    doc.build(story)
    print(f"Generated {output_pdf}")


if __name__ == "__main__":
    build_storyboard()
