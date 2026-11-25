"""
Shared configuration, color palette, easing functions, and drawing helpers
for the M3 Linear Algebra animation: "Span, Basis, and Dimension".
"""

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

# Video specifications (16:9, 1080p, 30 fps, 300 seconds = 5:00)
WIDTH = 1920
HEIGHT = 1080
DPI = 100
FIG_W = WIDTH / DPI   # 19.2 inches
FIG_H = HEIGHT / DPI  # 10.8 inches
FPS = 30
TOTAL_SECONDS = 387  # 6m 27s (matches 385.24s audio + 1.76s closing hold)

# Editable student metadata for Opening & Closing frames
STUDENT_NAME = "Student Name"
STUDENT_ID = "Student ID"
COURSE_TITLE = "Linear Algebra & Calculus (M3) • Internal Assessment"
VIDEO_TITLE = "Span, Basis, and Dimension"
VIDEO_SUBTITLE = "How vectors generate a subspace, how a basis forms a minimal spanning set, and what dimension counts"

# 3Blue1Brown-inspired dark mathematical palette
BG_DARK = "#0D1117"
PANEL_BG = "#161B22"
PANEL_BORDER = "#30363D"
GRID_COLOR = "#21262D"
AXIS_COLOR = "#8B949E"
TEXT_PRIMARY = "#F0F6FC"
TEXT_MUTED = "#8B949E"

CYAN = "#58A6FF"       # v1, primary vector
GOLD = "#F2CC60"       # v2, secondary vector
CORAL = "#FF7B72"      # v3 / redundant / warning
EMERALD = "#3FB950"    # target / basis / success
PURPLE = "#BC8CFF"     # subspace / span highlight
TEAL = "#39C5CF"       # accents

# Scene time boundaries in seconds (synced to user audio, total = 387s = 6:27)
SCENE_DURATIONS = {
    "scene1_hook": 65,       # 0:00 - 1:05
    "scene2_intro": 66,      # 1:05 - 2:11
    "scene3_intuition": 79,  # 2:11 - 3:30
    "scene4_example": 97,    # 3:30 - 5:07
    "scene5_interpret": 53,  # 5:07 - 6:00
    "scene6_summary": 27,    # 6:00 - 6:27
}


def clamp(x, lo=0.0, hi=1.0):
    return max(lo, min(hi, float(x)))


def ease_in_out(t):
    t = clamp(t)
    return 3 * t * t - 2 * t * t * t


def ease_out(t):
    t = clamp(t)
    return 1 - (1 - t) ** 3


def seg_progress(t, start, end):
    """Normalized [0, 1] progress within [start, end] with smooth easing."""
    if end <= start:
        return 1.0 if t >= start else 0.0
    return ease_in_out((t - start) / (end - start))


def linear_progress(t, start, end):
    if end <= start:
        return 1.0 if t >= start else 0.0
    return clamp((t - start) / (end - start))


def new_canvas():
    """Create a clean 1920x1080 figure with a full-bleed normalized [0, 1] axis."""
    fig = plt.figure(figsize=(FIG_W, FIG_H), dpi=DPI, facecolor=BG_DARK)
    ax = fig.add_axes([0.0, 0.0, 1.0, 1.0], facecolor=BG_DARK)
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")
    return fig, ax


def draw_header(ax, scene_label, title, progress_frac):
    """Consistent top bar with scene badge, title, and subtle progress bar."""
    # Progress bar along very top
    ax.add_patch(FancyBboxPatch(
        (0.0, 0.992), 1.0, 0.008,
        boxstyle="square,pad=0", facecolor=PANEL_BG, edgecolor="none"
    ))
    ax.add_patch(FancyBboxPatch(
        (0.0, 0.992), clamp(progress_frac), 0.008,
        boxstyle="square,pad=0", facecolor=CYAN, edgecolor="none"
    ))
    # Scene badge
    ax.text(
        0.04, 0.945, scene_label.upper(),
        color=CYAN, fontsize=13, fontweight="bold", family="DejaVu Sans",
        va="center", ha="left"
    )
    ax.text(
        0.04, 0.905, title,
        color=TEXT_PRIMARY, fontsize=25, fontweight="bold", family="DejaVu Sans",
        va="center", ha="left"
    )


def draw_caption(ax, text, alpha=1.0, y=0.055):
    """Bottom subtitle/caption bar for silent video clarity."""
    if alpha <= 0.01 or not text:
        return
    box = FancyBboxPatch(
        (0.08, y - 0.032), 0.84, 0.064,
        boxstyle="round,pad=0.008,rounding_size=0.012",
        facecolor=PANEL_BG, edgecolor=PANEL_BORDER, linewidth=1.5,
        alpha=0.92 * alpha
    )
    ax.add_patch(box)
    ax.text(
        0.50, y, text,
        color=TEXT_PRIMARY, fontsize=16.5, family="DejaVu Sans",
        va="center", ha="center", alpha=alpha
    )


def draw_card(ax, x, y, w, h, title=None, border_color=PANEL_BORDER, alpha=1.0):
    """Draw a rounded dark card."""
    if alpha <= 0.01:
        return
    card = FancyBboxPatch(
        (x, y), w, h,
        boxstyle="round,pad=0.008,rounding_size=0.015",
        facecolor=PANEL_BG, edgecolor=border_color, linewidth=1.8,
        alpha=0.95 * alpha
    )
    ax.add_patch(card)
    if title:
        ax.text(
            x + 0.02, y + h - 0.032, title,
            color=border_color if border_color != PANEL_BORDER else CYAN,
            fontsize=16, fontweight="bold", family="DejaVu Sans",
            va="center", ha="left", alpha=alpha
        )


def draw_2d_axes(ax_plot, xlim=(-5, 5), ylim=(-4, 4)):
    """Style a 2D mathematical coordinate plane."""
    ax_plot.set_facecolor(BG_DARK)
    ax_plot.set_xlim(*xlim)
    ax_plot.set_ylim(*ylim)
    ax_plot.set_aspect("equal")
    for spine in ax_plot.spines.values():
        spine.set_color(PANEL_BORDER)
        spine.set_linewidth(1.2)
    ax_plot.grid(True, color=GRID_COLOR, linewidth=0.9, zorder=0)
    ax_plot.axhline(0, color=AXIS_COLOR, linewidth=1.4, zorder=1)
    ax_plot.axvline(0, color=AXIS_COLOR, linewidth=1.4, zorder=1)
    ax_plot.tick_params(colors=TEXT_MUTED, labelsize=11)


def draw_vector(ax_plot, start, vec, color, label=None, label_offset=(0.2, 0.2),
                lw=3.0, alpha=1.0, zorder=5, ls="-"):
    """Draw a crisp mathematical vector arrow on a 2D plot."""
    if alpha <= 0.01:
        return
    end = (start[0] + vec[0], start[1] + vec[1])
    if np.hypot(vec[0], vec[1]) < 1e-4:
        return
    arrow = FancyArrowPatch(
        start, end,
        arrowstyle="-|>,head_length=9,head_width=5.5",
        color=color, linewidth=lw, linestyle=ls, alpha=alpha, zorder=zorder
    )
    ax_plot.add_patch(arrow)
    if label:
        mx = start[0] + vec[0] * 0.55 + label_offset[0]
        my = start[1] + vec[1] * 0.55 + label_offset[1]
        ax_plot.text(
            mx, my, label, color=color, fontsize=15, fontweight="bold",
            alpha=alpha, zorder=zorder + 1
        )
