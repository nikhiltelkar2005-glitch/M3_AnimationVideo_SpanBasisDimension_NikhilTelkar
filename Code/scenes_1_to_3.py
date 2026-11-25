"""
Scenes 1 to 3 of the M3 Linear Algebra Animation:
- Scene 1: Hook / Context (0s - 40s)
- Scene 2: Concept Introduction (40s - 85s)
- Scene 3: Visual Intuition (85s - 150s)
"""

import numpy as np
from matplotlib.patches import FancyBboxPatch, Polygon
from config import (
    BG_DARK, PANEL_BG, PANEL_BORDER, TEXT_PRIMARY, TEXT_MUTED,
    CYAN, GOLD, CORAL, EMERALD, PURPLE, TEAL,
    COURSE_TITLE, VIDEO_TITLE, VIDEO_SUBTITLE, STUDENT_NAME, STUDENT_ID,
    clamp, seg_progress, linear_progress,
    new_canvas, draw_header, draw_caption, draw_card, draw_2d_axes, draw_vector,
)


def render_scene_1(t, global_t, total_t):
    """Scene 1: Hook / Context (duration: 65s, synced to audio 0:00 - 1:05)."""
    fig, ax = new_canvas()

    if t < 7.0:
        # Opening Frame
        a_in = seg_progress(t, 0.0, 1.0)
        a_out = 1.0 - seg_progress(t, 5.8, 7.0)
        alpha = a_in * a_out

        # Decorative subtle grid behind title
        for gx in np.linspace(0.1, 0.9, 9):
            ax.plot([gx, gx], [0.15, 0.85], color=PANEL_BORDER, lw=0.6, alpha=0.25 * alpha)
        for gy in np.linspace(0.2, 0.8, 7):
            ax.plot([0.1, 0.9], [gy, gy], color=PANEL_BORDER, lw=0.6, alpha=0.25 * alpha)

        ax.text(0.5, 0.72, COURSE_TITLE, color=CYAN, fontsize=18, fontweight="bold",
                ha="center", va="center", alpha=alpha)
        ax.text(0.5, 0.57, VIDEO_TITLE, color=TEXT_PRIMARY, fontsize=46, fontweight="bold",
                ha="center", va="center", alpha=alpha)
        ax.text(0.5, 0.45, VIDEO_SUBTITLE, color=TEXT_MUTED, fontsize=16,
                ha="center", va="center", alpha=alpha)

        # Student info badge
        box = FancyBboxPatch((0.28, 0.22), 0.44, 0.11,
                             boxstyle="round,pad=0.01,rounding_size=0.015",
                             facecolor=PANEL_BG, edgecolor=CYAN, lw=1.6, alpha=0.9 * alpha)
        ax.add_patch(box)
        ax.text(0.5, 0.292, f"Concept: {VIDEO_TITLE}", color=TEXT_PRIMARY,
                fontsize=14.5, fontweight="bold", ha="center", va="center", alpha=alpha)
        ax.text(0.5, 0.248, f"{STUDENT_NAME}   |   ID: {STUDENT_ID}", color=GOLD,
                fontsize=14, ha="center", va="center", alpha=alpha)
        return fig

    # 8s - 40s: Motivating Puzzle
    draw_header(ax, "Scene 1 • Hook & Context", "Can Two Vectors Reach Every Point?", global_t / total_t)

    # Left: 2D Coordinate Plane
    ax_p = fig.add_axes([0.05, 0.15, 0.50, 0.70])
    draw_2d_axes(ax_p, xlim=(-1.5, 5.5), ylim=(-1.0, 4.5))
    ax_p.set_title("2D Navigation Grid", color=TEXT_PRIMARY, fontsize=15, pad=10)

    v1 = np.array([2.0, 1.0])
    v2 = np.array([1.0, 2.0])
    target = np.array([4.0, 3.0])

    # Target point appears (audio ~11s)
    p_target = seg_progress(t, 9.5, 13.0)
    if p_target > 0:
        ax_p.scatter([target[0]], [target[1]], s=180 * p_target, color=EMERALD, zorder=8)
        ax_p.text(target[0] + 0.18, target[1] + 0.15, r"Target $p = (4, 3)$",
                  color=EMERALD, fontsize=14, fontweight="bold", alpha=p_target)

    # Phase A (14s - 31s): Try with only v1
    p_v1 = seg_progress(t, 14.0, 17.0)
    if p_v1 > 0:
        s_vals = np.linspace(-0.5, 2.6, 50)
        p_line = seg_progress(t, 18.0, 22.0)
        ax_p.plot(s_vals * v1[0], s_vals * v1[1], color=CYAN, ls="--", lw=1.8, alpha=0.55 * p_line)
        scale = 1.0 + 1.0 * seg_progress(t, 19.0, 24.0) * (1.0 - seg_progress(t, 28.0, 31.0))
        draw_vector(ax_p, (0, 0), v1 * p_v1 * scale, CYAN,
                    label=r"$\mathbf{v}_1 = (2,1)$" if scale < 1.2 else r"$2\mathbf{v}_1 = (4,2)$",
                    label_offset=(0.1, -0.4))

    # Phase B (32s - 48s): Add v2 and reach target!
    p_v2 = seg_progress(t, 32.0, 35.0)
    if p_v2 > 0:
        c1 = 1.0 + (2.0 / 3.0) * seg_progress(t, 36.0, 41.0)
        c2 = 1.0 * seg_progress(t, 34.0, 37.0) - (1.0 / 3.0) * seg_progress(t, 37.0, 41.0)
        vec1_cur = c1 * v1
        vec2_cur = c2 * v2
        draw_vector(ax_p, (0, 0), vec1_cur, CYAN, label=rf"${c1:.2f}\mathbf{{v}}_1$", label_offset=(0.1, -0.42))
        draw_vector(ax_p, vec1_cur, vec2_cur * p_v2, GOLD, label=rf"${c2:.2f}\mathbf{{v}}_2$", label_offset=(0.15, 0.1))
        if t > 40.0:
            p_sum = seg_progress(t, 40.0, 43.0)
            draw_vector(ax_p, (0, 0), (vec1_cur + vec2_cur) * p_sum, EMERALD,
                        label=r"$p = c_1\mathbf{v}_1 + c_2\mathbf{v}_2$", label_offset=(-1.4, 0.25), lw=3.2)

    # Right panel: Guiding Questions
    draw_card(ax, 0.58, 0.15, 0.38, 0.70, title="The Big Questions", border_color=CYAN)

    q1_a = seg_progress(t, 14.0, 17.0)
    ax.text(0.60, 0.73, "1. With only v₁ = (2, 1):", color=CYAN, fontsize=15.5, fontweight="bold", alpha=q1_a)
    ax.text(0.61, 0.68, "We are trapped on a single 1D line.\nTarget (4, 3) is unreachable!", color=TEXT_PRIMARY, fontsize=14, alpha=q1_a)

    q2_a = seg_progress(t, 32.0, 35.0)
    ax.text(0.60, 0.57, "2. Adding a 2nd direction v₂ = (1, 2):", color=GOLD, fontsize=15.5, fontweight="bold", alpha=q2_a)
    ax.text(0.61, 0.51, "Now we can combine c₁v₁ + c₂v₂\nto reach any point in 2D space!", color=TEXT_PRIMARY, fontsize=14, alpha=q2_a)

    q3_a = seg_progress(t, 48.0, 51.0)
    ax.text(0.60, 0.39, "3. Three Core Questions:", color=EMERALD, fontsize=15.5, fontweight="bold", alpha=q3_a)
    ax.text(0.61, 0.28, "• Span: What space can vectors reach?\n• Basis: What is the smallest set needed?\n• Dimension: How many directions is that?",
            color=TEXT_PRIMARY, fontsize=14, linespacing=1.6, alpha=q3_a)

    if t < 32.0:
        draw_caption(ax, "Scaling a single vector v₁ only moves along one line — we cannot reach (4, 3).")
    elif t < 48.0:
        draw_caption(ax, "Adding a second non-parallel vector v₂ unlocks the entire 2D plane!")
    else:
        draw_caption(ax, "Span, Basis, and Dimension give us the exact language to measure generated spaces.")

    return fig


def render_scene_2(t, global_t, total_t):
    """Scene 2: Concept Introduction (duration: 45s).
    0-12s: Learning Objective.
    12-45s: Formal definitions & notation (Linear Combination, Span, Basis, Dimension).
    """
    fig, ax = new_canvas()
    draw_header(ax, "Scene 2 • Concept Introduction", "Definitions, Notation & Learning Goal", global_t / total_t)

    # Learning Objective Banner
    lo_a = seg_progress(t, 0.5, 2.5)
    draw_card(ax, 0.05, 0.74, 0.90, 0.12, title="Learning Objective", border_color=EMERALD, alpha=lo_a)
    ax.text(0.07, 0.775,
            "By the end of this video, you will be able to explain how vectors span a subspace,\n"
            "why a basis is a minimal spanning set, and what dimension counts.",
            color=TEXT_PRIMARY, fontsize=15, va="center", ha="left", alpha=lo_a)

    # Four definition cards in a 2x2 grid (synced to audio 1:05 - 2:11)
    cards = [
        (0.05, 0.44, CYAN, "1. Linear Combination & Span", 10.0,
         r"Given vectors $\mathbf{v}_1, \dots, \mathbf{v}_k \in \mathbb{R}^n$ and scalars $c_i \in \mathbb{R}$:" + "\n" +
         r"$\mathbf{w} = c_1\mathbf{v}_1 + c_2\mathbf{v}_2 + \cdots + c_k\mathbf{v}_k$" + "\n" +
         r"$\mathrm{Span}\{\mathbf{v}_1, \dots, \mathbf{v}_k\}$ = set of all linear combinations."),
        (0.51, 0.44, PURPLE, "2. Subspace", 26.0,
         "A subset $W \\subseteq \\mathbb{R}^n$ that:\n"
         "• Contains the zero vector $\\mathbf{0}$\n"
         "• Is closed under addition & scalar multiplication.\n"
         "Every Span forms a valid subspace!"),
        (0.05, 0.14, GOLD, "3. Basis (Minimal Spanning Set)", 36.0,
         r"A set $B = \{\mathbf{v}_1, \dots, \mathbf{v}_k\}$ is a basis of $W$ if:" + "\n"
         "1) $B$ spans $W$  ($\\mathrm{Span}(B) = W$)\n"
         "2) $B$ is linearly independent (no redundant vectors)."),
        (0.51, 0.14, EMERALD, "4. Dimension", 52.0,
         r"$\dim(W)$ = the number of vectors in any basis of $W$." + "\n"
         "• Every basis of $W$ has the exact same size.\n"
         "• Measures independent degrees of freedom."),
    ]

    for cx, cy, col, title, t_start, body in cards:
        a = seg_progress(t, t_start, t_start + 3.0)
        draw_card(ax, cx, cy, 0.44, 0.26, title=title, border_color=col, alpha=a)
        ax.text(cx + 0.02, cy + 0.115, body, color=TEXT_PRIMARY, fontsize=14,
                va="center", ha="left", linespacing=1.45, alpha=a)

    if t < 10.0:
        draw_caption(ax, "First, let's establish clear notation before visualizing the geometry.")
    elif t < 36.0:
        draw_caption(ax, "A Span is the set of all possible linear combinations — it always forms a subspace.")
    elif t < 52.0:
        draw_caption(ax, "A Basis spans the subspace with zero redundancy (linearly independent).")
    else:
        draw_caption(ax, "Dimension is simply the count of vectors in a basis.")

    return fig


def render_scene_3(t, global_t, total_t):
    """Scene 3: Visual Intuition (duration: 65s).
    0-22s: 1 vector in R^2 -> 1D line (dim = 1).
    22-45s: 2 non-collinear vectors in R^2 -> entire 2D plane (dim = 2).
    45-65s: Collinear trap (dim collapses to 1) + 2 vectors in R^3 (2D plane in 3D).
    """
    fig, ax = new_canvas()
    draw_header(ax, "Scene 3 • Visual Intuition", "From 1D Lines to 2D Planes & Redundancy", global_t / total_t)

    if t < 46.0:
        # 2D Plane on Left
        ax_p = fig.add_axes([0.05, 0.15, 0.50, 0.70])
        draw_2d_axes(ax_p, xlim=(-5.5, 5.5), ylim=(-4.2, 4.2))
        v1 = np.array([2.0, 1.0])
        v2 = np.array([-1.0, 1.5])

        if t < 22.0:
            ax_p.set_title(r"Case 1: Span of 1 Vector $\{\mathbf{v}_1\}$ in $\mathbb{R}^2$", color=TEXT_PRIMARY, fontsize=15, pad=10)
            # Animate c1 sweeping back and forth
            sweep = np.sin(linear_progress(t, 2.0, 20.0) * 2.5 * np.pi) * 2.4
            s_vals = np.linspace(-2.5, 2.5, 100)
            p_line = seg_progress(t, 1.5, 5.0)
            ax_p.plot(s_vals * v1[0], s_vals * v1[1], color=PURPLE, lw=3.0, alpha=0.65 * p_line, zorder=2)
            draw_vector(ax_p, (0, 0), v1 * sweep, GOLD, label=rf"${sweep:.1f}\mathbf{{v}}_1$", label_offset=(0.15, -0.35), lw=2.8, zorder=4)
            draw_vector(ax_p, (0, 0), v1, CYAN, label=r"$\mathbf{v}_1=(2,1)$", label_offset=(0.15, 0.2), lw=3.2, zorder=6)

            draw_card(ax, 0.58, 0.15, 0.38, 0.70, title="Case 1: 1 Vector", border_color=CYAN)
            ax.text(0.60, 0.72, r"$\mathbf{v}_1 = (2, 1)$", color=CYAN, fontsize=17, fontweight="bold")
            ax.text(0.60, 0.58,
                    "• Varying $c_1 \\in \\mathbb{R}$ only stretches,\n  shrinks, or flips $\\mathbf{v}_1$.\n\n"
                    "• $\\mathrm{Span}\\{\\mathbf{v}_1\\}$ = a 1D line\n  passing through the origin $(0,0)$.\n\n"
                    "• Basis: $\\{\\mathbf{v}_1\\}$\n"
                    "• Dimension: $\\dim = 1$",
                    color=TEXT_PRIMARY, fontsize=14.5, va="top", linespacing=1.45)
            draw_caption(ax, "One non-zero vector generates a 1-dimensional line through the origin.")

        else:
            # 22s - 46s: 2 non-collinear vectors filling R^2
            lt = t - 22.0
            ax_p.set_title(r"Case 2: Span of 2 Vectors $\{\mathbf{v}_1, \mathbf{v}_2\}$ in $\mathbb{R}^2$", color=TEXT_PRIMARY, fontsize=15, pad=10)
            p_grid = seg_progress(lt, 2.0, 12.0)
            # Draw skewed grid of c1*v1 + c2*v2
            for k in range(-4, 5):
                p1 = np.array([-4, k])
                p2 = np.array([4, k])
                a1 = p1[0] * v1 + p1[1] * v2
                a2 = p2[0] * v1 + p2[1] * v2
                ax_p.plot([a1[0], a2[0]], [a1[1], a2[1]], color=PURPLE, lw=1.0, alpha=0.45 * p_grid, zorder=1)
                q1 = np.array([k, -4])
                q2 = np.array([k, 4])
                b1 = q1[0] * v1 + q1[1] * v2
                b2 = q2[0] * v1 + q2[1] * v2
                ax_p.plot([b1[0], b2[0]], [b1[1], b2[1]], color=PURPLE, lw=1.0, alpha=0.45 * p_grid, zorder=1)

            # Shade filled region
            poly = Polygon([(-6, -5), (6, -5), (6, 5), (-6, 5)], facecolor=PURPLE, alpha=0.10 * p_grid, zorder=0)
            ax_p.add_patch(poly)

            # Animated linear combination sweeping around
            ang = linear_progress(lt, 4.0, 21.0) * 2 * np.pi
            c1 = 1.4 * np.cos(ang)
            c2 = 1.3 * np.sin(ang)
            draw_vector(ax_p, (0, 0), v1, CYAN, label=r"$\mathbf{v}_1$", label_offset=(0.1, -0.35), lw=3.0)
            draw_vector(ax_p, (0, 0), v2, GOLD, label=r"$\mathbf{v}_2$", label_offset=(-0.45, 0.1), lw=3.0)
            draw_vector(ax_p, (0, 0), c1 * v1 + c2 * v2, EMERALD,
                        label=rf"${c1:.1f}\mathbf{{v}}_1 + {c2:.1f}\mathbf{{v}}_2$",
                        label_offset=(0.15, 0.15), lw=3.2, zorder=7)

            draw_card(ax, 0.58, 0.15, 0.38, 0.70, title="Case 2: 2 Independent Vectors", border_color=EMERALD)
            ax.text(0.60, 0.72, r"$\mathbf{v}_1=(2,1),\ \ \mathbf{v}_2=(-1,1.5)$", color=GOLD, fontsize=16, fontweight="bold")
            ax.text(0.60, 0.58,
                    "• $\\mathbf{v}_2$ points off the line of $\\mathbf{v}_1$.\n\n"
                    "• Together, $c_1\\mathbf{v}_1 + c_2\\mathbf{v}_2$ tiles\n  the ENTIRE 2D plane $\\mathbb{R}^2$.\n\n"
                    "• Basis: $\\{\\mathbf{v}_1, \\mathbf{v}_2\\}$\n"
                    "• Dimension: $\\dim(\\mathbb{R}^2) = 2$",
                    color=TEXT_PRIMARY, fontsize=14.5, va="top", linespacing=1.45)
            draw_caption(ax, "Two non-collinear vectors in R² span the entire 2D plane (dimension 2).")

    else:
        # 46s - 79s: Left = Collinear Trap (R^2), Right = 2D Plane in R^3
        lt = t - 46.0
        ax_l = fig.add_axes([0.05, 0.16, 0.42, 0.66])
        draw_2d_axes(ax_l, xlim=(-5, 5), ylim=(-3.5, 3.5))
        ax_l.set_title("Trap: Collinear Vectors (Redundant!)", color=CORAL, fontsize=15, pad=10)
        v1 = np.array([2.0, 1.0])
        v_bad = np.array([4.0, 2.0])
        s_vals = np.linspace(-2.5, 2.5, 50)
        ax_l.plot(s_vals * v1[0], s_vals * v1[1], color=CORAL, lw=2.5, alpha=0.6)
        draw_vector(ax_l, (0, 0), v_bad, CORAL, label=r"$\mathbf{v}_2 = 2\mathbf{v}_1$", label_offset=(-0.8, 0.35), lw=2.8)
        draw_vector(ax_l, (0, 0), v1, CYAN, label=r"$\mathbf{v}_1$", label_offset=(0.15, -0.4), lw=3.2)
        ax_l.text(-4.5, 2.6, "No new direction!\nSpan collapses to 1D line\n$\\dim = 1$ (NOT 2)",
                  color=TEXT_PRIMARY, fontsize=13, bbox=dict(facecolor=PANEL_BG, edgecolor=CORAL, boxstyle="round,pad=0.4"))

        # Right: 3D subplot showing 2 vectors spanning a 2D plane inside R^3
        ax_r = fig.add_axes([0.52, 0.16, 0.44, 0.66], projection="3d", facecolor=BG_DARK)
        ax_r.set_title(r"In $\mathbb{R}^3$: 2 Vectors Span a 2D Plane", color=PURPLE, fontsize=15, pad=10)
        ax_r.set_xlim(-2, 2); ax_r.set_ylim(-2, 2); ax_r.set_zlim(-2, 2)
        ax_r.xaxis.pane.fill = False; ax_r.yaxis.pane.fill = False; ax_r.zaxis.pane.fill = False
        ax_r.tick_params(colors=TEXT_MUTED, labelsize=9)
        ax_r.view_init(elev=22, azim=30 + lt * 3.5)

        xx, yy = np.meshgrid(np.linspace(-1.6, 1.6, 8), np.linspace(-1.6, 1.6, 8))
        zz = 0.4 * xx + 0.3 * yy
        ax_r.plot_surface(xx, yy, zz, color=PURPLE, alpha=0.28, edgecolor=PURPLE, linewidth=0.4)
        ax_r.quiver(0, 0, 0, 1.4, 0, 0.56, color=CYAN, lw=2.5, arrow_length_ratio=0.15)
        ax_r.quiver(0, 0, 0, 0, 1.4, 0.42, color=GOLD, lw=2.5, arrow_length_ratio=0.15)
        ax_r.text(1.45, 0, 0.65, "v₁", color=CYAN, fontsize=13, fontweight="bold")
        ax_r.text(0, 1.45, 0.5, "v₂", color=GOLD, fontsize=13, fontweight="bold")

        draw_caption(ax, "Count independent directions, not raw vectors: collinear vectors add 0 new dimensions.")

    return fig
