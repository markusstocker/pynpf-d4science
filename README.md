# Instructions

* Create a D4Science account [here](https://services.d4science.org/)
* Verify your email, sign in and follow the instructions
* In [explore virtual research environments](https://services.d4science.org/explore) search the "ParticleFormation" VRE and Request Access
* Sign out (yes, it is necessary) and wait until the VRE administrator grants you access; you will be informed by email
* Follow the link in the email to the "[ParticleFormation](https://services.d4science.org/group/particleformation)" VRE; you will need to sign in (if you did not sign out earlier you may get an access denied error message)
* Select [Jupyter @ EGI](https://services.d4science.org/group/particleformation/jupyter-egi)
* In JupyterLab, select Terminal execute the following

```
git clone https://github.com/markusstocker/pynpf-d4science.git
```

* Copy the `classification.ipynb` to the `persistent` folder as follows

```
cp pynpf-d4science/classification.ipynb persistent
```

* On the left panel (`Files`) select the `persistent` folder and open `classification.ipynb`
* Setup the notebook by adding your `gcube_token`

```
gcube_token = 'MY GCUBE TOKEN HERE'
```

* Run the two code blocks (SHIFT+ENTER) to complete setting up the notebook
* Now you can start analysing new particle formation events
* Go to the first code block, enter a day (place is currently Hyytiaelae), and execute it
* Move on to the next code block, interpret the visualization and record data about the event

# Notes

* Tested on Chrome, should work on Firefox; IE 11 and Brave have issues with Jupyter
* The system makes heavy use of caching: you may want to run it in a private (incognito) browser window







