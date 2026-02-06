import subprocess, os, sys

FACEFUSION_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'facefusion')
PYTHON = os.path.join(FACEFUSION_DIR, 'venv', 'bin', 'python3')
SCRIPT = os.path.join(FACEFUSION_DIR, 'facefusion.py')

source = sys.argv[1]
target = sys.argv[2]
output = sys.argv[3]

cmd = [
    PYTHON, SCRIPT, 'headless-run',
    '-s', os.path.abspath(source),
    '-t', os.path.abspath(target),
    '-o', os.path.abspath(output),
    '--processors', 'face_swapper', 'face_enhancer',
    '--face-swapper-model', 'inswapper_128_fp16',
    '--face-enhancer-model', 'gfpgan_1.4',
    '--face-enhancer-blend', '70',
    '--output-image-quality', '100',
]

subprocess.run(cmd, check=True, cwd=FACEFUSION_DIR)
print(f'Done: {output}')
