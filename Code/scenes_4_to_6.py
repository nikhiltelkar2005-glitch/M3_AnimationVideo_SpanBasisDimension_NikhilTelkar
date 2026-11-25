"""
Scenes 4 to 6 of the M3 Linear Algebra Animation:
- Scene 4: Worked Example (150s - 225s, duration 75s)
- Scene 5: Interpretation (225s - 265s, duration 40s)
- Scene 6: Summary & Credits (265s - 300s, duration 35s)
"""

import numpy as np
from matplotlib.patches import FancyBboxPatch
from config import (
    BG_DARK, PANEL_BG, PANEL_BORDER, TEXT_PRIMARY, TEXT_MUTED,
    CYAN, GOLD, CORAL, EMERALD, PURPLE, TEAL,
    VIDEO_TITLE, STUDENT_NAME, STUDENT_ID,
    seg_progress, linear_progress,
    new_canvas, draw_header, draw_caption, draw_card,
)


def draw_matrix(ax, cx, cy, rows, col_colors=None, pivot_cells=None,
                title=None, cell_w=0.048, cell_h=0.052, alpha=1.0, fontsize=16):
    """Draw a clean mathematical matrix with brackets and optional pivot highlights."""
    if alpha <= 0.01:
        return
    n_rows = len(rows)
    n_cols = len(rows[0])
    total_w = n_cols * cell_w
    total_h = n_rows * cell_h
    x0 = cx - total_w / 2
    y0 = cy - total_h / 2

    if title:
        ax.text(cx, cy + total_h / 2 + 0.03, title, color=TEXT_PRIMARY,
                fontsize=14, fontweight="bold", ha="center", va="center", alpha=alpha)

    # Brackets
    pad = 0.008
    tick = 0.014
    bx_l = x0 - pad
    bx_r = x0 + total_w + pad
    by_b = y0 - pad
    by_t = y0 + total_h + pad
    for xs, d in [(bx_l, 1), (bx_r, -1)]:
        ax.plot([xs, xs], [by_b, by_t], color=TEXT_PRIMARY, lw=2.0, alpha=alpha)
        ax.plot([xs, xs + d * tick], [by_t, by_t], color=TEXT_PRIMARY, lw=2.0, alpha=alpha)
        ax.plot([xs, xs + d * tick], [by_b, by_b], color=TEXT_PRIMARY, lw=2.0, alpha=alpha)

    pivot_cells = pivot_cells or set()
    for r in range(n_rows):
        for c in range(n_cols):
            px = x0 + (c + 0.5) * cell_w
            py = y0 + (n_rows - 1 - r + 0.5) * cell_h
            color = col_colors[c] if (col_colors and c < len(col_colors)) else TEXT_PRIMARY
            if (r, c) in pivot_cells:
                circ = FancyBboxPatch(
                    (px - cell_w * 0.36, py - cell_h * 0.36),
                    cell_w * 0.72, cell_h * 0.72,
                    boxstyle="round,pad=0.002,rounding_size=0.008",
                    facecolor="none", edgecolor=EMERALD, lw=2.0, alpha=alpha
                )
                ax.add_patch(circ)
            ax.text(px, py, str(rows[r][c]), color=color, fontsize=fontsize,
                    fontweight="bold" if (r, c) in pivot_cells else "normal",
                    ha="center", va="center", alpha=alpha)


def render_scene_4(t, global_t, total_t):
    """Scene 4: Worked Example (duration: 75s).
    0-15s: Problem setup with 3 vectors in R^3.
    15-50s: Step-by-step Gaussian elimination to RREF, identifying pivots.
    50-75s: Explicit verification v3 = 2v1 + v2 -> Basis = {v1, v2}, dim(W) = 2.
    """
    fig, ax = new_canvas()
    draw_header(ax, "Scene 4 • Worked Example", r"Finding a Basis & Dimension in $\mathbb{R}^3$", global_t / total_t)

    # Top Problem Card (always visible)
    draw_card(ax, 0.05, 0.71, 0.90, 0.15, title="Problem Setup", border_color=CYAN)
    ax.text(0.07, 0.785,
            r"Let  $W = \mathrm{Span}\{\mathbf{v}_1, \mathbf{v}_2, \mathbf{v}_3\} \subseteq \mathbb{R}^3$,  where:",
            color=TEXT_PRIMARY, fontsize=15.5, va="center", ha="left")
    draw_matrix(ax, 0.52, 0.78, [[1], [0], [1]], col_colors=[CYAN], cell_w=0.036, cell_h=0.034, fontsize=13.5)
    ax.text(0.47, 0.78, r"$\mathbf{v}_1 =$", color=CYAN, fontsize=15, fontweight="bold", ha="right", va="center")
    draw_matrix(ax, 0.67, 0.78, [[0], [1], [1]], col_colors=[GOLD], cell_w=0.036, cell_h=0.034, fontsize=13.5)
    ax.text(0.62, 0.78, r"$\mathbf{v}_2 =$", color=GOLD, fontsize=15, fontweight="bold", ha="right", va="center")
    draw_matrix(ax, 0.82, 0.78, [[2], [1], [3]], col_colors=[CORAL], cell_w=0.036, cell_h=0.034, fontsize=13.5)
    ax.text(0.77, 0.78, r"$\mathbf{v}_3 =$", color=CORAL, fontsize=15, fontweight="bold", ha="right", va="center")
    ax.text(0.07, 0.73, r"Goal:  Find a basis for $W$ and determine $\dim(W)$.", color=EMERALD, fontsize=14.5, fontweight="bold")

    # Step 1: Matrix A (audio ~24s)
    a1 = seg_progress(t, 23.0, 26.0)
    draw_card(ax, 0.05, 0.38, 0.27, 0.30, title="Step 1: Form Matrix A", border_color=PANEL_BORDER, alpha=a1)
    draw_matrix(ax, 0.185, 0.51, [[1, 0, 2], [0, 1, 1], [1, 1, 3]],
                col_colors=[CYAN, GOLD, CORAL], alpha=a1)
    ax.text(0.185, 0.405, r"Columns = $[\mathbf{v}_1\ \ \mathbf{v}_2\ \ \mathbf{v}_3]$",
            color=TEXT_MUTED, fontsize=13, ha="center", alpha=a1)

    # Step 2: R3 <- R3 - R1 (audio ~31s)
    a2 = seg_progress(t, 30.0, 34.0)
    draw_card(ax, 0.365, 0.38, 0.27, 0.30, title="Step 2: R₃ ← R₃ − R₁", border_color=PURPLE, alpha=a2)
    draw_matrix(ax, 0.50, 0.51, [[1, 0, 2], [0, 1, 1], [0, 1, 1]],
                col_colors=[CYAN, GOLD, CORAL], pivot_cells={(0, 0), (1, 1)}, alpha=a2)
    ax.text(0.50, 0.405, "Eliminate entry (3, 1)", color=TEXT_MUTED, fontsize=13, ha="center", alpha=a2)

    # Step 3: R3 <- R3 - R2 (audio ~44s)
    a3 = seg_progress(t, 43.0, 47.0)
    draw_card(ax, 0.68, 0.38, 0.27, 0.30, title="Step 3: R₃ ← R₃ − R₂", border_color=EMERALD, alpha=a3)
    draw_matrix(ax, 0.815, 0.51, [[1, 0, 2], [0, 1, 1], [0, 0, 0]],
                col_colors=[CYAN, GOLD, CORAL], pivot_cells={(0, 0), (1, 1)}, alpha=a3)
    ax.text(0.815, 0.405, "2 Pivots (Col 1 & 2) | Col 3 Free", color=EMERALD, fontsize=13, fontweight="bold", ha="center", alpha=a3)

    # Bottom Conclusion Cards (audio ~59s and ~84s)
    a4 = seg_progress(t, 58.0, 62.0)
    draw_card(ax, 0.05, 0.13, 0.43, 0.22, title="Step 4: Check Redundancy", border_color=CORAL, alpha=a4)
    ax.text(0.07, 0.26,
            r"Row-reduced form shows $2\mathbf{v}_1 + 1\mathbf{v}_2 = \mathbf{v}_3$:",
            color=TEXT_PRIMARY, fontsize=14, alpha=a4)
    ax.text(0.07, 0.185,
            r"$2(1,0,1)^T + 1(0,1,1)^T = (2,1,3)^T = \mathbf{v}_3$" + "\n" +
            r"$\mathbf{v}_3$ is linearly dependent on $\{\mathbf{v}_1, \mathbf{v}_2\}$!",
            color=CORAL, fontsize=14, fontweight="bold", linespacing=1.45, alpha=a4)

    a5 = seg_progress(t, 83.0, 87.0)
    draw_card(ax, 0.52, 0.13, 0.43, 0.22, title="Step 5: Basis & Dimension", border_color=EMERALD, alpha=a5)
    ax.text(0.54, 0.23,
            r"• Removing $\mathbf{v}_3$ keeps the exact same Span." + "\n" +
            r"• Basis of $W$:  $B = \{\mathbf{v}_1, \mathbf{v}_2\}$  (pivot columns)" + "\n" +
            r"• Dimension:  $\dim(W) = 2$",
            color=TEXT_PRIMARY, fontsize=14.5, va="center", linespacing=1.55, alpha=a5)

    if t < 24.0:
        draw_caption(ax, "Place the 3 vectors as columns of matrix A and row-reduce to find independent directions.")
    elif t < 59.0:
        draw_caption(ax, "Gaussian elimination reveals 2 pivot columns and 1 zero row — column 3 is dependent.")
    else:
        draw_caption(ax, "Since v₃ = 2v₁ + v₂, {v₁, v₂} is a minimal spanning set (a basis), so dim(W) = 2.")

    return fig


def render_scene_5(t, global_t, total_t):
    """Scene 5: Interpretation (duration: 40s).
    0-24s: 3D Geometric view of the worked example (plane z = x + y in R^3).
    24-40s: Non-uniqueness of basis ({v1, v2} vs {v1, v3}) -> same plane, same dimension = 2.
    """
    fig, ax = new_canvas()
    draw_header(ax, "Scene 5 • Geometric Interpretation", "Connecting the Algebra Back to 3D Space", global_t / total_t)

    # Left: Rotating 3D Plot of W: z = x + y
    ax_3d = fig.add_axes([0.04, 0.13, 0.50, 0.67], projection="3d", facecolor=BG_DARK)
    ax_3d.set_xlim(-1.0, 2.5); ax_3d.set_ylim(-1.0, 2.5); ax_3d.set_zlim(-1.0, 3.5)
    ax_3d.xaxis.pane.fill = False; ax_3d.yaxis.pane.fill = False; ax_3d.zaxis.pane.fill = False
    ax_3d.tick_params(colors=TEXT_MUTED, labelsize=9)
    ax_3d.set_xlabel("x", color=TEXT_MUTED); ax_3d.set_ylabel("y", color=TEXT_MUTED); ax_3d.set_zlabel("z", color=TEXT_MUTED)
    ax_3d.view_init(elev=22, azim=25 + t * 2.2)
    ax_3d.set_title(r"Subspace $W$: The Plane $z = x + y$ in $\mathbb{R}^3$", color=PURPLE, fontsize=15, pad=8)

    xx, yy = np.meshgrid(np.linspace(-0.5, 2.2, 8), np.linspace(-0.5, 2.2, 8))
    zz = xx + yy
    ax_3d.plot_surface(xx, yy, zz, color=PURPLE, alpha=0.26, edgecolor=PURPLE, linewidth=0.5)

    # Vectors v1=(1,0,1), v2=(0,1,1), v3=(2,1,3)
    ax_3d.quiver(0, 0, 0, 1, 0, 1, color=CYAN, lw=3.0, arrow_length_ratio=0.14)
    ax_3d.text(1.05, 0, 1.1, "v₁=(1,0,1)", color=CYAN, fontsize=11, fontweight="bold")

    ax_3d.quiver(0, 0, 0, 0, 1, 1, color=GOLD, lw=3.0, arrow_length_ratio=0.14)
    ax_3d.text(0, 1.05, 1.1, "v₂=(0,1,1)", color=GOLD, fontsize=11, fontweight="bold")

    p_v3 = seg_progress(t, 16.0, 23.0)
    if p_v3 > 0:
        ax_3d.quiver(0, 0, 0, 2 * p_v3, 1 * p_v3, 3 * p_v3, color=CORAL, lw=2.8, ls="--", arrow_length_ratio=0.10)
        if p_v3 > 0.8:
            ax_3d.text(2.0, 1.0, 3.15, "v₃=(2,1,3) ∈ Plane", color=CORAL, fontsize=11, fontweight="bold")

    # Right: Interpretation Cards
    a1 = seg_progress(t, 1.0, 4.0)
    draw_card(ax, 0.57, 0.52, 0.39, 0.33, title="1. What the Numbers Mean", border_color=PURPLE, alpha=a1)
    ax.text(0.59, 0.66,
            "• Every vector in $W$ satisfies $z = x + y$.\n"
            "  ($1=1+0$,  $1=0+1$,  $3=2+1$)\n\n"
            "• $\\mathbf{v}_3$ already lies flat inside the\n  plane spanned by $\\mathbf{v}_1$ and $\\mathbf{v}_2$.",
            color=TEXT_PRIMARY, fontsize=14, va="center", linespacing=1.45, alpha=a1)

    a2 = seg_progress(t, 32.0, 36.0)
    draw_card(ax, 0.57, 0.15, 0.39, 0.33, title="2. Bases Are Not Unique — Dim Is!", border_color=EMERALD, alpha=a2)
    ax.text(0.59, 0.29,
            "• $\\{\\mathbf{v}_1, \\mathbf{v}_2\\}$ is a basis of $W$.\n"
            "• $\\{\\mathbf{v}_1, \\mathbf{v}_3\\}$ is ALSO a valid basis of $W$!\n\n"
            "• Different bases, SAME plane, SAME size:\n"
            "  $\\dim(W) = 2$ (2 degrees of freedom).",
            color=TEXT_PRIMARY, fontsize=14, va="center", linespacing=1.45, alpha=a2)

    if t < 32.0:
        draw_caption(ax, "Geometrically, v₃ lies directly on the 2D plane z = x + y generated by v₁ and v₂.")
    else:
        draw_caption(ax, "A subspace can have many different bases, but every basis has the exact same size: dim(W) = 2.")

    return fig


def render_scene_6(t, global_t, total_t):
    """Scene 6: Summary & Credits (duration: 27s, synced to audio 6:00 - 6:25+)."""
    fig, ax = new_canvas()

    if t < 20.5:
        draw_header(ax, "Scene 6 • Summary", "Three Core Takeaways", global_t / total_t)
        takeaways = [
            (0.62, CYAN, "1. Span = Reachable Space", 1.0,
             r"$\mathrm{Span}\{\mathbf{v}_1, \dots, \mathbf{v}_k\}$ is the set of all linear combinations $c_1\mathbf{v}_1 + \cdots + c_k\mathbf{v}_k$ — always a subspace through $\mathbf{0}$."),
            (0.39, GOLD, "2. Basis = Minimal Spanning Set", 7.0,
             "A basis spans the subspace with zero redundancy (linearly independent). Row reduction pivots identify a basis."),
            (0.16, EMERALD, "3. Dimension = Independent Directions", 13.5,
             r"$\dim(W)$ is the number of vectors in any basis of $W$ — counting true degrees of freedom, not raw vector count."),
        ]
        for y, col, title, ts, desc in takeaways:
            a = seg_progress(t, ts, ts + 2.5)
            draw_card(ax, 0.08, y, 0.84, 0.19, title=title, border_color=col, alpha=a)
            ax.text(0.10, y + 0.08, desc, color=TEXT_PRIMARY, fontsize=15, va="center", ha="left", alpha=a)

        draw_caption(ax, "Span builds the space, a Basis keeps it minimal, and Dimension counts its degrees of freedom.")
        return fig

    # 20.5s - 27s: Closing Frame & Credits
    a = seg_progress(t, 20.5, 22.0)
    draw_header(ax, "Scene 6 • Credits & Disclosure", "Summary, References & AI Disclosure", 1.0)

    draw_card(ax, 0.08, 0.46, 0.84, 0.36, title="Quick Recap", border_color=EMERALD, alpha=a)
    ax.text(0.10, 0.62,
            "• Span: All linear combinations of a vector set.\n"
            "• Basis: Linearly independent spanning set (found via pivot columns).\n"
            "• Dimension: Number of basis vectors (invariant across all bases).",
            color=TEXT_PRIMARY, fontsize=16, va="center", linespacing=1.65, alpha=a)

    draw_card(ax, 0.08, 0.12, 0.40, 0.29, title="References", border_color=CYAN, alpha=a)
    ax.text(0.10, 0.24,
            "1. Gilbert Strang, Introduction to Linear Algebra\n"
            "2. 3Blue1Brown, Essence of Linear Algebra\n"
            "3. M3 Linear Algebra & Calculus Course Notes",
            color=TEXT_PRIMARY, fontsize=13.5, va="center", linespacing=1.55, alpha=a)

    draw_card(ax, 0.52, 0.12, 0.40, 0.29, title="Production & AI Disclosure", border_color=PURPLE, alpha=a)
    ax.text(0.54, 0.24,
            f"Created by: {STUDENT_NAME} ({STUDENT_ID})\n"
            "Tools: Python, Matplotlib, NumPy, FFmpeg\n"
            "Audio: Student voice-over narration\n"
            "AI Disclosure: AI used for storyboard & Python code.",
            color=TEXT_PRIMARY, fontsize=13.5, va="center", linespacing=1.5, alpha=a)

    return fig
