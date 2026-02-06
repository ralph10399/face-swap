# Face Swap Pipeline

High-quality face swap using [FaceFusion](https://github.com/facefusion/facefusion) with `inswapper_128_fp16` + `gfpgan_1.4` enhancement.

## Setup

```bash
# 1. Clone
git clone git@github.com:ralph10399/face-swap.git
cd face-swap

# 2. System deps
sudo apt-get update && sudo apt-get install -y python3-venv ffmpeg

# 3. Create FaceFusion venv and install deps
cd facefusion
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
pip uninstall -y opencv-python && pip install opencv-python-headless  # headless fix
deactivate
cd ..
```

## Usage

```bash
python3 swap.py <source_face> <target_body> <output>
```

Example:

```bash
python3 swap.py examples/target_face.png examples/target_body_1.png examples/output1.png
```

Models are downloaded automatically on first run.
