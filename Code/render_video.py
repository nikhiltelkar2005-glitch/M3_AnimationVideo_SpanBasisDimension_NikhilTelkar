"""
Main renderer for the 5-minute (300s) 1080p 16:9 silent MP4 video:
"Span, Basis, and Dimension"

Usage:
  python Code/render_video.py --preview   # Render 1 sample frame per scene to Code/preview/
  python Code/render_video.py             # Render full 5:00 Video.mp4 (1920x1080, 30fps)
"""

import os
import sys
import time
import argparse
import subprocess
import multiprocessing as mp

os.environ.setdefault("MPLCONFIGDIR", "/tmp/mplconfig_m3")
os.makedirs(os.environ["MPLCONFIGDIR"], exist_ok=True)

import matplotlib.pyplot as plt

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from config import WIDTH, HEIGHT, FPS, TOTAL_SECONDS, SCENE_DURATIONS
from scenes_1_to_3 import render_scene_1, render_scene_2, render_scene_3
from scenes_4_to_6 import render_scene_4, render_scene_5, render_scene_6

SCENE_SCHEDULE = [
    ("scene1", SCENE_DURATIONS["scene1_hook"], render_scene_1),
    ("scene2", SCENE_DURATIONS["scene2_intro"], render_scene_2),
    ("scene3", SCENE_DURATIONS["scene3_intuition"], render_scene_3),
    ("scene4", SCENE_DURATIONS["scene4_example"], render_scene_4),
    ("scene5", SCENE_DURATIONS["scene5_interpret"], render_scene_5),
    ("scene6", SCENE_DURATIONS["scene6_summary"], render_scene_6),
]


def render_frame_at_time(global_t):
    """Dispatch global timestamp global_t to the appropriate scene renderer."""
    acc = 0.0
    for name, dur, fn in SCENE_SCHEDULE:
        if global_t < acc + dur or name == "scene6":
            local_t = max(0.0, min(dur, global_t - acc))
            return fn(local_t, global_t, TOTAL_SECONDS)
        acc += dur
    return render_scene_6(SCENE_DURATIONS["scene6_summary"], TOTAL_SECONDS, TOTAL_SECONDS)


def frame_to_rgb_bytes(frame_idx):
    """Worker function: render frame_idx and return raw RGB bytes."""
    global_t = frame_idx / float(FPS)
    fig = render_frame_at_time(global_t)
    fig.canvas.draw()
    buf = fig.canvas.buffer_rgba()
    # Convert RGBA -> RGB bytes to cut pipe bandwidth by 25%
    rgb_bytes = bytes(buf)
    plt.close(fig)
    return rgb_bytes


def run_preview(out_dir):
    os.makedirs(out_dir, exist_ok=True)
    sample_times = [
        ("01_opening.png", 3.0),
        ("01_hook_puzzle.png", 25.0),
        ("02_concepts.png", 76.0),
        ("03_intuition_2d.png", 118.0),
        ("03_intuition_trap_3d.png", 140.0),
        ("04_worked_example.png", 215.0),
        ("05_interpretation_3d.png", 250.0),
        ("06_summary.png", 280.0),
        ("06_closing_credits.png", 295.0),
    ]
    for fname, gt in sample_times:
        fig = render_frame_at_time(gt)
        out_path = os.path.join(out_dir, fname)
        fig.savefig(out_path, dpi=100, facecolor=fig.get_facecolor())
        plt.close(fig)
        print(f"Saved preview: {out_path}")


def run_full_render(output_mp4):
    total_frames = TOTAL_SECONDS * FPS
    workers = max(2, min(8, os.cpu_count() or 4))
    print(f"Rendering {total_frames} frames ({TOTAL_SECONDS}s @ {FPS}fps, {WIDTH}x{HEIGHT}) using {workers} workers...")

    cmd = [
        "ffmpeg", "-y",
        "-f", "rawvideo",
        "-vcodec", "rawvideo",
        "-pix_fmt", "rgba",
        "-s", f"{WIDTH}x{HEIGHT}",
        "-r", str(FPS),
        "-i", "-",
        "-an",
        "-c:v", "libx264",
        "-pix_fmt", "yuv420p",
        "-preset", "medium",
        "-crf", "20",
        "-movflags", "+faststart",
        output_mp4,
    ]

    proc = subprocess.Popen(cmd, stdin=subprocess.PIPE)
    t0 = time.time()

    with mp.Pool(processes=workers) as pool:
        for idx, frame_bytes in enumerate(pool.imap(frame_to_rgb_bytes, range(total_frames), chunksize=16)):
            proc.stdin.write(frame_bytes)
            if (idx + 1) % 300 == 0 or (idx + 1) == total_frames:
                elapsed = time.time() - t0
                pct = 100.0 * (idx + 1) / total_frames
                print(f"  [{pct:5.1f}%] Frame {idx + 1}/{total_frames} ({elapsed:.1f}s elapsed)", flush=True)

    proc.stdin.close()
    ret = proc.wait()
    if ret != 0:
        raise RuntimeError(f"ffmpeg exited with code {ret}")
    print(f"Done! Video saved to {output_mp4}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--preview", action="store_true", help="Render keyframe PNGs instead of full MP4")
    parser.add_argument("--output", default="Video.mp4", help="Output MP4 path")
    args = parser.parse_args()

    if args.preview:
        run_preview(os.path.join(os.path.dirname(os.path.abspath(__file__)), "preview"))
    else:
        run_full_render(args.output)
