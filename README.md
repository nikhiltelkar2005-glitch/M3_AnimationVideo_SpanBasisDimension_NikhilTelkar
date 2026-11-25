# M3 Internal Assessment — Animation Video: Span, Basis, and Dimension

- **Course:** Linear Algebra & Calculus (M3)
- **Topic:** Span, Basis, and Dimension — *How vectors generate a subspace, how a basis forms a minimal spanning set, and what dimension counts.*
- **Format:** 1080p (1920×1080), 16:9, 30 fps, MP4 (with voice-over narration, 6:27 / 387s)
- **Student Name / ID:** Edit `STUDENT_NAME` and `STUDENT_ID` in `Code/config.py` if you want to re-render with your details.

## Repository Structure

```text
.
├── Video.mp4                               # Final 5-minute 1080p 16:9 MP4 video
├── Storyboard_Span_Basis_Dimension.pdf     # 6-scene storyboard PDF
├── Code/
│   ├── config.py                           # Palette, timing, student metadata, drawing helpers
│   ├── scenes_1_to_3.py                    # Scenes 1–3 (Hook, Concept Intro, Visual Intuition)
│   ├── scenes_4_to_6.py                    # Scenes 4–6 (Worked Example, Interpretation, Summary)
│   ├── render_video.py                     # Main renderer (pipes 9,000 frames to FFmpeg)
│   └── generate_storyboard_pdf.py          # Generates the 6-scene Storyboard PDF
└── README.md
```

## 6-Scene Breakdown (6:27 Total)

1. **0:00 – 1:05 | Hook / Context:** Opening title frame + 2D navigation puzzle comparing 1 vector (1D line) vs. 2 vectors reaching $(4, 3)$.
2. **1:05 – 2:11 | Concept Introduction:** Learning objective, linear combinations, Span, Subspace, Basis, and Dimension.
3. **2:11 – 3:30 | Visual Intuition:** 1D line span, 2D plane span in $\mathbb{R}^2$, collinear redundancy trap, and a 2D plane inside $\mathbb{R}^3$.
4. **3:30 – 5:07 | Worked Example:** Step-by-step Gaussian elimination on $\mathbf{v}_1=(1,0,1)^T, \mathbf{v}_2=(0,1,1)^T, \mathbf{v}_3=(2,1,3)^T$, identifying 2 pivot columns, verifying $\mathbf{v}_3 = 2\mathbf{v}_1 + \mathbf{v}_2$, and finding basis $\{\mathbf{v}_1, \mathbf{v}_2\}$ with $\dim(W) = 2$.
5. **5:07 – 6:00 | Interpretation:** Rotating 3D visualization of the plane $z = x + y$ containing all three vectors, and non-uniqueness of bases.
6. **6:00 – 6:27 | Summary & Credits:** Three core takeaways, references, and AI disclosure.

## Reproducing the Video & Storyboard

```bash
# Preview keyframes (PNG)
.venv/bin/python Code/render_video.py --preview

# Render full 5-minute 1080p MP4
.venv/bin/python Code/render_video.py --output Video.mp4

# Regenerate Storyboard PDF
.venv/bin/python Code/generate_storyboard_pdf.py
```

## Credits & AI Disclosure

- **Mathematical References:** Gilbert Strang (*Introduction to Linear Algebra*), 3Blue1Brown (*Essence of Linear Algebra*), M3 Course Notes.
- **Software:** Python 3.13, Matplotlib, NumPy, ReportLab, FFmpeg.
- **AI Disclosure:** AI assistance was used to draft the 6-scene storyboard structure and write the Python/Matplotlib animation scripts.
