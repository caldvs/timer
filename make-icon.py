"""Generate a stopwatch app icon as a set of PNGs for iconutil."""
from PIL import Image, ImageDraw
import math
import os

OUT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "icon.iconset")
os.makedirs(OUT_DIR, exist_ok=True)

def draw_stopwatch(size):
    # High-res render at 4x for anti-aliasing, then downsample
    S = size * 4
    img = Image.new("RGBA", (S, S), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)

    cx = S / 2
    cy = S / 2 + S * 0.04  # slightly lower to make room for crown
    r = S * 0.38

    # --- Crown (top button) ---
    crown_w = S * 0.12
    crown_h = S * 0.06
    crown_top = cy - r - crown_h - S * 0.015
    d.rounded_rectangle(
        [cx - crown_w / 2, crown_top, cx + crown_w / 2, crown_top + crown_h],
        radius=S * 0.015,
        fill=(60, 60, 70, 255),
    )

    # --- Side buttons (tiny nubs at ~45°) ---
    for angle_deg in (225, -45):
        a = math.radians(angle_deg)
        nub_cx = cx + math.cos(a) * (r + S * 0.025)
        nub_cy = cy + math.sin(a) * (r + S * 0.025)
        nub_r = S * 0.025
        d.ellipse(
            [nub_cx - nub_r, nub_cy - nub_r, nub_cx + nub_r, nub_cy + nub_r],
            fill=(60, 60, 70, 255),
        )

    # --- Outer ring (watch body) ---
    ring_width = int(S * 0.04)
    # Dark outer
    d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=(40, 44, 52, 255))
    # Inner face (lighter)
    inner_r = r - ring_width
    d.ellipse(
        [cx - inner_r, cy - inner_r, cx + inner_r, cy + inner_r],
        fill=(248, 248, 250, 255),
    )

    # --- Tick marks ---
    for i in range(12):
        angle = math.radians(i * 30 - 90)
        is_major = (i % 3 == 0)
        tick_len = S * (0.035 if is_major else 0.02)
        tick_width = int(S * (0.014 if is_major else 0.008))
        outer_x = cx + math.cos(angle) * (inner_r - S * 0.01)
        outer_y = cy + math.sin(angle) * (inner_r - S * 0.01)
        inner_x = cx + math.cos(angle) * (inner_r - S * 0.01 - tick_len)
        inner_y = cy + math.sin(angle) * (inner_r - S * 0.01 - tick_len)
        d.line(
            [(outer_x, outer_y), (inner_x, inner_y)],
            fill=(50, 55, 65, 255),
            width=tick_width,
        )

    # --- Hands: minute pointing up-right (≈ 2 o'clock-ish for interest) ---
    hand_angle = math.radians(-60)  # up and slightly right
    hand_len = inner_r * 0.82
    hand_end_x = cx + math.cos(hand_angle) * hand_len
    hand_end_y = cy + math.sin(hand_angle) * hand_len
    d.line(
        [(cx, cy), (hand_end_x, hand_end_y)],
        fill=(33, 150, 243, 255),  # blue (matches app progress ring)
        width=int(S * 0.022),
    )

    # Short "minute" hand going down-left
    hand2_angle = math.radians(120)
    hand2_len = inner_r * 0.55
    h2x = cx + math.cos(hand2_angle) * hand2_len
    h2y = cy + math.sin(hand2_angle) * hand2_len
    d.line(
        [(cx, cy), (h2x, h2y)],
        fill=(50, 55, 65, 255),
        width=int(S * 0.022),
    )

    # Center hub
    hub_r = S * 0.02
    d.ellipse(
        [cx - hub_r, cy - hub_r, cx + hub_r, cy + hub_r],
        fill=(33, 150, 243, 255),
    )

    # Downsample
    return img.resize((size, size), Image.LANCZOS)


# iconset requires these sizes
sizes = [
    (16, "16x16"),
    (32, "16x16@2x"),
    (32, "32x32"),
    (64, "32x32@2x"),
    (128, "128x128"),
    (256, "128x128@2x"),
    (256, "256x256"),
    (512, "256x256@2x"),
    (512, "512x512"),
    (1024, "512x512@2x"),
]

for size, name in sizes:
    img = draw_stopwatch(size)
    path = os.path.join(OUT_DIR, f"icon_{name}.png")
    img.save(path)
    print(f"wrote {path}")

print("Done")
