# Instructions

* Create a D4Science account [here](https://services.d4science.org/)
* Verify your email, sign in and follow the instructions
* In [explore virtual research environments](https://services.d4science.org/explore) search the *ParticleFormation* VRE and Request Access
* Sign out and wait until the VRE administrator grants you access; you will be informed by email
* Follow the link in the email to the [ParticleFormation](https://services.d4science.org/group/particleformation) VRE
* Select [Jupyter @ EGI](https://services.d4science.org/group/particleformation/jupyter-egi)
* In JupyterLab, select Terminal and execute the following

```
git clone https://github.com/markusstocker/pynpf-d4science.git
```

* Copy the Jupyter notebooks to the `persistent` folder as follows

```
cp pynpf-d4science/*.ipynb persistent
```

* On the left panel (`Files`) select the `persistent` folder
* Start with the `classification` notebook
* Setup the notebook by adding your `gcube_token`
* You can obtain your token in the [Token Management](https://services.d4science.org/group/particleformation/token-management) tab

```
gcube_token = 'MY GCUBE TOKEN HERE'
```

* Run the two code blocks (SHIFT+ENTER) to complete setting up the notebook
* Now you can start analysing new particle formation events
* Go to the first code block, enter a day (place is currently Hyytiaelae), and execute it
* Move on to the next code block, interpret the visualization and record data about the event
* As you record derivative information, check how it is [catalogued](https://services.d4science.org/group/particleformation/catalogue)
* Proceed to the `processing` notebook to compute mean durations of catalogued information about events
* Finally, use the `provenance` notebook to inspect the provenance of catalogued information

# Notes

* Tested on Chrome, should work on Firefox; IE 11 and Brave have issues with Jupyter
* The system makes heavy use of caching: you may want to run it in a private (incognito) browser window
* Users need to be authorized to catalog resources







