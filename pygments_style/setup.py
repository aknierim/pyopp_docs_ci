from setuptools import setup


setup(
    name="pyopp_style",
    version="1.0.0",
    py_modules=["pyopp_style"],
    entry_points={"pygments.styles": ["pyopp = pyopp_style:Pyopp"]},
)
