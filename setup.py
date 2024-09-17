from setuptools import setup, find_packages

setup(
    name='video_processor_lib',
    version='0.1',
    packages=find_packages(),
    url='https://github.com/joaowcitino/video_processor',
    license='MIT',
    author='Joao Citino & Artur',
    author_email='joaocitino10@gmail.com',
    description='Processador de vídeo em tempo real com rotação e escala.',
    install_requires=[
        'numpy>=1.18.0',
        'opencv-python>=4.5.0'
    ],
    entry_points={
        'console_scripts': [
            'video_processor=video_processor_lib.main:run',
        ],
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)