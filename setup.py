from setuptools import setup, find_packages
import os

os.system('wget -cP /home/xlab-app-center/ https://cv.cs.columbia.edu/zero123/assets/105000.ckpt')
print('ckpt exist?', os.path.isfile('./105000.ckpt'))

setup(
    name='latent-diffusion',
    version='0.0.1',
    description='',
    packages=find_packages(),
    install_requires=[
        'torch',
        'numpy',
        'tqdm',
    ],
)