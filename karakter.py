import cv2
import numpy as np
import os

os.makedirs("output", exist_ok=True)

# --- CANVAS ---
canvas = np.full((400, 600, 3), 255, dtype=np.uint8)  # white background

# --- DRAW CARTOON CROCODILE (BUAYA) ---
# Body (ellipse)
cv2.ellipse(canvas, (300, 260), (220, 100), 0, 0, 360, (34,139,34), -1)  # green body
# Belly
cv2.ellipse(canvas, (300, 280), (160, 60), 0, 0, 360, (200,255,200), -1)
# Head
cv2.ellipse(canvas, (150, 200), (90, 60), -20, 0, 360, (34,139,34), -1)
# Eye whites
cv2.circle(canvas, (130, 170), 14, (255,255,255), -1)
cv2.circle(canvas, (160, 155), 12, (255,255,255), -1)
# Pupils
cv2.circle(canvas, (132, 172), 6, (0,0,0), -1)
cv2.circle(canvas, (160, 155), 6, (0,0,0), -1)
# Nostrils
cv2.circle(canvas, (115, 195), 6, (0,0,0), -1)
# Mouth (line)
cv2.ellipse(canvas, (170, 220), (60, 20), -20, 0, 180, (0,0,0), 3)
# Teeth (triangles)
pts = np.array([[200,220],[190,230],[210,230]], np.int32)
cv2.fillPoly(canvas, [pts], (255,255,255))
pts = np.array([[220,210],[210,230],[230,230]], np.int32)
cv2.fillPoly(canvas, [pts], (255,255,255))
# Legs (simple rectangles)
cv2.rectangle(canvas, (380, 320), (420, 360), (34,139,34), -1)
cv2.rectangle(canvas, (240, 320), (280, 360), (34,139,34), -1)
# Tail (polygon)
tail = np.array([[480,260],[560,230],[580,250],[520,280]], np.int32)
cv2.fillPoly(canvas, [tail], (34,139,34))
# Scales on back (small circles)
for x in range(170,460,30):
    cv2.circle(canvas, (x,180), 8, (0,100,0), -1)
# Text label
cv2.putText(canvas, "BUAYA - UTS CV", (10,20), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,0,0), 2, cv2.LINE_AA)

# Save base character
cv2.imwrite("output/karakter.png", canvas)

# --- TRANSFORMATIONS ---
# 1. TRANSLATE
M_trans = np.float32([[1,0,80],[0,1,30]])
translated = cv2.warpAffine(canvas, M_trans, (600,400))
cv2.imwrite("output/translate.png", translated)

# 2. ROTATE (around center)
center = (300,200)
M_rot = cv2.getRotationMatrix2D(center, -30, 1)
rotated = cv2.warpAffine(canvas, M_rot, (600,400))
cv2.imwrite("output/rotate.png", rotated)

# 3. RESIZE
resized = cv2.resize(canvas, (300,200))
cv2.imwrite("output/resize.png", resized)

# 4. CROP (crop snout/head area)
crop = canvas[120:280, 50:260]
cv2.imwrite("output/crop.png", crop)

# --- ARITHMETIC / BITWISE OPERATIONS ---
# Create a background image (optional)
background = np.full((400,600,3), (180,220,255), dtype=np.uint8)  # light sky blue
cv2.imwrite("img/background.jpg", background)

# Bitwise OR - combine
bitwise_or = cv2.bitwise_or(canvas, background)
cv2.imwrite("output/bitwise.png", bitwise_or)

# Add - brighten the buaya a bit
added = cv2.add(canvas, np.full(canvas.shape, 20, dtype=np.uint8))
cv2.imwrite("output/final.png", added)

print("All images saved to output/ (karakter.png, translate.png, rotate.png, resize.png, crop.png, bitwise.png, final.png)")
