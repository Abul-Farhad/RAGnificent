from setuptools import setup, find_packages

setup(
    name='simple_rag',
    version='0.1.0',

    packages=find_packages(),
    install_requires=[
        "pydantic",
        "langchain",
        "langchain-core",
        "langchain-community",
        "langchain-groq",
        "langgraph",
        "python-dotenv"
    ],
    author='K. M. Abul Farhad-Ibn-Alam',
    author_email='abulfarhad.ibnalam@gmail.com',
    description='A simple RAG chatbot using LangChain and LangGraph',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/Abul-Farhad/simple-rag',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License"
    ],
    python_requires='>=3.9',
)
