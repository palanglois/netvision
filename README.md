# Netvision - Made by vision researcher.

***Alyosha Efros:***
 ***​		" What's the most important aspect of training deep networks? Visualization "***

***Original Human:***
		  ***" Tribe, tonight we're eating mamuth. Do you know how? Teamwork. "***



Fuel your collaborations by sending awesome webpage results.
Forget about HTML and CSS and Javascript, just effortlessly use Python.

Features:
* Images (auto thumbnail)
* Adaptive loading of what is in the viewer
* Curves
* 3D models

PRs welcome!


## Pypi push

```
# 1. Increment version in setup.py
rm dist/*
python -m build
python3 -m twine upload --repository pypi dist/* # prompt for Pypi token.
```