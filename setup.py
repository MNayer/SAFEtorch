from setuptools import find_packages, setup

setup(name="safetorch",
      version="0.1",
      description="Torch SAFE implementation.",
      url="https://github.com/MNayer/SAFEtorch",
      author="",
      author_email="",
      license="MIT",
      packages=find_packages(),
      #install_requires=["torch==1.4.0", "capstone==4.0.1", "numpy==1.18.1"],
      install_requires=["torch==1.4.0", "capstone==4.0.2", "numpy==1.20.2"],
      zip_safe=False)
