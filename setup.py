from setuptools import setup, find_packages

setup(
    name='video_processor_lib',
    version='0.1',
    packages=find_packages(),
    url='https://github.com/seu_usuario/seu_repositorio',  # Substitua pelo URL do seu repositório
    license='MIT',
    author='Seu Nome',  # Substitua pelo seu nome
    author_email='seuemail@example.com',  # Substitua pelo seu e-mail
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
